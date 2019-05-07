# TC01 - Signup | Phone Number Field Empty.

# Expected result
# Message "Field cannot be empty".

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
driver.find_element_by_id("io.neksosh.passenger.debug:id/continueButton").click()


