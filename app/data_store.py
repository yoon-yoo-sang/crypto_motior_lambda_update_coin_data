import datetime

from app.models import Coin, CoinPriceHistory, CoinAnalysisHistory


def store_data(coin: Coin, data: dict, new_datas) -> None:
    coin_price_history = CoinPriceHistory(
        coin_id=coin.id,
        price=data['trade_price'],
        timestamp=datetime.datetime.fromtimestamp(data['timestamp'] / 1000),
        change=data['change'],
        change_price=data['change_price'],
        change_rate=data['change_rate'],
        acc_trade_price_24h=data['acc_trade_price_24h']
    )
    # TODO: Implement RSI and MACD calculation, coin_price_id is not available yet
    coin_analysis_history = CoinAnalysisHistory(
        coin_id=coin.id,
        coin_history_id=coin_price_history.id,
        dopamine_index=data['dopamine_index'],
        rsi=data['rsi'],
        macd=data['macd']
    )
    new_datas.append(coin_price_history)
    new_datas.append(coin_analysis_history)
