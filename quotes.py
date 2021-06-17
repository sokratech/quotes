import sys

from quotesbot.bot import QuotesBot

from g_python.gextension import Extension

extension_info = {
    "title": "Quotes",
    "description": "Sokratech QuotesBot",
    "version": "1.0",
    "author": "sokratech"
}


if __name__ == '__main__':
    QuotesBot(extension=Extension(extension_info, sys.argv))
