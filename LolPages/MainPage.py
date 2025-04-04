from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self,driver):
         self.driver = driver
         self.news_section = (By.XPATH,"//div/a[@data-testid='riotbar:desktopNav:link-internal-news']")
         self.dall_section = (By.CSS_SELECTOR, "li >[data-testid='riotbar:desktopNav:link-ALL']")
         self.lol_icon = (By.XPATH,"//img[@src='https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/9eb028de391e65072d06e77f06d0955f66b9fa2c-736x316.png?auto=format&fit=fill&q=80&w=300']")
         self.champions_section = (By.CSS_SELECTOR, "a[href='https://www.leagueoflegends.com/en-us/champions/']")
         self.language_change_icon = (By.CSS_SELECTOR,"a[data-testid='riotbar:localeswitcher:button-toggleLocaleMenu']")
         self.selected_language = (By.XPATH,"//span[contains(text(),'Türkçe')]")
         self.play_button = (By.XPATH,"//span/*[@data-testid='cta-content'][1]")




    def navigate_league_of_legends_news_page(self):
     self.driver.find_element(*self.news_section).click()
     self.driver.find_element(*self.dall_section).click()



    def get_lol_icon(self):
     return  self.driver.find_element(*self.lol_icon)

    def get_lol_icon_attribute(self):
        return self.driver.find_element(*self.lol_icon).get_attribute("data-testid")

    def navigate_champions_page(self):
     self.driver.find_element(*self.champions_section).click()

    def change_language(self):
         self.driver.find_element(*self.language_change_icon).click()
         self.driver.find_element(*self.selected_language).click()


    def get_text_of_gameplay_button(self):
        return  self.driver.find_element(*self.play_button).text


