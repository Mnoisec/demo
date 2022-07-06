import pytest, os, allure
from selenium import webdriver
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver