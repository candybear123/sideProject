from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
from datetime import datetime
import re

#捷運站附近餐廳抓取爬蟲練習

area_data = {
    '臺北市': [
        '中正區', '大同區', '中山區', '萬華區', '信義區', '松山區', '大安區', '南港區', '北投區', '內湖區', '士林區', '文山區'
    ],
    '新北市': [
        '板橋區', '新莊區', '泰山區', '林口區', '淡水區', '金山區', '八里區', '萬里區', '石門區', '三芝區', '瑞芳區', '汐止區', '平溪區', '貢寮區', '雙溪區', '深坑區', '石碇區', '新店區', '坪林區', '烏來區', '中和區', '永和區', '土城區', '三峽區', '樹林區', '鶯歌區', '三重區', '蘆洲區', '五股區'
    ]}



#抓取各個捷運站
def MRT():
    url='https://m.metro.taipei/roadmap.asp'

    res=requests.get(url)
    res.encoding='utf-8'
    soup=bs(res.text,'html.parser')
    
    selections=soup.find('select',id='sstation').find_all('optgroup')
    
    station={}
    for select in selections:
        a=[]
        for i in select.find_all('option'):
            a.append(i.text.split(' ')[-1])
           
        station[select.get('label')]=a
    return station


def getMrt_mapping(name):
    dd=pd.read_csv(r'mrt_MappingList.csv')
    line=dd[dd['站名']==name].iloc[0,1]
    return line

url ='https://www.google.com.tw/maps/'


def Crawler(station):
    #打開瀏覽器,確保已經有chromedriver在你的目錄下
    browser=webdriver.Chrome()
    #設定最大loading時間
    browser.set_page_load_timeout(200)
    #在瀏覽器打上網址連入
    browser.get(url) 
    
    #輸入捷運站名
    place = browser.find_element_by_id('searchboxinput')
    place.send_keys(station)
        
    browser.implicitly_wait(5)
    browser.find_element_by_id('searchbox-searchbutton').click()
    time.sleep(3)
    #出現查詢關鍵字有多個結果
    try:
        tt=browser.find_elements_by_class_name('section-result-title')
        for t in range(len(tt)):
            
            if '捷運' in tt[t].text :
                browser.find_elements_by_class_name('section-result-content')[t].click()

        mtype=browser.find_elements_by_class_name('section-result-details')
        for m in range(len(mtype)):
            if mtype[m].text=='大眾運輸站':
                browser.find_elements_by_class_name('section-result-content')[m].click()
                break
            elif mtype[m].text=='地鐵站':
                browser.find_elements_by_class_name('section-result-content')[m].click()
                break
    except TimeoutException:
        for i in range(5):
            WebDriverWait(browser, 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'section-result-content')))
        
        mtype=browser.find_elements_by_class_name('section-result-details')
        for m in range(len(mtype)):
            if mtype[m].text=='大眾運輸站':
                browser.find_elements_by_class_name('section-result-content')[m].click()
                break
            elif mtype[m].text=='地鐵站':
                browser.find_elements_by_class_name('section-result-content')[m].click()
                break
    except:
        pass    
    
    
    
    # 等待 捷運站相關 的section出現
    try:
        place = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, 'section-layout')))
    except:
        place = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, 'section-layout')))
    
    #點選附近
    try:
        WebDriverWait(browser, 10).until(
        expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'iRxY3GoUYUY__button')))
        near = browser.find_elements_by_class_name('iRxY3GoUYUY__button')[2]
        near.click()
    except:
        for i in range(10):
                
            WebDriverWait(browser, 30).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'iRxY3GoUYUY__button')))
            near = browser.find_elements_by_class_name('iRxY3GoUYUY__button')[2]
            near.click()
        
    
    #選擇餐廳
    
    time.sleep(3)
    place = browser.find_element_by_id('searchboxinput')
    place.send_keys('餐廳')
    time.sleep(3)
    
    browser.find_element_by_id('searchbox-searchbutton').click()
    
    place = WebDriverWait(browser, 10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME, 'section-layout'))
    )
    
    time.sleep(3)
    
    #準備list裝所有資料
    data=[]    
    Week=[]
    rc=0
    
    while rc<100:
       
            
        count=0
  
        #取得所有餐廳
        titles=browser.find_elements_by_class_name('section-result-title')
        
        for i in range(len(titles)):
            
   
            try:
                
                WebDriverWait(browser, 30).until(
                expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'section-result-title')))
                
                titles=browser.find_elements_by_class_name('section-result-title') 
                time.sleep(3)
                titles[i].click()
                
                WebDriverWait(browser, 30).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, 'section-info-line')))
