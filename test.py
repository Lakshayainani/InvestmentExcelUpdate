from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions

driver = Chrome()
usernamestr="kbhattad@sonicwall.com"
passwordstr="Sonali97k@"
driver.get("https://www.mysonicwall.com/muir/login")
try:
    # wait 10 seconds before looking for element
    element = driver.find_element_by_id(
        presence_of_element_located((By.ID, "username"))
    )
except:
    driver.quit()
driver.find_element_by_id("username").send_keys(usernamestr)
driver.find_element_by_id("nextButton").click()
driver.find_elements_by_id("password").send_keys("Sonali97k@")
driver.find_elements_by_id("password").send_keys()
driver.find_element_by_css_selector(".s-login-button").click()
driver.find_elements_by_link_text("LOG IN").click()