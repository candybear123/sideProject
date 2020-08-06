import csv
import json
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import xml.etree.ElementTree as et
from collections import Counter
from collections import OrderedDict
from bubbly.bubbly import bubbleplot #pip install bubbly 
from plotly.offline import plot    #pip install plotly
plt.style.use('ggplot')

#中文的基本設定
mpl.rcParams['font.family']='SimSun'
mpl.rcParams['font.family']='Simhei'

#匯入新北市人口統計表(108年7月)
fn='1087_nt_population.csv'   #新北市總人口
listCsv=pd.read_csv(fn)


fn='1087_city_p0.csv'   #板橋
with open(fn,encoding='ANSI')as csvFile:
    Preader1=csv.reader(csvFile)
    listCsv1=list(Preader1)


fn='1087_city_p1.csv'   #三重
with open(fn,encoding='ANSI')as csvFile:
    Preader2=csv.reader(csvFile)
    listCsv2=list(Preader2)

fn='1087_city_p2.csv'   #中和
with open(fn,encoding='ANSI')as csvFile:
    Preader3=csv.reader(csvFile)
    listCsv3=list(Preader3)

fn='1087_city_p3.csv'   #永和
with open(fn,encoding='ANSI')as csvFile:
    Preader4=csv.reader(csvFile)
    listCsv4=list(Preader4)

fn='1087_city_p4.csv'   #新莊
with open(fn,encoding='ANSI')as csvFile:
    Preader5=csv.reader(csvFile)
    listCsv5=list(Preader5)

fn='1087_city_p5.csv'   #新店
with open(fn,encoding='ANSI')as csvFile:
    Preader6=csv.reader(csvFile)
    listCsv6=list(Preader6)
    
fn='1087_city_p6.csv'   #土城
with open(fn,encoding='ANSI')as csvFile:
    Preader7=csv.reader(csvFile)
    listCsv7=list(Preader7)
    
fn='1087_city_p7.csv'   #蘆洲
with open(fn,encoding='ANSI')as csvFile:
    Preader8=csv.reader(csvFile)
    listCsv8=list(Preader8)

fn='1087_city_p8.csv'   #樹林
with open(fn,encoding='ANSI')as csvFile:
    Preader9=csv.reader(csvFile)
    listCsv9=list(Preader9)    

fn='1087_city_p9.csv'   #鶯歌
with open(fn,encoding='ANSI')as csvFile:
    Preader10=csv.reader(csvFile)
    listCsv10=list(Preader10)
#older=sum(listCsv1[66:101][6])
    
fn='1087_city_p10.csv'   #三峽
with open(fn,encoding='ANSI')as csvFile:
    Preader11=csv.reader(csvFile)
    listCsv11=list(Preader11)
    
fn='1087_city_p11.csv'   #淡水
with open(fn,encoding='ANSI')as csvFile:
    Preader12=csv.reader(csvFile)
    listCsv12=list(Preader12)
    
fn='1087_city_p12.csv'   #瑞芳
with open(fn,encoding='ANSI')as csvFile:
    Preader13=csv.reader(csvFile)
    listCsv13=list(Preader13)
    
fn='1087_city_p13.csv'   #汐止
with open(fn,encoding='ANSI')as csvFile:
    Preader14=csv.reader(csvFile)
    listCsv14=list(Preader14)
    
fn='1087_city_p14.csv'   #五股
with open(fn,encoding='ANSI')as csvFile:
    Preader15=csv.reader(csvFile)
    listCsv15=list(Preader15)
    
fn='1087_city_p15.csv'   #泰山
with open(fn,encoding='ANSI')as csvFile:
    Preader16=csv.reader(csvFile)
    listCsv16=list(Preader16)
    
fn='1087_city_p16.csv'   #林口
with open(fn,encoding='ANSI')as csvFile:
    Preader17=csv.reader(csvFile)
    listCsv17=list(Preader17)
    
fn='1087_city_p17.csv'   #八里
with open(fn,encoding='ANSI')as csvFile:
    Preader18=csv.reader(csvFile)
    listCsv18=list(Preader18)
    
fn='1087_city_p18.csv'   #深坑
with open(fn,encoding='ANSI')as csvFile:
    Preader19=csv.reader(csvFile)
    listCsv19=list(Preader19)
    
fn='1087_city_p19.csv'   #石碇
with open(fn,encoding='ANSI')as csvFile:
    Preader20=csv.reader(csvFile)
    listCsv20=list(Preader20)
    
fn='1087_city_p20.csv'   #坪林
with open(fn,encoding='ANSI')as csvFile:
    Preader21=csv.reader(csvFile)
    listCsv21=list(Preader21)
    
fn='1087_city_p21.csv'   #三芝
with open(fn,encoding='ANSI')as csvFile:
    Preader22=csv.reader(csvFile)
    listCsv22=list(Preader22)
    
