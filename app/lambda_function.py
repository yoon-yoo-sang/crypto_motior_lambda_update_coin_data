from app.data_conn import session
from app.data_fetcher import fetch_coin_data, get_coin, get_all_coins
from app.data_processor import process_data
from app.data_store import store_data
from app.logger import logger


def lambda_handler(event, context):
    try:
        coins = get_all_coins()
        coin_price_datas = fetch_coin_data(coins)
        new_datas = []

        for index, coin in enumerate(coins):
            coin_price_data = coin_price_datas[index]
            processed_data = process_data(coin_price_data)
            store_data(coin, processed_data, new_datas)

        session.bulk_save_objects(new_datas)
        session.commit()

        return {
            'statusCode': 200,
            'body': 'Data updated successfully'
        }
    except Exception as e:
        logger.error(f"Error in lambda_handler: {str(e)}")
        return {
            'statusCode': 500,
            'body': 'Internal server error'
        }
