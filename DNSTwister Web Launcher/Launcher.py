import pandas as pd
from selenium import webdriver
from tkinter.filedialog import askopenfilename
from tkinter import Tk

def open_tab(driver,website):
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(website)

def get_domainList():
	#Open csv
        while True:
                try:
                        Tk().withdraw()
                        # Read in urls as a dataframe
                        csvfile = askopenfilename(initialdir="/", title="Please Select domainList.csv", filetypes=(("CSV (Comma delimited)", "*.csv"), ("Excel workbook", "*.xlsx")))
                        domains_df = pd.read_csv(csvfile)
                        # For readability
                        domains = domains_df['domain']
                        return domains
                except:
                        print("Wrong file uploaded. Please upload a domainList.csv file!")
                else:
                        break
def get_searchvalues(domains):
        searchvalue_list=[]
        for domain in domains:
                searchvalue = ""
                for char in domain:
                        hexvalue = format(ord(char), 'x')
                        searchvalue += hexvalue
                searchvalue_list.append(searchvalue)
        return searchvalue_list


domains = get_domainList()
searchvalues = get_searchvalues(domains)

url = "https://dnstwister.report/search?ed=" + searchvalues[0]

driver.get(url)
for i in searchvalues[1:]:
        url = "https://dnstwister.report/search?ed=" + i
        open_tab(driver,url)


