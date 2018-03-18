from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from time import  sleep

home_page = "http://www.baidu.com";

driver = webdriver.Chrome();
driver.get(home_page);

# 打印当前页面
print('Before search------------------')
print(driver.title)  # 打印标题
print(driver.current_url) # 打印url
driver.find_element_by_id("kw").send_keys("selenium");
driver.find_element_by_id("su").click();
sleep(1)

print('After search------------------')
print(driver.title)  # 打印标题
print(driver.current_url) # 打印url
search_count = driver.find_element_by_class_name("nums").text # 打印输出结果
print(search_count)