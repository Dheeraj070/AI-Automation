# amazon_scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from requests.exceptions import ReadTimeout
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import time
import os
from dotenv import load_dotenv

load_dotenv()
api_key= os.getenv("2CAPTCHA_API_KEY")

# Function to solve the captcha using 2Captcha API
def solve_captcha():
    google_key = "6Lefh7oUAAAAANgUdfL83YgF8qErZoOHP6Uxg7vv"  # Replace with the actual Google reCAPTCHA site key
    page_url = "https://www.amazon.in/"  # Replace with the actual URL

    url = "http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(api_key, google_key, page_url)    
    response = requests.get(url)
    request_id = response.text.split('|')[1]

    solution = requests.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(api_key, request_id))
    captcha_answer = solution.text.split('|')[1]
    
    return captcha_answer


def scrape_amazon_soft_toys():
    url = "https://www.amazon.in/"

    # Initialize Selenium
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # for running without UI
    # Path to chromedriver in the same directory
    driver_path = os.path.join(os.getcwd(), "chromedriver.exe")
    service = Service(driver_path)    
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(3)  # allow JS to load

    # Check if CAPTCHA is present (by checking if CAPTCHA element exists)
    try:
        captcha_element = driver.find_element(By.ID, "g-recaptcha-response")
        if captcha_element:
            captcha_solution = solve_captcha()  # Use 2Captcha to solve CAPTCHA
            driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML='{captcha_solution}';")
            driver.find_element(By.ID, 'recaptcha-verify-button').click()  # Click the verify button after filling CAPTCHA
            time.sleep(5)  # Wait for CAPTCHA to be processed
    except Exception as e:
        print("No CAPTCHA detected, continuing with scraping.")

    # Find the search bar and submit query
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("soft toys")
    try:
        search_box.send_keys(Keys.RETURN)
    except ReadTimeout:
        print("Timeout occurred while sending keys. Retrying...")
        time.sleep(5)
        search_box.send_keys(Keys.RETURN)
    
    time.sleep(3)  # wait for results to load

    # Scroll to load more products
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 3000)")
        time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    data = []
    sponsored_blocks = soup.select('[data-component-type="s-search-result"]')
    total_sponsored = 0
    for item in sponsored_blocks:
        sponsored_tag = item.find(string=lambda s: s and "Sponsored" in s)
        if sponsored_tag:
            print("Sponsored product found:", sponsored_tag)
            total_sponsored += 1
            continue  # Skip sponsored

        if item.h2 and item.h2.a:
            title = item.h2.text.strip()
            product_url = "https://www.amazon.in" + item.h2.a['href']
        else:
            title = None
            product_url = None
        brand = item.select_one('.s-line-clamp-1')  # heuristic for brand
        brand = brand.text.strip() if brand else None
        rating = item.select_one('.a-icon-alt')
        rating = rating.text.split()[0] if rating else None
        reviews = item.select_one('[aria-label$="ratings"]')
        reviews = reviews.text.replace(',', '') if reviews else '0'
        price_whole = item.select_one('.a-price-whole')
        price_fraction = item.select_one('.a-price-fraction')
        price = (price_whole.text + price_fraction.text) if price_whole and price_fraction else None
        image = item.select_one('.s-image')
        image_url = image['src'] if image else None

        print("Sponsored product found:", title)
        data.append({
            "Title": title,
            "Brand": brand,
            "Rating": rating,
            "Reviews": reviews,
            "Selling Price": price,
            "Product URL": product_url,
            "Image URL": image_url
        })
        print("Total sponsored products:", len(data))


    # Save to CSV
    df = pd.DataFrame(data)
    df.to_csv("sponsored_soft_toys.csv", index=False)
    print(f"[Success] Scraped {len(df)} sponsored products.")
    return df


scrape_amazon_soft_toys()