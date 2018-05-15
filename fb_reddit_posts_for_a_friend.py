import praw
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



browser =  webdriver.Chrome()


##facebook - login
browser.get('https://facebook.com')

email_address = browser.find_element_by_css_selector('#email')
email_address.send_keys('TYPE YOUR EMAIL ADDRESS HERE')
password = browser.find_element_by_css_selector('#pass')
password.send_keys=('TYPE YOUR EMAIL ADDRESS HERE')
login_button = browser.find_element_by_css_selector('#u_0_2')
login_button.click()



reddit = praw.Reddit(client_id = 'TYPE REDDIT CREDENTIALS HERE',
                   client_secret = 'TYPE REDDIT CREDENTIALS HERE',
                   username = 'TYPE REDDIT CREDENTIALS HERE',
                   password = 'TYPE REDDIT CREDENTIALS HERE',
                   user_agent = 'TYPE REDDIT CREDENTIALS HERE')


##get top 5 posts of all time
post_links = []

subreddit = reddit.subreddit('drawing')  

top_python = subreddit.top(limit=5)     
for submission in top_python:
    if not submission.stickied:
        post_links.append(submission.url)

print(post_links)

for i in range(0, len(post_links)):
    print(post_links[i] + "\n")





##facebook - send messages
browser.get("https://www.facebook.com/messages/t/TYPE YOUR FRIEND'S NAME HERE")
browser.switch_to_active_element().send_keys("Hey!\n")
browser.switch_to_active_element().send_keys("Take a look at these amazing pictures!\n")

for i in range(0, len(post_links)):
    browser.switch_to_active_element().send_keys("{}.: ".format(i+1) + post_links[i] + "\n")



browser.quit()
