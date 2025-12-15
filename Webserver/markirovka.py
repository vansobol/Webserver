
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys
import os


from selenium.webdriver.common.action_chains import ActionChains

import subprocess
from appium.webdriver.common.appiumby import AppiumBy

def test_markirovka(driver_setup):
    driver, udid = driver_setup
    mark = "136303469896970619001CERZEYGXGE2JKSHHGDAMNIIRVQEF5A3HWKWIK2PDSOKVRDE42U3SXGZWB4QNTHELURSE37YOQAR2G7FMU3SRXO7UFHGPOR5Y3C4HYSWOARCO26DRI7BAKFZ6GRBES7USQ"
    input_field = driver.find_element(AppiumBy.ID,'com.bifit.cashdesk.mobile.webserver.webserver:id/text_input_alcohol_mark')
    input_field.click()
    input_field.send_keys(mark + "\n")

    # mark = "136303469896970619001CERZEYGXGE2JKSHHGDAMNIIRVQEF5A3HWKWIK2PDSOKVRDE42U3SXGZWB4QNTHELURSE37YOQAR2G7FMU3SRXO7UFHGPOR5Y3C4HYSWOARCO26DRI7BAKFZ6GRBES7USQ"
    # input_command = f'adb shell input text "{mark}"'
    # os.system(input_command)
    # ActionChains(driver).send_keys(mark).send_keys(Keys.ENTER).perform()

    # mark = "0000004621065422dBtACAAPidGVz"
    #
    #
    #
    #
    #
    # # Подготовка команды для ADB
    # input_command = f'adb shell input text "{mark}"'
    #
    # # Отправляем команду
    # os.system(input_command)
    #
    # # Нажимаем Enter после передачи строки
    # os.system("adb shell input keyevent 66")