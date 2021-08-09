# 1.代码实现


getNum = int(input("1.登入\n2.注册\nPlease Input the Choose :"))
while getNum<1 or getNum>2:
    getNum =int(input("无效值 :"))
    username = input("用户名: ")
    password = input("密码: ")
    if getNum == 1:#登入
        ErrNums = 0
    while ErrNums<3:
        T = False