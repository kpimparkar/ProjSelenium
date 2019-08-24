from selenium import webdriver
import time
import LinkedInJobs
from pprint import pprint

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.url = "https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin"

        self.uid_textbox_id = "username"
        self.pwd_textbox_id = "password"
        self.signIn_button_class = "btn__primary--large"

    def openUrl(self, driver):
        driver.get(self.url)

    def enterDetails(self, userid, password):

        self.uid = self.driver.find_element_by_id(self.uid_textbox_id)
        self.uid.clear()
        self.uid.send_keys(userid)

        self.pwd = self.driver.find_element_by_id(self.pwd_textbox_id)
        self.pwd.clear()
        self.pwd.send_keys(password)

    def login(self):
        self.signInBtn = self.driver.find_element_by_class_name(self.signIn_button_class)
        self.signInBtn.click()


def main():
    global driver
    driver = webdriver.Chrome('D:/chromedriver_win32/chromedriver')
    driver.implicitly_wait(10)
    login = LoginPage(driver)

    login.openUrl(driver)
    driver.maximize_window()
    login.enterDetails('kpimparkar@gmail.com','14Vrindavan')
    login.login()
    print(login.url)
    ## To be shifted to next .py

    jobsPage = LinkedInJobs.LinkedInJobsPage(driver)
    with open('PageContent.txt', 'w+', encoding='utf-8') as fo:
        print(driver.page_source, file=fo)


    jobsPage.getJobsPage()

    jobsPage.enterSearchDetails('Python','United States')
    jobsPage.searchJobs()

    #time.sleep(5)
    #driver.close()


if __name__=="__main__":
    main()
