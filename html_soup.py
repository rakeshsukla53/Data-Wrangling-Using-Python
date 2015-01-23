__author__ = 'rsukla'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the approprate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function

from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:

        soup = BeautifulSoup(html)
        inputvs = soup.find("input", id="__VIEWSTATE")
        data["viewstate"] =  inputvs['value']
        inputev = soup.find("input", id="__EVENTVALIDATION")
        data["eventvalidation"] =  inputev['value']
        print data
        '''
        from BeautifulSoup import BeautifulSoup
        html = #the HTML code you've written above
        parsed_html = BeautifulSoup(html)
        print parsed_html.body.find('div', attrs={'class':'container'}).text
        '''

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_data(html_page)
    #assert data["eventvalidation"] != ""
    #assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
    #assert data["viewstate"].startswith("/wEPDwUKLTI")


test()

'''
reference for solving this problem
soup = BeautifulSoup(r.content)

soup.prettify()

soup.find_all("a")


#for link in soup.find_all("a"):
#    if "http" in link.get("href"):
#        print "<a href = '%s'>%s</a>" %(link.get("href"), link.text)

g_data = soup.find_all("div", {"class": "info"})

for item in g_data:
    print item.contents[0].find_all("a", {"class": "business-name"})[0].text
    print item.contents[1].find_all("p", {"class": "adr"})[0].text
    try:
        print item.contents[1].find_all("li", {"class": "primary"})[0].text
    except:
        pass
'''

'''
finding the _viewstate and __eventmanager using beautiful programs
'''


'''
More elegant solution here--->

def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        ev = soup.find(id="__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]

        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]

    return data
'''








