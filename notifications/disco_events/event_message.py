"""
Event message representation
"""
from .core import AbstractMessage
from .core import MessageType

class EventMesasge(AbstractMessage):
    """A string notification that will appear in the web app 
    and will express the overall state of the job."""

    def __init__(self, message): 
        self._message = message

    @property
    def message(self) :
        """
        Event description message.
        Type: 
            str: description message
        """
        return self._message

    @message.setter
    def message(self, message) :
        self._message = message

    def messageType(self) :
        return MessageType.Event

    def messageData(self) :
        return {
            "Label" : self.message
        }