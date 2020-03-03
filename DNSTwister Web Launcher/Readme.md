A simple python script that reads the URLs in the domainList.csv and automatically launch multiple DNSTwister chrome tabs which queries the said URLs.
It is an automation script useful for Threat Intelligence by allowing user to check multiple URLs in DNSTwister without manually opening tabs and searching for the URLs.

How to use:
1. Add URLs into domainList.csv
2. Run Launcher.py
3. Select domainList.csv
4. Wait for chrome to launch.

Troubleshoot:
1. Chromedriver may not match the current chrome version. Check your chrome version and download the current version of the chromedriver. Put it in the chromedriver_32 directory and change the path in the script: driver = webdriver.Chrome(executable_path="chromedriver_win32\\chromedriver80.exe")
2. Certain modules not install. Ensure pandas,selenium and tkinter is installed. Can be install with the "pip install {module}" in the cmd.
