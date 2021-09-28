from sqlalchemy import create_engine
import pandas as pd

from revolve_analyze_database.queries.queries import *
from revolve_analyze_database.models.lap import Lap
from revolve_analyze_database.errors.revolve_analyze_database_errors import *

class RevolveAnalyzeDatabase:
    """
        Class for reading data from a Revolve Analyze SQLite database.
    """

    def __init__(self, db_path):
        self.engine = create_engine(f"sqlite:///{db_path}")

    def get_laps_for_log(self, logname):
        """
            Loads Laps for the specified log from the database.
        """
        lapsDataFrame = None
        with self.engine.connect() as db_connection:
            lapsDataFrame = pd.read_sql_query(query_laps_for_log(logname), db_connection)
        laps = []
        for _, lap in lapsDataFrame.iterrows():
            laps.append(Lap(lap["lapNumber"], lap["lapStart"], lap["lapEnd"]))
        return laps

    def get_dataseries(self, logname, channelname, lap=None):
        """
            Loads a dataseries, for a given log, channel (and optionally a lap).
        """
        dataFrame = None

        if lap is not None:
            with self.engine.connect() as db_connection:
                dataFrame = pd.read_sql_query(query_dataseries_for_log_channel_and_lap(logname, channelname, lap), db_connection)
        else:
            with self.engine.connect() as db_connection:
                dataFrame = pd.read_sql_query(query_dataseries_for_log_and_channel(logname, channelname), db_connection)
        if dataFrame is None:
            raise DataseriesNotFoundError(logname, channelname)
        min = dataFrame['x'].min()
        dataFrame['x'] -= min
        dataFrame['x'] /= 1_000_000
        return dataFrame
