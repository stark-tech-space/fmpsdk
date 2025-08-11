import typing

from .url_methods import (
    __return_json_stable,
    __validate_statistics_type,
    __validate_technical_indicators_time_delta,
)


def technical_indicators(
    apikey: str,
    symbol: str,
    period: int = 10,
    statistics_type: str = "sma",
    time_delta: str = "1day",
    from_date: str = None,
    to_date: str = None,
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Query FMP /technical_indicator/ API.

    :param apikey: Your API key
    :param symbol: Company ticker
    :param period: period length for the indicator, e.g. 10, 20, 50, etc.
    :param statistics_type: different types of statistics(lower case), e.g. 'sma', 'ema', 'rsi', etc.
    :param time_delta: '1day' or intraday: '1min' - '4hour'
    :param from_date: Date to start from.  YYYY-MM-DD
    :param to_date: Date to end at.  YYYY-MM-DD
    :return:
    """
    if not symbol:
        raise ValueError("symbol must be provided")
    if period is None or int(period) <= 0:
        raise ValueError("period must be a positive integer")
    if not statistics_type:
        raise ValueError("statistics_type must be provided")
    
    stat_type = __validate_statistics_type(statistics_type.lower())
    path = f"technical-indicator/{stat_type}/"
    
    query_vars = {
        "symbol": symbol,
        "apikey": apikey,
        "periodLength": period,
        "timeframe": __validate_technical_indicators_time_delta(time_delta),
    }

    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date

    return __return_json_stable(path=path, query_vars=query_vars)
