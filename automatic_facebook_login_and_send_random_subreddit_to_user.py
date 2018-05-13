from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



browser = webdriver.Chrome()
browser.get('https://facebook.com')

email_address = browser.find_element_by_css_selector('#email')
email_address.send_keys('INSERT YOUR EMAIL HERE')

password = browser.find_element_by_css_selector('#pass')
password.send_keys('INSERT YOUR PASSWORD HERE')

login_button = browser.find_element_by_css_selector('#u_0_2')
login_button.click()


random_subreddit_links = []

for i in range(0, 3):
    browser.get('https://www.reddit.com/r/random')
    time.sleep(1.5)
    random_subreddit_links.append(browser.current_url);


    

subreddit_links_str = '\n'.join(random_subreddit_links)
print(subreddit_links_str)




browser.get("https://www.facebook.com/messages/t/INSERT YOUR FRIEND'S NAME HERE")
browser.switch_to_active_element().send_keys("Hi!\n")
browser.switch_to_active_element().send_keys("Enjoy these three random subreddits on me. Happy browsing!\n")
browser.switch_to_active_element().send_keys(subreddit_links_str + "\n")


browser.quit()
