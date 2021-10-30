import requests
import pandas as p
from bs4 import BeautifulSoup

def MS(link):
    global BCoMSN
    global BCoMSH
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoMSN=[]
    BCoMSH=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoMSN.append(c) 
   
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoMSH.append(total)
def MS2(link):
    global BCoMSN2
    global BCoMSH2
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoMSN2=[]
    BCoMSH2=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoMSN2.append(c) 
   
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoMSH2.append(total)
def MS3(link):
    global BCoMSN3
    global BCoMSH3
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoMSN3=[]
    BCoMSH3=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoMSN3.append(c) 
   
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoMSH3.append(total)
                        
def WS(link):
    global BCoWSN
    global BCoWSH
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoWSN=[]
    BCoWSH=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoWSN.append(c) 
   
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoWSH.append(total)
def WS2(link):
    global BCoWSN2
    global BCoWSH2
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoWSN2=[]
    BCoWSH2=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoWSN2.append(c) 
   
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoWSH2.append(total)
def WS3(link):
    global BCoWSN3
    global BCoWSH3
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoWSN3=[]
    BCoWSH3=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoWSN3.append(c) 
   
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoWSH3.append(total)

    
def MV(link):
    global BCoMVN
    global BCoMVH
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoMVN=[]
    BCoMVH=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoMVN.append(c) 
   
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoMVH.append(total) 
def MV2(link):
    global BCoMVN2
    global BCoMVH2
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoMVN2=[]
    BCoMVH2=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoMVN2.append(c) 
   
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoMVH2.append(total) 
def MV3(link):
    global BCoMVN3
    global BCoMVH3
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoMVN3=[]
    BCoMVH3=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoMVN3.append(c) 
   
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoMVH3.append(total) 
  
            
def WV(link):
    global BCoWVN
    global BCoWVH
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoWVN=[]
    BCoWVH=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoWVN.append(c) 
     
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoWVH.append(total) 
def WV2(link):
    global BCoWVN2
    global BCoWVH2
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoWVN2=[]
    BCoWVH2=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoWVN2.append(c) 
     
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoWVH2.append(total) 
def WV3(link):
    global BCoWVN3
    global BCoWVH3
    URL = link
    page = requests.get(URL, verify=True)
    soup = BeautifulSoup(page.content, 'html.parser')
    List = soup.find_all('li', class_="sidearm-roster-player")
    HeightlList = soup.find_all('li', class_="sidearm-roster-player")   
    BCoWVN3=[]
    BCoWVH3=[]
    
    for z in List:
        a = z.find_all('div', class_="sidearm-roster-player-name")
        for b in a:
            c = b.find_all('a')
            for d in c:
                c = d.get_text()
                BCoWVN3.append(c) 
     
    for x in HeightlList:
        a = x.find_all('span', class_="sidearm-roster-player-height")
        for u in a:
            b = u.get_text()
            b = b.strip('"')
            b = b.split("'")
            feet = int(b[0]) * 12
            inches = float(b[1])
            total = feet + inches
            BCoWVH3.append(total) 
            
            
            
#College Men’s Swimming Team
MS('https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster')
MS2('https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster')
MS3('https://yorkathletics.com/sports/mens-swimming-and-diving/roster')

MS=p.DataFrame()
MS['Name']         = BCoMSN
MS['Height']       = BCoMSH


MS2=p.DataFrame()
MS2['Name']         = BCoMSN2
MS2['Height']       = BCoMSH2


MS3=p.DataFrame()
MS3['Name']         = BCoMSN3
MS3['Height']       = BCoMSH3

MS = MS2.append(MS,ignore_index=True)
MS = MS3.append(MS,ignore_index=True)

#Answer1
print("\n\n Answer 1 \n\n")
print("All players of the men’s swimming team \n", MS)

#College WoMen’s Swimming Team
WS('https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster')
WS2('https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster')
WS3('https://queensknights.com/sports/womens-swimming-and-diving/roster')


WS=p.DataFrame()
WS['Name']         = BCoWSN
WS['Height']       = BCoWSH

WS2=p.DataFrame()
WS2['Name']         = BCoWSN2
WS2['Height']       = BCoWSH2

WS3=p.DataFrame()
WS3['Name']         = BCoWSN3
WS3['Height']       = BCoWSH3

WS = WS2.append(WS,ignore_index=True)
WS = WS3.append(WS,ignore_index=True)

#Answer2
print("\n\n Answer 2 \n\n")
print("All players of the Women’s swimming team \n", WS)

#Men’s Volleyball Team = MV    
MV('https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster/2019')
MV2('https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster')
MV3('https://yorkathletics.com/sports/mens-volleyball/roster')


