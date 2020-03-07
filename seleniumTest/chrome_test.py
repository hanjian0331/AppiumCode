from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://218.108.90.228:10089/hexin-crm/index.html")
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("韩坚")
# driver.find_element_by_xpath("//*[@id='su']").click()
# ActionChains(driver).key_down(Keys.COMMAND).key_down(Keys.ALT).send_keys('i').key_up(Keys.COMMAND).key_up(Keys.ALT).perform()
# ActionChains(driver).key_down(Keys.COMMAND).send_keys("t").key_up(Keys.COMMAND).perform()
ActionChains(driver).move_to_element_with_offset(driver.find_element_by_xpath("/html"), 0, ).double_click().perform()


sleep(500)
driver.quit()
