"""
Progress message representation
"""
from .event_message import EventMesasge
from .core import MessageType

class ProgressMesasge(EventMesasge):
    """A numeric + label notification that will be presented in the web app."""
    
    def __init__(self, message, value = 0):
        super().__init__(message=message)
        self._value = value

    def messageType(self) :
        return MessageType.Progress

    @property
    def value(self):
        """
        Progress value, should be more or equal than 0 and less or equal then 100
        Type: 
            int
        Raise:
            ValueError: wrong progress value is set
        """
        return self._value

    @value.setter
    def value(self, value:int):
        if 0 <= value <= 100:
            self._value = value
        else:
            raise ValueError('Value is out of range, should be more or equal than 0 and less or equal then 100 ')
        

    def messageData(self):
        data = super().messageData()
        data['Value'] = self._value
        return data
