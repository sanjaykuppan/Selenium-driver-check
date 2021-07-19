from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import os.path
import requests
import zipfile
import wget

class Loaddriver:

    def __init__(self):
        self.fname="chromedriver.exe"

    #get latest chrome driver 
    def getdriver(self):
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        response = requests.get(url)
        version_number = response.text
        download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"
        latest_driver_zip = wget.download(download_url,'chromedriver.zip')
        #remove old version of chromedriver.exe
        if os.path.isfile(self.fname):
            os.remove(self.fname)
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall() # specify destination folder path here
        os.remove(latest_driver_zip)
        print("Driver updated successfully!")

    #check driver version and browser version
    def checkdriver(self):
        def sampletest():
            driver=webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://www.google.com/")
            driver.find_element_by_name("q").send_keys("github")
            time.sleep(3)
            driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
            time.sleep(3)
            driver.quit()
            print("Driver Updated!")

        if os.path.isfile(self.fname):
            try:
                driver=webdriver.Chrome(self.fname)
                driver.quit()
                print("Driver latest version already present!")
            except Exception as e:
                print(e.msg)
                ind=e.msg.index("browser")
                browserver=e.msg[ind+19:ind+31]
                ind=e.msg.index("Chrome version")
                drivever=e.msg[ind+15:ind+17]
                print("Browser version :"+browserver)
                print("Driver version :"+drivever)
                self.getdriver()
            finally:
                if __name__=="__main__":
                    sampletest()  

        else:
            self.getdriver()
            if __name__=="__main__":
                sampletest()
            


if __name__=="__main__":
    Loaddrver=Loaddriver()
    Loaddrver.checkdriver()
