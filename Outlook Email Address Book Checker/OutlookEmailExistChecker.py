import re
import codecs
import win32com.client
import sys


def validate(emailToValidate):

    outlook = win32com.client.gencache.EnsureDispatch('Outlook.Application')

    recipient = outlook.Session.CreateRecipient(emailToValidate)

    if recipient.AddressEntry.Type == "EX":
        email_address = recipient.AddressEntry.GetExchangeUser().PrimarySmtpAddress
        
        if recipient.Resolve() == True:
            print(email_address+" exist in address book. CHECK AGAIN!")
            
        else:
            #EX resolve false. Should not even happen.
            print("EX Error Message. Please ask for assistance.")

    elif recipient.AddressEntry.Type == "SMTP":
        email_address = recipient.AddressEntry.Address
        
        if recipient.Resolve() == True:
            print(email_address+" does NOT exist in address book.")
        else:
            #SMTP resolve false. Should not even happen.
            print("SMTP Error Message. Please ask for assistance.")
    else:
        print("No case ERROR Message. Please ask for assistance.")

def main():
    try:
        #To open file by dropping in
        droppedFile = sys.argv[1]
        print("Reading "+ droppedFile)
        #to store content of file in variable file
        file="".join([i for i in codecs.open(droppedFile,"r","utf-16")])
    except:
        print("Please drop file into the exe rather than open it!")
        input()
        sys.exit()

    #file="".join([i for i in codecs.open("TM-2019-08-27-868947-DWAC_error.log","r","utf-16")])

    #to obtain emails by matching email format
    match = re.findall(r'[\w\.-]+@[\w\.-]+', file)

    #to remove duplicates
    match = list(dict.fromkeys(match))


    for j in match:
        validate(j)

    input("Check complete! Press enter to exit.")

if __name__ == "__main__":
    main()


        
   
    
