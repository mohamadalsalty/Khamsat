#import the files
import time
from selenium import webdriver
#ask the user for the function
req = input("what are you looking for (start or stop): ")
#include the webdriver file
driver = webdriver.Chrome('The path to chromedriver');#You have to change
#go to the login link
driver.get("https://accounts.hsoub.com/login?source=khamsat&locale=ar");
#set the email;
email = driver.find_element_by_name('email');
email.send_keys('example@gmail.com');#You have to change
#set the password
password = driver.find_element_by_name('password');
password.send_keys('myfuckingpassword');#You have to change
#send enter
password.submit();
#get the home page
time.sleep(2)
driver.get("https://khamsat.com");
#click on login button
time.sleep(2)
driver.execute_script("$('.fa-sign-in').click();");
time.sleep(2)


file = open("gigs.txt","r")
for line in file.readlines():
    driver.get(line);
    time.sleep(2)
    if req == "start":
        driver.execute_script(' $("[value=\'true\']").attr("selected","selected"); ');#to start
    elif req == "stop":
        driver.execute_script(' $("[value=\'false\']").attr("selected","selected"); ');#to stop

    else:
        print("please use an available function")
        
    driver.execute_script(' $(\'button:contains("تحديث")\').click(); ');
    time.sleep(2)
    
driver.get("https://khamsat.com/user/Your_Account");#You have to change


