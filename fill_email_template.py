# import pandas as pd
# from jinja2 import Template
#
# # Load data
# df = pd.read_excel("Final_ICP_Data.xlsx")
#
# # Load the email template
# with open("email_template.html", "r", encoding="utf-8") as f:
#     template_content = f.read()
#
# template = Template(template_content)
#
# # Generate personalized emails
# for index, row in df.iterrows():
#     email_content = template.render(
#         recipient_name=row.get("Contact Person", "there"),
#         company_name=row.get("Company Name", "your company")
#     )
#
#     # Save each email as HTML
#     filename = f"output_email_{index + 1}.html"
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write(email_content)
#
#     print(f"✅ Saved: {filename}")
#
# print("✅ All personalized emails generated successfully!")







from jinja2 import Template

def fill_template(name, company):
    try:
        with open("email_template.html", "r", encoding="utf-8") as f:
            template_content = f.read()
        template = Template(template_content)
        return template.render(recipient_name=name, company_name=company)
    except Exception as e:
        print(f"❌ Error generating email content: {e}")
        return ""
