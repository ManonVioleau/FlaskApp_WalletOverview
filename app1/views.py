from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('get_data')
# To get one variable, tape app.config['MY_VARIABLE']

app.config.from_object('get_data_coinbasepro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Overview')
def overview():
    title = 'The Lucid Wallet'
    return render_template('overview.html', title = title, balances = app.config['PROCESSED_BALANCE'], balance_coinbase_pro = app.config['BALANCE_COINBASE_PRO'])

if __name__ == "__main__":
    app.run()