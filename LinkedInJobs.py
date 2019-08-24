from selenium import webdriver

class LinkedInJobsPage():
    def __init__(self, driver):
        self.driver = driver
        self.jobs_btn_id = "jobs-tab-icon"
        # self.jobSearchTextBoxId = "jobs-search-box-keyword-id-ember575"
        # self.jobLocationTextBoxId = "jobs-search-box-location-id-ember575"
        self.searchButtonClass = "jobs-search-box__submit-button"
        self.jobText = "//input[starts-with(@id,'jobs-search-box-keyword-id')]"
        self.jobLocationText = "//input[starts-with(@id,'jobs-search-box-location-id')]"



    def getJobsPage(self):
        self.jobsButton = self.driver.find_element_by_id(self.jobs_btn_id)
        self.jobsButton.click()

    def enterSearchDetails(self,JobKey, JobLocation):
        # self.jobKeyText = self.driver.find_element_by_id(self.jobSearchTextBoxId)
        self.jobKeyText = self.driver.find_element_by_xpath(self.jobText )
        self.jobKeyText.clear()
        self.jobKeyText.send_keys(JobKey)

        # self.jobLocationText = self.driver.find_element_by_id(self.jobLocationTextBoxId)
        self.jobLocationText = self.driver.find_element_by_xpath(self.jobLocationText)
        self.jobLocationText.clear()
        self.jobLocationText.send_keys(JobLocation)

    def searchJobs(self):
        self.searchBtn = self.driver.find_element_by_class_name(self.searchButtonClass)
        self.searchBtn.click()

