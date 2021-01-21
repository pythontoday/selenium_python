from selenium import webdriver
import time


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
    driver.get("https://www.avito.ru/moskva/transport")
    # print(driver.window_handles)
    print(f"Currently URL is: {driver.current_url}")
    time.sleep(5)

    items = driver.find_elements_by_xpath("//div[@data-marker='item-photo']")
    items[0].click()
    # print(driver.window_handles)
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")

    username = driver.find_element_by_class_name("seller-info-name")
    print(f"User name is: {username.text}")
    print("#" * 20)
    time.sleep(5)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")

    items[1].click()
    time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
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

    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
