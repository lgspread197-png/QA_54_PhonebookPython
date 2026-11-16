import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class ContactsPage(BasePage):
    CONTACTS_LINK = (By.CSS_SELECTOR, "[href='/contacts']")
    CONTACTS_CARDS = (By.CLASS_NAME, "contact-item_card__2SOIM")

    BUTTON_EDIT = (By.XPATH, "//button[text()='Edit']")
    EDIT_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Name']")
    EDIT_LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    EDIT_PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EDIT_EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    EDIT_ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    EDIT_DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='desc']")
    EDIT_SAVE_BUTTON = (By.XPATH, "//button[text()='Save']")

    def open_contacts_list(self):
        self.click(self.CONTACTS_LINK)
        WebDriverWait(self.driver, 10).until(EC.url_contains("/contacts"))
        time.sleep(1)

    def get_contact_cards(self, phone):
        return self.driver.find_elements(By.XPATH, f"//h3[text()='{phone}']")

    def contact_cards_visible(self, phone):
        locator = self.get_card_locator(phone)
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        return element.is_displayed()

    def open_contact_details_card(self, phone):
        # card = self.driver.find_element(By.XPATH, f"//h3[contains(text(),'{phone}')]/..").click()
        self.click(self.get_card_locator(phone))

    @staticmethod   # позволяет найти локатор по нужному нам телефону
    def get_card_locator(phone):
        return By.XPATH, f"//h3[contains(text(), '{phone}')]"

    def open_edit_mode(self):
        self.click(self.BUTTON_EDIT)

    def set_edit_mode(self,locator,value):
        self.fill(locator,value)

    def submit_edit(self):
        self.click(self.EDIT_SAVE_BUTTON)
        time.sleep(1)



