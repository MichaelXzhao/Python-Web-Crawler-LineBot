from bs4 import BeautifulSoup
import requests
 

 
# 熱門餐廳爬蟲
class IFoodie:
    
    def __init__(self,area):
        self.area= area
        
        
 
    def scrape(self):
        
        url='https://ifoodie.tw/explore/'+ self.area +'/list?sortby=popular&opening=true'
        response = requests.get(url)
 
        soup = BeautifulSoup(response.text, "html.parser")
 
        # 爬取前五筆餐廳卡片資料
        cards = soup.find_all(
            'div', {'class': 'jsx-3292609844 restaurant-info'}, limit=5)
 
        content = ""
        n=1
        for card in cards:
 
            title = card.find(  # 餐廳名稱
                "a", {"class": "jsx-3292609844 title-text"}).getText()
 
            stars = card.find(  # 餐廳評價
                "div", {"class": "jsx-1207467136 text"}).getText()
 
            address = card.find(  # 餐廳地址
                "div", {"class": "jsx-3292609844 address-row"}).getText()
            
            r= 'TOP'+str(n)+' '+ title+'\n'+ stars+'顆星'+'\n'+address+'\n\n'
            
            #將取得的餐廳名稱、評價及地址連結一起，並且指派給content變數
            content += r
            n+=1
 
        return content
    
    

  
