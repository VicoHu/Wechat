#Anthor:Blakcduty
#Data:2018/2/2 night
#coding:utf-8

import itchat
import matplotlib.pyplot as plt
import pandas as pd
import jieba
import re
import time
# import WordCloud
import numpy as np
import PIL.Image as Image

itchat.auto_login()         #enableCmdQR=2
time_start = time.time()    #time.time()为1970.1.1到当前时间的毫秒数
Friends = itchat.get_friends()

class FriendsInfo():
    '''
    This class can get your Wechat friends infomationm, 
    and write them to a file that your named and appointtd.
    Mothod:
    FriendsInfo(File Loaction, File Name,)
    '''
    def __init__(self, file_location, file_write_mothod, file_name, friends_list):
        self.file_location = file_location
        self.file_write_mothod= file_write_mothod
        self.file_name = file_name
        self.friends_list = friends_list
        self.friends_keys = []
        self.friends_values = []
        self.MyName = ""
        self.location = ""

    def reduction(self):
        count = 0
        friends_dic = []
        for media in self.friends_list:
            friends_dic.append(media)
            count = count + 1
        return friends_dic

    def friends_dic_keys(self,friends_dic):
        friends_dic_keys = []
        for madia in friends_dic:
            friends_dic_keys.append(madia.keys())
        return friends_dic_keys

    def friends_dic_values(self,friends_dic):
        friends_dic_values = []
        for madia in friends_dic:
            friends_dic_values.append(madia.values())
        return friends_dic_values
               
    def assign_mothod(self):
        friends_dic = self.reduction()
        self.friends_keys = self.friends_dic_keys(friends_dic)
        self.friends_values = self.friends_dic_values(friends_dic)
    
    def writer(self):
        Friends_ForName = itchat.search_friends()
        self.MyName = Friends_ForName['NickName']
        location = self.file_location + self.MyName + "_" + self.file_name
        self.location = location
        fp = open(location,self.file_write_mothod)
        count = 0
        for a in self.friends_keys[0]:
            if count == 0:
                count = count + 1
                continue                
            fp.write(a)
            fp.write(",")
        fp.write("\n")
        count = 0
        for a in self.friends_values[0]:
            if count == 0:
                count = count + 1
                continue
            a = str(a)
            fp.write(a)
            fp.write(",")
        fp.write("\n")
        count = 0
        for a in self.friends_keys[1]:
            if count == 0:
                count = count + 1
                continue
            if count == 1:
                count = count + 1
                continue
            a = str(a)
            fp.write(a)
            fp.write(",")
        fp.write("\n")
        
        count = 0
        for madia in self.friends_values:
            if count == 0:
                count = count + 1
                continue
            count = 0
            for a in madia:
                if count == 0:
                    count = count + 1
                    continue
                if count == 1:
                    count = count + 1
                    continue
                try:
                    a = str(a)
                    fp.write(a)     
                    fp.write(",")
                except UnicodeEncodeError:
                    fp.close()
                    fp = open(location,"at", encoding="utf-8")
                    a = str(a)
                    fp.write(a)
                    fp.write(",")
                    fp.close()
                    fp = open(location,"at")
            fp.write("\n")
        fp.close()

friends_info = FriendsInfo("E:\\ItchatData\\", "wt", "MyFriendsList.csv", Friends)
friends_info.assign_mothod()
friends_info.writer()
print("开始数据搜集及绘图进程：\n")
print("用户及好友基本信息输出为表格文件完成")
print(">>>已保存")
print("\n")

friends = Friends
NickName = friends[0].NickName
male = 0
female = 0
other = 0
# friends[0]是自己的信息，因此我们要从[1:]开始
for i in friends[1:]:
    sex = i['Sex']  # 注意大小写，2 是女性， 1 是男性
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
# 计算好友总数
total = len(friends[1:])
# print('好友总数：', total)
# print('男性比例：%2f%%' % (float(male) / total * 100))
# print('女性比例：%2f%%' % (float(female) / total * 100))
# print('未知性别：%2f%%' % (float(other) / total * 100))

