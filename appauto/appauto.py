import unittest
from appium import webdriver
import pygetwindow as gw


def window_by_title(title):
    ws = gw.getWindowsWithTitle(title)[0]
    if ws:
        ws.minimize()
        ws.restore()
        return str(hex(ws._hWnd))
    else:
        return None
    


class BitcoinCorePassInputTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #set up appium
        desired_caps = {}
        #desired_caps["app"] = "C:\\Program Files\\Bitcoin\\bitcoin-qt.exe"
        #desired_caps["appTopLevelWindow"] = window_hwnd("KeePass.exe")
        desired_caps["platformName"] = "Windows"
        desired_caps["appTopLevelWindow"] = window_by_title("db.kdbx - KeePass")
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def getresults(self):
        displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("Display is " )
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext


    #def test_initialize(self):
    #    self.driver.find_element_by_name("Clear").click()
    #    self.driver.find_element_by_name("Seven").click()
    #    self.assertEqual(self.getresults(),"7")
    #    self.driver.find_element_by_name("Clear").click()


    def test_combination(self):
        elements = self.driver.find_elements("Изменить пароль")
        elements[2] = '1'
        elements[4] = '12'
        elements[6] = '123'
        self.assertEqual("8","8")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BitcoinCorePassInputTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
