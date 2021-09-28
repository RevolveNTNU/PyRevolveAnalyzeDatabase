## Revolve Analyze Database for Python
This is a Python package that can be used to read testing data from your local Revolve Analyze SQLite database.

## Installation guide
1. Navigate to the release section of this repository
2. Download the wheel package from the latest release
3. Install the wheel package using pip (Package is not on PyPi yet)

## Getting started

### Setting up a database connection
```python
dbFile = "C:\PATH\TO\REVOLVE_ANALYZE\DATABASE\local_database.db"
db = RevolveAnalyzeDatabase(dbFile)
```

### Load some data
Dataseries loaded from the database are returned as pandas (https://pandas.pydata.org/) Dataframes.

```python
logname = "FSG19 - Endurance"
channelname = "vcu.INS.vx"

dataseries = db.get_dataseries(logname, channelname)

laps = db.get_laps_for_log(logname)

dataseries_lap_1 = db.get_dataseries(logname, channelname, laps[0])
```
