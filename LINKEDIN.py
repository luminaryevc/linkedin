#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:50:07 2023

@author: shahadsami
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# تعيين مسار ملف تنفيذي لمتصفح Chrome WebDriver
webdriver_path = 'PATH_TO_CHROMEDRIVER_EXECUTABLE'

# إنشاء متصفح Chrome
driver = webdriver.Chrome(webdriver_path)

# فتح موقع LinkedIn
driver.get('https://www.linkedin.com')

# تسجيل الدخول إلى حساب LinkedIn
email = 'YOUR_EMAIL'
password = 'YOUR_PASSWORD'

email_field = driver.find_element_by_id('session_key')
email_field.send_keys(email)

password_field = driver.find_element_by_id('session_password')
password_field.send_keys(password)

login_button = driver.find_element_by_class_name('sign-in-form__submit-button')
login_button.click()

# انتظار تحميل صفحة البداية
time.sleep(5)

# افتح صفحة الملف الشخصي التي ترغب في إضافتها
linkedin_profile_url = 'LINKEDIN_PROFILE_URL'
driver.get(linkedin_profile_url)

# انقر على زر إضافة صديق
add_connection_button = driver.find_element_by_class_name('pv-s-profile-actions__label')
add_connection_button.click()

# انتظار ظهور نافذة إضافة صديق
time.sleep(2)

# انقر على زر إرسال الدعوة
send_invite_button = driver.find_element_by_class_name('ml1')
send_invite_button.click()

# انتظار لحظة ثم إغلاق المتصفح
time.sleep(2)
driver.quit()