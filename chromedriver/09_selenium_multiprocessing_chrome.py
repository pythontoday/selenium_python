import random

from selenium import webdriver
import time
from multiprocessing import Pool

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
# options.headless = True

# urls_list = ["https://stackoverflow.com", "https://instagram.com", "https://vk.com"]


# def get_data(url):
#     try:
#         driver = webdriver.Chrome(
#             executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
#             options=options
#         )
#         # "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
#         # r"C:\users\selenium_python\chromedriver\chromedriver.exe"
#         driver.get(url=url)
#         time.sleep(5)
#         driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#
#
# if __name__ == '__main__':
#     p = Pool(processes=2)
#     p.map(get_data, urls_list)

def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
            options=options
        )
        # "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
        # r"C:\users\selenium_python\chromedriver\chromedriver.exe"
        driver.get(url=url)
        time.sleep(5)
        driver.find_element_by_class_name("lazyload-wrapper").find_element_by_class_name("item-video-container").click()
        time.sleep(random.randrange(3, 10))
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    print(urls_list)
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)