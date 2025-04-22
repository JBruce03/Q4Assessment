import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_article(article_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes professional wrestling news articles for a newsletter."
                },
                {
                    "role": "user",
                    "content": f"Summarize the following wrestling article in 2-3 sentences:\n\n{article_text}"
                }
            ],
            max_tokens=150,
            temperature=0.5
        )

        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error summarizing article: {e}"
