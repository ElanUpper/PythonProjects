from selenium import webdriver
from time import sleep

driver = webdriver.Chrome();
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 如果设置太小就会 unknown error: Element is not clickable at point
driver.set_window_size(800, 500);
driver.find_element_by_id("kw").send_keys("hello world");
sleep(1);
driver.find_element_by_id("su").click();
driver.close()

driver.get_screenshot_as_file("C:\\Users\\wangyang37\\Desktop\\files\\hello_world.jpg")
#driver.get_screenshot_as_file("C:\\Users\\wangyang37\\Desktop\\files\\hello.png")