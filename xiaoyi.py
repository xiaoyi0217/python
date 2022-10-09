# Liang Xiao Yi
# TP068653

# mainpage
def mainpage():
    print('Welcome to FRESHCO Sdn Bhd !!!')
    print("Please choose your login option")
    print('1.Admin\n2.New customer\n3.Registered customer')
    while True:
        option = input("Enter 1-3 to select your option:")
        if option == "1":
            admin_login()
            break
        elif option == "2":
            new_customer()
            break
        elif option == "3":
            registered_customer()
        else:
            print("error")


# admin login
def admin_login():
    print('Welcome!')
    username = input('enter admin username:')
    pw = input('enter password:')
    if username == 'xiaoyi' and pw == '0217':
        print('login successful')
        admin_page()
    else:
        print(' login unsuccessful')
        mainpage()


def admin_page():
    while True:
        print(
            'Please select your option\n1. Upload groceries detail\n2. View uploaded groceries\n3.Update/modify '
            'groceries info\n4. Delete groceries '
            'info\n5. Search specific groceries detail\n6. View all orders of customers\n7. Search order of '
            'specific customer')
        option = (input('choose 1 - 7:'))
        if option == '1':
            upload_groceries_detail()
            break
        elif option == '2':
            view_groceries()
            break
        elif option == '3':
            update_or_modify_groceries_info()
            break
        elif option == '4':
            delete()
            break
        elif option == '5':
            search_specific_groceries_detail()
            break
        elif option == '6':
            view_all_orders_of_customers()
            break
        elif option == '7':
            search_order_of_specific_customer()
            break


# Admin upload
def upload_groceries_detail():
    GD = []
    print('Upload groceries detail here')
    Medicine_name = input('Enter item name:')
    Expiry_date = input('Enter expiry date:')
    Price = input('Enter price:')
    Specification = input('Enter specification:')
    Groceries_detail = open('Groceries_detail.txt', 'a')
    GD.append(Medicine_name)
    GD.append(Expiry_date)
    GD.append(Price)
    GD.append(Specification)
    print(GD)
    for i in GD:
        Groceries_detail.write(i + ' ')
    Groceries_detail.write('\n')
    Groceries_detail.close()
    print('Upload groceries or return to admin page')
    upload_or_return = input('Enter Upload to continue, Back to return')
    if upload_or_return == 'Upload':
        upload_groceries_detail()
    elif upload_or_return == 'Back':
        admin_page()


# Admin view
def view_groceries():
    list = open('Groceries_detail.txt', 'r')
    view_g = list.read()
    print(view_g)
    ans = input('Enter [B] to back to admin page')
    if ans == 'B':
        admin_page()


# Admin modify
def update_or_modify_groceries_info():
    print('Update or modify your groceries info')
    count = 0
    detail = open('Groceries_detail.txt', 'r')
    view_g = detail.readlines()
    detail.close()
    while count < len(view_g):
        print(str(count + 1) + ') ' + view_g[count])
        count += 1
    print('Enter the item to modify and update?')
    NDetail = []
    count = 0
    detail = open('Groceries_detail.txt', 'r')
    view_g = detail.readlines()
    detail.close()
    TDetail = len(view_g)
    while count < TDetail:
        detail = open('Groceries_detail.txt', 'r')
        R = detail.readlines()
        NDetail.append(R[count].split())
        count += 1
    FDetail = []
    number_chosen = int(input(': '))
    Medicine_name = input('Enter item name:')
    Expiry_date = input('Enter expiry date:')
    Price = input('Enter price:')
    Specification = input('Enter specification:')
    FDetail.append(Medicine_name)
    FDetail.append(Expiry_date)
    FDetail.append(Price)
    FDetail.append(Specification)
    NDetail[number_chosen - 1] = FDetail
    print(NDetail)
    GD = open('Groceries_detail.txt', 'w')
    for i in NDetail:
        for y in i:
            GD.write(y + ' ')
        GD.write('\n')
    GD.close()
    print('Modify groceries or return to admin page')
    modify_or_return = int(input('Enter Modify to continue, Back to return'))
    if modify_or_return == 'Modify':
        update_or_modify_groceries_info()
    elif modify_or_return == 'Back':
        admin_page()


