# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# # options.add_argument('--headless')
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# driver.get("https://www.nseindia.com/option-chain")
# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "equity_underlyingVal")))
# nifty = driver.find_element(By.XPATH, '//*[@id="equity_underlyingVal"]').text
# time_stamp = driver.find_element(By.XPATH, '//*[@id="equity_timeStamp"]').text
# print(nifty,time_stamp)
# driver.quit()

score = input("Enter Score: ")

if float(score) >= 0.9:
    print("A")
elif float(score)>=0.8:
    print('B')
elif float(score)>=0.7:
    print('C')
elif float(score)>=0.6:
    print('D')
else:
    print('F')

# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F