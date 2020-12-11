from .settings import DEFAULT_LIMIT
from .url_methods import return_json
import typing


def earning_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP /earning_calendar/ API.

    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"earning_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)


def historical_earning_calendar(apikey: str, symbol: str, limit: int = DEFAULT_LIMIT) -> typing.List[typing.Dict]:
    """
    Query FMP /historical/earning_calendar/ API.

    :param apikey: Your API key.
    :param symbol: Company ticker.
    :param limit: Number of rows to return.
    :return: A list of dictionaries.
    """
    path = f"historical/earning_calendar/{symbol}"
    query_vars = {
        "apikey": apikey,
        "symbol": symbol,
        "limit": limit,
    }
    return return_json(path=path, query_vars=query_vars)


def ipo_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP /ipo_calendar/ API.

    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"ipo_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)


def stock_split_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP /stock_split_calendar/ API.

    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"stock_split_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)


def dividend_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP /stock_dividend_calendar/ API.

    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"stock_dividend_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)


def economic_calendar(apikey: str, from_date: str = None, to_date: str = None) -> typing.List[typing.Dict]:
    """
    Query FMP /economic_calendar/ API.

    :param apikey: Your API key.
    :param from_date: 'YYYY:MM:DD'
    :param to_date: 'YYYY:MM:DD'
    :return: A list of dictionaries.
    """
    path = f"economic_calendar"
    query_vars = {
        "apikey": apikey,
    }
    if from_date:
        query_vars['from'] = from_date
    if to_date:
        query_vars['to'] = to_date
    return return_json(path=path, query_vars=query_vars)
