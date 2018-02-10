import itchat


itchat.auto_login()         #enableCmdQR=2
# itchat.run()
print("**********")
Friends = itchat.get_friends()
print(Friends)
print("*********")


itchat.logout()