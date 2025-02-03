import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Target website (Replace with your desired site)
URL = "https://example.com/products"

# Headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Create data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

def scrape_website():
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Example: Scrape product data (Modify selectors based on target site)
    products = []
    for item in soup.select(".product-item"):
        title = item.select_one(".product-title").get_text(strip=True)
        price = item.select_one(".product-price").get_text(strip=True)
        link = item.select_one("a")["href"]
        
        products.append({"Title": title, "Price": price, "Link": link})
    
    # Save data to CSV
    df = pd.DataFrame(products)
    df.to_csv("data/scraped_data.csv", index=False)
    print("Data saved to data/scraped_data.csv")

if __name__ == "__main__":
    scrape_website()
