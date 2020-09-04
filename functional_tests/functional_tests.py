from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class FunctionalTests(LiveServerTestCase):
    def setUp(self):
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True
        self.browser = webdriver.Firefox(capabilities=cap, executable_path='/usr/local/bin/geckodriver/geckodriver')

    def tearDown(self):
        pass

    def test_can_navigate_site(self):
        self.browser.get('http://localhost:8000')
        assert "Page d'accueil" in self.browser.title