fn='1087_city_p22.csv'   #石門
with open(fn,encoding='ANSI')as csvFile:
    Preader23=csv.reader(csvFile)
    listCsv23=list(Preader23)
    
fn='1087_city_p23.csv'   #金山
with open(fn,encoding='ANSI')as csvFile:
    Preader24=csv.reader(csvFile)
    listCsv24=list(Preader24)
    
fn='1087_city_p24.csv'   #萬里
with open(fn,encoding='ANSI')as csvFile:
    Preader25=csv.reader(csvFile)
    listCsv25=list(Preader25)
    
fn='1087_city_p25.csv'   #平溪
with open(fn,encoding='ANSI')as csvFile:
    Preader26=csv.reader(csvFile)
    listCsv26=list(Preader26)
    
    
fn='1087_city_p26.csv'   #雙溪
with open(fn,encoding='ANSI')as csvFile:
    Preader27=csv.reader(csvFile)
    listCsv27=list(Preader27)
    
fn='1087_city_p27.csv'   #貢寮
with open(fn,encoding='ANSI')as csvFile:
    Preader28=csv.reader(csvFile)
    listCsv28=list(Preader28)
    
fn='1087_city_p28.csv'   #烏來
with open(fn,encoding='ANSI')as csvFile:
    Preader29=csv.reader(csvFile)
    listCsv29=list(Preader29)

#匯入新北市土地面積列表(180118)
area=pd.read_csv('180118_NTarea.csv')


#定義函數計算新北市各行政區65歲以上老年人口數
def older(city,listCsv):
    Sum=0
    older=[city,Sum]
    for i in range(66,102):
        n=listCsv[i][6]
        Sum+=int(n)
        older[1]=Sum
    return older

olderT=[]
#呼叫older()函數計算新北市各行政區65歲以上老年人口數
olderT.append(older('板橋區',listCsv1)) #計算板橋區65歲以上老年人口數
olderT.append(older('三重區',listCsv2))  #計算三重區65歲以上老年人口數
olderT.append(older('中和區',listCsv3)) #計算中和區65歲以上老年人口數
olderT.append(older('永和區',listCsv4))  #計算永和區65歲以上老年人口數
olderT.append(older('新莊區',listCsv5))   #計算新莊區65歲以上老年人口數
olderT.append(older('新店區',listCsv6))
olderT.append(older('土城區',listCsv7))
olderT.append(older('蘆洲區',listCsv8))
olderT.append(older('樹林區',listCsv9))
olderT.append(older('鶯歌區',listCsv10))
olderT.append(older('三峽區',listCsv11))
olderT.append(older('淡水區',listCsv12))
olderT.append(older('瑞芳區',listCsv13))
olderT.append(older('汐止區',listCsv14))
olderT.append(older('五股區',listCsv15))
olderT.append(older('泰山區',listCsv16))
olderT.append(older('林口區',listCsv17))
olderT.append(older('八里區',listCsv18))
olderT.append(older('深坑區',listCsv19))
olderT.append(older('石碇區',listCsv20))
olderT.append(older('坪林區',listCsv21))
olderT.append(older('三芝區',listCsv22))
olderT.append(older('石門區',listCsv23))
olderT.append(older('金山區',listCsv24))
olderT.append(older('萬里區',listCsv25))
olderT.append(older('平溪區',listCsv26))
olderT.append(older('雙溪區',listCsv27))
olderT.append(older('貢寮區',listCsv28))
olderT.append(older('烏來區',listCsv29))

total=[]    #各行政區總人口
for i in range(0,len(listCsv)-1):
    c=listCsv['隸屬區'][i] #隸屬區=行政區
    p=int(listCsv['合計'][i]) #總人口數
    e=[c,p]
    total.append(e)


total=pd.DataFrame(total)
total.columns=['行政區','總人口數']
total=total.sort_values('行政區')
olderT=pd.DataFrame(olderT)
olderT.columns=['行政區','老年人口數']
olderT=olderT.sort_values('行政區')

#total1為各行政區老年人口與總人口的整合
total1=pd.merge(olderT,total,how='left',on='行政區')
#在total1列表加上各行政區面積與人口密度
total1=pd.merge(total1,area,how='left',on='行政區')

#在total1加入老年人口比率、人口密度及都市化程度的欄位
total1.insert(3,column="老年人口比率(%)",value=round(((total1['老年人口數']/total1['總人口數'])*100),2))
total1.insert(5,column='人口密度',value=round(total1['總人口數']/total1['面積(Km²)'],2))
total1.insert(6,column='都市化程度',value=round(np.log(total1['人口密度']),2))

#畫出新北市各區都市化程度與老年人口比相關泡泡圖
figure=bubbleplot(dataset=total1,x_column='都市化程度',y_column='老年人口比率(%)',bubble_column='行政區',
                  size_column='老年人口數',color_column='行政區',
                  x_title='都市化程度(以人口密度取自然對數為都市化指標)',y_title='老年人口比',
                  title='新北市各區都市化程度與老年人口比相關泡泡圖',x_logscale=True,scale_bubble=1,height=600)
