import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import requests
from sheet_config import log_to_sheet
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! Send me a name like:\n👉 'Find details of Sundar Pichai'")

def search_apollo(person_name):
    url = "https://api.apollo.io/v1/mixed_people/search"
    headers = {"Cache-Control": "no-cache"}
    params = {
        "api_key": APOLLO_API_KEY,
        "q_organization_domains": "",
        "person_titles": "",
        "q_keywords": person_name,
        "page": 1
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx, 5xx)
        
        # Log response for debugging
        print(f"API Response: {response.json()}")
        
        people = response.json().get("people", [])
        results = []
        for p in people[:1]:  # top 1 result
            results.append({
                "name": p.get("name"),
                "title": p.get("title"),
                "company": p.get("organization", {}).get("name"),
                "email": p.get("email_status", {}).get("email") or "N/A",
                "linkedin_url": p.get("linkedin_url")
            })
        return results
    
    except requests.exceptions.RequestException as e:
        print(f"Error with Apollo API request: {e}")
        return []  # Return empty list in case of error


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    person_name = text.replace("Find details of", "").replace("Email of", "").strip()
    await update.message.reply_text(f"🔍 Searching Apollo for **{person_name}**...")
    
    results = search_apollo(person_name)
    print("Search results:", results)  # Log the search results for debugging
    if not results:
        await update.message.reply_text("❌ No results found.")
        return
    msg = ""
    for r in results:
        msg += f"👤 *{r['name']}*\n📌 {r['title']} @ {r['company']}\n📧 {r['email']}\n🔗 [LinkedIn]({r['linkedin_url']})\n"
    
    await update.message.reply_text(msg, parse_mode="Markdown")

    # log to Google Sheet
    print("Logging to sheet with results:", results)
    log_to_sheet(text, results)
    print("Successfully logged to sheet.")




app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print("✅ Bot is running...")
app.run_polling()
