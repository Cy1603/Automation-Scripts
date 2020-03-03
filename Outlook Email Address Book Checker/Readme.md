A python script which checks for emails in a log file and then check their existence in the Outlook Address Book.

How it works:
1. The a.log file contains multiple emails in a messy log file.
2. A simple regex is done to extract the emails from the log file.
3. The emails are checked in the Outlook Address Book of the current user. Do note that you must have Outlook installed and logged in.

How to use:
1. Drag and drop a.log into the exe. 

Troubleshoot:
1. Run the python script with a.log as argument in the cmd and debug from there. 
2. Once debugged and modified the python file, then use auto-py-to-exe to convert it to an exe file.