# Admin delete
def delete():
    NDetail = []
    count = 0
    detail = open('Groceries_detail.txt', 'r')
    view_g = detail.readlines()
    detail.close()
    TDetail = len(view_g)
    while count < TDetail:
        detail = open('Groceries_detail.txt', 'r')
        R = detail.readlines()
        NDetail.append(R[count].splitlines())
        count += 1
    count = 0
    detail = open('Groceries_detail.txt', 'r')
    view_g = detail.readlines()
    detail.close()
    while count < len(view_g):
        print(str(count + 1) + ') ' + view_g[count])
        count += 1
    Ask = int(input('Select the number to delete?'))
    del NDetail[Ask - 1]
    print(NDetail)
    detail = open('Groceries_detail.txt', 'w')
    for i in NDetail:
        for y in i:
            detail.write(y + ' ')
        detail.write('\n')
    delete_or_return = int(input('Enter Delete to continue, Back to return'))
    if delete_or_return == 'Delete':
        delete()
    elif delete_or_return == 'Back':
        admin_page()


# Admin search
def search_specific_groceries_detail():
    search = input('What do you want to search?')
    detail = open('Groceries_detail.txt', 'r')
    for data in detail:
        name = data.split()[0]
        if search == name:
            print('found')
            print(data.split())
            item = data.split()
            print('Name:' + item[0])
            print('Expiry date:' + item[1])
            print('Price:' + item[2])
            print('Specification:' + item[3])
            while True:
                ask = input('Enter S to continue search, Back to return')
                if ask == 'S':
                    search_specific_groceries_detail()
                elif ask == 'Back':
                    admin_page()


# Admin view customer orders
def view_all_orders_of_customers():
    file = open('Customer_order.txt', 'r')
    print(file.read())
    while True:
        ask = input('Press [B] to back to menu')
        if ask == 'B':
            admin_page()
        else:
            continue


# Admin search order
def search_order_of_specific_customer():
    search = input('Which customer you want to search?')
    order = open('Customer_order.txt', 'r')
    for data in order:
        if search == data.split(' ')[0]:
            print(data.split())
            item = data.split()
            print('Name:' + item[0])
            print('Order:' + item[1])
            while True:
                ask = input('Enter S to continue search, Back to return')
                if ask == 'S':
                    search_order_of_specific_customer()
                elif ask == 'Back':
                    admin_page()


# New customer
def new_customer():
    print('Hi new customer')
    print('1. View groceries detail\n2. Registration\n3.Exit')
    select = input('Please select your option:')
    if select == '1':
        detail = open('Groceries_detail.txt', 'r')
        view_g = detail.read()
        print(view_g)
        detail.close()
        while True:
            ask = input('Press [B] to return')
            if ask == 'B':
                new_customer()
            else:
                mainpage()
    if select == '2':
        L = []
        print('Welcome to new customer registration')
        name = input('Enter name:')
        address = input('Enter address:')
        email = input('Enter email:')
        contact = input('Enter contact number:')
        gender = input('Enter gender:')
        dob = input('Enter date of birth:')
        id = input('Enter user ID:')
        pw = input('Enter password:')
        pw2 = input('Rewrite password:')
        L.append(name)
        L.append(address)
        L.append(email)
        L.append(contact)
        L.append(gender)
        L.append(dob)
        L.append(id)
        L.append(pw)
        L.append(pw2)
        print(L)
        fetch = open('customer_detail.txt', 'a')
        for i in L:
            fetch.write(i + ' ')
        fetch.write('\n')
        fetch.close()
        customer_page()


