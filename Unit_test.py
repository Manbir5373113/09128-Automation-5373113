import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys



def test_search_results(search_query, num_results=10):
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

search_box = driver.find_element_by_name("q")
search_box.send_keys("HP Laptops")
search_box.send_keys(Keys.RETURN)

search_results = driver.find_elements_by_class_name("g")
assert(search_results) >= 10,
driver.close()


def test_youtube_search_results(search_query, num_results=10):
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")
search_box = driver.find_element_by_xpath("//*[@id='search']")
search_box.send_keys("Punjabi Songs")
search_box.send_keys(Keys.RETURN)
search_results = driver.find_elements_by_class_name("yt-lockup-video")
assert(search_results) >= 10,
driver.close()