import re, requests, os, time 
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# List of regular expressions indicating that the web page has sql vulnerabilities
#TODO : add for all databases info.
sql_errors = {
    "MySQL": (),
    "PostgreSQL": (),
    "Microsoft SQL Server": (),
    "Microsoft Access": (),
    "Oracle": (),
    "IBM DB2": (),
    "SQLite": (),
    "Informix": (),
    "Sybase": ()
}

# function that receives the HTML code of the web page and checks it for the presence of keys
# indicating the presence of SQL injection, returns two variables - True/False

def checksql(html):
    for db, errors in sql_errors.items():
        for error in errors:
            if re.compile(error).search(html):
                return True, db
    return False, None

# Create a list of options for running Geckodriver in stealth mode
opts = webdriver.ChromeOptions()
#opts = webdriver.Chrome(ChromeDriverManager().install())
opts.headless = True
browser = webdriver.Chrome(options=opts)

# Open the file from where we will take the list of dorks
f = open('dorcs.txt', 'r', encoding='UTF-8')

# Open the file where we will write vulnerable URLs
f2 = open('sqls.txt', 'w', encoding='UTF-8')

def checkcheck (url):
    return True





