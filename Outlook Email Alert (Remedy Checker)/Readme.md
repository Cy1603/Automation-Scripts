A python script which polls for unread emails in a specific Outlook folder and throws a visual and sound alert if it contains one.

The use case for this script is for a SecOps environment. It is to generate an alert from the SOC (Security Operation Centre) mainscreen for critical event logs so that analyst can rectify them immediately.

How it works:
1. It is actually incorporated with Microsoft Flow to throw alerts not just in the SOC mainscreen, but also in the SOC's Microsoft Teams chat.
2. An email for an incident event log will be send to a mailbox.
3. Since the log can be from a previous incident, there is a Microsoft Flow workflow script which will first analyse the email for duplicates.
4. If the log is new, it will be checked for its urgency priority. if the urgency is critical, the logs will be sent to the SOC Microsoft Teams chat group to notify the analysts.
5. There is a chance that the analyst did not notice the Teams message. Hence, the email will be forwarded to the company's Outlook email box which stores Critical logs.
6. Since the email is new, this script will check for unread emails in the event box and throw an alert in the office environment.

How to use:
1. Download and login to your Outlook email.
2. Set-up the email box to poll for in the python script. This can be modified in "root_folder = outlook.Folders.Item(1)" for the mailbox index and "remedyAlertBox = root_folder.Folders['Remedy-ALERT']" for the subfolder.
3. Run the script.

