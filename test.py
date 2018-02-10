import itchat


itchat.auto_login()         #enableCmdQR=2
# itchat.run()
print("**********")
Friends = itchat.search_friends()
# print(Friends)
print("*********")


itchat.logout()