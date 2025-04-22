import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")

def send_email(subject, summaries):
    content = "<h2>📰 Today's Pro Wrestling News</h2><ul>"
    for item in summaries:
        content += f"<li><strong>{item['title']}</strong><br>{item['summary']}<br><a href='{item['url']}'>Read more</a></li><br>"
    content += "</ul>"

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject=subject,
        html_content=content
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return f"Email sent! Status code: {response.status_code}"
    except Exception as e:
        return f"Error sending email: {e}"
