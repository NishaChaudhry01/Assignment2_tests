import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

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
        

    def test_TC01_assert_title(self):
        actual = self.driver.title
        expected = "Sign in to GitHub · GitHub"
        self.assertEqual(actual,expected)    

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
             

    def test_TC03_createaccount_link(self):
        create_account = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Create an account")))
        create_account.click()
        print("page navigated after click:",self.driver.title) 
  

    def test_TC04_back_to_previouspage(self):
        create_account = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Create an account")))
        create_account.click()
        print("page title:",self.driver.title)

        self.driver.back()
        print("previous page/signin page title:",self.driver.title) 


class TestHomePage(TestGitHubBase):
    def setUp(self) -> None:
        self.driver.get("https://github.com/")
    def tearDown(self) -> None:
        self.driver.delete_all_cookies
        print ("Test completed!")
        

    def test_TC05_search_button(self):
        search = self.mywait.until(EC.element_to_be_clickable((By.NAME,"q")))
        
        search.send_keys("webpage_tests")
        search.send_keys(Keys.RETURN)


    def test_TC06_subscribe_button(self):
        height = self.driver.execute_script("return document.body.scrollHeight")
        for scrol in range(2000,height,2000):
            self.driver.execute_script(f"window.scrollTo(0,{scrol})")

        subscribe = self.mywait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/footer/div[1]/div/div[1]/div/a")))
        subscribe.click()
        print("page navigated after click:",self.driver.title)
    

    def test_TC07_scroll_page_slowly(self):
        height = self.driver.execute_script("return document.body.scrollHeight")
        for scrol in range(2000,height,2000):
            self.driver.execute_script(f"window.scrollTo(0,{scrol})")

    def test_TC08_forward_to_nextpage(self):
        sign_in = self.mywait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a")))
        sign_in.click()
        print("Sign in page title:",self.driver.title)

        self.driver.back()
        print("Home page page title:",self.driver.title)

        self.driver.forward()
        print("Sign in page title:",self.driver.title)


if __name__=='__main__':
    unittest.main()
    
