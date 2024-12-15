from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoAlertPresentException,
    TimeoutException
)
# for i in range(1,10):
driver=webdriver.Chrome()
subjects=[]
marks=[]

driver.get("https://www.google.com")

search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("mserp kiet")


search_box.send_keys(Keys.RETURN)
mserp_link=driver.find_element(By.CLASS_NAME,"LC20lb")
mserp_link.click()

username=driver.find_element(By.ID,"txt_username")
username.send_keys("2327cse1259")
password=driver.find_element(By.ID,"txt_password")
password.send_keys("Raj@200101")
captcha_field=driver.find_element(By.ID,"txtcaptcha")
captcha_value=captcha_field.get_attribute("data-captcha")

captcha_field.send_keys(captcha_value)

signin_button=driver.find_element(By.ID,"btnLogin")
signin_button.click()

attendance = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "lblAttPer"))
).text
print("Current attendance:", attendance)



driver.get("https://mserp.kiet.edu/Academic/iitmsPFkXjz+EbtRodaXHXaPVt3dlW3oTGB+3i1YZ7alodHeRzGm9eTr2C53AU6tMBXuOXVbvNfePRUcHp4rLz3edhg==?enc=3Q2Y1k5BriJsFcxTY7ebQh0hExMANhAKSl1CmxvOF+Y=")

internal_m=driver.find_element(By.XPATH,"//a[normalize-space()='Internal Marks']")
internal_m.click()

# subject_marks=driver.find_element(By.TAG_NAME,"tbody")
subject_marks=driver.find_elements(By.XPATH,"/html/body/form/div[6]/div[2]/div/section/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/div[16]/div/div/div[2]/div/div/table/tbody/tr")
# //div[@id='div3']//div[@class='col-12']

for i in range(len(subject_marks)):
    subject_marks = driver.find_elements(
        By.XPATH, "/html/body/form/div[6]/div[2]/div/section/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div[3]/div[16]/div/div/div[2]/div/div/table/tbody/tr"
    )
    current_row = subject_marks[i]
    
    ind_subj = WebDriverWait(current_row, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//td[1]/a"))
    )
    subjects.append(ind_subj.text)
    driver.execute_script("arguments[0].scrollIntoView(true);",ind_subj)
    ind_subj.click()

    # ind_marks=driver.find_element(
    #     By.XPATH,"/html/body/form/div[6]/div[2]/div/section/div/div/div[5]/div/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td[3]").text
    # marks.append(ind_marks)
    try:
        ind_subj_name=WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(( By.XPATH,"/html/body/form/div[6]/div[2]/div/section/div/div/div[5]/div/div/div[2]/div/div/div/div[1]/div[1]/span[2]"))
        ).text
        ind_marks= WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(( By.XPATH,"/html/body/form/div[6]/div[2]/div/section/div/div/div[5]/div/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td[3]"))
        ).text
        marks.append(ind_marks)
        print("marks in",ind_subj_name," is: ",ind_marks)
        close_but=WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/form/div[6]/div[2]/div/section/div/div/div[5]/div/div/div[3]/button"))
        )
        close_but.click()
    except UnexpectedAlertPresentException:
            try:
                alert = driver.switch_to.alert
                alert.accept()  
            except NoAlertPresentException:
                pass


    


print()
print("lislt ",subjects)
print("marks ",marks)
time.sleep(30)
driver.quit()