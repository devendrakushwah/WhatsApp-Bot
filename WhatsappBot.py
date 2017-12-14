from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


web = webdriver.Firefox()
message="Hello there!!!!"
name="Name"
web.get('http://web.whatsapp.com')
time.sleep(25)


elem = web.find_element_by_xpath('//span[contains(text(),"'+name+'")]')
elem.click()
print "chat open"
elem2=web.find_element_by_xpath("/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]")
i=0
while (True):
    elem2.send_keys(message)
    elem2.send_keys(Keys.RETURN)
    print str(i)+"<-- message sent -->"
    i+=1

