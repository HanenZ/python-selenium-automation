from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')
sleep(2)
#accept the cookies
driver.find_element(By.CSS_SELECTOR, '[class="QS5gu sy4vM"]').click()

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('computer')

# wait for 4 sec
sleep(4)

# click search button
driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'computer' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
