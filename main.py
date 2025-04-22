from NewsFetcher.fetcher import fetch_wrestling_news
from Summarizer.summarize import summarize_article
from Emailer.send_email import send_email

def main():
    print("🚀 Starting Newsletter Script...")

    print("📡 Fetching articles...")
    try:
        articles = fetch_wrestling_news()
        print(f"✅ Fetched {len(articles)} articles.")
    except Exception as e:
        print(f"❌ Error fetching news: {e}")
        return

    print("✍️ Summarizing articles...")
    summaries = []
    for i, article in enumerate(articles):
        try:
            print(f"📰 Summarizing article {i+1}: {article['title']}")
            summary = summarize_article(article["content"])
            print("✅ Summary created:", summary[:100], "...")
            summaries.append({
                "title": article["title"],
                "url": article["url"],
                "summary": summary
            })
        except Exception as e:
            print(f"❌ Error summarizing article {i+1}: {e}")

    print("📧 Sending email...")
    try:
        status = send_email("📰 Today's Pro Wrestling News", summaries)
        print("✅ Email status:", status)
    except Exception as e:
        print(f"❌ Error sending email: {e}")

if __name__ == "__main__":
    main()
