from quotesbot.quote import Quote
from quotesbot.database import QuotesDatabase


class QuotesProvider:
    def __init__(self, max_length=101):
        self._database = QuotesDatabase(max_length=max_length)

    def provide_quote(self):
        return Quote(self._database.get_quote())

    def get(self):
        return self.provide_quote()


