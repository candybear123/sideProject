import requests
from bs4 import BeautifulSoup
import pandas as pd


#職缺抓取爬蟲練習

try:
    data=pd.read_excel('每日廠商職缺.xlsx')
    #公司名稱
    comN=data['公司名稱']
    page=0
   
    count=0
    
    comNS=''
    for i in range(len(comN)):
        comNS+=comN[i]
    
    #jobTitle=[]
    #jobUrl=[]
    #comNa=[]
except:
    print('input data error')





try:    
    while count <= 20:
        
        jobTitle=[]
        jobUrl=[]
        comNa=[]
    
        #給他查詢參數
        my_param={
                'keyword': 'python',
                'area': '6001001000,6001002000',
                'page': page}    
        
        url='https://www.104.com.tw/jobs/search'
           
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        
        re=requests.get(url,params=my_param,headers=header)
        
        print(re.status_code)
        print()
        soup=BeautifulSoup(re.text,'lxml')
        #print(soup.prettify())
    
        
        #抓工作的title、連結
        job=soup.select('div.b-block__left > h2 > a')
        com=soup.select('div.b-block__left > ul:nth-child(2) > li:nth-child(2) > a')
        try:
            for j in range(len(job)):
                jobTitle.append(job[j].text)
                comNa.append(com[j].text.strip())
                jobUrl.append(job[j]['href'])
        except:
            print('href error')
            pass
                   
        for i in range(len(jobTitle)):
            if (comNa[i] not in comNS):
                url2='https:'+jobUrl[i]
                re2=requests.get(url2,headers=header)
                if re2.status_code==200:
                    #print('200*')
                    soup2=BeautifulSoup(re2.text,'lxml')
                    root=soup2.find('main').find_all('section')
                    tool=root[1].text
                    mail=root[3].text                 
                    
                    if '@' in mail and ('python'or'Python'or'MySQL' in tool):
                        count+=1
                        print(comNa[i])
                        print(jobTitle[i])
                        
        page+=1
        print('='*30)
except:
    print('error')


    
