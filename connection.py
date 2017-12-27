from appium import webdriver

class Connection():

    def __init__(self):
        pass

    @property
    def capabilities(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Asus Zenfone 2'
        desired_caps['udid'] = '192.168.154.101:5555'
        # desired_caps['udid'] = 'G4AZGF00C729HT9'
        desired_caps['appPackage'] = "au.geekseat.com.hub3candroid"
        desired_caps['appActivity'] = ".activities.SplashActivity"
        desired_caps['noReset'] = False
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['appiumVersion'] = '1.6.5'

        return desired_caps

    def driver(self):
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=self.capabilities)


