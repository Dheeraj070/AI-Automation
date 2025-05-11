# Apollo Lookup Bot

This project is a Telegram bot that integrates with the Apollo API to search for people based on their name and provide details like their title, company, email, and LinkedIn profile. The bot logs each query and the results to a Google Sheet.

## Features

- **Telegram Bot**: Responds to users with detailed information about a person based on a given name.
- **Apollo API Integration**: Searches for people using the Apollo People API.
- **Google Sheets Logging**: Logs each search query and the results to a Google Sheet for tracking purposes.
- **Error Handling**: If no results are found, the bot informs the user.



## Requirements

- Python 3.8+
- Install dependencies from `requirements.txt`.



## File Structure

```bash
.
├── main.py               # Main bot script
├── sheet_config.py       # Configuration for Google Sheets logging
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables (API keys)
├── credentials.json      # Google Sheets API credentials
└── README.md             # Project documentation
```



## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Dheeraj070/AI-Automation
cd Apollo_Lookup_Bot
```

### 2. Install dependencies

- Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
- Install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a .env file in the project root and add your Apollo API key and Telegram Bot token:
```bash
APOLLO_API_KEY=your_apollo_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### 4. Configure Google Sheets
Make sure you have access to Google Sheets API and create the necessary credentials for Google Sheets integration.
- Go to Google Developers Console.
- Create a new project or select an existing project.
- Enable the Google Sheets API.
- Download the credentials.json and place it in the project directory.

### 5. Run the Bot
To run the bot, use the following command:
```bash
python main.py
```
The bot will now start and listen for incoming messages on Telegram.

### 6. Test the Bot
Once the bot is running, you can test it by sending a message like:


