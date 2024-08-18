'''
本加密器仅用于教学，无法用于商业。（密码强度太垃圾了）
'''
# 前期准备
import turtle
alphabet = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = alphabet[20:] + alphabet[:20]
# 好戏开始
choice = turtle.textinput("选择","选择操作：(ed)")
t = turtle.Pen()
if choice == 'e':
    word = turtle.textinput("输入：","原文：")
    secret = ""
    for i in word:
        if i in alphabet:
            ind = alphabet.index(i)
            secret += cipher[ind]
        else:
            secret += i
    t.write(secret,font=("宋体",40))
    t.hideturtle()
    turtle.done()
elif choice == 'd':
    yuanwen = ""
    password = turtle.textinput("输入","密文：")
    for i in password:
        if i in cipher:
            pw_ind = cipher.index(i)
            yuanwen += alphabet[pw_ind]
        else:
            yuanwen += i
    t.write(yuanwen,font=("宋体",40))
    t.hideturtle()
    turtle.done()
else:
    print("错误：无法识别操作")
