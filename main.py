from Bank import  Bank
import  time
from datetime import datetime
from History import History
from prettytable import PrettyTable

list_user = []

def show_data_user(name,age,gender,ID,password,money=0):
    print('\n★--------------------------------------------★')
    print(f'Your Name : {name}')
    print(f'Your Age  : {age}')
    print(f'Your Gender : {gender}')
    print(f'Your ID : {ID}')
    print(f'Your Password : {password}')
    print(f'Your Balance : {money} EGP')
    print('\n★--------------------------------------------★')

def append_history(Type,money,date,id,current=0):
    try:
        myFile = open(f'data\\{id}.txt','a+')
        myFile.write(f'{Type}.{money}.{date}.{current}.\n')
        myFile.close()

    except Exception as e:
        print(type(e).__name__)
        myFile.close()

def get_history(id):
    try:
        myFile = open(f'data\\{id}.txt','a+')
        myHistry = []
        myFile.seek(0)
        for line in myFile.readlines():
            line = str(line).split('.')
            if len(line)==1:
                continue
            his = History(line[0],line[1],line[2],current=line[4])
            myHistry.append(his)
        return  myHistry

    except Exception as e:
        print(type(e).__name__)


#Function check that id found or not
def chec_id(ID):
    index = 0
    for user in list_user:
        if user.getID() == ID:
            return  index
        index+=1


    return index

# Function to get data from File
def get_data_user():
    try:
        myFile = open('User_data.txt','r+')
        for line in myFile.readlines() :
            line = line.split('.')
            myUser = Bank(line[0],line[1],line[2],line[3],line[4],line[5])
            list_user.append(myUser)


        myFile.close()
    except Exception as e :
        print(type(e).__name__)
        print("Opps Error In File")
        myFile.close()

def save_data_user():
    try:
        myFile = open('User_data.txt','w+')
        for user in list_user:
            myFile.write(f'{user.getName()}.{user.getAge()}.{user.getGender()}.{user.getID()}.{user.getPassword()}.{user.getBalance()}.\n')
    except Exception as e:
        print(type(e).__name__)

def bankSystem(user):

    print(f'\n\t\t\t\t\t\t★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★   Bank System Welcome You {user.getName().capitalize()}  ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\n')
    while True:
        print('\n-----------------------------------------------------------------------------------------------------------')
        print('1_ deposit \t\t 2_ withdraw \t\t 3_ transfer money to onther person \t\t 4_Show Balance \t\t 5_History \t\t 6_show my data \t\t 7_SIGN OUT ')
        print('-------------------------------------------------------------------------------------------------------------')
        while True:
            print("Enter Number Do You Want : ", end='')
            number = input()
            if (isIntger(number)):
                number = int(number)
                break
        if number == 1:
            print('★--------------------------------------------★')
            while True:
                print('Please Enter Value Of Money : ',end='')
                money = input()
                if isIntger(money):
                   mydate = str(datetime.now())
                   user.deposite(int(money))
                   append_history('deposit',money,mydate,user.getID(),current=user.getBalance())


                   break
            print('\n★--------------------------------------------★')
            print (f'✔ Process success your balance now is {user.getBalance()} EGP')
            print('★--------------------------------------------★')

        elif number== 2:
            print('★--------------------------------------------★')
            while True:
                print('Please Enter Value Of Money That you want to withdraw : ', end='')
                money = input()
                if isIntger(money):

                    if user.getBalance() < int(money):
                        print(f'#### Sorry you current Balance is {user.getBalance()} EGP can not make this process ####')

                    else:
                        mydate = str(datetime.now())
                        user.withDraw(int(money))
                        append_history('withdraw', money, mydate, user.getID(),current=user.getBalance())

                        print('\n★--------------------------------------------★')
                        print(f'✔ Process success your balance now is {user.getBalance()} EGP')
                        print('★--------------------------------------------★')

                    break

        elif number ==3:
            print('★--------------------------------------------★')

            while True:
                if user.getBalance() ==0:
                    print('#### Sorry you Balance Zero can not transfer Money ####')
                    break
                print('please Enter ID That You Want To Transfer Money : ',end='')
                success = False
                ID = input()
                if isIntger(ID):
                    index = chec_id(ID)
                    if index!= len(list_user):
                        while True:
                            print('please Enter ID That You Want To Transfer Money : ', end='')
                            money = input()
                            if isIntger(money):
                                if user.getBalance() < int(money):
                                    print(f'#### Sorry you current Balance is {user.getBalance()} EGP can not make this process ####')
                                else:
                                    mydate = str(datetime.now())
                                    user.withDraw(int(money))
                                    append_history('transfer', money, mydate, user.getID(),current=user.getBalance())

                                    list_user[index].deposite(int(money))
                                    success = True
                                    print('\n★--------------------------------------------★')
                                    print(f'✔ Process success your balance now is {user.getBalance()} EGP')
                                    print('★--------------------------------------------★')
                                    break
                    else:
                        print('#### Sorry not found this ID IN Bank System')
                    if success:
                        break







        elif number ==4 :
            print('\n★--------------------------------------------★')
            print(f'✔ Your Current Balance is {user.getBalance()} EGP')
            print('★--------------------------------------------★')
        elif number == 5:

            myHistory = get_history(user.getID())

            table = PrettyTable()
            table.field_names = ['      Process     ', '     Money       ', '     Current       ', '      date        ']
            for history in myHistory:
               table.add_row([history.type, f'{history.money} EGP',history.current, history.date])
            table.title='History Of your process'
            print(table)


        elif number == 6:
            show_data_user(user.getName(),user.getAge(),user.getGender(),user.getID(),user.getPassword(),user.getBalance())
        elif number ==7:
            break





