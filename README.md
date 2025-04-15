# sales-process-automation

Sales Process Automation using Python is a complete, modular automation solution designed to streamline lead generation, personalized outreach, and basic lead tracking for marketing and business development teams.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🚀 Objectives
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Automate personalized email creation for potential clients using Jinja2 templating.
 
- Send emails directly via Gmail using secure app password and SMTP.
  
- Securely store sensitive credentials using `.env` file.
  
- Enhance scalability and reusability for future CRM and marketing integrations.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


✨ Features
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-  Extract contact details from Excel files.
 
-  Generate personalized email content with company and contact info.
  
-  Send HTML emails automatically using Gmail SMTP.
  
-  Skip and notify if email ID is missing.
  
-  Secure environment using `.env` file (never exposed to GitHub).
  
-  Log success/failure of each sent email.



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🛠️ Tech Stack
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- **Python** (Core Language)
  
- **Pandas** (Data Processing)
  
- **Jinja2** (Email Template Rendering)
  
- **smtplib & email** (Email Sending)
 
- **dotenv** (Environment Variable Handling)
  
- **Excel (.xlsx)** (Data Source)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📁 Project Structure
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


sales-process-automation/

├── .env                        # Environment variables (email, password) — kept secret

├── .gitignore                  # Files/folders ignored by Git (includes .env, __pycache__, etc.)

├── chromedriver.exe            #  ChromeDriver for scraping 

├── email_template.html         # Jinja2 HTML template for personalized email content

├── Final_ICP_Data.xlsx         # Excel sheet containing client/company data

├── generate.py                 # Script to generate emails from Excel and template

├── send_email.py               # Script to send emails via Gmail SMTP

├── README.md                   # Project documentation 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Demo Video
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

https://www.loom.com/share/07fd3052ac2e49f5a2b270765084f800?sid=482342c9-91ba-418f-ab95-a62b4696723a



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------








✩ How to Run
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Setup

Install the required packages:

pip install pandas beautifulsoup4 selenium openpyxl jinja2 fake-useragent python-dotenv


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
✨ Execution Order:
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Run linkedin_scraper.py or use dummy Excel file

Run generate_emails.py to create HTML emails

Run send_emails.py to launch email campaign

Run track_leads.py to simulate and categorize lead response analytics





------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📈 Future Scope 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This Python-based automation can be extended into an AI/ML-powered system. Future features may include:

Lead Scoring using ML: Score leads based on behavior, industry, engagement

Email Sentiment Analysis (NLP): Detect reply tone (positive/negative)

Smart Reply Generator: Use GPT APIs to auto-generate smart replies

Reply Prediction Model: Predict likelihood of reply from lead

Lead Clustering: Use unsupervised ML to find similar high-quality leads

These upgrades can turn this into a complete AI-driven sales assistant platform ✨



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🧠 Skills Demonstrated
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Python scripting and modular coding  
- Web scraping using BeautifulSoup and requests  
- Email automation using smtplib and email.message  
- Secure credential management via `.env`  
- Personalized email generation using HTML templates  
- Data analytics with pandas  
- Lead categorization based on engagement  
- GitHub documentation and video demo submission




 


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

👩‍💻 Developed By
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Krisha Baldha

B.Tech IT Engineering |  Python Enthusiast

















