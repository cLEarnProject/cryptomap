from flask import Flask, request, jsonify
from pycoingecko import CoinGeckoAPI

app = Flask(__name__)
cg = CoinGeckoAPI()

@app.route('/current-price')
def get_current_price():
    crypto_id = request.args.get('crypto_id', 'bitcoin')
    currency = request.args.get('currency', 'usd')
    try:
        price_data = cg.get_price(ids=crypto_id, vs_currencies=currency)
        price = price_data[crypto_id][currency]
        return jsonify({'price': price})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/historical-price')
def get_historical_price():
    crypto_id = request.args.get('crypto_id', 'bitcoin')
    date = request.args.get('date', '01-01-2022')
    currency = request.args.get('currency', 'usd')
    try:
        historical_data = cg.get_coin_history_by_id(id=crypto_id, date=date)
        price = historical_data['market_data']['current_price'][currency]
        return jsonify({'price': price})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
