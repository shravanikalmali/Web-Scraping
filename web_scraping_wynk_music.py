
import requests
import string
from bs4 import BeautifulSoup
list_char=[]
for letter in string.ascii_lowercase:
   list_char.append(str(letter))
list_char.remove("w")
list_char.remove("x")

URL ="https://wynk.in/music/package/trending-in-hindi/amsta_4jf452131595580528558?ref=sub_header"
myURL=[]
reqs=[]
reqs.append(requests.get(URL))
page0=BeautifulSoup(reqs[0].content,'html5lib')
links=page0.find_all(class_='jsx-7c093e1a359b5feb text-title font-normal line-clamp-1 md:line-clamp-2 text-sm hover:underline')
newlink=[]
newnewlink=[]
for link in links: 
    newlink=link.get('href')
    newnewlink="https://wynk.in"+newlink
    print(newnewlink)
