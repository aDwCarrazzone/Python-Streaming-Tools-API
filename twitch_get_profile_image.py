import bs4
import requests

async def get_twitch_profile_image_url(username: str):
    try:
        session = requests.Session()
        session.max_redirects = 100
        url = "https://www.twitch.tv/{}".format(username)
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        response = session.get(url, verify=False, headers=headers)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        # find meta content with name="twitter:image"
        meta_content = soup.find("meta", {"name": "twitter:image"})
        # get the content attribute of the meta tag
        profile_image_url = meta_content.get("content")
        return(profile_image_url)
    except Exception as error:
        print("Error getting profile image url, i got the error:", error)
        return("ERROR")