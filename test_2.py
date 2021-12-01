from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.shell.com/investors/results-and-reporting/quarterly-results.html")
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "equity_underlyingVal")))
# nifty = driver.find_element(By.XPATH, '//*[@id="equity_underlyingVal"]').text
# time_stamp = driver.find_element(By.XPATH, '//*[@id="equity_timeStamp"]').text

driver.quit()