# encoding: utf-8
import logging
from rx.subject import Subject

from wstomp.frame import Frame, Connect
from wstomp.websocket import WebSocket

log = logging.getLogger('Stomp')


class Status(enumerate):
    ESTABLISHED = 0
    CONNECTED = 1
    CLOSED = 2


class Stomp:

    def __init__(self, url):
        self.ws = WebSocket(url)

        # Stomp streams
        self.rx_status = Subject()
        self.rx_frame = Subject()
        self.rx_message = Subject()
        self.rx_receipt = Subject()
        self.rx_error = Subject()

        # Assign streams
        self.ws.rx_on_open.subscribe(on_next=self.__on_open)
        self.ws.rx_on_data.subscribe(on_next=self.__on_data)
        self.ws.rx_on_close.subscribe(on_next=self.__on_close)
        self.ws.rx_on_ping.subscribe(on_next=self.__on_ping)
        self.ws.rx_on_pong.subscribe(on_next=self.__on_pong)
        self.ws.rx_on_count_message.subscribe(on_next=self.__on_count_message)
        self.ws.rx_on_error.subscribe(on_next=self.__on_error)
        self.ws.rx_on_message.subscribe(on_next=self.__on_message)

    def transmit(self, frame: Frame):
        self.ws.send(frame.build())

    def connect(self):
        pass

    def send(self):
        pass

    def subscribe(self):
        pass

    def unsubscribe(self):
        pass

    def disconnect(self):
        pass

    def __on_open(self):
        pass

    def __on_close(self):
        pass

    def __on_data(self):
        pass

    def __on_ping(self):
        pass

    def __on_pong(self):
        pass

    def __on_count_message(self):
        pass

    def __on_error(self):
        pass

    def __on_message(self, c, message):
        self.rx_frame.on_next(Frame.parse(message))