plot(figure,config={'scrollzoom': True})


#依照泡泡圖的都市化程度結果對行政區分組
total1.insert(0,column='行政區1',value=total1['行政區'])
total1=total1.set_index('行政區')
total1=total1.rename(columns={'行政區1':'行政區'})
#g1組:平溪、雙溪、坪林、貢寮、石碇、烏來
g1=total1.ix[['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']]
#g2組:瑞芳、三芝、石門、三峽、金山、萬里、八里
g2=total1.ix[['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']]
#g3組:淡水、深坑、汐止、鶯歌、新店、五股、林口、泰山、樹林、土城
g3=total1.ix[['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']] 
#g4組:板橋、中和、三重、新莊、蘆洲、永和
g4=total1.ix[['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']]


#畫出新北市老年人口佔全市總人口比例圓餅G圖
plt.figure(figsize=(7,6),facecolor='#F8F8C7')
color=['#AD66D5','#FF6B40']
x=[total1['老年人口數'].sum(),listCsv['合計'][29]-total1['老年人口數'].sum()]
plt.pie(x,labels=['新北市老年人口數','新北市非老年人口數'],shadow=True,explode=(0.1,0),autopct='%1.2f%%',counterclock=False,colors=color,textprops={'fontsize': 14})
plt.title('新北市老年人口佔全市總人口比例',fontsize=28)
plt.axis('equal')
plt.show()

#畫出4組的老年人口佔總老年人口比例
plt.figure(figsize=(7,6),facecolor='#BEAAD1')
color=['#FF4040','#FF9700','#3DA028','#5ccccc']
x1=[g1['老年人口數'].sum(),g2['老年人口數'].sum(),g3['老年人口數'].sum(),g4['老年人口數'].sum()]
plt.pie(x1,labels=['g1','g2','g3','g4'],autopct='%1.2f%%',shadow=True,counterclock=False,explode=(0,0.1,0,0),colors=color,textprops={'fontsize': 14})
plt.title('4組的老年人口比例',fontsize=28)
plt.axis('equal')
plt.show()


#匯入新北市公共托老中心(含日照中心)的json資料
fn='NewTaipeiCity_ElderCenter1.json'
with open(fn,encoding='utf-8-sig') as f:
    data=json.load(f)

#匯入新北市樂活友善供餐點的json資料
fn1='meal.json'
with open(fn1,encoding='utf-8-sig') as f1:
    data1=json.load(f1)

#匯入新北市銀髮俱樂部的xml資料
tree=et.parse('club.xml')
root=tree.getroot()
district2=[]
for i in root.findall('row'):
    e1=i.find('Col2').text
    district2.append(e1)    #將俱樂部行政區存成一個list

district2=Counter(district2)
district2N=OrderedDict(district2)

#畫出新北市銀髮俱樂部分佈長條圖
pd4=pd.DataFrame.from_dict(district2N,orient='index',columns=['個數'])
club_g1=pd4['個數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']].sum()
club_g2=pd4['個數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']].sum()
club_g3=pd4['個數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']].sum()
club_g4=pd4['個數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']].sum()
pd4.plot(kind='bar',title='新北市銀髮俱樂部分佈長條圖',width=0.2,color='#8C67A1',figsize=(10,6),rot=45)
med=float(pd4.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(14,med+5,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()
pd4_0=pd.DataFrame([club_g1,club_g2,club_g3,club_g4],index=['g1','g2','g3','g4'],columns=['個數'])
pd4_0.plot(kind='bar',title='新北市銀髮俱樂部分佈長條圖',width=0.2,color='#8C67A1',figsize=(6,5),rot=0)
i=range(4)
for a,b in zip(i,pd4_0['個數']):
    plt.text(a,b+0.1,'{}'.format(int(b)),color='#642F04',fontsize=14)
med=float(pd4_0.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(-0.5,med+5,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#設定4組新北市銀髮俱樂部分佈
pd4_1=pd4['個數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']]
pd4_2=pd4['個數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']]
pd4_3=pd4['個數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']]
pd4_4=pd4['個數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']]


#畫出新北市銀髮俱樂部分佈盒鬚圖
#離群值(outliers)是盒鬚圖籬笆外的值，就是Q1-1.5IQR(內四分位距)及Q3+1.5IQR範圍外的值
pd4_01=pd.DataFrame({'g1':pd4_1,'g2':pd4_2,'g3':pd4_3,'g4':pd4_4})
pd4_01.boxplot(fontsize=14)
plt.title('新北市銀髮俱樂部分佈盒鬚圖',fontsize=20)
plt.show()

