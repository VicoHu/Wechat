#Anthor:Blakcduty
#Data:2018/2/2 night
#coding:utf-8

import itchat

# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     print(msg['Text'])

itchat.auto_login()         #enableCmdQR=2
# itchat.run()
print("**********")
Friends = itchat.get_friends()
# print(Friends)
print("*********")

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
            # if count == 1:
            #     count = count + 1
            #     continue
            friends_dic_keys.append(madia.keys())
        # friends_dic_keys = [ str(i) for i in friends_dic_keys]         #
        return friends_dic_keys

    def friends_dic_values(self,friends_dic):
        friends_dic_values = []
        for madia in friends_dic:
            # if count == 1:
            #     count = count + 1
            #     continue
            friends_dic_values.append(madia.values())
        # friends_dic_values = [ str(i) for i in friends_dic_values ]     #
        return friends_dic_values
            
    
    def assign_mothod(self):
        friends_dic = self.reduction()
        self.friends_keys = self.friends_dic_keys(friends_dic)
        self.friends_values = self.friends_dic_values(friends_dic)
    
    def writer(self):
        Friends_ForName = itchat.search_friends()
        self.MyName = Friends_ForName['NickName']
        location = self.file_location + self.MyName + "_" + self.file_name
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
                    fp.write(a)     #UnicodeEncodeError: 'gbk' codec can't encode character '\U0001f4a1' in position 105: illegal multibyte sequen
                    fp.write(",")
                except UnicodeError:
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



# fp = open(r"E:\MyFriendsList.csv","wt")
# A1 = Friends[0].keys()
# A2 = Friends[0].values()
# B1 = Friends[1].keys()
# B2 = Friends[1].values()
# A1 = [ str(i) for i in A1 ]
# A2 = [ str(i) for i in A2 ]
# B1 = [ str(i) for i in B1 ]
# B2 = [ str(i) for i in B2 ]
# N = 0
# for a in list(A1):
#     if N == 0:
#         N = N + 1
#         continue
#     fp.write(a)
#     fp.write(",")
# fp.write("\n")
# N = 0
# for a in list(A2):
#     if N == 0:
#         N = N + 1
#         continue
#     fp.write(a)                    
#     fp.write(",")
# fp.write("\n")
# N = 0
# for a in list(B1):
#     if N == 0:
#         N = N + 1
#         continue
#     fp.write(a)
#     fp.write(",")
# fp.write("\n")
# N = 0
# for a in list(B2):
#     if N == 0:
#         N = N + 1
#         continue
#     fp.write(a)
#     fp.write(",")
# fp.write("\n")
# fp.close()

itchat.logout()