# plt.rcParams['font.sans-serif']=['SimHei']    # 如果不设置这一句，中文不显示
# arr = ['1'] * male  # 男性
# arr1 = ['2']*female # 女性
# arr2 = ['0'] * other    #未知
# arr.extend(arr1)
# arr.extend(arr2)
# plt.hist(arr)
# plt.savefig('E:\\ItchatData\\' + friends_info.MyName + '_Sex_bar.png') #绘制性别条形统计图，并保存
# plt.show()
# print("绘制性别条形统计图完成，已保存")

plt.rcParams['font.sans-serif']=['SimHei']    # 如果不设置这一句，中文不显示
labels = ['男性', '女性', '未知']
sizes = []
sizes.append(float(male) / total * 100)
sizes.append(float(female) / total * 100)
sizes.append(float(other) / total * 100)
colors = ['yellowgreen', 'gold', 'lightskyblue']
explode = (0, 0, 0) 
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.4f%%', shadow=True, startangle=90) 
# Set aspect ratio to be equal so that pie is drawn as a circle.
# plt.axis('equal') 
plt.savefig('E:\\ItchatData\\' + friends_info.MyName + '_Sex_pie.png') ##绘制性别统计图，并保存
# plt.show()
plt.ion()
plt.pause(1)  #显示秒数
plt.close()
print("绘制好友性别饼图完成")
print(">>>已保存")
print("\n")

data = pd.DataFrame(friends)
df_friends = data
columns=['NickName', 'Sex', 'Province', 'City', 'Signature']
for col in columns:
    val = []
    for i in friends[1:]:
        val.append(i[col])
    data[col] = pd.Series(val)

plt.rcParams['font.sans-serif']=['SimHei']    # 如果不设置这一句，中文不显示
plt.bar(data['City'].value_counts().index,data['City'].value_counts())  # 选择柱状图，而不是直方图。
plt.xticks(rotation=90)     # 横坐标旋转90度
plt.savefig('E:\\ItchatData\\' + friends_info.MyName + 'City_bar.png') ##绘制城市分布情况条形统计图，并保存
# plt.show()
plt.ion()
plt.pause(1)  #显示秒数
plt.close()
print("绘制好友城市分布情况条形统计图完成")
print(">>>已保存")
print("\n")
# Signatures = df_friends.Signature
# regex1 = re.compile('<span.*?</span>') #匹配表情
# regex2 = re.compile('\s{2,}') #匹配两个以上占位符
# Signatures = [regex2.sub(' ',regex1.sub('',signature,re.S)) for signature in Signatures] #用一个空格替换表情和多个空格。
# Signatures = [signature for signature in Signatures if len(signature)>0] #去除空字符串
# text = ' '.join(Signatures)
# file_name = NickName +'_wechat_signatures.txt'
# with open(file_name,'w',encoding='utf-8') as f:
#     f.write(text)
#     f.close()
# wordlist = jieba.cut(text, cut_all=True)
# word_space_split = ' '.join(wordlist)
# coloring = np.array(Image.open('E:\\ItchatData\\' + friends_info.MyName + '_WordCloud.png')) #词云的背景和颜色。这张图片在本地。
# my_wordcloud = WordCloud(background_color="white", max_words=2000,mask=coloring, max_font_size=60, random_state=42, scale=2,font_path="C:\Windows\Fonts\msyhl.ttc").generate(word_space_split) #生成词云。font_path="C:\Windows\Fonts\msyhl.ttc"指定字体，有些字不能解析中文，这种情况下会出现乱码。
# my_wordcloud.to_file('E:\\ItchatData\\' + friends_info.MyName + '_WordCloud.png') #保存图片


time_end=time.time()
print("总共耗时：") 
print(time_end - time_start) 
print("秒")
itchat.logout()