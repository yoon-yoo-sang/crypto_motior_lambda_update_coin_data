def process_data(data):
    volatility = abs(data['signed_change_rate'])
    volume_score = data['acc_trade_price_24h']
    dopamine_index = volatility * 0.5 + volume_score * 0.5

    processed_data = {
        **data,
        'dopamine_index': dopamine_index,
        'rsi': 0,
        'macd': 0,
    }
    return processed_data
