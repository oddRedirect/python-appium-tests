# TC02 - Signup | Enter Invalid phone number.

# Expected result
# Message " Enter a valid phone number" is displayed.

from appium import webdriver
from time import sleep

caps = {}
caps["deviceName"] = "Pixel"
caps["platformName"] = "Android"
caps["platformVersion"] = "8"
caps["appPackage"] = "io.neksosh.passenger.debug"
caps["appActivity"] = "io.neksosh.passenger.business.launcher.LauncherActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
driver.find_element_by_id("io.neksosh.passenger.debug:id/phoneNumberInput").send_keys("0000000000")
driver.find_element_by_id("io.neksosh.passenger.debug:id/continueButton").click()
    