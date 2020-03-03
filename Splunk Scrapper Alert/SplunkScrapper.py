from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import Tkinter as tk
import pythoncom
import winsound
import win32com.client
from selenium.common.exceptions import StaleElementReferenceException

def call_alert():
    pythoncom.CoInitialize()
    # range 0(low) - 100(loud)
    volume = 100
    # range -10(slow) - 10(fast)
    rate = -1.5

    text = 'A new Splunk critical or high urgency unassigned'
    winsound.PlaySound("C:\\Users\\ntuintern\\Downloads\\Selenium\\fileopening\\Splunk.wav",winsound.SND_FILENAME)
    speak = win32com.client.Dispatch('Sapi.SpVoice')
    speak.Voice = speak.GetVoices().Item(1)
    speak.Rate = rate
    speak.Volume = volume
    speak.Speak(text)

def display_alert(newCritical,newHigh):
    #Create a window for each alert
    window = tk.Toplevel()
    window.title("Splunk Alert!")
    window.geometry("500x150")
    window.resizable(width=False, height=False)
    #Popup above all windows and stays above
    window.lift()
    window.attributes("-topmost", True)
    #Default colour
    bgcolour ="red2"

    window.configure(bg = "red2")
    #display Incident ID and close button
    tk.Label(window, text = "Current Unassigned",bg =bgcolour,font = " Helvetica 15").pack(side = "top")
    tk.Label(window, text = "Critical: "+newCritical,bg=bgcolour,font = " Helvetica 30 bold").pack()
    tk.Label(window, text = "High: "+newHigh,bg=bgcolour,font = " Helvetica 30 bold").pack()
    close_btn = tk.Button(window, text = "Close", command = window.destroy) # closing the 'window' when you click the button
    close_btn.pack(side = "bottom")

def write_urgencyfile(critical,high):
    urgency = open("urgency.txt","w+")
    urgency.write(critical+"\n"+high)
    urgency.close()

def urgency_update(root,driver):
    while True: #To prevent Stale Element Reference Exception when website refresh
        try:
            newCritical = driver.find_element_by_xpath("//button[@class='urgency-btn active' and @value='critical']/span[@class='urgency-btn-right-label']").text
            newHigh = driver.find_element_by_xpath("//button[@class='urgency-btn active' and @value='high']/span[@class='urgency-btn-right-label']").text
            break
        except StaleElementReferenceException:
            print("Stale Element Exception, retrying..")
    #Read file to obtain initial critical and high value    
    urgency = open("urgency.txt","r")
    values = [value.strip("\n") for value in urgency]
    critical = values[0]
    high = values[1]
    critHit = False
    highHit = False
    #Update file with new values
    write_urgencyfile(newCritical,newHigh)
    #Comparison to determine whether to throw popup and voice alert
    if(int(newCritical)>int(critical)):
        critHit = True
    if(int(newHigh)>int(high)):
        highHit = True
 
    if(critHit == True or highHit ==True):
        display_alert(newCritical,newHigh)
        root.update() #update gui view 
        call_alert() #play voice alert
        print("Critical: "+newCritical)
        print("High: "+newHigh)

    print("Checking..") #Delay to rerun method again
    root.after(10000,urgency_update,root,driver)

def initialSearch(driver):
    #deselecting info,low,medium urgency
    medbtn = driver.find_element_by_xpath("//button[@class='urgency-btn active' and @value='medium']")
    medbtn.click()
    lowbtn = driver.find_element_by_xpath("//button[@class='urgency-btn active' and @value='low']")
    lowbtn.click()
    infobtn = driver.find_element_by_xpath("//button[@class='urgency-btn active' and @value='informational']")
    infobtn.click()
    #change status to New
    allremovebtn = driver.find_element_by_xpath("(//button[@class='sc-itybZL kKafkj sc-jTzLTM eKAABD'])[1]")
    allremovebtn.click()
    newStatus = driver.find_element_by_xpath("//button[@class='sc-gGBfsJ dUygiE sc-jTzLTM eKAABD' and @value='1']")
    newStatus.click()
    clickoutside = driver.find_element_by_xpath("//body")
    clickoutside.click()
    sleep(1)
    #change owner to unassigned
    allremovebtn2 = driver.find_element_by_xpath("(//button[@class='sc-itybZL kKafkj sc-jTzLTM eKAABD'])[2]")
    allremovebtn2.click()
    unassignedStatus = driver.find_element_by_xpath("//button[@class='sc-gGBfsJ dUygiE sc-jTzLTM eKAABD' and @value='unassigned']")
    unassignedStatus.click()
    #Change to 24hours window
    selecthourbtn = driver.find_element_by_xpath("//button[@class='sc-kpOJdX hWESIZ sc-kGXeez kfKfzb sc-jTzLTM eKAABD' and @label='Last 1 hour']")
    selecthourbtn.click()
    presetbtn = driver.find_element_by_xpath("(//button[@class='sc-epnACN fuyjsX sc-jTzLTM eKAABD'])[1]")
    presetbtn.click()
    selecthourbtn = driver.find_element_by_xpath("//button[@class='sc-eNQAEJ jrYcoK sc-jTzLTM eKAABD' and @label='24 hour window']")
    selecthourbtn.click()
    #submit
    submitbtn = driver.find_element_by_xpath("//button[@class='btn btn-primary']")
    submitbtn.click()


chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(executable_path="C:\\Windows\\chromedriver.exe",options = chrome_options)
driver.get("https://example.com/en-US/app/SplunkEnterpriseSecuritySuite/incident_review")

assert "Incident Review" in driver.title, "Not Title!"
sleep(5)

initialSearch(driver)
#Wait for query
sleep(60)


critical = driver.find_element_by_xpath("//button[@class='urgency-btn active' and @value='critical']/span[@class='urgency-btn-right-label']").text
high = driver.find_element_by_xpath("//button[@class='urgency-btn active' and @value='high']/span[@class='urgency-btn-right-label']").text

write_urgencyfile(critical,high)

#Initialise root window
root = tk.Tk()
#Hide the root window since it is not applicable
root.withdraw()
urgency_update(root,driver)
#Only can have one mainloop. It's an infinite loop until root window is close(will not happen in our case)
root.mainloop()






