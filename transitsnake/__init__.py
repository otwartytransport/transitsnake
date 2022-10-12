import abc
import csv
import io
import zipfile


class BaseDatasetType(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def filename(self) -> str:
        pass

    def csv_data(self):
        return dict([(key, str(value)) for key, value in self.__dict__.items() if value])


def dump(feed, fp):
    with zipfile.ZipFile(fp, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for dataset_type, data in feed.data.items():
            if len(data) == 0:
                continue
            type_attributes = data[0].__dict__.keys()

            fields = []
            for field_name in type_attributes:
                for entry in data:
                    if field_name in entry.__dict__ and entry.__dict__[field_name] is not None:
                        fields.append(field_name)
                        break

            memory = io.StringIO()
            writer = csv.DictWriter(memory, fieldnames=fields)

            writer.writeheader()
            for value in data:
                writer.writerow(value.csv_data())

            archive.writestr(dataset_type.filename, memory.getvalue())
