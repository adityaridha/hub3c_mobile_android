from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from page.base_page import Page



class Feature(Page):

    business = (By.ID, "au.geekseat.com.hub3candroid:id/sideNavBusiness")
    job2job = (By.ID, "au.geekseat.com.hub3candroid:id/sideNavJob2job")
    project_id = (By.ID, "au.geekseat.com.hub3candroid:id/sideProject")
    profile_picture = (By.ID, "au.geekseat.com.hub3candroid:id/imageProfile")
    header = "au.geekseat.com.hub3candroid:id/containerSideNavHeader"
    arrow_nav = "(//*[@id='sideNavHeader']/*[@class='android.widget.ImageView'])[2]"
    cancel = (By.ID, "au.geekseat.com.hub3candroid:id/edit_cancel")

    def __init__(self):
        super().__init__()

    def tap_business_network(self):
        pass

    def tap_projects(self):
        self.find_element(self.project_id).click()

    def tap_job2job(self):
        self.find_element(self.job2job).click()

    def tap_header(self):
        self.find_element(self.profile_picture).click()

    def tap_arrow_nav(self):
        self.driver.find_element()

    def tap_cencel(self):
        pass



''' alternative locator '''

# au.geekseat.com.hub3candroid:id/sideProject
# au.geekseat.com.hub3candroid:id/imageProject
# au.geekseat.com.hub3candroid:id/sideNavBusiness
# au.geekseat.com.hub3candroid:id/imageBusinessNetwork