#取出新北市公共托老中心(含日照中心)的地址
#在字串中的行政區取出來
length=len(data['result']['records'])
district=[] #托老中心所在全部行政區
mode=[] #採取的模式
for i in range(length):
    e=data['result']['records'][i]['address'][3:6] #[3:6]取出行政區的字串
    district.append(e)
    m=data['result']['records'][i]['mode']
    mode.append(m)

district=Counter(district)
districtN=OrderedDict(district)    

mode=Counter(mode)
modeN=OrderedDict(mode)


#用pandas畫出新北市公共托老中心(含日照中心)4組長條圖
#準備資料
pd1=pd.DataFrame.from_dict(districtN,orient='index',columns=['個數'])
center_g1=pd1['個數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']].sum()
center_g2=pd1['個數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']].sum()
center_g3=pd1['個數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']].sum()
center_g4=pd1['個數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']].sum()
#畫出新北市公共托老中心(含日照中心)29個行政區長條圖
pd1.plot(kind='bar',title='新北市公共托老中心(含日照中心)行政區長條圖',width=0.2,color='#006561',figsize=(10,6),rot=45)
med=float(pd1.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(10,med+0.2,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()
#畫出新北市公共托老中心(含日照中心)4組長條圖
pd1_0=pd.DataFrame([center_g1,center_g2,center_g3,center_g4],columns=['個數'],index=['g1','g2','g3','g4'])
pd1_0.plot(kind='bar',title='新北市公共托老中心(含日照中心)行政區長條圖',color='#006561',figsize=(6,5),rot=0,width=0.2)
i=range(4)
for a,b in zip(i,pd1_0['個數']):
    plt.text(a,b+0.1,'{}'.format(int(b)),color='#9D3232',fontsize=14)
med=float(pd1_0.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(-1,med+0.2,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#單一公共托老中心(含日照中心)應供人數
index1=list(pd1.index)
#pd1.insert(0,column='行政區',value=index1)
test=pd.merge(pd1,total1,left_index=True, right_index=True,how='inner')
test=test[['行政區','個數','老年人口數']]
test.insert(3,column='單一公共托老中心(含日照中心)應供人數',value=round(test['老年人口數']/test['個數'],2))
test.set_index(['行政區'],inplace=True)
cen1_g1t=test['單一公共托老中心(含日照中心)應供人數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']]
cen1_g2t=test['單一公共托老中心(含日照中心)應供人數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']]
cen1_g3t=test['單一公共托老中心(含日照中心)應供人數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']]
cen1_g4t=test['單一公共托老中心(含日照中心)應供人數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']]

#新北市公共托老中心(含日照中心)第一組棒棒糖圖
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
pd1_1=pd1['個數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']]
pd1_1=pd1_1.fillna(0)
(markers, stemlines, baseline) = plt.stem(pd1_1)
plt.setp(markers,markersize=10,color='purple')
r=range(len(pd1_1.index))
plt.setp(stemlines, linestyle="-", color="olive", linewidth=1)
plt.xticks(r,['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區'])
plt.ylim(0,5)
plt.title('g1公共托老中心(含日照中心)分佈棒棒糖圖')
i=range(6)
for a,b in zip(i,pd1_1):
    plt.text(a+0.2,b,'{}'.format(int(b)),color='#214765',fontsize=14)
med=float(pd1_1.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+0.5,'中位數：{}'.format(med),fontsize=14,color='r')
plt.subplot(1,2,2)
cen1_g1t['烏來區']=total1['老年人口數']['烏來區']
(markers, stemlines, baseline) = plt.stem(cen1_g1t)
plt.setp(markers,markersize=10,color='purple')
r=range(len(cen1_g1t.index))
plt.setp(stemlines, linestyle="-", color="olive", linewidth=1)
plt.xticks(r,['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區'])
plt.ylim(0,70000)
plt.title('g1公共托老中心(含日照中心)應供人數棒棒糖圖')
i=range(6)
for a,b in zip(i,cen1_g1t):
    plt.text(a+0.2,b,'{}'.format(int(b)),color='#214765',fontsize=14)
med=float(cen1_g1t.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+5000,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#新北市公共托老中心(含日照中心)第二組棒棒糖圖
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
pd1_2=pd1['個數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']]
pd1_2=pd1_2.fillna(0)
(markers, stemlines, baseline) = plt.stem(pd1_2)
plt.setp(markers,markersize=10,color='purple')
r=range(len(pd1_2.index))
plt.setp(stemlines, linestyle="-", color="olive", linewidth=1)
plt.xticks(r,['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區'])
plt.ylim(0,5)
plt.title('g2公共托老中心(含日照中心)分佈棒棒糖圖')
i=range(7)
for a,b in zip(i,pd1_2):
    plt.text(a+0.2,b,'{}'.format(b),color='#214765',fontsize=14)
