from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os.path
import requests
import zipfile
import wget

class Loaddriver:

    def __init__(self,path=""):
        self.fname=path+"chromedriver.exe"
        self.path=path

    #get latest chrome driver 
    def getdriver(self):
        if os.path.isdir(self.path) is False:
            os.mkdir(self.path)
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        response = requests.get(url)
        version_number = response.text
        download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"
        latest_driver_zip = wget.download(download_url,out=self.path+'chromedriver.zip')
        #remove old version of chromedriver.exe
        if os.path.isfile(self.fname):
            os.remove(self.fname)
        with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
            zip_ref.extractall(self.path) # specify destination folder path here
        os.remove(latest_driver_zip)
        print("/n Driver updated successfully!")

    #check driver version and browser version
    def checkdriver(self):
        def sampletest():
            opt = Options()
            opt.headless = True
            print("test window!!")
            driver=webdriver.Chrome(self.fname,options=opt)
            driver.maximize_window()
            driver.get("https://www.google.com/")
            driver.quit()
            print("Driver Working fine!")

        if os.path.isfile(self.fname):
            try:
                opt = Options()
                opt.headless = True
                driver=webdriver.Chrome(self.fname,options=opt)
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
                print("program complete!")


if __name__=="__main__":
    Loaddrver=Loaddriver("test/")
    Loaddrver.checkdriver()
