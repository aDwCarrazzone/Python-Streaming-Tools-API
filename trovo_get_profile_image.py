import bs4
import requests

async def get_trovo_profile_image_url(username: str):
    session = requests.Session()
    session.max_redirects = 100
    url = "https://trovo.live/{}".format(username)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = session.get(url, verify=False, headers=headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    div = soup.find("div", class_="streamer-wrap")
    img = div.find("img", class_="img-face")
    src = img.get("src")
    # return a html image tag
    return src