MV=p.DataFrame()
MV['Name']         = BCoMVN
MV['Height']       = BCoMVH


MV2=p.DataFrame()
MV2['Name']         = BCoMVN2
MV2['Height']       = BCoMVH2


MV3=p.DataFrame()
MV3['Name']         = BCoMVN3
MV3['Height']       = BCoMVH3


MV = MV2.append(MV,ignore_index=True)
MV = MV3.append(MV,ignore_index=True)

#Answer3 
print("\n\n Answer 3 \n\n")
print("All players of the men’s volleyball team \n", MV)

#Women’s Volleyball Team = MV   
WV('https://www.brooklyncollegeathletics.com/sports/womens-volleyball/roster/2019')
WV2('https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster')
WV3('https://johnjayathletics.com/sports/womens-volleyball/roster')

WV=p.DataFrame()
WV['Name']         = BCoWVN
WV['Height']       = BCoWVH


WV2=p.DataFrame()
WV2['Name']         = BCoWVN2
WV2['Height']       = BCoWVH2


WV3=p.DataFrame()
WV3['Name']         = BCoWVN3
WV3['Height']       = BCoWVH3

WV = WV2.append(WV,ignore_index=True)
WV = WV3.append(WV,ignore_index=True)

#Answer4 
print("\n\n Answer 4 \n\n")
print("All players of the women’s Volleyball team \n", WV)

#Answer5 
print("\n\n Answer 5 \n\n")
MS_mean= MS['Height'].mean()
print("Men’s Swimming Avg Height: ",MS_mean)
WS_mean= WS['Height'].mean()
print("Women’s Swimming Avg Height: ", WS_mean)
MV_mean= MV['Height'].mean()
print("Men’s volleyball Avg Height: ", MV_mean)
WV_mean= WV['Height'].mean()
print("Women’s volleyball Avg Height: ", WV_mean)


#Answer6 
print("\n\n Answer 6 \n\n")
MS_tall= MS.nlargest(5, 'Height')
print("Tallest men swimmers \n",MS_tall, "\n")
MS_short= MS.nsmallest(5, 'Height')
print("Shortest men swimmers \n",MS_short, "\n")

WS_tall= WS.nlargest(5, 'Height')
print("Tallest women swimmers \n",WS_tall, "\n")
WS_short= WS.nsmallest(5, 'Height')
print("Shortest women swimmers \n",WS_short, "\n")

MV_tall= MV.nlargest(5, 'Height')
print("Tallest men volleyball players \n",MV_tall, "\n")
MV_short= MV.nsmallest(5, 'Height')
print("Shortest men volleyball players \n",MV_short, "\n")

WV_tall= WV.nlargest(5, 'Height')
print("Tallest women volleyball players \n",WV_tall, "\n")
WV_short= WV.nsmallest(5, 'Height')
print("Shortest women volleyball players \n",WV_short, "\n")

#Answer6 
print("\n\n Answer 7 \n\n")

# =============================================================================
# From homework 1, we saw that the average male swimmers are shorter than the average male volleyball player. As well as the average female swimmers are shorter than the average female volleyball player. 
# From the vast data we collected, we see the same result showing throughout the different gender and sports. First, we will talk about the avg height of the swimmers for both genders. The average Men’s Swimmer Height is 70.71 and the women’s Swimmer Height is 64.85. Statistically, it’s known that men are taller than women in general world pollution, and we can see that from the data we have collected can calculate. It reflects the same on the sport of volleyball as well. The average Men’s Volleyball player Height is 70.71 and the women’s Volleyball Player Height is 64.85. 
# Our main objective for this project is to find out if the average swimmer is taller than the average volleyball player. And the answer is no. Volleyball players of both genders are taller than the average height of swimmers. The tallest player in all these groups is Akil Vaughn at 77.0 inches, who is a volleyball player. The shortest player in all these groups is Young Gi Go    60.0 and Amanda Lee 60.0.  Both of these individuals play different sports. One is a swimmer, and one is a volleyball player.  We can conclude that Volleyball players are taller than swimmers. But why is that? As in Volleyball, there are different positions played by the Volleyball team. Spikers need to be taller than the net, so they can easily reach above the blocker to spike the ball above the enemy blockers. Height gives a competitive advantage in Volleyball. Where else in swimming, you need to have good stamina and have a variety of techniques to win a race. If you are a shorter swimmer, you don't have to exert as much energy as the taller swimmer would to gain the same distance.
# The average swimmer is shorter than a volleyball player. It doesn't matter if they are male or female. 
# 
# 
# =============================================================================



