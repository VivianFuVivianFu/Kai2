# import pandas as pd
# from fill_email_template import fill_email_template as fill_template
#
# # from fill_email_template import fill_template
# from send_email import send_email
#
# # Load lead data
# df = pd.read_excel("Final_ICP_Data.xlsx")
#
# for index, row in df.iterrows():
#     name = row["Name"]
#     company = row["Company"]
#     email = row["Email"]
#
#     # Generate personalized email content
#     subject = f"Opportunity for {company}"
#     email_body = fill_template(name, company)
#
#     # Send the email
#     sent = send_email(email, subject, email_body)
#
#     if sent:
#         print(f"✅ Email sent to {name} ({company})")
#     else:
#         print(f"❌ Failed to send email to {name} ({company})")




import pandas as pd
from fill_email_template import fill_template
from send_email import send_email

# Load lead data
df = pd.read_excel("Final_ICP_Data.xlsx")

for index, row in df.iterrows():
    name = row.get("Contact Person", "there")
    company = row.get("Company Name", "your company")
    email = row.get("Email", "demo@example.com")  # Replace with actual column if available

    subject = f"Opportunity for {company}"
    html_body = fill_template(name, company)

    sent = send_email(email, subject, html_body)

    if sent:
        print(f"✅ Email sent to {name} ({company})")
    else:
        print(f"❌ Failed to send email to {name} ({company})")

print("📬 All emails sent successfully.")