# Registered customer
def registered_customer():
    new_list = []
    print('Welcome to customer login')
    id = input('Enter ur user ID:')
    pw = input('Enter your password:')
    verify = open('verify.txt', 'r')
    new_list.append(verify.read().split())
    if new_list[0][0] == id and new_list[0][1] == pw:
        print('login successful')
        customer_page()
    else:
        print('Invalid user ID or password')
        while True:
            ask = input('Enter [B] to return to menu')
            if ask == 'B':
                customer_page()
            else:
                registered_customer()


# Customer page
def customer_page():
    print('Welcome customer!')
    print("Please choose your option")
    print('1.View groceries detail\n2.Place order\n3.View order\n4.Personal Info\n5.Exit')
    option = (input('choose 1 - 5:'))
    if option == '1':
        view_groceries_detail()
    elif option == '2':
        place_order()
    elif option == '3':
        view_order()
    elif option == '4':
        personal_info()
    elif option == '5':
        mainpage()


# Customer view groceries
def view_groceries_detail():
    count = 0
    file = open('Groceries_detail.txt', 'r')
    view_g = file.readlines()
    file.close()
    while count < len(view_g):
        print(str(count + 1) + ') ' + view_g[count])
        count += 1
    while True:
        ask = input('Enter [B] to return\n:')
        if ask == 'B':
            customer_page()
        else:
            continue


# Customer place order
def place_order():
    count = 0
    list = open('Groceries_detail.txt', 'r')
    view_g = list.readlines()
    list.close()
    while count < len(view_g):
        print(str(count + 1) + ') ' + view_g[count])
        count += 1
    L = []
    count = 0
    list = open('Groceries_detail.txt', 'r')
    view_g = list.readlines()
    list.close()
    TList = len(view_g)
    while count < TList:
        file = open('Groceries_detail.txt', 'r')
        R = file.readlines()
        L.append(R[count].split())
        count += 1
    Ask = int(input('What do you want to order?: '))
    Order_list = [L[Ask - 1]]
    order = open('order.txt', 'w')
    for i in Order_list:
        for z in i:
            order.write(str(z) + ' ')
        order.write('\n')
    order.close()
    while True:
        Ask = (input('Do you want to order again? (yes/no)'))
        if Ask == 'yes':
            Ask = int(input('What do you want to order?: '))
            Order_list = [L[Ask - 1]]
            order = open('order.txt', 'a')
            for i in Order_list:
                for z in i:
                    order.write(str(z) + ' ')
                order.write('\n')
            order.close()

        elif Ask == 'no':
            make_payment()


# Customer view order
def view_order():
    list = open('order.txt', 'r')
    view_g = list.read()
    list.close()
    print(view_g)
    while True:
        ask = input('Enter [B] to return\n:')
        if ask == 'B':
            customer_page()
        else:
            continue


# Customer personal info
def personal_info():
    search = input('Enter your name')
    detail = open('customer_detail.txt', 'r')
    for data in detail:
        if search == data.split(' ')[0]:
            print(data.split())
    while True:
        ask = input('Enter [B] to return\n:')
        if ask == 'B':
            customer_page()
        else:
            continue


def make_payment():
    print('Payment Page')
    order_price = []
    file = open('order.txt', 'r')
    for i in file.readlines():
        order_price.append(i.strip().split()[2].replace('RM', ''))
    file.close()
    print(order_price)
    total_price = 0
    for i in order_price:
        total_price = total_price + int(i)
    while True:
        print('total you need to pay is RM ' + str(total_price))
        print('please enter amount you want to pay')
        while True:
            try:
                paying = int(input(':'))
                break
            except:
                print('only digit')
        balance = paying - total_price
        if balance < 0:
            print('not enough money!!!')
            continue
        else:
            print('payment success')
            print('here is your balance RM' + str(balance))
            file = open('order.txt', 'w')
            file.write('')
            file.close()
            break

mainpage()
