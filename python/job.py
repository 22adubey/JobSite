import requests
from bs4 import BeautifulSoup

BASE_URL = f"https://www.simplyhired.com"


#1. HTTP Get: Get the data from website with url
#2. Get soup of HTML from the variable we make at #1
#3. Find one div with class "pagination"
#4. In pagination, find all li's
#5. For each li, get the aria-label attribute of li's child
#6. Try printing #5 and see what we get
#7. Return the last page whose data type is int
def _extract_last_page_num(url):
    """
    Get the last page number
    :param url: str
    :return: int
    """
    #agent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
    #HTTP GET: Get data from url
    response = requests.get(url)
    #Get soup of HTML from response var
    soup = BeautifulSoup(response.text,"html.parser")
    #from the html soup, find the div with the class "pagination"
    try:
        nav = soup.find("nav", {"aria-label": "Pagination"})
        lis= nav.find_all("li")
        az=nav.find_all("a")
        num_list = []
        for a in az:
            text = a.string
            num_list.append(text)
        #div = soup.find("div", {"class": "LeftPane"})
        #div = soup.find("div")
        return (int(num_list[-2]))
    except:
        return 0

#1. In html (parameter), find the title
#1.1 We want to get one element who has the attribute "title"
#       For this we can pass title=True as a second arg like this:
#       html.find("span, title=True").string
#2. Find company, location, job title, and job description
def _extract_job(html):
    """
    Get a dictionary of a job's information
    :param html: Tag
    :return: dict[str, str]
    """
    simplyHired = "www.simplyhired.com"
    jobs = []
    title = html.find("h3", {"class":"jobposting-title"}).string
    company=html.find("span",{"class":"JobPosting-labelWithIcon jobposting-company"}).string
    applyLink = html.find("a",{"class":"SerpJob-link card-link"}).get("href")
    location=html.find("span",{"class":"jobposting-location"}).find("span",{"class":"jobposting-location"}).string
    description = html.find("p",{"class":"jobposting-snippet"}).string
    simplyHired += applyLink
    return {
        "title":title,
        "company":company,
        "applyLink":simplyHired,
        "location":location,
        "description": description
    }

#1. Make a "jobs" list to store each job's data.
#2. Repeatedly until we hit last_page_num:
#2.1 HTTP Get: Get the data from website with url
#2.2 Get soup of HTML from the variable we make at 2.1
#2.3 Find all divs from 2.2 whos class is "LeftPane" 
#2.4 For each div in 2.3 divs, append each div where we invoke _extract_job()
def _extract_jobs(term, last_page_num,location):
    jobs = []
    if last_page_num==0:
        return jobs
    for i in range(last_page_num):
        url = BASE_URL + f"/search?q={term}"  + f"&l={location}"  + f"&pn={i+1}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        divs = soup.find("div",{"class":"LeftPane"})
        try:
            lis = divs.find_all("li")
            #headings=divs.find_all("h3", {"class":"jobposting-title"})
            for li in lis:
                if(li.find("h3", {"class":"jobposting-title"})!=None):
                    #print(li)
                    jobs.append(_extract_job(li))
        except:
            return jobs
    return jobs
        
            #head=dv.find("h3", {"class":"jobposting-title"})
            #print(head)
            
            #title = head.find("a")
            #print(title.string)


#1. Make a job URL
#2. Get the last page # from _extract_last_page_num()
#3. Extract jobs with _extract_jobs()
#4. Return jobs
def get_jobs(search_term,location):
    """
    Extract jobs until the last page from website
    :param search_term: str
    :return: list[dict[str,str]]
    """
    #use the python f command, format, to use search term param in url
    page_number = 1
    url = BASE_URL + f"/search?q={search_term}" + f"&l={location}" + f"&pn={page_number}"
    last_page_num = _extract_last_page_num(url)
    jobs = _extract_jobs(search_term,last_page_num,location)
    return jobs

#get_jobs("Python","Dallas")