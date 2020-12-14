from abc import ABC, abstractmethod
import time


class Session(ABC):
    @abstractmethod
    def get_sessions(self):
        pass

    @abstractmethod
    def initialize(self, session_id, username):
        pass

    @abstractmethod
    def has(self, session_id):
        pass

    @abstractmethod
    def delete(self, session_id):
        pass

    # @abstractmethod
    # def get_username(self, session_id):
    #     pass

    @abstractmethod
    def append_unread_message(self, session_id, message):
        pass

    @abstractmethod
    def pop_unread_messages(self, session_id):
        pass


class Memory(Session):
    UNREAD_MESSAGE_LIMIT = 50

    def __init__(self):
        self._sessions = {}

    def initialize(self, receiver):
        self._sessions[receiver] = {
            'active': time.time(),
            # 'receiver': receiver,
            'unread': []
        }

    def get_sessions(self):
        return list(self._sessions.keys())

    def has(self, receiver):
        return receiver in self._sessions

    def delete(self, receiver):
        self._sessions.pop(receiver)

    # def get_username(self, session_id):
    #     if session_id not in self._sessions:
    #         raise ValueError("invalid session")

    #     return self._sessions[session_id]['username']

    def append_unread_message(self, receiver, message):
        if receiver not in self._sessions:
            raise ValueError("invalid session")

        self._sessions[receiver]['unread'].append(message)

        # TODO: Could replace this with a data structure which utilizes a
        # circular list?  Saving on these kinds of ops against the list.
        self._sessions[receiver]['unread'] = self._sessions[receiver]['unread'][-self.UNREAD_MESSAGE_LIMIT:]

    def pop_unread_messages(self, receiver):
        while len(self._sessions[receiver]['unread']) > 0:
            message = self._sessions[receiver]['unread'][0]
            del self._sessions[receiver]['unread'][0]
            yield message
