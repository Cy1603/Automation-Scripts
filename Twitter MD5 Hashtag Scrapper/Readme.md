A python script that scrapes the MD5 hashes from tweets based on a certain hashtag query.

This is useful for Threat Intelligence to obtain variant of hashes for malware samples, such as from APT (Advanced Persistent Threat), without manually looking through every single tweet.

It can be adapted to search for user tweets instead of hashtag tweets, as well as other hash types, and for other twitter automation.

How to use:
1. Launch the python script.
2. Type in the hashtag, for example "APT32"
3. The hashes will be extracted and stored in "Hashtag_{hashtag name}.csv"
4. A sample "Hashtag_apt32.csv" is provided.

How it works:
1. Uses selenium to search the hashtag and scroll the pages.
2. Scrape the content of each tweet under the hashtag.
3. Using regex to match MD5 hashes.(Can be modified to match other type of hashes)
4. Uses pandas to store the hashes in the csv file.

Update:
Seems like Twitter changed their class identification, as such the tweets are not being scrapped. Since I am not focusing on this project anymore, I will not be updating the script anymore. Other parts of the script are still working (Automation, regex and updating csv), you can still use it after modifying the scrapping algorithm.
