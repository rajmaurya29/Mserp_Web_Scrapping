from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Path to Brave browser executable
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# Configure options for Brave
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Initialize WebDriver with Brave
driver = webdriver.Chrome(options=options)

# Example: Open Google and search for something
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Hello Brave Browser!")
search_box.send_keys(Keys.RETURN)

# Close the browser
driver.quit()
