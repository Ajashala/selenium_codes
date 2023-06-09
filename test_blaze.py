import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture( scope= 'module')
def driver():
    driver = webdriver.Edge(executable_path="C:\drivers\edgedriver_win64\msedgedriver.exe")
    #driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_url(driver):
    driver.get("https://np.chimpvine.com/login/index.php")
    assert 'ChimpVine: Log in to the site' == driver.title
    #time.sleep(5)

    #assert 'index.php' in driver.current_url

def test_login(driver):
    driver.find_element(By.ID , "login_username").send_keys("pramod")
    driver.find_element(By.ID, "login_password").send_keys("Pramod12!@")
    driver.find_element(By.ID, "login-submit").click()
    #time.sleep(5)
    assert 'https://np.chimpvine.com/' == driver.current_url

