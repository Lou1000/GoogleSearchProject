from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/chromedriver')
driver = webdriver.Chrome(service=service)

# Define the list of names
names = ['Lady Gaga', 'Brad Pitt', 'Taylor Swift']

# Created a loop, to loop through each name and search them
for name in names:

    # Go to google.com
    driver.get('https://www.google.com/')

    # enters any name into a search field
    driver.find_element(By.ID, 'APjFqb').send_keys(name)

    # clicks on the search button
    SEARCH_BTN = driver.find_elements(By. XPATH, '//input[@class="gNO89b"]')
    SEARCH_BTN[0].click()

    # verifies search result page opens and text search for matches search results
    SEARCH_RESULT = driver.find_element(By. XPATH, '//span[@class="yKMVIe"]')
    SEARCH_INDEX = SEARCH_RESULT.get_attribute('innerHTML')

    expected_result = name
    actual_result = SEARCH_INDEX
    print(actual_result)

    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
    print('Test case passed')

