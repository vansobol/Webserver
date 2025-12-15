import time
import subprocess
import pytest
from pages.authorization import Authorization

def test_authorization_android(driver_setup):
    driver, udid = driver_setup

    # очистка данных
    subprocess.run(['adb', '-s', udid, 'shell', 'pm', 'clear', 'com.bifit.cashdesk.mobile.webserver'])
    time.sleep(1)

    # запуск LAUNCHER activity
    subprocess.run([
        'adb', '-s', udid, 'shell', 'am', 'start',
        '-a', 'android.intent.action.MAIN',
        '-c', 'android.intent.category.LAUNCHER',
        '-n', 'com.bifit.cashdesk.mobile.webserver/com.bifit.cashdesk.android.activity.login_options.LoginOptionsActivity'
    ])
    time.sleep(2)

    auth = Authorization(driver)
    auth.click_all_allow_buttons()
    auth.login(username='demo@gli', password='1234qwer')
    auth.click_access_code()
    auth.select_organization_and_object()

