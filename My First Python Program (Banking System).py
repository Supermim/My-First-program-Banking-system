#MUHAMMAD SYAMIM SAIFUDDIN
#TP064414

#LOGIN SYSTEM(ADMIN)
def log_in_systema():
    while True:

        login1 = input("Username(CaseSensitive): ")
        user_file = open('ADMINUSERNAMEDATABASE.txt', "r")
        # print(type(login1))
        for number, line in enumerate(user_file):
            # print(login1)
            if login1 in line:
                line_number = number
                # print(login1)
                # print(type(login1))
                break
        user_file.close()

        login2 = str(input('Password(CaseSensitive): '))
        #pwlinestoread = [line_number]
        pw_file = open('ADMINPWDATABASE.txt','r')
        content = pw_file.readlines()

        if login2 in content[line_number]:
            print('________________________________________________________'
                  '\n '
                '\nWelcome back Admin ' + login1 + '!'
                '\n________________________________________________________'
                  '\n')
            break

        print('Incorrect username or password.')

#LOGIN SYSTEM(CUSTOMER)
def log_in_systemc():
    while True:

        line_number = 'error'
        login1 = input("Username(CaseSensitive): ")
        user_file = open('CUSTUSERNAMEDATABASE.txt', "r")
        # print(type(login1))
        for number, line in enumerate(user_file):
            # print(login1)
            if login1 in line:
                line_number = number
                # print(login1)
                # print(type(login1))
                break
        user_file.close()

        login2 = input('Password(CaseSensitive): ')
        #pwlinestoread = [line_number]
        pw_file = open('CUSTPWDATABASE.txt')
        sn_file = open('SERIALNUMBERDATABASE.txt')
        contentpw = pw_file.readlines()
        contentsn = sn_file.readlines()

        if login2 in contentpw[line_number]:
            print('________________________________________________________'
                  '\n '
                '\nWelcome ' + login1 + '!'
                '\n________________________________________________________'
                  '\nYour Serial Number/ID to make deposit/withdraw/check history is ' + contentsn[line_number])
            break

        print('Incorrect username or password.')

#ADMIN OPTION
def admin_search3():
    print('''PROFILE SEARCHER
________________________________________________________''')
    print('ENTER A SERIAL NUMBER')
    searchid = input()
    # READ INPUT AND SEARCH FILE
    f = open(searchid + ".txt", "r")
    print(f.read())
    return admin_page2()

def admin_creation3():
    print('''PROFILE CREATION
________________________________________________________''')
    custserialnumber = input('CREATE ID NUMBER(number only): ')
    custcreatename = input('ENTER FULL NAME: ')
    custcreateloginid = input('ENTER USERNAME: ')
    custcreatepw = input('ENTER A PASSWORD: ')
    print('''________________________________________________________
ACCOUNT SUCCESSFULLY CREATED
________________________________________________________''')

    # CREATE & WRITE INTO FILE
    f = open(custserialnumber + '.txt', "x")
    f.write('FULL NAME: ' + custcreatename +
            '\nUSERNAME: ' + custcreateloginid +
            '\nPASSWORD: ' + custcreatepw +
            '\n________________________________________________________________________'
            '\nDEPOSIT                         WITHDRAW                         BALANCE')
                        #^^^ 25 spaces(ATTENTION!!!!! INDEX32)
    f.close()

    #CREATE & WRITE SERIAL NUMBER INTO SERIAL NUMBER DATABASE
    f = open('SERIALNUMBERDATABASE.txt',"a")
    f.write('\n' + custserialnumber)
    f.close()

    #CREATE & WRITE INTO FILE(BALANCE SHEET)
    f =     open(custserialnumber + 'balance.txt', 'w')
    f.write('0')
    f.close()

    # CREATE & WRITE INTO FILE(USERNAME)
    f = open('CUSTUSERNAMEDATABASE.txt', 'a')
    f.write('\n' + custcreateloginid)
    f.close()

    # CREATE & WRITE INTO FILE(PASSWORD)
    f = open('CUSTPWDATABASE.txt', 'a')
    f.write('\n' + custcreatepw)
    f.close()

    return admin_page2()

