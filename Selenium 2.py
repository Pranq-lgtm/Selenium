from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options

# Setup Edge driver with automatic management
service = Service(r"C:/Users/neela/Downloads/edgedriver_win64 (1)/msedgedriver.exe")

# Configure Edge options
edge_options = Options()
edge_options.use_chromium = True

# Ensure we're using Chromium-based Edge
edge_options.add_argument("--start-maximized")# Start browser maximized

# Initialize the Edge driver
driver = webdriver.Edge(service=service, options=edge_options)

try:
    # Navigate to Bing
    driver.get("https://www.bing.com")

    # Locate the search box and perform a search
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python Edge WebDriver")
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    driver.implicitly_wait(20)

    # Print the page title
    print("Page title:", driver.title)

    # Print the first result title
    first_result = driver.find_element(By.CSS_SELECTOR, "h2 a")

    print("First result:", first_result.text)

finally:
    # Close the browser
    driver.quit()
