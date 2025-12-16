from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebDriverHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.short_wait = WebDriverWait(driver, 2)
        self.long_wait = WebDriverWait(driver, 50)

    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_disappears(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def short_wait_present(self, locator):
        return self.short_wait.until(EC.presence_of_element_located(locator))

    def short_wait_clickable(self, locator):
        return self.short_wait.until(EC.element_to_be_clickable(locator))

    def short_wait_visible(self, locator):
        return self.short_wait.until(EC.visibility_of_element_located(locator))

    def long_wait_present(self, locator):
        return self.long_wait.until(EC.presence_of_element_located(locator))

    def tap(self, x, y):
        self.driver.execute_script("mobile: clickGesture", {
            "x": int(x),
            "y": int(y)
        })

    def tapK10(self):
        # координаты клавиши K10
        K10_X = 600
        K10_Y = 600
        self.tap(K10_X, K10_Y)


    def exists(self, locator, timeout=2):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
