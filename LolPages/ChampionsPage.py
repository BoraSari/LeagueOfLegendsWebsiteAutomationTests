from selenium.webdriver.common.by import By

class ChampionsPage:

    def __init__(self,driver):
        self.driver= driver
        self.champions_text = (By.XPATH,"//div[@data-testid='rich-text-html']")
        self.selected_champion = (By.XPATH,"//div[@data-testid='card-title'][1]")




    def get_selected_champion_img(self):
     return self.driver.find_element(*self.selected_champion)


    def get_champions_text(self):
     return self.driver.find_element(*self.champions_text).text



    def navigate_champion_details_page(self):
      self.driver.execute_script("scrollBy(0,500)")
      self.driver.find_element(*self.selected_champion).click()