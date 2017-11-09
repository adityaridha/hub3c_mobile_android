from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.0'
desired_caps['deviceName'] = 'SWEESK8PG6CETSJ7'
desired_caps['udid'] = 'SWEESK8PG6CETSJ7'
desired_caps['appPackage'] = "au.geekseat.com.hub3candroid'"
desired_caps['appActivity'] = ".activities.SplashActivity'"
desired_caps['noReset'] = False
desired_caps['automationName'] = 'uiautomator2'

desired_caps['appiumVersion'] = '1.6.5'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

#Lenovo : SWEESK8PG6CETSJ7
#Samsung : a986ce96

WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'au.geekseat.com.hub3candroid:id/textUsername')))
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/textUsername').send_keys("marsha@freehub.com")
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/textPassword').send_keys("ZXasqw12")
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/buttonLogin').click()
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'au.geekseat.com.hub3candroid:id/tab_profile')))
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/tab_profile').click()
WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'au.geekseat.com.hub3candroid:id/containerSideNavHeader')))
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/containerSideNavHeader').click()
driver.find_element_by_id('au.geekseat.com.hub3candroid:id/buttonLogout').click()


name = driver.find_element_by_id(yes)


