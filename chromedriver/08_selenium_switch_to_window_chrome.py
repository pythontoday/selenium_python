from selenium import webdriver
import time
import datetime

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
# options.headless = True

driver = webdriver.Chrome(
    executable_path="/home/cain/PycharmProjects/selenium_python/chromedriver/chromedriver",
    options=options
)

# "C:\\users\\selenium_python\\chromedriver\\chromedriver.exe"
# r"C:\users\selenium_python\chromedriver\chromedriver.exe"

try:
    start_time = datetime.datetime.now()

    driver.get("https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty")
    # print(driver.window_handles)
    print(f"Currently URL is: {driver.current_url}")

    # time.sleep(5)
    driver.implicitly_wait(5)

    items = driver.find_elements_by_xpath("//div[@data-marker='item-photo']")
    items[0].click()
    # print(driver.window_handles)

    # time.sleep(5)
    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])

    # time.sleep(5)
    driver.implicitly_wait(5)

    print(f"Currently URL is: {driver.current_url}")

    username = driver.find_element_by_class_name("seller-info-name")
    print(f"User name is: {username.text}")
    print("#" * 20)

    # time.sleep(5)
    driver.implicitly_wait(5)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    # time.sleep(5)
    driver.implicitly_wait(5)

    print(f"Currently URL is: {driver.current_url}")

    items[1].click()

    # time.sleep(5)
    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])

    # time.sleep(5)
    driver.implicitly_wait(5)

    print(f"Currently URL is: {driver.current_url}")
    username = driver.find_element_by_xpath("//div[@data-marker='seller-info/name']")
    print(f"User name is: {username.text}")
    print("-" * 20)

    ad_date = driver.find_element_by_class_name("title-info-metadata-item-redesign")
    print(f"An ad date is: {ad_date.text}")
    print("-" * 20)

    joined_date = driver.find_elements_by_class_name("seller-info-value")[1]
    print(f"User since: {joined_date.text}")
    print("#" * 20)

    # time.sleep(5)
    driver.implicitly_wait(5)

    finish_time = datetime.datetime.now()
    spent_time = finish_time - start_time
    print(spent_time)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

    "0:00:47.315298"
    "0:00:14.850836"
