import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class TestGitHubBase(unittest.TestCase):
    #To open the browser
    @classmethod
    def setUpClass(cls) -> None:
        service_object = Service("C:\\Selenium webdriver\\chromedriver\\chromedriver_win32 (1)\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service_object)
        cls.mywait = WebDriverWait(cls.driver,10)
        cls.driver.maximize_window()       
    @classmethod   
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
       # cls.driver.delete_all_cookies()

class TestSignInPage(TestGitHubBase):
    def setUp(self) -> None:
        self.driver.get("https://github.com/login")#opens the homepage
    def tearDown(self) -> None:
        self.driver.delete_all_cookies
        print ("Test completed!")
        
    # Test to see if title of the page is correct
    def test_TC01_assert_title(self):
        actual = self.driver.title
        expected = "Sign in to GitHub · GitHub"
        self.assertEqual(actual,expected)   

 
    # Test to check if the login is succesfull or not
    def test_TC02_login(self):
        self.driver.find_element(By.NAME,"login").send_keys("NishaChaudhry01")
        self.driver.find_element(By.ID,"password").send_keys("Aniya4845455")
        self.driver.find_element(By.NAME,"commit").click()

        #wait for the login process to complete
        self.mywait.until(lambda x:x.execute_script("return document.readyState ==='complete'"))

        #to verify that login was successful
        error_message = "incorrect username or password"
        #retrive any errors found
        errors = self.driver.find_elements(By.CLASS_NAME,"flash-error")
        # when errors are found the login will fail
        if any(error_message in e.text for e in errors):
            print("Login failed")
        else:
            print("Login successful")    
             
    # Test to check if the create account link takes us to the desired page or not
    def test_TC03_createaccount_link(self):
        create_account = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Create an account")))
        create_account.click()
        expected = "Join GitHub · GitHub"
        actual = self.driver.title
        # checking for the title match
        self.assertNotEqual(actual, expected, "Title does not match expected value")   
        

class TestHomePage(TestGitHubBase):
    def setUp(self) -> None:
        self.driver.get("https://github.com/")
    def tearDown(self) -> None:
        self.driver.delete_all_cookies
        print ("Test completed!")
        

    def test_TC04_search_button(self):
        search = self.mywait.until(EC.element_to_be_clickable((By.NAME,"q")))
        
        search.send_keys("webpage_tests")
        search.send_keys(Keys.RETURN)
         # Verify that the search results page is displayed
        expected = "Search · webpage_tests · GitHub"
        actual = self.driver.title
        self.assertEqual(actual, expected, f"Failed: Expected '{expected}', but got '{actual}'")


    def test_TC05_subscribe_button(self):
        height = self.driver.execute_script("return document.body.scrollHeight")
        for scrol in range(2000,height,2000):
            self.driver.execute_script(f"window.scrollTo(0,{scrol})")

        subscribe = self.mywait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/footer/div[1]/div/div[1]/div/a")))
        subscribe.click()
        actual_title = self.driver.title
        print("page navigated after click:", actual_title)
        # this is for not matching and showing faild
        assert "GitHub" in actual_title, "Title after clicking subscribe button doesn't contain 'GitHub'"


if __name__=='__main__':
    unittest.main()
    
