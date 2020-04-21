from abc import ABC, abstractmethod
import json

from .request_sender import RequestSender
from . import constants

class AbstractMessage(ABC):
    """Abstract class for any type of message"""

    jobId = None
    dispatchID = None

    @classmethod
    def setJobInfo(cls, jobId, dispatchID):
        """Sets the Job information
    
        Args:
            jobId (str): Job Id
            dispatchID (str): Dispatch Id
        """
        if jobId is not None and dispatchID is not None:
            cls.jobId = jobId
            cls.dispatchID = dispatchID
    
    @abstractmethod
    def messageType(self) -> constants.MessageType:
        """Type of message, abstract method, should be overridden in subclass.

        Returns:
            constants.MessageType: type of message
        """
        pass

    @abstractmethod
    def messageData(self) : #dictionary
        """Collects message information which need to be sent,
        abstract method, should be overridden in subclass.

        Returns:
            dict: message information
        """
        pass

    def _data(self):
        return {
            "jobID" : self.jobId,
            "dispatchID" : self.dispatchID,
            "eventType" : self.messageType().value,
            "data" : self.messageData()
        }

    def send(self) :
        """Sends message to Disco server
        
        Returns:
            requests.Response: response from server
        
        Raise:
            ValueError: Job information(Job Id and Dispatch Id) is not set
            HTTPError: When request failed
        """
        if self.jobId is None:
            raise ValueError('Job ID is not set.')
        if self.dispatchID is None:
            raise ValueError('Dispatch ID is not set.')

        payload = self._data()
        response = RequestSender.post(constants.EVENTS_ENDPOINT, json=payload)
        return response

def setJobInfo(jobId: str, dispatchID: str):
    """Sets the Job information

    Args:
        jobId (str): Job Id
        dispatchID (str): Dispatch Id
    """
    AbstractMessage.setJobInfo(jobId, dispatchID)