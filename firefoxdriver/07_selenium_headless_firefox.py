from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import instagram_password, instagram_login
import pickle

# options
options = webdriver.FirefoxOptions()

# user-agent
options.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# disable webdriver mode
options.set_preference("dom.webdriver.enabled", False)

# headless mode
options.headless = True

driver = webdriver.Firefox(
    executable_path="/home/cain/PycharmProjects/selenium_python/firefoxdriver/geckodriver",
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    driver.get("https://instagram.com/")
    time.sleep(5)

    print("Passing authentication...")
    username_input = driver.find_element_by_name("username")
    username_input.clear()
    username_input.send_keys(instagram_login)
    time.sleep(5)

    password_input = driver.find_element_by_name("password")
    password_input.clear()
    password_input.send_keys(instagram_password)
    time.sleep(5)

    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

    print("Going to the post...")
    video_post = driver.get("https://www.instagram.com/p/your_post/")
    print("Start watching the video...")
    time.sleep(5)

    print("Unmuting audio...")
    unmute_audio = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/span/div")
    unmute_audio.click()
    time.sleep(5)
    print("Finish watching the video...")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
