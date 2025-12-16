from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
import time
import logging
from driver_helper import WebDriverHelper

class Authorization:
    def __init__(self, driver):
        self.driver = driver
        self.helper = WebDriverHelper(driver)

    def click_all_allow_buttons(self):
        for _ in range(3):
                    try:
                        btn = self.helper.short_wait_present(
                            (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
                        )
                        btn.click()
                        time.sleep(0.5)
                    except TimeoutException:
                        break
        special_btn = self.helper.short_wait_present((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.RelativeLayout").instance(2)'))
        special_btn.click()
        time.sleep(1)
        switch_btn = self.helper.short_wait_present((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("android:id/switch_widget")'))
        switch_btn.click()
        time.sleep(1)
        btn2 = self.helper.short_wait_present((AppiumBy.ID, 'com.android.settings:id/permission_enable_allow_button'))
        btn2.click()
        for _ in range(3):
            try:
                back_btn = self.helper.short_wait_present((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Перейти вверх")'))
                back_btn.click()
                time.sleep(1)
            except TimeoutException:
                break


    def login(self, username, password):
        login_field = self.helper.long_wait_present((AppiumBy.ID, 'com.bifit.cashdesk.mobile.webserver:id/phoneInput'))
        login_field.send_keys(username)

        password_field = self.driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile.webserver:id/editTextPassword')
        password_field.send_keys(password)

        self.driver.hide_keyboard()
        time.sleep(0.5)

        login_button = self.driver.find_element(AppiumBy.ID, 'com.bifit.cashdesk.mobile.webserver:id/loginButton')
        login_button.click()

    def click_access_code(self):
        buttons = [
            'button_1',
            'button_2',
            'button_3',
            'button_4'
        ]

        # Проверяем наличие блока по первой кнопке
        if not self.helper.exists((AppiumBy.ID, 'com.bifit.cashdesk.mobile.webserver:id/button_1')):
            return

        for _ in range(2):
            for btn in buttons:
                locator = (AppiumBy.ID, f'com.bifit.cashdesk.mobile.webserver:id/{btn}')
                self.helper.short_wait_present(locator).click()

    def select_organization_and_object(self):

        # 1. Попытка выбрать организацию
        try:
            first_organization = self.helper.short_wait_present(
                (AppiumBy.XPATH, "//android.widget.ListView/android.widget.LinearLayout[1]")
            )
            first_organization.click()
            logging.info("Клик по организации выполнен")
        except TimeoutException:
            logging.info("Список организаций отсутствует. Продолжаем выполнение теста.")

        # 2. Попытка выбрать торговый объект
        try:
            first_object = self.helper.short_wait_present(
                (AppiumBy.XPATH,
                 '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.bifit.cashdesk.mobile.webserver:id/recycler"]'
                 '/android.widget.RelativeLayout[1]')
            )
            first_object.click()
            logging.info("Клик по торговому объекту выполнен")
        except TimeoutException:
            logging.info("Список торговых объектов отсутствует. Продолжаем выполнение теста.")

       # 3. Ожидание появления кнопки сайд-меню
        try:
            side_menu = self.helper.short_wait_present(
                (AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton")
            )
            side_menu.click()
            logging.info("Клик по кнопке сайд-меню выполнен")
        except TimeoutException:
            logging.error("Кнопка сайд-меню не появилась — тест прерван.")
            return





