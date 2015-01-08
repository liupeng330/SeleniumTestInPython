class MediaInfo:
    def __init__(self, name='', duration='', filesize='', date=''):
        self.name = name
        self.duration = duration
        self.date =date
        
    def __eq__(self, other):
        return (isinstance(other, self.__class__)) and self.name == other.name and self.duration ==  other.duration and self.date == other.date