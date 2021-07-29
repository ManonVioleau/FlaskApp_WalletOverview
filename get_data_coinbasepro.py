from flask import jsonify
from cbpro import CBProAuth, AuthenticatedClient, PublicClient
import config

auth_client = AuthenticatedClient(config.M_COINBASE_PRO_API_KEY, config.M_COINBASE_PRO_API_SECRET, config.M_COINBASE_PRO_PASSPHRASE)
public_client = PublicClient()


account_Coinbase_pro = auth_client.get_accounts()
# print(account_Coinbase_pro)
BALANCE_COINBASE_PRO = []

for balance in account_Coinbase_pro:
    if float(balance['balance']) != 0 or float(balance['hold']) != 0 or float(balance['available']) != 0:
        if balance['currency'] == 'EUR':
            prices = public_client.get_product_ticker(product_id='USDT-EUR')
            BALANCE_COINBASE_PRO.append([balance['currency'], float(balance['balance']) / float(prices['price'])])
        else :
            productid = "'" + balance['currency'] + '-USDT' + "'"
            print(productid)
            price_coinbasepro = public_client.get_product_ticker(product_id=productid)
            print(price_coinbasepro)
    #         for prices in price_coinbasepro:
    #             if prices['quote_currency'] == 'USDT':
    #                 if prices['base_curency'] == balance['currency']:
    #                     BALANCE_COINBASE_PRO.append([balance['currency'], float(balance['balance']) * float(prices['balance'])])
    # print(BALANCE_COINBASE_PRO)


