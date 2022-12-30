import time
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Functionality_Tests(softest.TestCase):
    ACCEPT_COOKIES = (By.XPATH, '//div[@class="col-12"]/p/a[@class="_brlbs-btn _brlbs-btn-accept-all _brlbs-cursor"]')
    CAREERS_MENU = (By.XPATH, '//body/header/div[2]/nav/div/div[6]')
    JOB_OPPORTUNITIES = (By.LINK_TEXT, 'Job Opportunities')
    SEARCH_BAR = (By.XPATH, '//div[@class="search-field"]/input[@type="text"]')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="search-field"]/button[@title="Search vacancies"]')
    JOB_OPTION = (By.XPATH, '//*[@id="search-results"]/div/div[1]/a')
    FIRST_NAME = (By.ID, 'candidate_first_name')
    LAST_NAME = (By.ID, 'candidate_last_name')
    EMAIL = (By.ID, 'candidate_email')
    PHONE = (By.ID, 'candidate_phone')
    RESUME = (By.ID, 'resume')
    CHECK_BOX_ONE = (By.ID, 'by_submitting_your_application_you_are_agreeing_to_recruiterbox_processing_your_personal_data_in_acc-0')
    CHECK_BOX_TWO = (By.ID, 'recruiterbox_processes_your_data_in_the_usa_this_means_us_public_authorities_may_access_your_data_fo-0')
    EXISTING_SALARY = (By.ID, 'existing_salary')
    EXPECTED_SALARY = (By.ID, 'expected_salary')
    NOTICE_PERIOD = (By.ID, 'notice_period')
    SELECT_DROPDOWN = (By.ID, 'by_submitting_your_application_you_are_agreeing_to_recruiterbox_processing_your_personal_data_in_acc')
    GOVT_ID = (By.ID, 'govt_id')
    EXPERIENCE = (By.ID, 'experience')
    SUBMIT = (By.XPATH, '//button[@name="_job_application_form"]')
    SUCCESS = (By.XPATH, '//*[@id="cta-form"]/div/div/div/p')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://kerv.com/')
        self.chrome.implicitly_wait(2)
        try:
            self.chrome.find_element(*self.ACCEPT_COOKIES).click()
        except:
            pass
        time.sleep(1)
        menu = WebDriverWait(self.chrome, 1).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-id="18659"]')))
        menu.click()
        self.chrome.find_element(*self.JOB_OPPORTUNITIES).click()
        self.chrome.find_element(*self.SEARCH_BAR).send_keys('CRM DEV')
        button = self.chrome.find_element(*self.SEARCH_BUTTON)
        self.chrome.execute_script("arguments[0].click();", button)
        position = self.chrome.find_element(*self.JOB_OPTION)
        self.chrome.execute_script("arguments[0].click();", position)
        chwd = self.chrome.window_handles
        self.chrome.switch_to.window(chwd[1])


    def tearDown(self) -> None:
        self.chrome.quit


    def test_POSITIVE_APPLICATION(self):
        self.chrome.find_element(*self.FIRST_NAME).send_keys("Tom")
        self.chrome.find_element(*self.LAST_NAME).send_keys("Smith")
        self.chrome.find_element(*self.EMAIL).send_keys('tomsmithtest@mail.com')
        self.chrome.find_element(*self.PHONE).send_keys('+40659562623')
        self.chrome.find_element(*self.RESUME).send_keys("C:/Users/Maxim/Desktop/Dummy_CV.pdf")
        try:
            self.chrome.find_element(*self.EXISTING_SALARY).send_keys('1000')
        except:
            pass
        try:
            self.chrome.find_element(*self.EXPECTED_SALARY).send_keys('2000')
        except:
            pass
        try:
            self.chrome.find_element(*self.NOTICE_PERIOD).send_keys('20')
        except:
            pass
        try:
            self.chrome.find_element(*self.GOVT_ID).send_keys('458965874')
        except:
            pass
        try:
            self.chrome.find_element(*self.EXPERIENCE).send_keys('2')
        except:
            pass
        try:
            self.chrome.find_element(*self.CHECK_BOX_ONE).click()
        except:
            pass
        try:
            self.chrome.find_element(*self.CHECK_BOX_TWO).click()
        except:
            pass
        try:
            select = Select(self.chrome.find_element(*self.SELECT_DROPDOWN))
            select.select_by_visible_text("Yes")
        except:
            pass
        self.chrome.find_element(*self.SUBMIT).click()
        assert self.chrome.find_element(*self.SUCCESS).is_displayed() == True, 'Error, Application not submitted'

    def test_NEGATIVE_APPLICATION(self):
        # self.chrome.find_element(*self.FIRST_NAME).send_keys("Tom")
        self.chrome.find_element(*self.LAST_NAME).send_keys("Smith")
        self.chrome.find_element(*self.EMAIL).send_keys('tomsmithtest@mail.com')
        self.chrome.find_element(*self.PHONE).send_keys('+40659562623')
        self.chrome.find_element(*self.RESUME).send_keys("C:/Users/Maxim/Desktop/Dummy_CV.pdf")
        try:
            self.chrome.find_element(*self.EXISTING_SALARY).send_keys('1000')
        except:
            pass
        try:
            self.chrome.find_element(*self.EXPECTED_SALARY).send_keys('2000')
        except:
            pass
        try:
            self.chrome.find_element(*self.NOTICE_PERIOD).send_keys('20')
        except:
            pass
        try:
            self.chrome.find_element(*self.GOVT_ID).send_keys('458965874')
        except:
            pass
        try:
            self.chrome.find_element(*self.EXPERIENCE).send_keys('2')
        except:
            pass
        try:
            self.chrome.find_element(*self.CHECK_BOX_ONE).click()
        except:
            pass
        try:
            self.chrome.find_element(*self.CHECK_BOX_TWO).click()
        except:
            pass
        try:
            select = Select(self.chrome.find_element(*self.SELECT_DROPDOWN))
            select.select_by_visible_text("Yes")
        except:
            pass
        self.chrome.find_element(*self.SUBMIT).click()
        time.sleep(1)
        assert self.chrome.find_element(*self.SUBMIT).is_displayed() == True, 'Error, Application submitted'