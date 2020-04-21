"""
Constants and Enum used by the events sdk
"""
import enum

HOST_URL = 'http://localhost:8080'
EVENTS_ENDPOINT = HOST_URL + '/update'

class MessageType(enum.Enum):
    """Message Types"""
    Unknown = 'Unknown'
    Event = 'Event'
    Progress = 'Progress'
    Alert = 'Alert'