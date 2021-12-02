from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

starturl="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("C:/Users/Vidhi/Desktop/Whj/chromedriver")
browser.get(starturl)
time.sleep(10)
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
planet_data=[]
newplanet=[]
def scrape():
    for i in range (0,428):
        while True:
            time.sleep(2)
            soup=BeautifulSoup(browser.page_source,"html.parser")
            currentpage=int(soup.find_all("input",attrs={"class","page_num"})[0].get("value"))
            if currentpage<i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif currentpage>i:
                browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else:
                break

        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            hyperlink_li_tag=li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a", href=True)[0]["href"])
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
def scrapemoredata(hyperlink):
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content,"html.parser")
        temp_list=[]
        for trtag in soup.find_all("tr",attrs={"class":"fact_raw"}):
            tdtags=trtag.find_all("td")
            for tdtag in tdtags:
                try :
                    temp_list.append(tdtag.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        newplanet.append(temp_list)
    except:
        time.sleep(1)
        scrapemoredata(hyperlink)
scrape()
for index,data in enumerate(planet_data):
    scrapemoredata(data[5])
    print("printingpage ",index+1)
for index,data in enumerate(planet_data):
    newpdelement=newplanet[index]
    newpdelement=[elm.replace("\n","") for elm in newpdelement]
    newpdelement=newpdelement[:7]
    finaldata.append(data+newpdelement) 

with open("final.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(finaldata)


