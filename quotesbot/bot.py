import threading
import time

from quotesbot.provider import QuotesProvider

from g_python.hdirection import Direction
from g_python.hmessage import HMessage
from g_python.gextension import Extension


class QuotesBot:
    def __init__(self, extension: Extension):
        self._extension = extension
        self._interval = 15000
        self._quotes_thread = False
        self._threadStarted = False
        self._provider = QuotesProvider(max_length=101)

        self._extension.intercept(Direction.TO_SERVER, self._on_chat_out, "Chat")
        self._extension.start()

    def _on_chat_out(self, message: HMessage):
        text = message.packet.read_string()
        if "!start" in text:
            message.is_blocked = True
            self._start_thread()
        if "!stop" in text:
            message.is_blocked = True
            self._quotes_thread.do_run = False
            print("Stopping quotes thread...")
        if "!interval" in text:
            message.is_blocked = True
            self._interval = int(text.replace("!interval ", ""))

    def _start_thread(self):
        if not self._threadStarted:
            self._quotes_thread = threading.Thread(target=self._share_quotes)
            self._quotes_thread.start()
            self._threadStarted = True

    def _share_quotes(self):
        thread = threading.currentThread()
        print('Starting quotes thread...')
        while getattr(thread, 'do_run', True):
            self._extension.send_to_server(
                '{out:Shout}{s:"' + str(self._provider.get().content()) + '"}{i:6}'
            )
            time.sleep(self._interval / 1000)
        print('Thread was interrupted')
        self._threadStarted = False
