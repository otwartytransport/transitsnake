import csv
import dataclasses
import io
import zipfile

from .feed import types_filename_mappings, Feed


def load(fp, hooks=None):
    with zipfile.ZipFile(fp, mode="r", compression=zipfile.ZIP_DEFLATED) as archive:
        feed = Feed()

        for filename in archive.namelist():
            cls = types_filename_mappings[filename]

            file = archive.open(filename, 'r')
            memory = io.StringIO(file.read().decode('utf-8'))

            reader = csv.DictReader(memory)
            for row in reader:
                params = dict()
                params.update(row)
                if hooks and cls in hooks:
                    params.update({'_hooks': hooks[cls]})

                feed.add(cls(**params))

        return feed


def loads(data, hooks=None):
    fp = io.BytesIO(data)
    return load(fp, hooks=hooks)


def dump(feed, fp, validate=True):
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
                    value.global_validate(feed.data)

                writer.writerow(value.csv_data())

            archive.writestr(dataset_type.filename, memory.getvalue())


def dumps(feed, validate=True) -> bytes:
    fp = io.BytesIO()
    dump(feed, fp, validate=validate)
    return fp.getvalue()
