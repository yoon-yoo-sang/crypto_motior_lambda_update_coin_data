def process_data(data, max_volatility, max_volume_score):
    normalized_volatility = abs(data['signed_change_rate']) / max_volatility
    normalized_volume_score = data['acc_trade_price_24h'] / max_volume_score

    raw_dopamine_index = normalized_volatility * 0.5 + normalized_volume_score * 0.5

    dopamine_index = raw_dopamine_index * 100

    processed_data = {
        **data,
        'dopamine_index': round(dopamine_index, 2),  # 소수점 2자리로 반올림
        'rsi': 0,
        'macd': 0,
    }
    return processed_data
