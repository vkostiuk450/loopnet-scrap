import pandas as pd  
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.chrome.options import Options  
from webdriver_manager.chrome import ChromeDriverManager  
from concurrent.futures import ThreadPoolExecutor  
import time  

# Function to set up and return a Chrome driver instance  
def create_driver():  
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))  

def scrape_property_data(url, title):  
    driver = create_driver()  # Create a new driver for each thread  
    data = {'URL': url, 'Title': title}  # Initialize with URL and Title to track which URL's data is getting scrapped  

    try:  
        driver.get(url)  
        time.sleep(5)  
        elements = driver.find_elements(By.CSS_SELECTOR, "#property-facts > div.property-facts__facts-wrap.property-data > div > div > div > .property-fact-value-container")  

        try:  
            data["Name"] = title  
            address_element = driver.find_element(By.CSS_SELECTOR, "#PropertyTimeStamp > li:nth-child(4) > h4")  
            address = address_element.text.split(":")[1].strip()  
            data["Address"] = address  
        except Exception as e:  
            print(f"Error extracting address for {url}: {e}")  
            data["Address"] = None  # Set to None if address extraction fails  

        for element in elements:  
            try:  
                key = element.find_element(By.CLASS_NAME, "fact-name").text.strip()  
                value = element.find_element(By.CLASS_NAME, "property-facts__data-item-text").text.strip()  
                data[key] = value  
            except Exception as e:  
                print(f"Error processing element for {url}: {e}")  

    except Exception as e:  
        print(f"Unexpected error for {url}: {e}")  
    finally:  
        driver.quit()  

    return data  

def main():  
    urls_df = pd.read_csv('listings.csv')  
    
    # Use ThreadPoolExecutor to parallelize scraping  
    with ThreadPoolExecutor(max_workers=5) as executor:  
        futures = [executor.submit(scrape_property_data, row['URL'], row['Title']) for index, row in urls_df.iterrows()]  
        
        all_property_data = [future.result() for future in futures]  

    # Convert to DataFrame  
    all_property_data_df = pd.DataFrame(all_property_data)  

    # Save to CSV  
    all_property_data_df.to_csv('all_property_data.csv', index=False, encoding='utf-8')  
    print("Scraping complete. Data saved to all_property_data.csv")  

if __name__ == "__main__":  
    main()