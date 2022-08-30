from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

driver = webdriver.Chrome()

driver.get('https://www.espn.com/soccer/transfers')

data = {}

n = driver.find_elements_by_xpath("//td[@class='Table__TD']/div/a")
d = driver.find_elements_by_xpath("//span[@class='hide-mobile']")

for i in range(0, len(n)):
    name = n[i].text
    club = d[(i * 2) + 1].text
    data[name] = club

with open('output.json', 'w') as outfile:
    json.dump(data, outfile)


