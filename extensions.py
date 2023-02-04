import requests
import json
from config import keys
class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ExchangeException(
                f'Одинаковые валюты перевести невозможно {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ExchangeException(f'Ошибка ввода данных {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ExchangeException(f'Ошибка ввода данных {base}')

        try:
            amount = int(amount)
        except ValueError:
            raise ExchangeException(f'Ошибка ввода данных {amount}')

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_base = float(json.loads(r.content)[keys[quote]])
        return total_base