# Function to sign in
def signIn():
    print('\n\t\t\t\t\t\t★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★   SIGN IN   ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\n')
    while True:
        print('please Enter ID : ', end='')
        ID = input()
        print('please Enter Password : ', end='')
        password = input()
        for user in list_user:
            if(user.getPassword() == password and user.getID() == ID):
                bankSystem(user)
                return 0

        print('✖ Not Found This User Please check your ID or Password  ✖')
        break


# Function check That value is integer or not
def isIntger(value,false = 0):
    try:
        x = int(value)
        if(x<=0):
            print('✖✖✖✖ please Enter valid Number ✖✖✖✖')
            return False
        return True
    except:
        if not false:
            print('✖✖✖✖ please Enter valid Number ✖✖✖✖')
            return False

# Function To Create New User
def creatAccount():
    print('\n\t\t\t\t\t\t★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★  Create An Account   ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\n')
    while True:
        print('Please Enter Your Name : ', end='')
        name = input()
        if not isIntger(name,false=1):
            break
        else:
            print('✖✖✖✖ please Enter valid name ✖✖✖✖')
    while True:
        print('please Enter Your Age : ',end='')
        age = input()
        if(isIntger(age)):
            age = int(age)
            break
    while True:
        list = ['M','F','MALE','FEMALE']
        print('please Enter Your Gender (M\F) : ', end='')
        gender = input()
        if(gender.upper() in list ):
            break
        else:
            print('✖✖✖✖ please Enter valid gender (M/F) ✖✖✖✖')
    while True:
        print('please Enter ID That contain  6 number form (0 to 9) : ',end = '')
        ID = input()
        if isIntger(ID):
            if( not len(ID)==6):
                print('✖✖✖✖ In Valid 6 number only ✖✖✖✖')
            else:
                break
    while True:
        print('please Enter Your password : ',end ='')
        password = input()
        if isIntger(password):
            break
    table = PrettyTable()
    table.title='Your Data'
    table.field_names = ['  Name  ','  Age  ','  Gender  ','  ID  ','  Password  ']
    table.add_row([name,age,gender,ID,password])
    print(table)

    #show_data_user(name,age,gender,ID,password)


    user = Bank(name,age,gender,ID,password,money=0)
    list_user.append(user)


    print('Please Waiting ' ,end= '')
    for i in range(1,10):
        print('☺'*i,end='')
        time.sleep(0.5)

    print('\n ✅ Account Created Successfully! ')






# 2021-11-26 11:43:06

print('\n\n\t\t\t\t\t\t★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★  WELCOME TO BANK SYSTEM   ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★\n\n')

get_data_user()

while True:
    print('\n★---------------------------------------------------★')
    print ('1_ Sign IN \t\t 2_ Create Account \t\t 3_ Exit')
    print('★---------------------------------------------------★')
    number = 0

    while True:
        print("Enter Number Do You Want : ", end='')
        number = input()
        if(isIntger(number)):
            number = int(number)
            break


    if number == 1:
       signIn()

    elif number == 2:
        creatAccount()

    elif number == 3:
        save_data_user()
        break

    else:
        print('#### sorry please enter number from (1 to 3) ####')


