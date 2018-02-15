# -*- coding: utf-8 -*-

"""Main module."""

from selenium import webdriver
import json
import numpy as np
import pandas as pd
import matplotlib as plt


def get_reddit_data(subreddit, date):
    """
    :param subreddit: in the form 'r/subreddit'
    :param date:      date to scrape data from in form YYYYMMDD
    :return:
    Retrieves titles from given subreddit on given day
    """
    pass


def preprocess_text(data, date):
    """
    :param data:
    :param date:
    :return:
    Returns VECTORIZED/SENTIMENT of given data
    """
    pass


def get_historical_prices(date):
    """
    :param date:      day on which we want price data for
    :return:
    Retrieves BTC price on given date
    """
    pass

def perform_sentiment_analysis(textdf):
    """
    Given a dataframe of short text snippets, return a df of sentiment analysis ratings
    :param textdf:
    :return:
    """

def perform_regression(data):
    """
    N/A
    :param data:
    :return:
    """