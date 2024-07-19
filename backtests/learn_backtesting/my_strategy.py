from typing import Optional

import numpy as np

from backtesting import Strategy

from .my_indicators import sma


class MyStrategy(Strategy):
    lower_bound: int = 8
    upper_bound: int = 16
    
    def init(self):
        print(self.lower_bound)
        print(self.upper_bound)
        self.entry = self.I(sma, self.data.df, self.lower_bound, self.upper_bound)
    
    def next(self):
        if self.entry == 1:
            self.position.close()
            self.buy()
        elif self.entry == 0:
            pass
        elif self.entry == -1:
            self.position.close()
            self.sell()
