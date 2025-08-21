import os
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from template import digest
from storage import collector
from typing import List, Any

def Send(listOfNews: List[Any]) -> None:
    smtp_server: str = "smtp.gmail.com"
    EMAIL_USER: str | None = os.getenv("EMAIL_USER") 
    EMAIL_PASS: str | None = os.getenv("EMAIL_PASS")
    TO_EMAIL: str = "ruanrodrigues393@gmail.com"

    msg: MIMEMultipart = MIMEMultipart("alternative")
    msg["Subject"] = "🔒 HackMonitor - The Latest Cybersecurity and IT News"
    msg["From"] = EMAIL_USER
    msg["To"]= TO_EMAIL
    
    try:
        htmlContent: str = digest.Digest(listOfNews)
        msg.attach(MIMEText(htmlContent, "html"))
        with smtplib.SMTP(smtp_server, 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)   
            server.sendmail(EMAIL_USER, TO_EMAIL, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        error_msg: str = f"Error sending email: {e}"
        print(error_msg)