#                    print(456)             
            except TimeoutException:
                for i in range(10):
                    WebDriverWait(browser, 30).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, 'section-info-line')))
                    print('等待第{}個30秒'.format(i))
                pass
            except:
                titles=browser.find_elements_by_class_name('section-result-title') 
                time.sleep(3)
                titles[i].click()
                
                WebDriverWait(browser, 30).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, 'section-info-line')))
            
            
            try:
                time.sleep(3)
                title=browser.find_element_by_class_name('GLOBAL__gm2-headline-5').text
                rcategory=browser.find_elements_by_class_name('section-rating-term')
                infoSection=browser.find_elements_by_class_name('section-info-line')
                star=browser.find_element_by_class_name('section-star-display').text
                
            except:
                star='無星等'
                pass
      
            #抓電話
            try:
                tel=''
                for i in infoSection:
                    if i.text.replace(' ','').isdigit():
                        tel=i.text.replace(' ','')
            except:
                tel=''
            
            #抓地址、市、區
            addr=infoSection[0].text
            pattern1 = re.compile(r'(..市)')
            pattern2 = re.compile(r'(..區)')
            try:
                #抓市
                result1=pattern1.search(addr)
                city=result1.group(1)
             
            except:
                try:
                    #由行政區判斷縣市
                    result2=pattern2.search(addr)
                    dist=result2.group(1)
                    if result2!=None:
                        result2=pattern2.search(addr)
                        dist=result2.group(1)
                        for i in area_data['臺北市']:
                            if i == dist:
                                city='臺北市1'
                                break
                        if city=='':
                            for i in area_data['新北市']:
                                if i == dist:
                                    city='新北市'
                                    break
                                
                    else:
                        city=''
                        
                except:
                    city=''
            
            try:
                #抓區
                result2=pattern2.search(addr)
                dist=result2.group(1)
            except:
                if '試院路' in addr:
                    dist='文山區'
                else:
                    dist=''
            
      
            
            #抓餐廳類型
            try:
                category=''
                for i in rcategory:
                    if i.text.isalpha():
                        category=i.text
            except:
                category=''
            #抓餐廳評論數
            try:
                for i in rcategory:
                    pattern = re.compile(r'([0-9]+)')
                    result=pattern.search(i.text)
                    if  result:
                        comCount=result.group(1)
                        break
                    else:
                        comCount='0'
            except:
                comCount='0'
                
            #點擊營業時間出現營業時間列表        
            try:
                WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'section-open-hours-button')))
                browser.find_element_by_class_name('section-open-hours-button').click()

                Open=browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')
            except TimeoutException:
                pass
            except:
                target_elem = browser.find_element_by_class_name('section-open-hours-button')
                browser.execute_script("arguments[0].click();",target_elem)
                #使用解決暫時隱藏的方法失敗，要用解決永久隱藏的方法
