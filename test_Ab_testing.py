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
try :
    #wait for the page to load element 
    wait= WebDriverWait(driver, 10)
    Welcome_to_internet=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"heading")))
    header_text=Welcome_to_internet.text

    print(f"this is text on header of herokuapp page:{header_text}")
except Exception as e:
    print("element non found",e)

driver.find_element(By.CSS_SELECTOR,"a[href='/abtest']").click()

A_btesting_page_header_xpath_locator="//div/h3[contains(text(),'A/B Test')]"
#wait for the page to load element 
wait= WebDriverWait(driver, 100)
ABtest_page_header=wait.until(EC.presence_of_element_located(
                                   (By.XPATH,A_btesting_page_header_xpath_locator)))
AABtest_page_header_text=ABtest_page_header.text

print( f"this is test of header {AABtest_page_header_text}")

#get the para text

para_locator_xpath="//div/h3[contains(text(),'A/B Test')]/parent::div/p" 
para_text=driver.find_element(By.XPATH,para_locator_xpath).text   
    
print(f"this is para text of ab testing page:{para_text}")

assert "A/B Test" in AABtest_page_header_text and para_text=="Also known as split testing. This is a way in which businesses are able to simultaneously test and learn different versions of a page to see which text and/or functionality works best towards a desired outcome (e.g. a user action such as a click-through)."
    

    


