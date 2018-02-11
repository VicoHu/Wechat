import itchat


itchat.auto_login()         #enableCmdQR=2
# itchat.run()
print("**********")
Friends_ForName = itchat.search_friends()
print(Friends_ForName['NickName'])




itchat.logout()