med=float(pd1_2.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+1,'中位數：{}'.format(med),fontsize=14,color='r')
plt.subplot(1,2,2)
(markers, stemlines, baseline) = plt.stem(cen1_g2t)
plt.setp(markers,markersize=10,color='purple')
r=range(len(cen1_g2t.index))
plt.setp(stemlines, linestyle="-", color="olive", linewidth=1)
plt.xticks(r,['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區'])
plt.ylim(0,70000)
plt.title('g2公共托老中心(含日照中心)應供人數棒棒糖圖')
i=range(7)
for a,b in zip(i,cen1_g2t):
    plt.text(a,b+2000,'{}'.format(int(b)),color='#214765',fontsize=14)
med=float(cen1_g2t.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+5000,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#新北市公共托老中心(含日照中心)第三組棒棒糖圖
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
pd1_3=pd1['個數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']]
pd1_3=pd1_3.fillna(0)
(markers, stemlines, baseline) = plt.stem(pd1_3)
plt.setp(markers,markersize=10,color='purple')
r=range(len(pd1_3.index))
plt.setp(stemlines, linestyle="-", color="olive", linewidth=1)
plt.xticks(r,['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區'],rotation=45)
plt.ylim(0,5)
plt.title('g3公共托老中心(含日照中心)分佈棒棒糖圖')
i=range(10)
for a,b in zip(i,pd1_3):
    plt.text(a+0.2,b,'{}'.format(int(b)),color='#214765',fontsize=14)
med=float(pd1_3.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+0.5,'中位數：{}'.format(med),fontsize=14,color='r')
plt.subplot(1,2,2)
cen1_g3t=cen1_g3t.fillna(0)
(markers, stemlines, baseline) = plt.stem(cen1_g3t)
plt.setp(markers,markersize=10,color='purple')
r=range(len(cen1_g3t.index))
plt.setp(stemlines, linestyle="-", color="olive", linewidth=1)
plt.xticks(r,['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區'],rotation=45)
plt.ylim(0,70000)
plt.title('g3公共托老中心(含日照中心)應供人數棒棒糖圖')
i=range(10)
for a,b in zip(i,cen1_g3t):
    plt.text(a+0.2,b,'{}'.format(b),color='#214765',fontsize=14)
med=float(cen1_g3t.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+5000,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#新北市公共托老中心(含日照中心)第四組棒棒糖圖
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
pd1_4=pd1['個數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']]
pd1_4=pd1_4.fillna(0)
(markers, stemlines, baseline) = plt.stem(pd1_4)
plt.setp(markers,markersize=10,color='purple')
r=range(len(pd1_4.index))
plt.setp(stemlines, linestyle="-", color="olive", linewidth=1)
plt.xticks(r,['板橋區','中和區','三重區','新莊區','蘆洲區','永和區'])
plt.title('g4公共托老中心(含日照中心)分佈棒棒糖圖')
plt.ylim(0,5)
i=range(6)
for a,b in zip(i,pd1_4):
    plt.text(a+0.2,b,'{}'.format(b),color='#214765',fontsize=14)
med=float(pd1_4.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+0.5,'中位數：{}'.format(med),fontsize=14,color='r')
plt.subplot(1,2,2)
(markers, stemlines, baseline) = plt.stem(cen1_g4t)
plt.setp(markers,markersize=10,color='purple')
r=range(len(cen1_g4t.index))
plt.setp(stemlines, linestyle="-", color="olive", linewidth=1)
plt.xticks(r,['板橋區','中和區','三重區','新莊區','蘆洲區','永和區'])
plt.ylim(0,70000)
plt.title('g4公共托老中心(含日照中心)應供人數棒棒糖圖')
i=range(6)
for a,b in zip(i,cen1_g4t):
    plt.text(a+0.2,b,'{}'.format(b),color='#214765',fontsize=14)
