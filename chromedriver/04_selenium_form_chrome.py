from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import vk_password

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

driver = webdriver.Chrome(
    executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("https://vk.com/")
    time.sleep(5)

    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys("79623618753")
    time.sleep(5)

    password_input = driver.find_element_by_id("index_pass")
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)

    # login_button = driver.find_element_by_id("index_login_button").click()
    time.sleep(10)

    news_link = driver.find_element_by_id("l_nwsf").click()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
