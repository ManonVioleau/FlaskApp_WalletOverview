from flask import jsonify
from binance.client import Client
import config

client_binance = Client(config.M_BINANCE_API_KEY, config.M_BINANCE_API_SECRET)

# balances = {['asset', 'balance']}
account = client_binance.get_account()
balances = account['balances'] 

# paires = {['symbol', 'baseAsset', 'quoteAsset']}
exchange_info = client_binance.get_exchange_info()
paires = exchange_info['symbols']

# prices = {['symbol', 'price']}
prices = client_binance.get_all_tickers()
PROCESSED_BALANCE = []

for balance in balances:
    if float(balance['free']) > 0 or float(balance['locked']) > 0 :
        if balance['asset'] == 'USDT':
            PROCESSED_BALANCE.append([balance['asset'], float(balance['free']) + float(balance['locked'])])
        else :
            for paire in paires:
                if paire['quoteAsset'] == 'USDT':
                    if paire['baseAsset'] in balance['asset']:
                        for price in prices:
                            if price['symbol'] in paire['symbol']:
                                value = float(price['price']) * ( float(balance['free']) + float(balance['locked']))
                                PROCESSED_BALANCE.append([balance['asset'], value])

# print(PROCESSED_BALANCE)
