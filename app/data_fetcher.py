import requests

from app.data_conn import session
from app.models import Coin


def get_coin(market) -> Coin:
    coin = session.query(Coin).filter_by(market=market).first()

    if coin:
        return coin
    else:
        raise ValueError(f"Coin with market {market} not found")


def get_all_coins():
    return session.query(Coin).all()


def fetch_coin_data(coins):
    try:
        all_get_url = "https://api.upbit.com/v1/market/all?is_details=true"
        response = requests.get(all_get_url)
        response.raise_for_status()
        all_data = response.json()
        markets = ','.join([data['market'] for data in all_data])
        url = f"https://api.upbit.com/v1/ticker"
        response = requests.get(url, params={"markets": markets})
        print(response.json())
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise ValueError(f"Error fetching data: {str(e)}")
