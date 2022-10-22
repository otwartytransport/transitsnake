> ⚠️ **NOTE:**  This project is still in early development ⚠️

# transitsnake

Library to create, read and validate [General Transit Feed Spec (GTFS)](https://gtfs.org/schedule/) files.

## Creating GTFS
```py
feed = Feed()
feed.add(Agency(
    agency_name='Example',
    agency_url='https://example.com',
    agency_timezone='Europe/Warsaw',
    agency_lang='pl'
))

with open('gtfs.zip', 'wb') as file:
    transitsnake.dump(feed, file)
```

## Reading GTFS
```py
with open('gtfs.zip', 'rb') as file:
    feed = transitsnake.load(file)
```