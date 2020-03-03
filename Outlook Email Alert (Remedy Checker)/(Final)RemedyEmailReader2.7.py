import win32com.client
import pythoncom
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
import winsound
import Tkinter as tk
import logging


def call_alert():
    pythoncom.CoInitialize()
    # range 0(low) - 100(loud)
    volume = 100
    # range -10(slow) - 10(fast)
    rate = -2

    text = 'Alert! Remedy Ticket Created!'
    winsound.PlaySound("C:\\Users\\ntuintern\\Downloads\\pythonscripts\\Remedy Email Alert Checker(Python+Microsoft Flow)\\RemedySound.wav",winsound.SND_FILENAME)
    speak = win32com.client.Dispatch('Sapi.SpVoice')
    speak.Rate = rate
    speak.Volume = volume
    speak.Speak(text)

def getIncidentID(bodytext):
    #Based on email from Microsoft Flow, obtain incident ID
    return bodytext.split(" ")[2].split("\n")[0]

def getPriority(bodytext):
    #Based on email from Microsoft Flow, obtain priority
    return bodytext.split(" ")[3].strip()

def display_alert(priority,incidentID):
    #Create a window for each alert
    window = tk.Toplevel()
    window.title("Remedy Alert!")
    window.geometry("400x120")
    window.resizable(width=False, height=False)
    #Popup above all windows and stays above
    window.lift()
    window.attributes("-topmost", True)
    #Default colour
    bgcolour ="#F0F0F0"
    #Set colour of background window based on priority
    if priority == "Critical":
        bgcolour = "red3"
    elif priority == "High":
        bgcolour = "red2"
    elif priority == "Medium":
        bgcolour = "yellow"
    elif priority == "Low":
        bgcolour = "yellow2"
    window.configure(bg = bgcolour)
    #display Incident ID and close button
    tk.Label(window, text = "Remedy Incident",bg =bgcolour,font = " Helvetica 15").pack(side = "top")
    tk.Label(window, text = incidentID,bg=bgcolour,font = " Helvetica 30 bold").pack()
    close_btn = tk.Button(window, text = "Close", command = window.destroy) # closing the 'window' when you click the button
    close_btn.pack(side = "bottom")

def remedy_check(root):
    pythoncom.CoInitialize()
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    #get root_folder based on index in Outlook. Then obtain subfolder Remedy-ALERT
    root_folder = outlook.Folders.Item(1)
    remedyAlertBox = root_folder.Folders['Remedy-ALERT']
    print(remedyAlertBox.Name + " is running!")
    #Store all messages in Remedy-ALERT to loop through
    messages = remedyAlertBox.Items
    #Check for unassigned remedy emails(Will be initially unread) then flag and read it
    for message in messages:
        if message.UnRead:
            print(message.Subject)
            message.FlagRequest = "Alert Settled"
            message.FlagStatus = 1
            message.UnRead = False
            bodytext = message.body
            priority = getPriority(bodytext)
            incidentID = getIncidentID(bodytext)
            #Display popup alert
            display_alert(priority,incidentID)
            root.update() #To update the view since mainloop is not nearby
            #Initiate voice alert
            call_alert()
            
    #recursive function to run remedy_check every xxx milliseconds
    root.after(2000,remedy_check,root)
    
#Initialise root window
root = tk.Tk()
#Hide the root window since it is not applicable
root.withdraw()
remedy_check(root)
#Only can have one mainloop. It's an infinite loop until root window is close(will not happen in our case)
root.mainloop()

