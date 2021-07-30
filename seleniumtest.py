from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os.path
import os
import requests
import zipfile
import wget
import sys

class Loaddriver:

    def __init__(self,path=""):
        self.fname=path+"chromedriver.exe"
        self.path=path

    #get latest chrome driver 
    def getdriver(self,version_number):
        try:
            if os.path.isdir(self.path) is False:
                os.mkdir(self.path)
            if version_number=='':
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
            print("\n Driver updated successfully!")
        except:
            print("unable to connect to internet!!")
            os._exit(0)

    #check driver version and browser version
    def checkdriver(self):
        #method to handle exception
        def handle_execpt(e):
            try:
                if e.msg=="unknown error: cannot find Chrome binary":
                        print(e.msg, "\nPlease install chrome and try again!")
                        os._exit(0)
                    #print(e.msg)  
                ind=e.msg.index("browser")
                browserver=e.msg[ind+19:ind+31]
                ind=e.msg.index("Chrome version")
                drivever=e.msg[ind+15:ind+17]
                print("Browser version :"+browserver)
                print("Driver version :"+drivever)
                url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_'+browserver[0:2]
                response = requests.get(url)
                version_number = response.text
                self.getdriver(version_number)
            except:
                print("Check internet connection and try again, unable to conenct to internet!!")
                sys.exit()
        #Connection test function
        def sampletest():
            try:
                opt = Options()
                opt.headless = True
                if __name__=='__main__':
                    print("test window!!")
                driver=webdriver.Chrome(self.fname,options=opt)
                driver.maximize_window()
                driver.get("https://www.google.com/")
                driver.quit()
                print("Driver Working fine!")
            except Exception as e:
                handle_execpt(e)
                os._exit(0)
        if os.path.isfile(self.fname):
            try:
                opt = Options()
                opt.headless = True
                driver=webdriver.Chrome(self.fname,options=opt)
                driver.quit()
                print("Driver latest version already present!")
            except Exception as e:
                handle_execpt(e)
                os._exit(0)
            finally:
                if __name__=="__main__":
                    sampletest()     
        else:
            self.getdriver(version_number='')
            sampletest()
            if __name__=="__main__":
                print("program complete!")


if __name__=="__main__":
    Loaddrver=Loaddriver("test/")
    Loaddrver.checkdriver()
