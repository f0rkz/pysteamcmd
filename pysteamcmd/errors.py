class PySteamcmdException(Exception):
    """
    Base exception for the pysteamcmd package
    """
    def __init__(self, message=None, *args, **kwargs):
        self.message = message
        super(PySteamcmdException, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return repr(self.message)

    def __str__(self):
        return repr(self.message)
