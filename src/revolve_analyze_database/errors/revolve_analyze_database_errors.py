
class DataseriesNotFoundError(Exception):
    """Exception raised when a dataseries could not be found.

    Attributes:
        logname -- Name of the log trying to find data for.
        channelname -- Name of the channel to find data for.
        message -- Explanation of the error.
    """

    def __init__(self, logname, channelname, message=None):
        self.logname = logname
        self.channelname = channelname
        if message is None:
            self.message = f"Could not load dataseries for log {logname} and channel {channelname}."
        else:
            self.message = message
        super().__init__(self.message)