from quotesbot.provider import QuotesProvider


provider = QuotesProvider(max_length=90)

for i in range(1000):
    print(provider.provide_quote().to_string())
