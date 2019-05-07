# TC77 - Signup | Enter a Valid Phone Number.

# Expected result
# Phone number accepted.

from appium import webdriver
from time import sleep
import sys

caps = {}
caps["deviceName"] = "Pixel"
caps["platformName"] = "Android"
caps["platformVersion"] = "8"
caps["appPackage"] = "io.neksosh.passenger.debug"
caps["appActivity"] = "io.neksosh.passenger.business.launcher.LauncherActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

my_number = sys.argv[1]

driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
driver.find_element_by_id("io.neksosh.passenger.debug:id/phoneNumberInput").send_keys(my_number)
driver.find_element_by_id("io.neksosh.passenger.debug:id/continueButton").click()