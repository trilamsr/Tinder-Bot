from selenium import webdriver
import json

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.data = json.load(open('./settings.json'))

    def login(self):
        self.driver.get("http://tinder.com")
        login_button = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        login_button.click()

        if self.data.login_mode == "facebook"


bot = TinderBot()
print(bot.data)
print("aloha")