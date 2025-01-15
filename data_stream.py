import requests
import pandas as pd


class DataStream:
    def __init__(self, symbol="BTCUSDT", interval="1m"):
        self.symbol = symbol
        self.interval = interval
        self.base_url = "https://api.binance.com/api/v3/klines"

    def get_data(self, limit=100):
        params = {
            "symbol": self.symbol,
            "interval": self.interval,
            "limit": limit
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data, columns=[
                "open_time", "open", "high", "low", "close", "volume",
                "close_time", "quote_asset_volume", "number_of_trades",
                "taker_buy_base", "taker_buy_quote", "ignore"
            ])
            df["close"] = pd.to_numeric(df["close"])
            return df[["open_time", "close"]]
        else:
            raise Exception(f"Error fetching data: {response.status_code}")