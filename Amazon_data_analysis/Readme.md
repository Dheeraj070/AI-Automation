# Amazon Data Analysis

This project involves scraping, cleaning, and analyzing Amazon product data for soft toys. The analysis focuses on key product metrics such as price, rating, reviews, and brand performance.

## Project Overview

The project consists of two main parts:

1. **Data Scraping**: Extracts product data (price, reviews, ratings, etc.) from Amazon.
2. **Data Cleaning and Analysis**: Processes and analyzes the data to provide insights, including visualizations like bar charts, scatter plots, and pie charts.



## File Structure
```
.
├── amazon_scraper.py     # Script for scraping Amazon data
├── analysis.py           # Script for data analysis and visualization
├── data_cleaning.py      # Cleaning the data
├── main.py               # Main file to run all the files one by one
├── .env                  # Environment variables (API keys)
├── requirements.txt      # List of dependencies
├── chromedriver.exe      # Chromedriver for scrapping through selenium
└── README.md             # Project documentation
```



## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Dheeraj070/AI-Automation
cd Amazon_data_analysis
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
Create a .env file in the project root and add your 2Captcha API Key:
```bash
2CAPTCHA_API_KEY=your_2captcha_api_key  
```


### 4. Run the Scraper
To run, use the following command:
```bash
python main.py
```
