from typing import Optional, Tuple
import re
import requests

# Function to extract user information from the message
def extract_user_info(message: str) -> Optional[Tuple[str, str]]:
    # Regex to find email in the message
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    email_match = re.search(email_pattern, message)
    
    if email_match:
        email = email_match.group(0)
        interest = " ".join(message.split())  # Assuming the entire message indicates interest
        return email, interest
    return None

# Function to log lead information to Supabase or Airtable
def log_lead(email: str, interest: str) -> None:
    # Example for logging to Supabase
    supabase_url = "https://your-supabase-url.supabase.co/rest/v1/leads"
    supabase_api_key = "your-supabase-api-key"
    
    headers = {
        "Authorization": f"Bearer {supabase_api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "email": email,
        "interest": interest
    }
    
    response = requests.post(supabase_url, headers=headers, json=data)
    
    if response.status_code == 201:
        print("Lead logged successfully.")
    else:
        print("Failed to log lead:", response.text)