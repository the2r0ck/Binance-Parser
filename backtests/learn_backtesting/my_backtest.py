import numpy as np
import pandas as pd
from backtesting import Backtest

from .my_strategy import MyStrategy


def load_data(symbol):
    df = pd.read_csv(f"backtests/data/{symbol}.csv")
    df["time_open"] = pd.to_datetime(df.time_open)
    df.set_index("time_open", inplace=True)
    df.sort_index(inplace=True)
    df.rename(columns={"open": "Open"}, inplace=True)
    df.rename(columns={"high": "High"}, inplace=True)
    df.rename(columns={"low": "Low"}, inplace=True)
    df.rename(columns={"close": "Close"}, inplace=True)
    df.rename(columns={"volume": "Volume"}, inplace=True)
    return df
    


if __name__ == "__main__":
    symbol = "BTCUSDT"
    df = load_data(symbol)
    
    bt = Backtest(df.iloc[:1000], MyStrategy, cash=1_000_000, commission=.01)
    
    bounds = tuple(2 ** i for i in range(1, 9))

    stats = list()

    for lower_bound in bounds:
        for upper_bound in bounds:
            if lower_bound >= upper_bound:
                continue
            stat, heatmap = bt.optimize(
                lower_bound=(lower_bound, ),
                upper_bound=(upper_bound, ),
                constraint=lambda params: params["lower_bound"] < params["upper_bound"],
                return_heatmap=True
            )
            stats.append((stat, heatmap))
    print(stats)

    # bt.plot()