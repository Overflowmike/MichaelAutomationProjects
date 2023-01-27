import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# FBN Web Automation Task Project

# Section A: Automate Login Test For Sauce-Demo Website

def send_keys_to_element(element, *keys):
    element.send_keys(keys)

def main():
    #Launch browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    time.sleep(4)

    # Enter Username and Password
    send_keys_to_element(driver.find_element(By.ID, "user-name"), "standard_user")
    time.sleep(2)
    send_keys_to_element(driver.find_element(By.ID, 'password'), "secret_sauce")
    time.sleep(3)

    # Log in
    log_in_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    time.sleep(3)
    log_in_button.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(4)

    # Add 5 Items to Cart
    add_sauce_labsBackPack_button = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
    add_sauce_labsBackPack_button.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack').click()
    time.sleep(3)
    add_sauce_labsBikeLight_button = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bike-light')
    add_sauce_labsBikeLight_button.find_element(By.NAME, 'add-to-cart-sauce-labs-bike-light').click()
    time.sleep(3)
    add_sauce_labsBoltTshit_button = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-bolt-t-shirt')
    add_sauce_labsBoltTshit_button.find_element(By.Name, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    time.sleep(3)
    add_sauce_labsOnesie_button = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-onesie')
    add_sauce_labsOnesie_button.find_element(By.NAME, 'add-to-cart-sauce-labs-onesie').click()
    add_sauce_labsFleeceJacket_button = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-fleece-jacket')
    add_sauce_labsFleeceJacket_button.find_element(By.NAME, 'add-to-cart-sauce-labs-fleece-jacket').click()

    # Click on Cart Menu
    Cart_buttonMenu = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    Cart_buttonMenu.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Remove Items 1,3 & 5
    remove_sauce_labsBackPack_button = driver.find_element(By.NAME, 'remove-sauce-labs-backpack')
    remove_sauce_labsBackPack_button.find_element(By.NAME, 'remove-sauce-labs-backpack').click()
    time.sleep(3)
    remove_sauce_labsBoltTshit_button = driver.find_element(By.NAME, 'remove-sauce-labs-bolt-t-shirt')
    remove_sauce_labsBoltTshit_button.find_element(By.NAME, 'remove-sauce-labs-bolt-t-shirt').click()
    time.sleep(3)
    remove_sauce_labsFleeceJacket_button = driver.find_element(By.NAME, 'remove-sauce-labs-fleece-jacket')
    remove_sauce_labsFleeceJacket_button.find_element(By.NAME, 'remove-sauce-labs-fleece-jacket').click()

    # Add Two more items
    Add 
    driver.close()

if __name__ == '__main__':
    main()
    print("Test Pass")