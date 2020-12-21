from selenium import webdriver
import time
from fake_useragent import UserAgent

# url = "https://www.vk.com/"

# options
options = webdriver.FirefoxOptions()

# change useragent
useragent = UserAgent()
options.set_preference("general.useragent.override", useragent.random)

driver = webdriver.Firefox(
    executable_path="/home/cain/PycharmProjects/selenium_python/firefoxdriver/geckodriver",
    options=options
)
# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # driver.save_screenshot("vk.png")
    time.sleep(5)
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