med=float(cen1_g4t.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+7000,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#畫出新北市公共托老中心(含日照中心)分佈盒鬚圖
#離群值(outliers)適合鬚圖籬笆外的值，就是Q1-1.5IQR(內四分位距)及Q3+1.5IQR範圍外的值
pd1_01=pd.DataFrame({'g1':pd1_1,'g2':pd1_2,'g3':pd1_3,'g4':pd1_4})
pd1_01.boxplot(fontsize=14)
plt.title('新北市公共托老中心(含日照中心)分佈盒鬚圖',fontsize=20)
plt.show()




#新北市公共托老中心(含日照中心)運作模式
pd2=pd.DataFrame.from_dict(modeN,orient='index',columns=['個數'])
pd2.plot(kind='bar',title='新北市公共托老中心(含日照中心)模式',color='#F66F89',figsize=(6,5),width=0.2,rot=0)
i=range(3)
for a,b in zip(i,pd2['個數']):
    plt.text(a,b+0.1,'{}'.format(int(b)),fontsize=14,color='#2E256D')
plt.show()


length=len(data1['result']['records'])
district1=[] #樂活供餐點所在全部行政區
for i in range(length):
    e=data1['result']['records'][i]['area'] #取出行政區
    district1.append(e)

district1=Counter(district1)    #用Counter計算各個行政區的樂活供餐點個數
district1N=OrderedDict(district1)

del district1N['']  #刪除空白資料


#畫出新北市友善供餐點長條圖
pd3=pd.DataFrame.from_dict(district1N,orient='index',columns=['個數'])
meal_g1=pd3['個數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']].sum()
meal_g2=pd3['個數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']].sum()
meal_g3=pd3['個數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']].sum()
meal_g4=pd3['個數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']].sum()
pd3.plot(kind='bar',title='新北市友善供餐點長條圖',width=0.2,color='#4571D5',figsize=(10,6),rot=45)
med=float(pd3.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(6,med+10,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()
pd3_0=pd.DataFrame([meal_g1,meal_g2,meal_g3,meal_g4],columns=['個數'],index=['g1','g2','g3','g4'])
pd3_0.plot(kind='bar',title='新北市友善供餐點長條圖',width=0.2,color='#4571D5',figsize=(6,5),rot=0)
i=range(4)
for a,b in zip(i,pd3_0['個數']):
    plt.text(a,b+3,'{}'.format(int(b)),fontsize=14,color='r')
med=float(pd3_0.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0.5,med+2,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#新北市友善供餐點可供人數列表
index1=list(pd3.index)
test=pd.merge(pd3,total1,left_index=True, right_index=True,how='inner')
test=test[['行政區','個數','老年人口數']]
test.insert(3,column='單一友善供餐點應供人數',value=round(test['老年人口數']/test['個數'],2))
test.set_index(['行政區'],inplace=True)
meal1_g1t=test['單一友善供餐點應供人數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']]
meal1_g2t=test['單一友善供餐點應供人數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']]
meal1_g3t=test['單一友善供餐點應供人數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']]
meal1_g4t=test['單一友善供餐點應供人數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']]


#畫出g1新北市友善供餐點分佈棒棒糖圖
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
pd3_1=pd3['個數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']]
pd3_1=pd3_1.fillna(0)
r=range(len(pd3_1.index))
plt.hlines(y=r, xmin=0, xmax=pd3_1, color='skyblue')
plt.plot(pd3_1, r, "D")
plt.yticks(r,['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區'])
plt.xlim(0,180) #統一x軸範圍，以利比較
plt.title('g1新北市友善供餐點棒棒糖圖',fontsize=20)
i=range(6)
for a,b in zip(i,pd3_1):
    plt.text(b+4,a,'{}'.format(int(b)),fontsize=14,color='#9D3A32')
med=float(pd3_1.median())
plt.axvline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(med+20,0,'中位數：{}'.format(med),fontsize=14,color='r')
plt.subplot(1,2,2)
meal1_g1t['烏來區']=total1['老年人口數']['烏來區']
r=range(len(meal1_g1t.index))
plt.hlines(y=r, xmin=0, xmax=meal1_g1t, color='skyblue')
plt.plot(meal1_g1t, r, "D")
plt.yticks(r,['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區'])
plt.xlim(0,17000) #統一x軸範圍，以利比較
plt.title('g1友善供餐點應供人數棒棒糖圖',fontsize=20)
i=range(6)
for a,b in zip(i,meal1_g1t):
    plt.text(b+4,a,'{}'.format(b),fontsize=14,color='#9D3A32')
med=float(meal1_g1t.median())
plt.axvline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(med+20,0.5,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#畫出g2新北市友善供餐點分佈棒棒糖圖
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
pd3_2=pd3['個數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']]
pd3_2=pd3_2.fillna(0)
r=range(len(pd3_2.index))
plt.hlines(y=r, xmin=0, xmax=pd3_2, color='skyblue')
plt.plot(pd3_2, r, "D")
plt.yticks(r,['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區'])
plt.xlim(0,180) #統一x軸範圍，以利比較
plt.title('g2新北市友善供餐點棒棒糖圖',fontsize=20)
i=range(7)
for a,b in zip(i,pd3_2):
    plt.text(b+4,a,'{}'.format(int(b)),fontsize=14,color='#9D3A32')
med=float(pd3_2.median())
plt.axvline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(med+20,0,'中位數：{}'.format(med),fontsize=14,color='r')
plt.subplot(1,2,2)
meal1_g2t['金山區']=total1['老年人口數']['金山區']
r=range(len(meal1_g2t.index))
plt.hlines(y=r, xmin=0, xmax=meal1_g2t, color='skyblue')
plt.plot(meal1_g2t, r, "D")
plt.yticks(r,['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區'])
plt.xlim(0,17000) #統一x軸範圍，以利比較
plt.title('g2友善供餐點應供人數棒棒糖圖',fontsize=20)
i=range(7)
for a,b in zip(i,meal1_g2t):
    plt.text(b+4,a,'{}'.format(b),fontsize=14,color='#9D3A32')
