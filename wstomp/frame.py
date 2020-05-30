BYTE = {'LF': '\x0A', 'NULL': '\x00'}


def extract_command(data):
    command = data.split(BYTE['LF'])[0]
    return command


def extract_headers(data):
    return None


def extract_payload(data):
    return None


class Frame:

    def __init__(self, command, headers=None, payload=None):
        self.command = command
        self.headers = headers
        self.payload = payload

    def build(self):
        lines = [self.command + BYTE['LF']]
        for key in self.headers:
            lines.append(key + ":" + self.headers[key] + BYTE['LF'])
        if self.payload is not None:
            lines.append('\n')
            lines.append(self.payload)
        return ''.join(lines) + BYTE['LF'] + BYTE['NULL']

    @staticmethod
    def parse(data):
        return Frame(extract_command(data), extract_headers(data), extract_payload(data))


class Connect(Frame):
    def __init__(self, accept_version, host, login=None, passcode=None, heart_beat=None):
        super().__init__('STOMP', {accept_version, host, login, passcode, heart_beat})


class Connected(Frame):
    def __init__(self, version, heart_beat=None, session=None, server=None):
        super().__init__('CONNECTED', {'version': version, 'heart-beat': heart_beat, 'session': session, 'server': server})


class Send(Frame):
    def __init__(self, destination, transaction=None):
        super().__init__('SEND', {destination, transaction})


class Subscribe(Frame):
    def __init__(self, destination, id, ack=None):
        super().__init__('STOMP',  {destination, id, ack})


class Unsubscribe(Frame):
    def __init__(self, id):
        super().__init__('STOMP', {id})


class Ack(Frame):
    def __init__(self, id, transaction=None):
        super().__init__('ACK', {id, transaction})


class Nack(Frame):
    def __init__(self, id, transaction=None):
        super().__init__('NACK', {id, transaction})


class Begin(Frame):
    def __init__(self, transaction):
        super().__init__('BEGIN', {transaction: transaction})


class Commit(Frame):
    def __init__(self, transaction):
        super().__init__('COMMIT', {transaction: transaction})


class Abort(Frame):
    def __init__(self, transaction):
        super().__init__('ABORT', {transaction})


class Disconnect(Frame):
    def __init__(self, receipt):
        super().__init__('DISCONNECT', {receipt})


class Message(Frame):
    def __init__(self, destination, message_id, subscription, ack=None):
        super().__init__('MESSAGE', {'destination': destination, 'message-id': message_id, 'subscription': subscription, 'ack': ack})


class Receipt(Frame):
    def __init__(self, receipt_id):
        super().__init__('RECEIPT', {'receipt-id': receipt_id})


class Error(Frame):
    def __init__(self, message=None):
        super().__init__('ERROR', {message})
