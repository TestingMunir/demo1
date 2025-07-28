import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    


driver=webdriver.Chrome()
driver.get("https://www.google.com")


# Print all main properties
print("Browser Name        :", driver.name)
print("Current URL         :", driver.current_url)
print("Title               :", driver.title)
print("Page Source Length  :", len(driver.page_source))
#print("Page Source         :", driver.page_source)
print("Window Handle       :", driver.current_window_handle)
print("All Window Handles  :", driver.window_handles)
print("Session ID          :", driver.session_id)
print("Capabilities        :", driver.capabilities)
print("Command Executor    :", driver.command_executor)
print("Log Types           :", driver.log_types)

driver.log_types.clear()  # Clear logs if needed
print("Log Types after clear:", driver.log_types)

logs = driver.get_log("browser")  # Or "performance", "driver", etc.
for entry in logs:
    print(entry)

time.sleep(4)  # Wait for a while to observe the output

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='APjFqb']")))
search_box.send_keys("AI")
time.sleep(2)
search_box.send_keys(Keys.ENTER)



time.sleep(5)