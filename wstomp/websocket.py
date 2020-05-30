from rx.subject import Subject
from websocket import WebSocketApp, ABNF


class WebSocket:

    def __init__(self, url, header=None, keep_running=True, get_mask_key=None, cookie=None, subprotocols=None):
        self.url = url
        self.ws = WebSocketApp(url, header=header, keep_running=keep_running, get_mask_key=get_mask_key, cookie=cookie,
                               subprotocols=subprotocols)

        # Create streams
        self.rx_on_close            = Subject()
        self.rx_on_data             = Subject()
        self.rx_on_error            = Subject()
        self.rx_on_open             = Subject()
        self.rx_on_message          = Subject()
        self.rx_on_count_message    = Subject()
        self.rx_on_ping             = Subject()
        self.rx_on_pong             = Subject()

        # Assign callbacks to streams
        self.ws.on_close         = lambda x: self.rx_on_close.on_next(x)
        self.ws.on_data          = lambda x, s, t, f: self.rx_on_data.on_next((x, s, t, f))
        self.ws.on_error         = lambda x, e: self.rx_on_error.on_next((x, e))
        self.ws.on_open          = lambda x: self.rx_on_open.on_next(x)
        self.ws.on_message       = lambda x, s: self.rx_on_message.on_next((x, s))
        self.ws.on_count_message = lambda x, s, f: self.rx_on_count_message.on_next((x, s, f))
        self.ws.on_ping          = lambda: self.rx_on_ping.on_next(None)
        self.ws.on_ping          = lambda: self.rx_on_ping.on_next(None)

    def run_forever(self, sockopt=None, sslopt=None, ping_interval=0, ping_timeout=None, http_proxy_host=None,
                    http_proxy_port=None, http_no_proxy=None, http_proxy_auth=None, skip_utf8_validation=False,
                    host=None, origin=None, dispatcher=None, suppress_origin=False, proxy_type=None):
        self.ws.run_forever(sockopt=sockopt, sslopt=sslopt, ping_interval=ping_interval, ping_timeout=ping_timeout,
                            http_proxy_host=http_proxy_host, http_proxy_port=http_proxy_port,
                            http_no_proxy=http_no_proxy, http_proxy_auth=http_proxy_auth,
                            skip_utf8_validation=skip_utf8_validation, host=host, origin=origin, dispatcher=dispatcher,
                            suppress_origin=suppress_origin, proxy_type=proxy_type)

    def close(self):
        self.ws.close()

    def send(self, data, opcode=ABNF.OPCODE_TEXT):
        self.ws.send(data, opcode)