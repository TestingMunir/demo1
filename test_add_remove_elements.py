from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


driver=webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(3)

#get https://the-internet.herokuapp.com/

driver.get("https://the-internet.herokuapp.com/")

add_element_css_selector="a[href='/add_remove_elements/']"

driver.find_element(By.CSS_SELECTOR,add_element_css_selector).click()

add_ele_header_xpath="//h3[normalize-space()='Add/Remove Elements']"

WebDriverWait(driver, 10).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

add_ele_text=driver.find_element(By.XPATH,add_ele_header_xpath).text

print(f"this is headr of add remove page {add_ele_text}")

add_ele_butto_xpath="//button[.='Add Element']"

for i in range(1,5,1):
    driver.find_element(By.XPATH,add_ele_butto_xpath).click()
print(i,"number of elements added")

delete_button_xpath="//button[.='Delete']"
delete_elements=driver.find_elements(By.XPATH,delete_button_xpath)
print("lenth of deleted elements{} before deleting".format(len(delete_elements)))


for index, ele in enumerate(delete_elements):
    
    if index % 2 == 0:
        ele.click()
    elif index==0:
        ele.click()
    else:
        pass


delete_elements=driver.find_elements(By.XPATH,delete_button_xpath)
print("lenth of deleted elements{} after deleting".format(len(delete_elements)))



