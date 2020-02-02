from selenium import webdriver
from time import sleep


#automating log in
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def login(self):
        self.driver.get('https://tinder.com')

        sleep(3)
        phone_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')

        phone_btn.click()
        sleep(3)
        phone_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        sleep(2)
        phone_in.send_keys('Your Number Here')

        login = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        login.click()

        sleep(5)

        ### Requests verification with sms :(, work around? ###


    # where the liking and disliking happens
    
    # def like(self):

    # def auto_like(self):
    #     while True:
    #     sleep(0.3)
    #     self.like()

    def dislike(self):
        dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[1]')
        dislike.click()


    def auto_dislike(self):
        while True:
            sleep(0.3)
            self.dislike()

bot = TinderBot()
bot.login()
# bot.auto_dislike()