med=float(meal1_g2t.median())
plt.axvline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(med+20,0.5,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#畫出g3新北市友善供餐點分佈棒棒糖圖
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
pd3_3=pd3['個數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']]
pd3_3=pd3_3.fillna(0) #遇到NAN補0
r=range(len(pd3_3.index))
plt.hlines(y=r, xmin=0, xmax=pd3_3, color='skyblue')
plt.plot(pd3_3, r, "D")
plt.yticks(r,['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區'])
plt.xlim(0,180) #統一x軸範圍，以利比較
plt.title('g3新北市友善供餐點棒棒糖圖',fontsize=20)
i=range(10)
for a,b in zip(i,pd3_3):
    plt.text(b+4,a,'{}'.format(int(b)),fontsize=14,color='#9D3A32')
med=float(pd3_3.median())
plt.axvline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(med+20,0,'中位數：{}'.format(med),fontsize=14,color='r')
plt.subplot(1,2,2)
meal1_g3t=meal1_g3t.fillna(0)
r=range(len(meal1_g3t.index))
plt.hlines(y=r, xmin=0, xmax=meal1_g3t, color='skyblue')
plt.plot(meal1_g3t, r, "D")
plt.yticks(r,['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區'])
plt.xlim(0,17000) #統一x軸範圍，以利比較
plt.title('g3友善供餐點應供人數棒棒糖圖',fontsize=20)
i=range(10)
for a,b in zip(i,meal1_g3t):
    plt.text(b+4,a,'{}'.format(b),fontsize=14,color='#9D3A32')
med=float(meal1_g3t.median())
plt.axvline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(med+20,0.5,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#畫出g4新北市友善供餐點分佈棒棒糖圖
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)
pd3_4=pd3['個數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']]

r=range(len(pd3_4.index))
plt.hlines(y=r, xmin=0, xmax=pd3_4, color='skyblue')
plt.plot(pd3_4, r, "D")
plt.yticks(r,['板橋區','中和區','三重區','新莊區','蘆洲區','永和區'])
plt.xlim(0,180) #統一x軸範圍，以利比較
plt.title('g4新北市友善供餐點棒棒糖圖',fontsize=20)
i=range(6)
for a,b in zip(i,pd3_4):
    plt.text(b+4,a,'{}'.format(b),fontsize=14,color='#9D3A32')
med=float(pd3_4.median())
plt.axvline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(med+20,0,'中位數：{}'.format(med),fontsize=14,color='r')
plt.subplot(1,2,2)
meal1_g4t=meal1_g4t.fillna(0)
r=range(len(meal1_g4t.index))
plt.hlines(y=r, xmin=0, xmax=meal1_g4t, color='skyblue')
plt.plot(meal1_g4t, r, "D")
plt.yticks(r,['板橋區','中和區','三重區','新莊區','蘆洲區','永和區'])
plt.xlim(0,17000) #統一x軸範圍，以利比較
plt.title('g4友善供餐點應供人數棒棒糖圖',fontsize=20)
i=range(6)
for a,b in zip(i,meal1_g4t):
    plt.text(b+1000,a,'{}'.format(b),fontsize=14,color='#9D3A32')
med=float(meal1_g4t.median())
plt.axvline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(med+20,0.5,'中位數：{}'.format(med),fontsize=14,color='r')
plt.show()

#畫出新北市友善供餐點盒鬚圖
#離群值(outliers)適合鬚圖籬笆外的值，就是Q1-1.5IQR(內四分位距)及Q3+1.5IQR範圍外的值
pd3_01=pd.DataFrame({'g1':pd3_1,'g2':pd3_2,'g3':pd3_3,'g4':pd3_4})
pd3_01.boxplot(fontsize=14)
plt.title('新北市友善供餐點盒鬚圖',fontsize=20)
plt.show()

#增加新北市銀髮俱樂部可供使用人數
index1=list(pd4.index)
test=pd.merge(pd4,total1,left_index=True, right_index=True,how='inner')
test=test[['行政區','個數','老年人口數']]
test.insert(3,column='單一銀髮俱樂部應供人數',value=round(test['老年人口數']/test['個數'],2))
test.set_index(['行政區'],inplace=True)

club_g1t=test['單一銀髮俱樂部應供人數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']]
club_g2t=test['單一銀髮俱樂部應供人數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']]
club_g3t=test['單一銀髮俱樂部應供人數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']]
club_g4t=test['單一銀髮俱樂部應供人數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']]

