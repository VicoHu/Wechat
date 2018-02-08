#Anthor:Blakcduty
#Data:2018/2/2 night


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
fp = open(r"E:\MyFriendsList.csv","wt")
A1 = Friends[0].keys()
A2 = Friends[0].values()
B1 = Friends[1].keys()
B2 = Friends[1].values()
N = 0
for a in list(A1):
    if N == 0:
        N = N + 1
        continue
    fp.write(a)
    fp.write(",")
fp.write("\n")
N = 0
for a in list(A2):
    if N == 0:
        N = N + 1
        continue
    fp.write(a)                    #write() argument must be str, not int
    fp.write(",")
fp.write("\n")
N = 0
for a in list(B1):
    if N == 0:
        N = N + 1
        continue
    fp.write(a)
    fp.write(",")
fp.write("\n")
N = 0
for a in list(B2):
    if N == 0:
        N = N + 1
        continue
    fp.write(a)
    fp.write(",")
fp.write("\n")
fp.close()





itchat.logout()