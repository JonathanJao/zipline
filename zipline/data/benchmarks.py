import numpy as np
import pandas as pd
import pandas_datareader.data as pd_reader

def get_benchmark_returns(symbol, first_date, last_date):
    """
    Get a Series of benchmark returns from Yahoo associated with `symbol`.
    Default is `SPY`.

    Parameters
    ----------
    symbol : str
        Benchmark symbol for which we're getting the returns.

    The data is provided by Yahoo Finance
    """
    # data = pd_reader.DataReader(
    #     symbol,
    #     'yahoo',
    #     first_date,
    #     last_date
    # )
    data = pd.read_csv('/Users/jonatjao/pdev/trade/backtest/SPY.csv', index_col=0, parse_dates=['date'])
    data = data['close']

    data[pd.Timestamp('2008-12-15')] = np.nan
    data[pd.Timestamp('2009-08-11')] = np.nan
    data[pd.Timestamp('2012-02-02')] = np.nan

    data = data.fillna(method='ffill')

    return data.sort_index().tz_localize('UTC').pct_change(1).iloc[1:]
