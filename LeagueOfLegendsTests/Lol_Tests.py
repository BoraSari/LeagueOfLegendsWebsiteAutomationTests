import pytest
from selenium import  webdriver
from  selenium.webdriver.chrome.service import  Service as ChromeService
from  webdriver_manager.chrome import  ChromeDriverManager
from LolPages.MainPage import  MainPage
from  LolPages.NewsPage import  LolNewsPage
from  LolPages.ChampionsPage import  ChampionsPage
from  LolPages.ChampionDetailsPage import ChampionDetailsPage


@pytest.fixture()
def driver():
 driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 driver.get("https://www.leagueoflegends.com/en-us/")
 driver.maximize_window()
 driver.implicitly_wait(15)
 yield driver
 driver.quit()


def test_navigate_league_of_legends_main_page(driver):
    # Class setup
    lol_main_page = MainPage(driver)

    # Functions and test values
    expected_result = lol_main_page.get_lol_icon()
    expected_result_attribute = lol_main_page.get_lol_icon_attribute()

    assert  expected_result.is_displayed(),f"{expected_result} successfuly displayed on susers screen"
    assert  expected_result_attribute == 'masthead-logo'f"{expected_result_attribute} has selected attribute"



def test_play_leblanc_introduction_video(driver):
    #Class setup
    lol_main_page = MainPage(driver)
    news_Page = LolNewsPage(driver)

    # Functions and test values
    lol_main_page.navigate_league_of_legends_news_page()
    news_Page.accept_cookies()
    news_Page.click_video_image()
    news_Page.play_video()

    image_text_element = news_Page.get_icon_web_element()
    image_text = news_Page.get_icon_web_element_text()
    news_title = news_Page.get_news_title_text()

    # Assertions
    assert image_text_element.is_displayed(),f"{image_text} successfully displayed on users screen"
    assert image_text == "LeBlanc Champion Theme",f"{image_text} equal LeBlanc Champion Theme"
    assert  news_title== "NEWS"f"{image_text} has expected title"


def test_for_champion_costumes_and_Language_change(driver):
    #Class setup
    lol_main_page = MainPage(driver)
    champions_page = ChampionsPage(driver)
    news_Page = LolNewsPage(driver)
    champions_details_page = ChampionDetailsPage(driver)

   #Functions and test values
    news_Page.accept_cookies()
    lol_main_page.navigate_champions_page()
    champions_page.navigate_champion_details_page()
    champions_details_page.check_champion_costumes()
    expected_image_text = champions_details_page.get_selected_skin_text()
    champions_details_page.navigate_main_page()
    lol_main_page.change_language()
    button_after_language_change = lol_main_page.get_text_of_gameplay_button()

     #Assertions
    assert  expected_image_text == "PRIMORDIAN AATROX",f"{expected_image_text} equal selected_skin"
    assert  button_after_language_change == "Ücretsiz Oyna",f"{button_after_language_change} new language successfuly changed on users screen"

