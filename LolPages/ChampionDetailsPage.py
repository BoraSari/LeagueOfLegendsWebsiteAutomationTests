import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class ChampionDetailsPage:

    def __init__(self,driver):
     self.driver = driver
     self.arrow_Button = (By.XPATH, "(//button[@aria-label='next-button'])[2]")
     self.selected_skin_text = (By.XPATH, "(//div[@class='sc-48874027-1 gKEZLS'])[13]")
     self.lol_icon = (By.XPATH,"(//a[@href='https://na.leagueoflegends.com/en-us/'])[2]")



    def check_champion_costumes(self):
     self.driver.execute_script("scrollBy(0,2400)")

     WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located(self.arrow_Button))
     for costumes in range(12):
       time.sleep(3)
       self.driver.find_element(*self.arrow_Button).click()






    def get_selected_skin_text(self):
      text =  self.driver.find_element(*self.selected_skin_text).text
      print(text)
      return text


    def navigate_main_page(self):
       self.driver.find_element(*self.lol_icon).click()




