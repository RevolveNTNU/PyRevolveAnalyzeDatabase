def query_laps_for_log(logname):
    query = ("SELECT lapNumber, lapStart, lapEnd " + 
            "FROM Laps INNER JOIN Log ON Log.id = Laps.logId "+ 
            f"WHERE name = '{logname}'")
    return query


def query_dataseries_for_log_and_channel(logname, channelname):
    query = (f"SELECT dp.xVal as x, dp.yVal as {channelname} "+
            "FROM Datapoints dp "+
            "INNER JOIN Series s ON s.id = dp.seriesId "+
            "INNER JOIN Log l ON s.logId = l.id "+
            "INNER JOIN Datachannel dc ON s.channelId = dc.id "+
            f"WHERE l.name = '{logname}' AND dc.name = '{channelname}'")
    return query

def query_dataseries_for_log_channel_and_lap(logname, channelname, lap):
    query = ("SELECT dp.xVal as x, dp.yVal as y "+
            "FROM Datapoints dp "+
            "INNER JOIN Series s ON s.id = dp.seriesId "+
            "INNER JOIN Log l ON s.logId = l.id "+
            "INNER JOIN Datachannel dc ON s.channelId = dc.id "+
            f"WHERE l.name = '{logname}' AND dc.name = '{channelname}' "+
            f"AND X > {lap.start} AND X < {lap.end}")
    return query