from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# has the "next" button clicked
def click_next_button(driver):
    button_next = driver.find_element(By.CSS_SELECTOR, "input#NextButton")
    button_next.click()

# has the best option selected, regardless of the questions amount
def choose_best_option(driver):
    choose_radio = driver.find_elements(By.CSS_SELECTOR, 'td[class^="Opt5"')
    for radio in choose_radio:
        radio.click()

# selects yes or no option for that question type
def choose_yes_no(driver, answer: str):
    if answer.lower() == "no":
        choose_radio = driver.find_elements(By.CSS_SELECTOR, 'td[class^="Opt2"')
    else:
        choose_radio = driver.find_elements(By.CSS_SELECTOR, 'td[class^="Opt1"')

    for radio in choose_radio:
        radio.click()

# selects the last option for the dropdowns question
def choose_dropdowns(driver):
    dropdowns = driver.find_elements(By.TAG_NAME, "select")
    for options in dropdowns:
        click_option = options.find_element(By.CLASS_NAME, "Opt9")
        click_option.click()

# selects text box area and types review
def type_review(driver):
    choose_area = driver.find_element(By.TAG_NAME, "textarea")
    choose_area.send_keys("Great food." + Keys.RETURN + "Great prices." + Keys.RETURN + "Great service.")


def main():
    # ask for survey code and validate format
    survey_code = input("\nType in your survey code, including dashes: ")
    if survey_code.count("-") != 5:
        raise Exception("\nPlease include all dashes!")
    survey_code = survey_code.split("-")
    
    # init FireFox driver and navigate to website
    driver = webdriver.Firefox()
    driver.get("https://www.pandaguestexperience.com")
    sleep(1)

    # return list of input elements for the code
    code_input = driver.find_elements(By.CSS_SELECTOR, "p.IndexText01 input")

    # input survey code into input elements
    i = 0
    for block in code_input:
        block.send_keys(survey_code[i])
        i += 1
    
    # find and click the 'submit' button
    button_submit = driver.find_element(By.CSS_SELECTOR, "div#Buttonholder input")
    button_submit.click()

    # Format of pages in order: 
    # 4 pages of multiple radio questions, 1 page of yes/no radio questions, 1 page of multiple radio questions
    # 1 page of text review questions, 1 page of multiple radio questions, 1 page of yes/no questions
    # 1 page of multiple radio questions (diff format), 1 page of yes/no questions, 1 page of multiple radio questions
    # 1 page of dropdown questions

    # First 4 pages
    for i in range(4):
        choose_best_option(driver)
        click_next_button(driver)

    # Pg 5
    choose_yes_no(driver, "no")
    click_next_button(driver)

    # Pg 6
    choose_best_option(driver)
    click_next_button(driver)
    
    # Pg 7
    type_review(driver)
    click_next_button(driver)

    # Pg 8
    choose_best_option(driver)
    click_next_button(driver)

    # Pg 9
    choose_yes_no(driver, "no")
    click_next_button(driver)

    # Pg 10
    choose_radio = driver.find_element(By.CLASS_NAME, 'radioSimpleInput')
    choose_radio.click()
    click_next_button(driver)

    # Pg 11
    choose_yes_no(driver, "no")
    click_next_button(driver)

    # Pg 12
    choose_best_option(driver)
    click_next_button(driver)

    # Pg 13
    choose_dropdowns(driver)
    click_next_button(driver)

    # waits 30 seconds for user to jot down code
    # and then quits the driver session
    sleep(30)
    print("Closing session...")
    driver.quit()



# start if not imported
if __name__ == "__main__":
    main()

