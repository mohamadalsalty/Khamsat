#import the files
import time
from selenium import webdriver
from tkinter import *
from tkinter import ttk
#create the form
root=Tk()
root.title('خمسات')
a=ttk.Button(root,text='بدء')
a.pack()
b=ttk.Button(root,text='ايقاف')
b.pack()
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton',background='Green',font=('Arial',50,'bold'),foreground='white')

#include the webdriver file
driver = webdriver.Chrome('chromedriver.exe');
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
gigs = file.readlines()
#the order function
def what(x):
    for line in gigs:
        driver.get(line);
        time.sleep(2)
        if x == 1:
            driver.execute_script(' $("[value=\'true\']").attr("selected","selected"); ');#to start
        elif x == 2:
            driver.execute_script(' $("[value=\'false\']").attr("selected","selected"); ');#to stop

        driver.execute_script(' $(\'button:contains("تحديث")\').click(); ');
        time.sleep(2)
#the UI loop
a.config(command=lambda : what(1))
b.config(command=lambda : what(2))
root.mainloop()    