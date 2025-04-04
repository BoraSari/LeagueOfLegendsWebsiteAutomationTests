import time
from inspect import isframe
from os import waitpid

from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v132.overlay import highlight_frame
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LolNewsPage:

     def __init__(self,driver):
        self.driver = driver
        self.cookie_section = (By.CSS_SELECTOR,"button[class=' osano-cm-accept osano-cm-buttons__button osano-cm-button osano-cm-button--type_accept ']")
        self.video_player = (By.CSS_SELECTOR,"button[class='ytp-large-play-button ytp-button ytp-large-play-button-red-bg']")
        self.image = (By.XPATH,"//*[contains(text(),'LeBlanc Champion Theme')]")
        self.close_button = (By.CSS_SELECTOR,"button[data-testid='close']")
        self.full_screen_button = (By.CSS_SELECTOR,"button[class='ytp-fullscreen-button ytp-button']")
        self.news = (By.CSS_SELECTOR,"h1[data-testid='title']")


     def accept_cookies(self):
      self.driver.find_element(*self.cookie_section).click()


     def click_video_image(self):
      self.driver.find_element(*self.image).click()

     def play_video(self):
         iframe = self.driver.find_element(By.XPATH, "//iframe[@src='https://youtube.com/embed/A9iOtL_fb2c?rel=0']")
         self.driver.switch_to.frame(iframe)
         WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(self.video_player))
         self.driver.find_element(*self.video_player).click()
         self.driver.find_element(*self.full_screen_button).click()
         time.sleep(30)
         self.driver.find_element(*self.full_screen_button).click()
         self.driver.switch_to.default_content()
         self.driver.find_element(*self.close_button).click()



     def get_icon_web_element(self):
      return self.driver.find_element(*self.image)


     def get_icon_web_element_text(self):
      return self.driver.find_element(*self.image).text

     def get_news_title_text(self):
         return self.driver.find_element(*self.news).text







