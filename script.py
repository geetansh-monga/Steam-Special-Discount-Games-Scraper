from bs4 import BeautifulSoup
import requests

url = "https://store.steampowered.com/search/?specials=1&specials=1"

try:
    page = requests.get(url)
    page.raise_for_status()
    print('''                                                                                                   
                                                                                                   
 222222222222222         000000000          000000000                           kkkkkkkk           
2:::::::::::::::22     00:::::::::00      00:::::::::00                         k::::::k           
2::::::222222:::::2  00:::::::::::::00  00:::::::::::::00                       k::::::k           
2222222     2:::::2 0:::::::000:::::::00:::::::000:::::::0                      k::::::k           
            2:::::2 0::::::0   0::::::00::::::0   0::::::0        ooooooooooo    k:::::k    kkkkkkk
            2:::::2 0:::::0     0:::::00:::::0     0:::::0      oo:::::::::::oo  k:::::k   k:::::k 
         2222::::2  0:::::0     0:::::00:::::0     0:::::0     o:::::::::::::::o k:::::k  k:::::k  
    22222::::::22   0:::::0 000 0:::::00:::::0 000 0:::::0     o:::::ooooo:::::o k:::::k k:::::k   
  22::::::::222     0:::::0 000 0:::::00:::::0 000 0:::::0     o::::o     o::::o k::::::k:::::k    
 2:::::22222        0:::::0     0:::::00:::::0     0:::::0     o::::o     o::::o k:::::::::::k     
2:::::2             0:::::0     0:::::00:::::0     0:::::0     o::::o     o::::o k:::::::::::k     
2:::::2             0::::::0   0::::::00::::::0   0::::::0     o::::o     o::::o k::::::k:::::k    
2:::::2       2222220:::::::000:::::::00:::::::000:::::::0     o:::::ooooo:::::ok::::::k k:::::k   
2::::::2222222:::::2 00:::::::::::::00  00:::::::::::::00      o:::::::::::::::ok::::::k  k:::::k  
2::::::::::::::::::2   00:::::::::00      00:::::::::00         oo:::::::::::oo k::::::k   k:::::k 
22222222222222222222     000000000          000000000             ooooooooooo   kkkkkkkk    kkkkkkk''')
except requests.exceptions.RequestException:
    print(print('''sorry there is some problem. Please check your internet connectiom or contact:                                                                                                                  
                                                                                                                 
        GGGGGGGGGGGGGMMMMMMMM               MMMMMMMM        GGGGGGGGGGGGG     OOOOOOOOO             GGGGGGGGGGGGG
     GGG::::::::::::GM:::::::M             M:::::::M     GGG::::::::::::G   OO:::::::::OO        GGG::::::::::::G
   GG:::::::::::::::GM::::::::M           M::::::::M   GG:::::::::::::::G OO:::::::::::::OO    GG:::::::::::::::G
  G:::::GGGGGGGG::::GM:::::::::M         M:::::::::M  G:::::GGGGGGGG::::GO:::::::OOO:::::::O  G:::::GGGGGGGG::::G
 G:::::G       GGGGGGM::::::::::M       M::::::::::M G:::::G       GGGGGGO::::::O   O::::::O G:::::G       GGGGGG
G:::::G              M:::::::::::M     M:::::::::::MG:::::G              O:::::O     O:::::OG:::::G              
G:::::G              M:::::::M::::M   M::::M:::::::MG:::::G              O:::::O     O:::::OG:::::G              
G:::::G    GGGGGGGGGGM::::::M M::::M M::::M M::::::MG:::::G    GGGGGGGGGGO:::::O     O:::::OG:::::G    GGGGGGGGGG
G:::::G    G::::::::GM::::::M  M::::M::::M  M::::::MG:::::G    G::::::::GO:::::O     O:::::OG:::::G    G::::::::G
G:::::G    GGGGG::::GM::::::M   M:::::::M   M::::::MG:::::G    GGGGG::::GO:::::O     O:::::OG:::::G    GGGGG::::G
G:::::G        G::::GM::::::M    M:::::M    M::::::MG:::::G        G::::GO:::::O     O:::::OG:::::G        G::::G
 G:::::G       G::::GM::::::M     MMMMM     M::::::M G:::::G       G::::GO::::::O   O::::::O G:::::G       G::::G
  G:::::GGGGGGGG::::GM::::::M               M::::::M  G:::::GGGGGGGG::::GO:::::::OOO:::::::O  G:::::GGGGGGGG::::G
   GG:::::::::::::::GM::::::M               M::::::M   GG:::::::::::::::G OO:::::::::::::OO    GG:::::::::::::::G
     GGG::::::GGG:::GM::::::M               M::::::M     GGG::::::GGG:::G   OO:::::::::OO        GGG::::::GGG:::G
        GGGGGG   GGGGMMMMMMMM               MMMMMMMM        GGGGGG   GGGG     OOOOOOOOO             GGGGGG   GGGG'''))


html = page.text
soup = BeautifulSoup(html, 'html.parser')  
container = soup.find("div", { "id" : "search_resultsRows" })
tags = container.find_all("a")

for divs in tags:
   title = (divs.find("div",{"class":"responsive_search_name_combined"}).div.span.text)
   print("Title: " + title)
   platform = (divs.find("div",{"class":"responsive_search_name_combined"}).div.p.span.get('class')[1])
   print("Platfrom: " + platform)
   released_date = (divs.find("div",{"class":"col search_released responsive_secondrow"}).text)
   print("Release Date: " + released_date)
   discount = (divs.find("div",{"class":"col search_discount responsive_secondrow"}).span.text)
   print("Discount of:" + discount)
   prices = (divs.find("div",{"class":"col search_price discounted responsive_secondrow"}).stripped_strings)
   flag = 1
   for price in prices:
      if (flag == 1):
         print("MRP: " + price)
         flag = flag * -1
      else:
         print("Currenet Price: " + price)
   link = divs.get('href')
   print(link)
   print("_______________________________________________________________________________________________________")
   