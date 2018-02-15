from selenium import webdriver
import pandas as pd
import json

def format_date(date):
    year = str(date.year)
    month = str(date.month)
    if len(month) < 2:
        month = "0" + month
    day = str(date.day)
    if len(day) < 2:
        day = "0" + day
    return year + '-' + month + '-' + day


def get_price_data(startdate, enddate):
    """
    returns a dataframe containing btc price data on every day between startdate and enddate
    :param startdate:
    :param enddate:
    :return:
    """
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=' + startdate + '&end=' + enddate
    driver.get(url)
    body = driver.find_element_by_tag_name("body")
    text = json.loads(body.text)

    timeindex = pd.DatetimeIndex(freq='d', start=startdate, end=enddate)
    data = pd.DataFrame()

    for date in timeindex:
        fdate = format_date(date)
        data.at[date, 'price'] = text['bpi'][fdate]
    return data


driver = webdriver.Firefox()

begin = '2015-02-01'
fin = '2018-02-13'

data = get_price_data(begin, fin)

data.to_csv(path_or_buf='data/price_data.csv')

driver.quit()
