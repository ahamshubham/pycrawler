import bs4,requests,urllib
from urllib.request import urlopen

base_url="http://www.jabong.com"

url_list = []
count=0

#Maximum depth of crawling
n_max=3

def get_links(url,l):
    global count
    count=count+1
    print(count,url)
    if l>=n_max:
        return
    r=requests.get(url)
    soup = bs4.BeautifulSoup(r.text,"lxml")
    for i in soup.select("a"):
        if 'href' not in i.attrs:
            continue
        link=i.attrs['href']
        if len(link)==0:
            continue    
        # Only accepts for relative links or links that start with http
        if link[0]=='/':
            link=base_url+link
            if link not in url_list:
                url_list.append(link)
                get_links(link,l+1)
        elif len(link)<4:
            continue
        elif link[:3]=='http':
            if link not in url_list:
                url_list.append(link)
                get_links(link,l+1)
        

get_links(base_url,0)
for i in url_list:
    print(i)

print(len(url_list))
