A python script that scrapes the incident review dashboard of Splunk for Critical and High alerts. It will then continue to poll and throw alerts in the SOC mainscreen to notify analyst the increased in important incidents, so that they can be rectified immediately.

How to use:
1. Have Splunk Enterprise Security installed. This is a company software hence very little will have use for it.
2. Set-up your user-data chrome options so as to prevent the need to key in sensitive credentials every time the script is launched.

How it works:
1. Splunk itself updates the incident review dashboard every 1.5seconds.
2. Selenium is used to automate the web scrapping part to know the number of incidents.
3. A txt file is used to save the number of important incidents. If there is an increase in such incidents, a voice and visual alert will be thrown.
