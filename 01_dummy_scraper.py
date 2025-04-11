import pandas as pd

# Dummy data based on ICP
data = [
    {
        "Company Name": "TechNova Solutions",
        "Contact Person": "Amit Patel",
        "Industry": "Software",
        "Website": "https://technova.in",
        "Location": "Ahmedabad",
        "Employee Size": "50-100"
    },
    {
        "Company Name": "CodeCraft Labs",
        "Contact Person": "Nisha Rao",
        "Industry": "IT Services",
        "Website": "https://codecraftlabs.com",
        "Location": "Bangalore",
        "Employee Size": "100-200"
    },
    {
        "Company Name": "InnoByte Tech",
        "Contact Person": "Ravi Sharma",
        "Industry": "Web Development",
        "Website": "https://innobyte.com",
        "Location": "Pune",
        "Employee Size": "10-50"
    },
{
        "Company Name": "Wipro Tech",
        "Contact Person": "Sanu kumar",
        "Industry": "Web Development",
        "Website": "https://Wipro.com",
        "Location": "Surat",
        "Employee Size": "10-50"
    },
{
        "Company Name": "Multisoft services",
        "Contact Person": "riya shah",
        "Industry": "Web Development",
        "Website": "https://Multisofr.com",
        "Location": "Ahmedabad",
        "Employee Size": "150-200"
    }
]



# Convert to DataFrame
df = pd.DataFrame(data)

# Export to Excel
df.to_excel("Final_ICP_Data.xlsx", index=False)

print("✅ Dummy data for Task 1 saved as 'Final_ICP_Data.xlsx'")