#                WebDriverWait(browser, 5).until(expected_conditions.invisibility_of_element_located((By.CLASS_NAME, 'section-open-hours-button')))
#                browser.find_element_by_class_name('section-open-hours-button').click()
#
                Open=browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')
                print('點不出來')
            
            try:        
                o={}        
                for i in Open:
                    week=i.find_element_by_tag_name('th').text
                    op=i.find_element_by_tag_name('td').text.replace('\n','')
                    if '休息' in op:
                        if '星期日' in week:
                            o['Sun']=0
                        elif '星期一' in week:
                            o['Mon']=0
                        elif '星期二' in week:
                            o['Tue']=0
                        elif '星期三' in week:
                            o['Wed']=0
                        elif '星期四' in week:
                            o['Thu']=0
                        elif '星期五' in week:
                            o['Fri']=0
                        elif '星期六' in week:
                            o['Sat']=0
                 
                    else:
                        if '星期日' in week:
                            o['Sun']=1
                        elif '星期一' in week:
                            o['Mon']=1
                        elif '星期二' in week:
                            o['Tue']=1
                        elif '星期三' in week:
                            o['Wed']=1
                        elif '星期四' in week:
                            o['Thu']=1
                        elif '星期五' in week:
                            o['Fri']=1
                        elif '星期六' in week:
                            o['Sat']=1
                    Week.append(o)        
            except:
                o={'Sun':'無資訊','Mon':'無資訊','Tue':'無資訊',\
                   'Wed':'無資訊','Thu':'無資訊','Fri':'無資訊','Sat':'無資訊'}  
                Week.append(o)
            

            data.append([title,category,star,comCount,city,dist,addr,tel])
            count+=1
            rc+=1
            try:
                    
                browser.find_element_by_class_name('section-back-to-list-button').click()
        #        browser.get(url1) 第一頁沒問題，第2頁會出錯，出現又返回第1頁的問題
                time.sleep(3)
            except:
               WebDriverWait(browser,10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'section-back-to-list-button'))).click()
               time.sleep(3)
   
        try:
            browser.find_element_by_id('n7lv7yjyC35__section-pagination-button-next').click()
        except:
            WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'n7lv7yjyC35__section-pagination-button-next'))).click()
             

    browser.quit()  
    return data,Week

def toDataFrame(stdir,data,name,week):
    line=getMrt_mapping(name)
    table=pd.DataFrame(columns=['Line','Station','Name','Type','Star','Comment','Tel','City','Dist','Addr','CostS','CostE','Sun','Mon','Tue','Wed','Thu','Fri','Sat'])
    
        
    for it,we in zip(data,week):
        try:
            item=pd.DataFrame({'Line':line,'Station':name+'站','Name':it[0],\
                               'Type':it[1],'Star':it[2],'Comment':it[3],'Tel':it[7],\
                               'City':it[4],'Dist':it[5],'Addr':it[6],'CostS':'空',\
                               'CostE':'空','Sun':we['Sun'],'Mon':we['Mon'],'Tue':we['Tue'],\
                               'Wed':we['Wed'],'Thu':we['Thu'],'Fri':we['Fri'],'Sat':we['Sat']},index=[0])
            table=table.append(item,ignore_index=True)
        except:
            item=pd.DataFrame({'Line':line,'Station':name+'站','Name':it[0],\
                               'Type':it[1],'Star':it[2],'Comment':it[3],'Tel':it[7],\
                               'City':it[4],'Dist':it[5],'Addr':it[6],'CostS':'空',\
                               'CostE':'空','Sun':'','Mon':'','Tue':'',\
                               'Wed':'','Thu':'','Fri':'','Sat':''},index=[0])
            table=table.append(item,ignore_index=True)
            
    if name=='台北101/世貿':
        name='台北101or世貿'
        table.to_csv(os.path.join(stdir,r''+name+'站.csv'))
    else:
        table.to_csv(os.path.join(stdir,r''+name+'站.csv'))

start=datetime.now()
print('開始：',start)     


station=MRT()


s=[]
for i in station.keys():
    s.append(i)
#
#for d in range(1,len(s)-1):    
#    stdir=s[d]
#    if not os.path.exists(stdir):
#        os.mkdir(stdir)
#
#    BL=station[s[d]]
#    print(stdir)
#    for j in range(len(BL)):
#        data,week=Crawler(BL[j]+'站')
#        toDataFrame(stdir,data,BL[j],week)

if not os.path.exists('R 淡水信義線'):
        os.mkdir('R 淡水信義線')
stdir='R 淡水信義線'       
BL=station['R 淡水信義線']
 
#for j in range(len(BL)):
data,week=Crawler(BL[27]+'站')
toDataFrame(stdir,data,BL[27],week)

   
        

end=datetime.now()    
print('結束：',end)
print(end-start)

