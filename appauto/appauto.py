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
        desired_caps["appTopLevelWindow"] = window_by_title("Bitcoin Core")
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)
        self.driver.switch_to.active_element

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def getresults(self):
        displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("Display is " )
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext

    def test_combination(self):
        edits = self.driver.find_elements_by_tag_name("Edit")        
        ok = self.driver.find_elements_by_tag_name("Button")
        
        edits[0].click()
        edits[0].clear()
        edits[0].send_keys("qqq")
        
        edits[1].click()
        edits[1].clear()
        edits[1].send_keys("qqq")
        
        edits[2].click()
        edits[2].clear()
        edits[2].send_keys("qqq")
        
        ok[2].click()
        
        

        self.assertEqual("8","8")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BitcoinCorePassInputTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
