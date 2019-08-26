class JobListPage:
    def __init__(self, driver):
        self.driver = driver
        self.dropDown_Xpath = "//form[@class='search-s-facet__form']/button"
        self.option_Xpath   = "//li[@class ='search-s-facet-value']/label/p/span[text()='Past 24 hours']"
        self.apply_Xpath    = "//button[starts-with(@class,'facet-collection-list__apply-button')]"

    def inquireJobs(self):
        dropDown = self.driver.find_element_by_xpath(self.dropDown_Xpath)
        dropDown.click()

        option = self.driver.find_element_by_xpath(self.option_Xpath)
        option.click()

        applyFilter = self.driver.find_element_by_xpath(self.apply_Xpath)
        applyFilter.click()

    def fetchJobList(self):
        ulObj = self.driver.find_element_by_xpath("//ul[@class='jobs-search-results__list artdeco-list']")
        jobs = ulObj.find_elements_by_tag_name("li")
        for idx, job in enumerate(jobs):
            print(idx, " => ", job)
            print("---------------------------------------------------------------------")


        # //a[@class ='job-card-search__link-wrapper js-focusable disabled ember-view'] has name of the job


# driver.find_element_by_class_name()
# driver.find_elements_by_class_name()


def main():
    print("\nCurrently, this module can't be called independently.")

if __name__ == "__main__":
    main()
