from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Prepare lists to store the data
    titles = []
    urls = []

    # Open the target URL
    for i in range(1, 21):
        url = f"https://www.loopnet.com/search/industrial-space/usa/for-lease/{i}/?sk=9ca28d15134ff54831916f7ace15b2df&e=u"
        driver.get(url)

        # Allow time for the page to load JavaScript content
        time.sleep(5)

        # Locate the elements using the CSS selector
        listings = driver.find_elements(
            By.CSS_SELECTOR,
            "#placardSec > div.placards > ul > li > article > header > div.header-col.header-left a",
        )

        seen_urls = set()

        # Extract title and URL for each listing
        for listing in listings:
            title = listing.get_attribute("title")
            link = listing.get_attribute("href")
            if link not in seen_urls:
                titles.append(title)
                urls.append(link)
                seen_urls.add(link)
                print(f"Title: {title}, URL: {link}")
        
        print(f"\nCount: ${len(urls)}")
        print("-----------------------------------------")

        # Create a DataFrame using the extracted data
        df = pd.DataFrame({"Title": titles, "URL": urls})

        # Save the DataFrame to a CSV file
        df.to_csv("listings.csv", index=False, encoding="utf-8")

    for i in range(1, 8):
        url = f"https://www.loopnet.com/search/industrial-space/usa/for-sale/{i}/?sk=61ad41e54818c8be6d459809951f6196"
        driver.get(url)

        # Allow time for the page to load JavaScript content
        time.sleep(5)

        # Locate the elements using the CSS selector
        listings = driver.find_elements(
            By.CSS_SELECTOR,
            "#placardSec > div.placards > ul > li > article > header > div.header-col.header-left a",
        )

        seen_urls = set()

        # Extract title and URL for each listing
        for listing in listings:
            title = listing.get_attribute("title")
            link = listing.get_attribute("href")
            if link not in seen_urls:
                titles.append(title)
                urls.append(link)
                seen_urls.add(link)
                print(f"Title: {title}, URL: {link}")

        
        print(f"\nCount: ${len(urls)}")
        print("-----------------------------------------")

        # Create a DataFrame using the extracted data
        df = pd.DataFrame({"Title": titles, "URL": urls})

        # Save the DataFrame to a CSV file
        df.to_csv("listings.csv", index=False, encoding="utf-8")

    for i in range (7, 21):
        url = f"https://www.loopnet.com/search/industrial-space/usa/for-sale/{i}/?sk=61ad41e54818c8be6d459809951f6196"
        driver.get(url)

        # Allow time for the page to load JavaScript content
        time.sleep(5)

        # Locate the elements using the CSS selector
        listings = driver.find_elements(
            By.CSS_SELECTOR,
            "#placardSec > div.placards > ul:nth-child(3) > li > article > div.placard-content.show-logos > header a",
        )

        seen_urls = set()

        # Extract title and URL for each listing
        for listing in listings:
            title = listing.get_attribute("title")
            link = listing.get_attribute("href")
            if link not in seen_urls:
                titles.append(title)
                urls.append(link)
                seen_urls.add(link)
                print(f"Title: {title}, URL: {link}")

        print(f"\nCount: ${len(urls)}")
        print("-----------------------------------------")

        # Create a DataFrame using the extracted data
        df = pd.DataFrame({"Title": titles, "URL": urls})

        # Save the DataFrame to a CSV file
        df.to_csv("listings.csv", index=False, encoding="utf-8")

    for i in range(1, 3):
        url = f"https://www.loopnet.com/search/industrial-space/usa/auctions/{i}/?sk=ac57cc1c07775b86c9baa03fcae59c4c"
        driver.get(url)

        # Allow time for the page to load JavaScript content
        time.sleep(5)

        # Locate the elements using the CSS selector
        listings = driver.find_elements(
            By.CSS_SELECTOR,
            "#placardSec > div.placards > ul > li > article > header > div.header-col.header-left a",
        )

        seen_urls = set()

        # Extract title and URL for each listing
        for listing in listings:
            title = listing.get_attribute("title")
            link = listing.get_attribute("href")
            if link not in seen_urls:
                titles.append(title)
                urls.append(link)
                seen_urls.add(link)
                print(f"Title: {title}, URL: {link}")

        print(f"\nCount: ${len(urls)}")
        print("-----------------------------------------")

        # Create a DataFrame using the extracted data
        df = pd.DataFrame({"Title": titles, "URL": urls})

        # Save the DataFrame to a CSV file
        df.to_csv("listings.csv", index=False, encoding="utf-8")

finally:
    # Close the WebDriver
    driver.quit()
