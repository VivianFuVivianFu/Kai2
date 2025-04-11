import pandas as pd
import random

# Load your original Excel file
df = pd.read_excel("Final_ICP_Data.xlsx")

# Simulate tracking
df['Email Opened'] = [random.choice(['Yes', 'No']) for _ in range(len(df))]
df['Lead Type'] = df['Email Opened'].apply(lambda x: 'Hot' if x == 'Yes' else 'Cold')

# Save updated file
df.to_excel("Tracked_Leads.xlsx", index=False)
print("📊 Tracking simulation complete — data saved to Tracked_Leads.xlsx")
