import allure
from selenium import webdriver
from time import sleep


def test_web():
    with allure.step('打开浏览器访问百度'):
        driver = webdriver.Chrome()
        driver.get('https://www.baidu.com')
        sleep(2)
    with allure.step('输入123，点击搜索'):
        driver.find_element_by_id('kw').send_keys('123')
        sleep(2)
        driver.find_element_by_id('su').click()
        sleep(2)
    with allure.step('保存图片'):
        driver.save_screenshot('b.png')
        allure.attach.file('b.png', '搜索结果', allure.attachment_type.PNG)
    with allure.step('关闭浏览器'):
        driver.quit()
