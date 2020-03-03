import requests
from selenium import webdriver
import time
import re
import tkinter as tk
import pandas as pd

def find_hashtags(hashtag):
    driver = webdriver.Chrome(executable_path="chromedriver_win32\\chromedriver80.exe")
    driver.get('https://twitter.com/search?q=%23' + hashtag)
    for i in range(100):
        #print(i)
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Scrolling page " + str(i+1))
        time.sleep(1.5)
        
        twitter_elm = driver.find_elements_by_class_name("tweet")
        new_height = driver.execute_script("return document.body.scrollHeight")
        #print("new height"+ str(new_height))
        #print("last height"+ str(last_height))

        if new_height == last_height:
            break
        last_height = new_height
        

    allposts = ""
    for post in twitter_elm:
        tweet = post.find_element_by_class_name("tweet-text")
        #print(tweet.text)
        allposts += tweet.text

    print("Obtaining hashes..")
    hashlist = re.findall("[0-9a-fA-F]{32}",allposts)
    #print(hashlist)
    print("Saving hashes to csv file..")
    df = pd.DataFrame(hashlist,columns=["Hashes"])
    filename = "Hashtag_"+str(hashtag)+".csv"
    df.to_csv(filename, encoding='utf-8', index=False)
    print(filename+" saved in same directory.")

        
def ok(hashtag_guess,hashtag_get):
    global hashtag
    hashtag = hashtag_guess.get()
    print("Automation begins..")
    hashtag_get.destroy()
    
hashtag_get = tk.Tk()
hashtag_get.title("Twitter Hashtag")
hashtag_get.geometry("500x150")
hashtag_text = tk.Label(hashtag_get, text="Enter the Hashtag without #:", font="Serif 25")
hashtag_guess = tk.Entry(hashtag_get, font="Serif 25")
okbtn = tk.Button(text="Ok", command= lambda :ok(hashtag_guess,hashtag_get), height=2, width=10)
hashtag_text.pack()
hashtag_guess.pack()
okbtn.pack()
hashtag_get.mainloop()

            
find_hashtags(hashtag)
