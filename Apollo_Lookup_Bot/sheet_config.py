import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def connect_sheet(sheet_name="Apollo Lookup Log"):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1

def log_to_sheet(prompt, results):
    sheet = connect_sheet()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for res in results:
        row = [
            now,
            prompt,
            res.get("name", ""),
            res.get("title", ""),
            res.get("company", ""),
            res.get("email", ""),
            res.get("linkedin_url", "")
        ]
        print("Adding row:", row)  # 👈 Add this line
        sheet.append_row(row)