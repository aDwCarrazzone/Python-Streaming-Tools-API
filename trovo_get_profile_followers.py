from encodings import utf_8
from multiprocessing.connection import wait
import re
from time import sleep
from urllib import response
import bs4
import requests
from requests_html import AsyncHTMLSession

async def get_trovo_profile_followers_quantity(username: str):
    session = AsyncHTMLSession()
    url = "https://trovo.live/{}".format(username)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # wait for the page to load in seconds
    response = await session.get(url, verify=False, headers=headers)
    await response.html.arender(sleep=40)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    with open("soup.html", "w", encoding="utf_8") as f:
        f.write(soup.prettify())
    i = soup.find("i", class_="vertical-bar")
    # get the div of i
    div = i.find_parent("div")
    spans = []
    for span in div.find_all("span"):
        spans.append(span.text)
        print(span.text)
    return {"followers": spans[2]}



    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # asession = AsyncHTMLSession()
    # r = await asession.get("https://trovo.live/{}".format(username), verify=False, headers=headers)
    # await r.html.arender(wait=1,sleep=1)
    # soup = bs4.BeautifulSoup(r.html.html, "html.parser")
    # with open("soup.html", "w", encoding="utf_8") as f:
    #     f.write(soup.prettify())
    # i = soup.find("i", class_="vertical-bar")
    # print(i)
    # print(i)
    # print(i)
    # # div = i.find_parent("div")
    # # spans = []
    # # for span in div.find_all("span"):
    # #     spans.append(span.text)
    # # return({"followers": spans[2]})   
    # return({"followers": "test"})

    # s = AsyncHTMLSession()
    # response = await s.get("https://trovo.live/{}".format(username))
    # await response.html.render(wait=1,sleep=1)
    # soup = bs4.BeautifulSoup(response.html.html, "html.parser")
    # await response.close()
    # print(soup)
    # return {"profile_followers": "123"}

    # session = requests.Session()
    # url = "https://trovo.live/{}".format(username)
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    # # wait for the page to load in seconds
    # response = session.get(url, verify=False, headers=headers)
    # soup = bs4.BeautifulSoup(response.text, "html.parser")
    # i = soup.find("i", class_="vertical-bar")
    # # get the div of i
    # div = i.find_parent("div")
    # spans = []
    # for span in div.find_all("span"):
    #     spans.append(span.text)
    #     print(span.text)
    # return {"followers": spans[1]}