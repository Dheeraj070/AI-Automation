# This a test file for debugging for development purposes
# This file is not intended to be used in production

import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

def search_apollo(person_name):
    url = "https://api.apollo.io/api/v1/mixed_people/search"
    headers = {
        "Content-Type": "application/json", 
        "Cache-Control": "no-cache",
        "X-Api-Key": APOLLO_API_KEY
    }
    
    # Setup request body for POST
    data = {
        "q_keywords": person_name,  # Search by person name
        "per_page": 1  # Limit to one result for simplicity
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        people = response.json().get("people", [])
        results = []
        for p in people[:1]:  # Only take the top result
            results.append({
                "name": p.get("name"),
                "title": p.get("title"),
                "company": p.get("organization", {}).get("name", "N/A"),
                "email": p.get("email_status", {}).get("email") or "N/A",
                "linkedin_url": p.get("linkedin_url") or "N/A"
            })
        return results
    else:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)
        return []

# Example usage
person_name = "Sundar Pichai"
results = search_apollo(person_name)
print(results)
