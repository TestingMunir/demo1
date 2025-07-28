from selenium import webdriver
import time

driver = webdriver.Chrome()

urls = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.amazon.in"
]

# Open the first URL
driver.get(urls[0])
current_handle=driver.current_window_handle
time.sleep(2)



# Open other URLs in new tab

for url in urls[1:]:
    driver.switch_to.new_window("tab")
    driver.get(url)

list_handles=driver.window_handles

print("list of handles:-",list_handles)


for handle in list_handles:
    driver.switch_to.window(handle)
    print("current title:",driver.current_url,driver.title)

driver.switch_to.window(current_handle)



#now we are adding new webdriver instance
driver2 = webdriver.Chrome()
driver2.get("https://www.youtube.com")
time.sleep(2)
#get all window handles
list_handles2 = driver2.window_handles  
print("list of handles in second driver:-", list_handles2)

print("-----------------##-----------------")

#we cant get window handles of first driver using secqnd driver     
#driver2.window_handles will not give handles of driver1
#driver.window_handles will not give handles of driver2
#we can only get handles of the current driver instance


#now add multiple tabs in second driver
for url in urls:
    driver2.switch_to.new_window("tab")
    driver2.get(url)

list_handles2 = driver2.window_handles
print("list of handles in second driver after adding tabs:-", list_handles2)
for handle in list_handles2:
    driver2.switch_to.window(handle)
    print("current title in second driver:", driver2.current_url, driver2.title)

# Close the drivers
driver.quit()
driver2.quit()

git add handling\ windows,\ tabs\ and\ drivers.py
