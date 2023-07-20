import requests
from bs4 import BeautifulSoup

#HTTP GET: Get data from websicd jobSte with url
response = requests.get("https://your-url.com")

#Get soup of HTML from responsee var
soup = BeautifulSoup(response.text, "html.parser")
#Soup looks like this
#<div>
#   <span> We are getting ready!</span>
#   <span class="qna">Are you excited?</span>
#   <span class="qna">I am!</span>
#</div>

#gets one div and stores it in div variable
div = soup.find("div")

#see div and print its children
# print(div)

#Gets all spands inside the div (div is soup itself)
# spans = div.find_all("span")
#Gets all the spans whose class is qna
#spans = div.find_all("span", {"class": "qna"})

#Gets the one span whose id is ready
# spans = div.find_all("span", {"id": "ready"})
spans = div.find_all("span", {"id": "ready"}).text