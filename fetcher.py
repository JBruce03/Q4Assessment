import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def fetch_wrestling_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "WWE OR AEW OR NJPW OR TNA OR AAA OR 'professional wrestling'",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)

    print(response.status_code, response.text)

    if response.status_code != 200:
        raise Exception(f"NewsAPI error: {response.status_code}, {response.text}")

    articles = response.json().get("articles", [])
    cleaned_articles = [
        {"title": a["title"], "url": a["url"], "content": a["content"] or a["description"]}
        for a in articles if a["content"] or a["description"]
    ]
    return cleaned_articles
