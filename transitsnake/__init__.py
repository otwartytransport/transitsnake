import csv
import dataclasses
import io
import zipfile

from dataclass_wizard import fromdict

from transitsnake.datasets import types_filename_mappings
from .feed import Feed


def load(fp, validate=True, hooks=None):
    with zipfile.ZipFile(fp, mode="r", compression=zipfile.ZIP_DEFLATED) as archive:
        new_feed = Feed()

        for filename in archive.namelist():
            if filename not in types_filename_mappings:
                continue

            cls = types_filename_mappings[filename]

            file = archive.open(filename, 'r')
            memory = io.StringIO(file.read().decode('utf-8'))

            reader = csv.DictReader(memory)
            for row in reader:
                instance = fromdict(cls, row)
                if hooks and cls in hooks:
                    for hook in hooks[cls]:
                        hook(instance)

                if validate:
                    instance.validate()
                new_feed.add(instance)

        return new_feed


def loads(data, validate=True, hooks=None):
    fp = io.BytesIO(data)
    return load(fp, validate=validate, hooks=hooks)


def dump(feed, fp, validate=True, hooks=None):
    with zipfile.ZipFile(fp, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for dataset_type, data in feed.data.items():
            if len(data) == 0:
                continue
            type_attributes = [x.name for x in dataclasses.fields(dataset_type)]

            fields = []
            for field_name in type_attributes:
                for entry in data:
                    if entry.__dict__[field_name] is not None:
                        fields.append(field_name)
                        break

            memory = io.StringIO()
            writer = csv.DictWriter(memory, fieldnames=fields)

            writer.writeheader()
            for value in data:
                if validate:
                    value.validate()
                    value.global_validate(feed.data)

                if hooks and dataset_type in hooks:
                    for hook in hooks[dataset_type]:
                        hook(value)

                writer.writerow(value.csv_data())

            archive.writestr(dataset_type.filename, memory.getvalue())


def dumps(feed, validate=True, hooks=None) -> bytes:
    fp = io.BytesIO()
    dump(feed, fp, validate=validate, hooks=hooks)
    return fp.getvalue()
