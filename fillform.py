from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Path to the chromedriver executable
service = Service("D:/chrome_driver/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# URL of the Google Form
form_url = "https://forms.gle/f8MMZ7R6ocRkjtr3A"  # Replace with your actual form URL
# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)
driver.get(form_url)


try:
    wait = WebDriverWait(driver, 10)

    for i in range(4):

        # Wait for the form to load and find all question sections
        questionelements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "geS5n")))

        for individual_element in questionelements:
            radio_buttons = individual_element.find_elements(By.CLASS_NAME, 'AB7Lab')
            # question = individual_element.find_element(By.CSS_SELECTOR,'strong')
            # print(question.text)

            print(len(radio_buttons))
            
            # Example: Select a random radio button in the section
            if radio_buttons:
                random_button = random.choice(radio_buttons)
                random_button.click()

        submit_button = driver.find_element(By.XPATH , "/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span")
        submit_button.click()

        print("Successfully sent form")

        # Wait for the page to load and find the link to submit another response
        add_new_survey = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'ส่งคำตอบเพิ่มอีก')))
        add_new_survey.click()

finally:
    print('Successfully interacted with the form.')
    # Optionally, you can close the browser or keep it open
    # driver.quit()  # Uncomment this if you want to close the browser at the end