#ADMIN MAIN PAGE
def admin_page2():

    print('''PRESS 1 TO CREATE NEW PROFILE
PRESS 2 TO SEARCH CUSTOMER'S PROFILE & TRANSACTION
PRESS 3 TO LOGOUT
PRESS 4 TO SHUTDOWN
________________________________________________________''')
    adminopt = input()
    if str(adminopt) == '1':
        admin_creation3()

    elif str(adminopt) == '2':
        admin_search3()

    elif str(adminopt) == '3':
        main_structure1()

#CUSTOMER OPTION
def customer_deposit3():
    print('ENTER YOUR ID NUMBER TO MAKE DEPOSIT')
    idcustomer = input()
    f = open(idcustomer + '.txt', 'a')
    print('PLEASE ENTER AMOUNT TO DEPOSIT')
    deposit = int(input())
    f.write('\n'  + str(deposit))
    f.close()

    #TO READ AND CONVERT STRING FROM BALANCE FILE TO INTEGER
    q = open(idcustomer + 'balance.txt', 'r')
    balance = q.readline()
    balance = int(balance)
    new_balance = balance + deposit
    new_balance = str(new_balance)

    #TO UPDATE BALANCE ON CUSTOMER'S BALANCE TEXT FILE
    ww = open(idcustomer + 'balance.txt', 'w')
    ww.write(new_balance)
    ww.close()

    #TO UPDATE BALANCE ON CUSTOMER'S TRANSACTION HISTORY
    d = open(idcustomer + '.txt', 'a')
    d.write('\n' + '                                                                 ' + new_balance)
    d.close()

    print('''________________________________________________________
DEPOSIT IS SUCCESSFUL
_____________________________________________________''')
    return customer_page2()

def customer_withdraw3():
    print('ENTER YOUR ID NUMBER TO MAKE WITHDRAWAL')
    idcustomer = str(input())
    f = open(idcustomer + '.txt', 'a')
    print('PLEASE ENTER AMOUNT TO WITHDRAW')
    withdraw = int(input())
    f.write('\n                                ' + str(withdraw))
    f.close()

    #TO READ AND CONVERT STRING FROM BALANCE FILE TO INTEGER
    q = open(idcustomer + 'balance.txt', 'r')
    balance = q.readline()
    balance = int(balance)
    new_balance = balance - withdraw
    new_balance = str(new_balance)

    #TO UPDATE BALANCE ON CUSTOMER'S BALANCE TEXT FILE
    ww = open(idcustomer + 'balance.txt', 'w')
    ww.write(new_balance)
    ww.close()
    
    #TO UPDATE BALANCE ON CUSTOMER'S TRANSACTION HISTORY
    d = open(idcustomer + '.txt', 'a')
    d.write('\n' + '                                                                 ' + new_balance)
    d.close()

    print('''________________________________________________________
WITHDRAW IS SUCCESSFUL''')
    return customer_page2()

def customer_history3():
    print('ENTER YOUR ID NUMBER FOR TRANSACTION HISTORY')
    idcustomer = str(input())
    f = open(idcustomer + '.txt', 'r')
    print(f.read())
    return customer_page2()

#CUSTOMER MAIN PAGE
def customer_page2():
    print('''PRESS 1 TO DEPOSIT
PRESS 2 TO WITHDRAW
PRESS 3 TO HISTORY
PRESS 4 TO LOGOUT
________________________________________________________''')
    customeropt = str(input())
    if str(customeropt) == '1':
        customer_deposit3()

    elif str(customeropt) == '2':
        customer_withdraw3()

    elif str(customeropt) == '3':
        customer_history3()

    elif str(customeropt) == '4':
        main_structure1()

#MAIN STRUCTURE(FUNCTION)
def main_structure1():
    print('''WELCOME TO ASIA PACIFIC UNIVERSITY ONLINE BANKING SYSTEM
________________________________________________________
    ''')

    print('''
PRESS 1 FOR ADMIN
PRESS 2 FOR CUSTOMER''')
    usertype = input()

    if usertype == '1':
        log_in_systema()
        admin_page2()

    elif usertype == '2':
        log_in_systemc()
        customer_page2()

#MAIN STRUCTURE(LAYER1)
print('''WELCOME TO ASIA PACIFIC UNIVERSITY ONLINE BANKING SYSTEM
________________________________________________________
''')

print('''
PRESS 1 FOR ADMIN
PRESS 2 FOR CUSTOMER''')
usertype = input()

if usertype == '1':

    log_in_systema()
    admin_page2()

elif usertype == '2':
    log_in_systemc()
    customer_page2()