"""
Alert message representation
"""
from .event_message import EventMesasge
from .core import MessageType

class AlertMesasge(EventMesasge):
    """An important notification that can be pushed as browser notification 
    or even as email, slack message."""
    
    def messageType(self) :
        return MessageType.Alert