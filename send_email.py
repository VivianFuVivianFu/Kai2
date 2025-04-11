import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# 🔐 Load credentials from .env file
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# 📩 Create the email
msg = EmailMessage()
msg['Subject'] = 'Test Email from Python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'receiver@example.com'  # <-- Replace with the recipient's email
msg.set_content('Hi there,\n\nThis is a test email sent using Python and Gmail App Password!')

# 📬 Send the email using Gmail SMTP
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("✅ Email sent successfully!")
