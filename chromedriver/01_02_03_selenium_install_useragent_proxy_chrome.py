# from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = "https://www.instagram.com/"

user_agents_list = [
    "hello_world",
    "best_of_the_best",
    "python_today"
]

# options
options = webdriver.ChromeOptions()

# change useragent
useragent = UserAgent()

# options.add_argument("user-agent=HelloWorld:)")
# options.add_argument("user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy
# options.add_argument("--proxy-server=138.128.91.65:8000")

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@138.128.91.65:8000"
    }
}

# driver = webdriver.Chrome(
#     executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
#     options=options
# )
driver = webdriver.Chrome(
    executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
    seleniumwire_options=proxy_options
)
# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # time.sleep(5)
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)

    # driver.refresh()
    # driver.get_screenshot_as_file("1.png")
    # driver.get(url="https://stackoverflow.com/")
    # time.sleep(5)
    # driver.save_screenshot("2.png")
    # time.sleep(2)

    driver.get("https://2ip.ru")
    time.sleep(5)
    
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
