import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_target_products():
    # Setup Chrome WebDriver (you'll need to have chromedriver installed)
    driver = webdriver.Chrome()

    try:
        # Navigate to the Target URL
        url = "https://www.target.com/c/frozen-foods-kids/-/N-rb4pu"
        driver.get(url)

        # Wait for products to load (adjust timeout as needed)
        time.sleep(5)  # Allow time for dynamic content to load

        # Wait for product elements to be present
        wait = WebDriverWait(driver, 10)
        products = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '[data-test="product-title"]')))

        # Extract product names
        product_names = []
        for product in products:
            product_names.append(product.text)

        return product_names

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    finally:
        driver.quit()


def main():
    print("Fetching products from Target...")
    products = get_target_products()

    print("\nFound Products:")
    for i, product in enumerate(products, 1):
        print(f"{i}. {product}")


if __name__ == "__main__":
    main()