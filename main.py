from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

chrome_service = fs.Service(
    executable_path="/Users/kumagai/Desktop/Python/python hello/tools/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service, options=options)

driver.implicitly_wait(10)

driver.get("https://google.com/")
sleep(3)

a_tag = driver.find_element(
    By.NAME, "q")
sleep(1)

a_tag.send_keys("amazon")
sleep(1)

a_tag.submit()
sleep(1)

b_tag = driver.find_element(
    By.CSS_SELECTOR, "a[class='sVXRqc']"
)
sleep(1)

b_tag.click()
sleep(1)

c_tag = driver.find_element(
    By.CSS_SELECTOR, "div.nav-search-field > input")
sleep(1)

c_tag.send_keys("python")
sleep(1)

c_tag.submit()
sleep(1)

d_tag = driver.find_element(
    By.CSS_SELECTOR, "h2.a-size-mini a-spacing-none a-color-base s-line-clamp-4 > a > span")
sleep(1)

d_tag.click()
sleep(1)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(2)

# with open("amazon_list.html", "w") as f:
# f.write(driver.page_source)


driver.quit()
