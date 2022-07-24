from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup 
import csv 



PATH = "/Users/farhanishraq/Downloads/Summer 2022/chromedriver"
driver = webdriver.Chrome(PATH)

url = 'https://leetcode.com/tag/recursion/'
driver.get(url) 

table = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "table-responsive")))
html = table.get_attribute("outerHTML")
soup = BeautifulSoup(html, 'html.parser')


def getProblem(tablecols):
    for i in range(len(tablecols)):
        if tablecols[2].find("a").text:
            return tablecols[2].find("a").text

def getProblemLink(tablecols):
    for i in range(len(tablecols)):
        if tablecols[2].find("a")['href']:
            return tablecols[2].find("a")['href']
        else:
            return None

def getDifficulty(tablecols):
    for i in range(len(tablecols)):
        return tablecols[4].find("span").text

def getAcceptance(tablecols):
    for i in range(len(tablecols)):
        return tablecols[3].text


with open('problems.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["problem_name","problem_link","difficulty","acceptance"])
    tablerows = soup.findAll("tr")
    for tablerow in tablerows:
        tablecols = tablerow.findAll("td")
        problem = getProblem(tablecols)
        if getProblemLink(tablecols):
            problemLink = "https://leetcode.com"+getProblemLink(tablecols)
        else:
            problemLink = None 
        difficulty = getDifficulty(tablecols)
        acceptance = getAcceptance(tablecols)

        try:
            writer.writerow([problem, problemLink, difficulty, acceptance])
        except:
             print("There was something wrong with " + problem + ". It could not be recorded")


    


driver.close()