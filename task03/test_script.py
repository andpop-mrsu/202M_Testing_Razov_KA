# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# РРЅРёС†РёР°Р»РёР·Р°С†РёСЏ РґСЂР°Р№РІРµСЂР°
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15)

try:
    # 1. РћС‚РєСЂС‹С‚РёРµ СЃР°Р№С‚Р° Рё Р°РІС‚РѕСЂРёР·Р°С†РёСЏ
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    
    wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@class="oxd-userdropdown-name"]')))
    print("вњ… РђРІС‚РѕСЂРёР·Р°С†РёСЏ СѓСЃРїРµС€РЅР°.")

    # 2. РџРµСЂРµС…РѕРґ РІ PIM Рё СЃРѕР·РґР°РЅРёРµ СЃРѕС‚СЂСѓРґРЅРёРєР°
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Add")]'))).click()

    # Р’РІРѕРґ РґР°РЅРЅС‹С… СЃРѕС‚СЂСѓРґРЅРёРєР°
    wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="First Name"]'))).send_keys("Test")
    driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]').send_keys("Employee")

    # РЎРѕС…СЂР°РЅРµРЅРёРµ
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//h6[text()="Personal Details"]')))
    print("вњ… РќРѕРІС‹Р№ СЃРѕС‚СЂСѓРґРЅРёРє СЃРѕР·РґР°РЅ.")

    # 3. РЈРґР°Р»РµРЅРёРµ СЃРѕС‚СЂСѓРґРЅРёРєР°
    wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "viewEmployeeList")]'))).click()
    
    search_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Search"]')))
    search_field.send_keys("Test Employee")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)  

    # Р’С‹Р±РёСЂР°РµРј С‡РµРєР±РѕРєСЃ Рё Р¶РјРµРј СѓРґР°Р»РёС‚СЊ
    checkbox = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@role="row" and .//div[text()="Test Employee"]]//div[@role="checkbox"]')
    ))
    checkbox.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Delete Selected")]'))).click()
    
    # РџРѕРґС‚РІРµСЂР¶РґР°РµРј СѓРґР°Р»РµРЅРёРµ
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(.,"Yes, Delete")]'))).click()
    time.sleep(2)
    print("вњ… РЎРѕС‚СЂСѓРґРЅРёРє СѓРґР°Р»С‘РЅ.")

    # 4. Р’С‹С…РѕРґ РёР· СЃРёСЃС‚РµРјС‹
    wait.until(EC.element_to_be_clickable((By.XPATH, '//p[@class="oxd-userdropdown-name"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Logout"]'))).click()
    print("вњ… Р’С‹С…РѕРґ РІС‹РїРѕР»РЅРµРЅ.")

    # 5. РџСЂРѕРІРµСЂРєР° РїСЂРѕРІР°Р»СЊРЅРѕР№ Р°РІС‚РѕСЂРёР·Р°С†РёРё
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("wrong_password")
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(2)
    print("вњ… РџСЂРѕРІРµСЂРєР° РѕС€РёР±РєРё РІС…РѕРґР° РІС‹РїРѕР»РЅРµРЅР°.")

except Exception as e:
    print("вќЊ РћС€РёР±РєР°:", e)

finally:
    driver.quit()