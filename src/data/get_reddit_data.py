from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

def get_reddit_data(subreddit, date):
    """
    Gets top 26 frontpage titles from 'subreddit' on 'date
    :param subreddit:   ex: 'r/bitcoin'
    :param date:        in 'YYYYMMDD'
    :return titles:     a list of strings of titles
    """
    titles = []

    url = "https://web.archive.org/web/" + date + "/reddit.com/" + subreddit
    print(url)
    driver.get(url)

    try:
        sitetable = driver.find_element_by_id("siteTable")
        posts = sitetable.find_elements_by_tag_name("div")

        for post in posts:
            if len(post.find_elements_by_class_name("title")) > 0:
                title = post.find_element_by_class_name("title").text
                titles.append(title)
        titles = set(titles)
        return titles
    except NoSuchElementException:
        return ['0'] * 26


def format_date(date):  # for way-way-back machine urls
    """
    Reformats date so that wayback machine will like it
    :param date:  in datetime64
    :return:
    """
    year = str(date.year)
    month = str(date.month)
    if len(month) < 2:
        month = "0" + month
    day = str(date.day)
    if len(day) < 2:
        day = "0" + day
    return year + month + day


def get_reddit_dataframe(begin, fin, subreddit, writefile):
    """
    Makes a big dataframe indexed by a DatetimeIndex for every day from begin to fin. Values are top reddit posts, columns
        separate titles on a given day/row.
    :param begin:       starting date of dataframe
    :param fin:         ending date of dataframe
    :param subreddit:   subreddit to scrape
    :return:            none
    """
    timeindex = pd.DatetimeIndex(freq='d', start=begin, end=fin)
    data = pd.DataFrame()
    for date in timeindex:
        fdate = format_date(date)
        titles = get_reddit_data(subreddit, fdate)
        i = 1
        for title in titles:   # probably can do this without a for loop
            data.at[date, i] = title
            i += 1
        data.to_csv(path_or_buf=writefile)


driver = webdriver.Firefox()
subreddit = 'r/bitcoin'
begin = '2018-01-31'
fin = '2018-02-13'
writefile = 'data/text/2018_2_14_832.csv'

get_reddit_dataframe(begin, fin, subreddit, writefile)

driver.quit()


# pd.read_csv(filepath_or_buffer='test_data/redditData.csv', infer_datetime_format=True)