#畫出新北市銀髮俱樂部分配長條圖與應供使用人數長條圖
##g1
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)  #g1組
pd4_1=pd4['個數'][['平溪區','雙溪區','坪林區','貢寮區','石碇區','烏來區']]
plt.bar(pd4_1.index,height=pd4_1,width=0.2,label='個數',color='#E9959D')
plt.legend()
i=range(6)
for a,b in zip(i,pd4_1):
    plt.text(a+0.2,b-0.2,'{}'.format(b),color='b',fontsize=14)
med=float(pd4_1.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+10,'中位數：{}'.format(med),fontsize=14,color='r')
plt.ylim(0,60)
plt.title('g1新北市銀髮俱樂部分佈長條圖')
plt.subplot(1,2,2)
plt.bar(club_g1t.index,height=club_g1t,width=0.2,label='人數',color='lightgreen')
plt.legend()
i=range(6)
for a,b in zip(i,club_g1t):
    plt.text(a,b,'{}'.format(b),color='b',fontsize=14)
med=float(club_g1t.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+500,'中位數：{}'.format(med),fontsize=14,color='r')
plt.ylim(0,3100)
plt.title('g1新北市銀髮俱樂部應供使用人數長條圖')
plt.show()

##g2
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)  #左圖
pd4_2=pd4['個數'][['三芝區','石門區','三峽區','金山區','萬里區','八里區','瑞芳區']]
plt.bar(pd4_2.index,height=pd4_2,width=0.2,label='個數',color='#7BC17B')
i=range(7)
for a,b in zip(i,pd4_2):
    plt.text(a+0.2,b-0.2,'{}'.format(b),color='b',fontsize=14)
med=float(pd4_2.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+10,'中位數：{}'.format(med),fontsize=14,color='r')
plt.ylim(0,60)
plt.title('g2新北市銀髮俱樂部分佈長條圖')
plt.legend()
plt.subplot(1,2,2) #右圖
plt.bar(club_g2t.index,height=club_g2t,width=0.2,label='人數',color='lightgreen')
plt.legend()
i=range(7)
for a,b in zip(i,club_g2t):
    plt.text(a,b+100,'{}'.format(b),color='b',fontsize=14,rotation=30)
med=float(club_g2t.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+500,'中位數：{}'.format(med),fontsize=14,color='r')
plt.ylim(0,3100)
plt.title('g2新北市銀髮俱樂部應供使用人數長條圖')
plt.show()

##g3
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)  #左圖
pd4_3=pd4['個數'][['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區']]
plt.bar(pd4_3.index,height=pd4_3,width=0.2,label='個數',color='#E9959D')
plt.legend()
i=range(10)
for a,b in zip(i,pd4_3):
    plt.text(a+0.2,b-0.2,'{}'.format(b),color='b',fontsize=14)
med=float(pd4_3.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+10,'中位數：{}'.format(med),fontsize=14,color='r')
plt.xticks(['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區'],rotation=45)
plt.ylim(0,60)
plt.title('g3新北市銀髮俱樂部分佈長條圖')
plt.subplot(1,2,2) #右圖
plt.bar(club_g3t.index,height=club_g3t,width=0.2,label='人數',color='lightgreen')
plt.xticks(['淡水區','深坑區','汐止區','鶯歌區','新店區','五股區','林口區','泰山區','樹林區','土城區'],rotation=45)
plt.legend()
i=range(10)
for a,b in zip(i,club_g3t):
    plt.text(a,b,'{}'.format(b),color='b',fontsize=14)
med=round(float(club_g3t.median()),2)
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+500,'中位數：{}'.format(med),fontsize=14,color='r')
plt.ylim(0,3100)
plt.title('g3新北市銀髮俱樂部應供使用人數長條圖')
plt.show()

##g4
plt.figure(figsize=(10,7))
plt.subplot(1,2,1)  #left
pd4_4=pd4['個數'][['板橋區','中和區','三重區','新莊區','蘆洲區','永和區']]
plt.bar(pd4_4.index,height=pd4_4,width=0.2,label='個數',color='#7BC17B')
i=range(6)
for a,b in zip(i,pd4_4):
    plt.text(a+0.2,b-0.2,'{}'.format(b),color='b',fontsize=14)
plt.ylim(0,60)
med=float(pd4_4.median())
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+10,'中位數：{}'.format(med),fontsize=14,color='r')
plt.title('g4新北市銀髮俱樂部分佈長條圖')
plt.legend()
plt.subplot(1,2,2)
plt.bar(club_g4t.index,height=club_g4t,width=0.2,label='人數',color='lightgreen')
plt.legend()
i=range(6)
for a,b in zip(i,club_g4t):
    plt.text(a,b,'{}'.format(b),color='b',fontsize=14)
med=round(float(club_g4t.median()),2)
plt.axhline(med,color='r',linestyle='dashed',linewidth=2)
plt.text(0,med+500,'中位數：{}'.format(med),fontsize=14,color='r')
plt.ylim(0,3100)
plt.title('g4新北市銀髮俱樂部應供使用人數長條圖')
plt.show()
