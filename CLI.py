import mysql.connector
import random

cnx = mysql.connector.connect(user = 'root', password = 'root', host = '127.0.0.1', database = 'retadn2',autocommit=True)
cursor = cnx.cursor()

orderid=0
shippers = [12345, 23456, 34567, 45678]

menu = {
    1: "View Products",
    2: "Customer Login",
    3: "Admin Login",
    4: "Employee Login",
    5: "New Customer Signup",
    6: "Exit"
}

def customer_sign_up():
    try:
        custName = input("Enter your name: ")
        custEmail = input("Enter your email ID: ")
        custPwd = input("Enter a password: ")
        custPhone = input("Enter your phone number: ")
        custAdd = input("Enter your address: ")
        custBillAdd = input("Enter your billing address: ")
        custWallet = int(input("Enter amount to be credited to your wallet: "))
        query = "SELECT * FROM customer ORDER BY cust_id DESC LIMIT 1;"
        cursor.execute(query)
        results = cursor.fetchall()
        newCustID = list({results[0][0]+1})[0]
        query2 = "INSERT INTO `customer` (`cust_id`, `cust_name`, `cust_email`, `cust_phone`, `cust_add`, `cust_billadd`, `cust_pwd`, `cust_wallet`) VALUES ("+str(newCustID)+", '"+str(custName)+"', '"+str(custEmail)+"', "+str(custPhone)+", '"+str(custAdd)+"', '"+str(custBillAdd)+"', '"+str(custPwd)+"', "+str(custWallet)+");"
        cursor.execute(query2)
        print("Signed up successfully!")
    except:
        print("Datatype mismatch, please try again!")
        customer_sign_up()

def update_inventory(a):
    cursor.execute("""SELECT * FROM inventory;""")
    results = cursor.fetchall()
    print("prod_id\tQuantity")
    for row in results:
        print(f"{row[0]}\t{row[1]}")
    prod_id=int(input("Enter the Product ID to be updated"))
    nqty=int(input("Enter the updated QTY"))
    query="UPDATE inventory SET qty="+str(nqty)+" WHERE prod_id="+str(prod_id)+";"
    cursor.execute(query)
    cursor.execute("""SELECT * FROM inventory;""")
    print("prod_id\tQuantity")
    results = cursor.fetchall()
    for row in results:
        print(f"{row[0]}\t{row[1]}")
    if(a==0):
        admin_menu()
    else:
        employee_menu()

def update_price(a):
    cursor.execute("""SELECT * FROM products;""")
    results = cursor.fetchall()
    print("Product ID\tCategory ID\tProduct Name\tProduct Descs\tProduct Cost")
    for row in results:
        print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t{row[4]}")
    prod_id=int(input("Enter the product ID for discount"))
    dis=int(input("Enter the discount percentage to be given"))
    products="SELECT * FROM products where products.prod_id="+str(prod_id)+";"
    cursor.execute(products)
    results = cursor.fetchall()
    fin=0
    for row in results: 
        fin=float(list({row[4]})[0])-(float(list({row[4]})[0])*dis/100)
        print(float(list({row[4]})[0]))
    query="UPDATE products SET prod_cost="+str(fin)+" WHERE prod_id="+str(prod_id)+";"
    cursor.execute(query)
    cursor.execute("""SELECT * FROM products;""")
    results = cursor.fetchall()
    print("Product ID\tCategory ID\tProduct Name\tProduct Name\tProduct Cost")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
    if(a==0):
        admin_menu()
    else:
        employee_menu()

    
def add_coupon():
    cp_id=int(input("Enter Coupon ID"))
    disc=float(input("Enter Discount Percent"))
    cp_desc=input("Enter the coupon description")
    cp="INSERT INTO `coupons` (`coupon_id`, `coupon_val`, `coupon_desc`) VALUES ("+str(cp_id)+", "+str(disc)+", "+"'"+cp_desc+"'"+");"
    cursor.execute(cp)
    cursor.execute("""SELECT * FROM coupons;""")
    results = cursor.fetchall()
    print("Coupon ID\tCoupon Value\tCoupon Description")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
    admin_menu()
        
def remove_coupon():
    cp_id=int(input("Enter Coupon ID"))
    cp="DELETE FROM coupons WHERE coupon_id="+str(cp_id)+";"
    cursor.execute(cp)
    cursor.execute("""SELECT * FROM coupons;""")
    results = cursor.fetchall()
    print("Coupon ID\tCoupon Value\tCoupon Description")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
    admin_menu()
    
def add_employee():
    emp_id=int(input("Enter Employee ID"))
    emp_name=(input("Enter Employee Name"))
    emp_login=int(input("Enter Employee Login"))
    emp_pwd=input("Enter the Employee Password")
    emp_desc=input("Enter the Employee description")
    emp="INSERT INTO `employee` (`emp_id`, `emp_name`, `emp_login`, `emp_pwd`, `emp_desc`) VALUES "+"("+str(emp_id)+", '"+str(emp_name)+"', "+str(emp_login)+", '"+str(emp_pwd)+"', '"+str(emp_desc)+"');"
    cursor.execute(emp)
    admin_menu()
    
def remove_employee():
    cp_id=int(input("Enter Employee ID to be removed"))
    cp="DELETE FROM employee WHERE emp_id="+str(cp_id)+";"
    cursor.execute(cp)
    admin_menu()
    
def add_product(a):
    prod_id=int(input("Enter Product ID"))
    cat_id=int(input("Enter Category ID"))
    prod_name=(input("Enter Product Name"))
    prod_desc=input("Enter the Product description")
    prod_cost=float(input("Enter the Product Price"))
    prod="INSERT INTO `products` (`prod_id`, `cat_id`, `prod_name`, `prod_desc`, `prod_cost`) VALUES ("+str(prod_id)+", "+str(cat_id)+", '"+prod_name+"', '"+prod_desc+"', '"+str(prod_cost)+"');"
    prod2="INSERT INTO `inventory` (`prod_id`, `qty`) VALUES ("+str(prod_id)+",1);"
    cursor.execute(prod)
    cursor.execute(prod2)
    if(a==0):
        admin_menu()
    else:
        employee_menu()


def remove_product(a):
    cp_id=int(input("Enter Product ID to be removed"))
    cp2="DELETE FROM inventory WHERE prod_id="+str(cp_id)+";"
    cp="DELETE FROM products WHERE prod_id="+str(cp_id)+";"
    cursor.execute(cp2)
    cursor.execute(cp)
    if(a==0):
        admin_menu()
    else:
        employee_menu()

def edit_wallet(a):
    custID = int(input("Enter customer's ID: "))
    newBal = int(input("Enter Wallet Balance: "))
    query = "UPDATE customer SET cust_wallet = "+str(newBal)+" WHERE cust_id = "+str(custID)+";"
    cursor.execute(query)
    query2 = "SELECT customer.cust_id, customer.cust_wallet FROM customer WHERE cust_id = "+str(custID)+";"
    cursor.execute(query)
    print("New Balance: "+str(newBal))
    admin_menu()
    

def admin_menu():
    menu = {
    1: "Update Inventory",
    2: "Add Discounts",
    3: "Add Coupons",
    4: "Remove Coupons",
    5: "Add Product to display",
    6: "Remove Product from display",
    7: "Add Employees",
    8: "Remove Employee",
    9: "View Shipper Details",
    10: "Edit Wallet",
    11: "Exit"
    }
    for key, value in menu.items():
        print(f"{key}. {value}")
    choice=input("Enter the admin Option you would like to perform")
    if choice == "1":
        update_inventory(0)
    elif choice == "2":
        update_price(0)
    elif choice == "3":
        add_coupon()
    elif choice == "4":
        remove_coupon()
    elif choice == "5":
        add_product(0)
    elif choice == "6":
        remove_product(0)
    elif choice == "7":
        add_employee()
    elif choice == "8":
        remove_employee()
    elif choice == "9":
        view_shipper()
        admin_menu()
    elif choice == "10":
        edit_wallet(0)

def admin_login():
    login=int(input("Enter admin Login Number"))
    pwd=input("Enter Admin Password")
    cursor.execute("""SELECT * FROM admina;""")
    valid=0
    results = cursor.fetchall()
#    print(results)
    for row in results:
        if((login)==list({row[1]})[0]):
            if(pwd==list({row[2]})[0]):
                valid=1
    if(valid==0):
        print("Wrong Details")
        admin_login()
    else:
        print("Welcome Mr. Stark")
        admin_menu()
        
def employee_menu():
    menu = {
    1: "Update Inventory",
    2: "Add Discounts",
    3: "Add Product to display",
    4: "Remove Product from display",
    5: "Exit"
    }
    for key, value in menu.items():
        print(f"{key}. {value}")
    choice=input("Enter the admin Option you would like to perform")
    if choice == "1":
        update_inventory(1)
    elif choice == "2":
        update_price(1)
    elif choice == "3":
        add_product(1)
    elif choice == "4":
        remove_product(1)


def employee_login():
    login=int(input("Enter Employee Login Number"))
    pwd=input("Enter Employee Password")
    cursor.execute("""SELECT * FROM employee;""")
    valid=0
    results = cursor.fetchall()
    for row in results:
        if((login)==list({row[2]})[0]):
            if(pwd==list({row[3]})[0]):
                valid=1
    if(valid==0):
        print("Wrong Details")
        re=int(input("Enter 1 to retry or 0 to exit"))
        if(re==1):
            employee_login()
    else:
        print("Welcome Mr. Stark")
        employee_menu()

def add_to_cart(cust_id):
    cat_id = 0
    cursor.execute("""SELECT * FROM category;""")
    results = cursor.fetchall()
    print("Category ID\tCategory Name\tCategory Description")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
    while(cat_id != -1):
        print("Select a category: ")
        cat_id=int(input("Enter cat_id (-1 to add to cart): "))
        products="SELECT * FROM products WHERE products.cat_id="+str(cat_id)+";"
        cursor.execute(products)
        results = cursor.fetchall()
        print("Product ID\tCategory ID\tProduct Name\tProduct Name\tProduct Cost")
        for row in results:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
    prod_id=input("Enter prod_id of product that you want to add to cart")
    qty=int(input("Enter Quantity of Product"))
    cursor.execute("SELECT * FROM inventory;")
    results = cursor.fetchall()
    for row in results:
        if(int(list({row[0]})[0]) == int(prod_id)):
            if(int(list({row[1]})[0]) < qty):
                print(f"Only {int(list({row[1]})[0])} left in stock! Try again")
                add_to_cart(cust_id)
    cursor.execute("SELECT * FROM CartItems;")
    results = cursor.fetchall()
    upd=0
    for row in results:
        if(str(cust_id)==str(list({row[1]})[0]) and prod_id==str(list({row[2]})[0])):
            preqty=int(list({row[3]})[0])
            qty=qty+preqty
            inv_qty="SELECT * FROM inventory WHERE prod_id="+str(prod_id)+";"
            cursor.execute(inv_qty)
            results2=cursor.fetchall()
            invqt=0
            for row2 in results2:
                invqt=int(list({row2[1]})[0])
                
            if(invqt<qty):
                print(f"Only {int(list({row2[1]})[0])} left in stock! Try again")
                add_to_cart(cust_id)
            else:    
                upd="UPDATE CartItems SET quantity="+str(qty)+" WHERE cart_index="+str(cust_id)+" AND prod_id="+str(prod_id)+";"
                cursor.execute(upd)
                upd=1
                break
    if(upd==0):
        ins="INSERT INTO `CartItems` (`cart_index`, `prod_id`, `quantity`) VALUES ("+str(cust_id)+", "+str(prod_id)+", "+str(qty)+");"
        cursor.execute(ins)
    check = input("Add more products?(Y/N): ")
    if(check == "Y" or check == "y"):
        add_to_cart(cust_id)
    else:
        cursor.execute("SELECT * FROM CartItems WHERE CartItems.cart_index = "+str(cust_id)+";")
        results = cursor.fetchall()
        print("Cart Item ID\tCustomer ID\tProduct ID\tQuantity")
        for row in results:
            print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
        cust_menu(cust_id)
 
 
def browse_products():
    cat_id = 0
    cursor.execute("""SELECT * FROM category;""")
    results = cursor.fetchall()
    print("Category ID\tCategory Name\tCategory Description")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
    while(cat_id != -1):
        print("Select a category: ")
        cat_id=int(input("Enter cat_id (-1 to go back): "))
        products="SELECT * FROM products where products.cat_id="+str(cat_id)+";"
        cursor.execute(products)
        results = cursor.fetchall()
        print("Product ID\tCategory ID\tProduct Name\tProduct Name\tProduct Cost")
        for row in results:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
    

#    if(cat_id == -1):
#        cust_menu(cust_email, local_idx)


def customer_login():
    print("Login")
    cust_id = input("Enter your Customer ID: ")
    cust_pwd = input("Enter your password: ")
    cursor.execute("""SELECT * FROM customer;""")
    valid=0
    results = cursor.fetchall()
#   print(results)
    for row in results:
        if(str(cust_id)==str(list({row[0]})[0])):
            print("Matched 1")
            if(str(cust_pwd)==str(list({row[6]})[0])):
                valid=1
    if(valid==0):
        print("Wrong Details")
        customer_login()
    else:
        print("Welcome!")
        cust_menu(cust_id)

def remove_from_cart(cust_id):
    cursor.execute("SELECT * FROM CartItems WHERE CartItems.cart_index = "+str(cust_id)+";")
    results = cursor.fetchall()
    print("Cart Item ID\tCustomer ID\tProduct ID\tQuantity")
    for row in results:
        print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
    prod_id=input("Enter prod_id of product that you want to remove from cart")
    qty=int(input("Enter Quantity of Product to be removed"))
    cursor.execute("SELECT * FROM CartItems")
    results = cursor.fetchall()
    preqty=0
    for row in results:
        print("Checking")
        if(str(cust_id)==str(list({row[1]})[0]) and prod_id==str(list({row[2]})[0])):
            preqty=int(list({row[3]})[0])
            if(preqty<qty):
                print("Invalid Quantity")
            else:
                preqty=preqty-qty
                upd="UPDATE CartItems SET quantity="+str(preqty)+" WHERE cart_index="+str(cust_id)+" and prod_id="+str(prod_id)+";"
                cursor.execute(upd)
                print("Executed")
                break


def apply_coupon(cust_id):
    cursor.execute("""SELECT * FROM coupons;""")
    results = cursor.fetchall()
    print("Coupon ID\tDiscount Percent\tCoupon Description")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")
    cpid=int(input("Enter the coupon to be applied"))
    cursor.execute("""SELECT * FROM coupons;""")
    results = cursor.fetchall()
    discper=0
    for row in results:
        if(str(cpid)==str(list({row[0]})[0])):
            discper=int(list({row[1]})[0])
            break
    cursor.execute("""SELECT * FROM cart;""")
    results = cursor.fetchall()
    finval=0
    for row in results:
        if(str(cust_id)==str(list({row[0]})[0])):
            finval=int(list({row[2]})[0])
            break
    finval=finval-(finval*discper/100)
    upd="UPDATE Cart SET fin_val="+str(finval)+"WHERE cart_index="+str(cust_id)+";"
    cursor.execute(upd)


def place_order(cust_id):
        global orderid
        print("Here rn")
        quer="SELECT * FROM CartItems WHERE CartItems.cart_index="+str(cust_id)+";"
        quer2="SELECT * FROM cart WHERE cart.cust_id="+str(cust_id)+";"
        quer3="SELECT * FROM customer WHERE customer.cust_id="+str(cust_id)+";"
        cursor.execute(quer3)
        results = cursor.fetchall()
        flag = 0
        custAddress = "a"
        for row in results:
            custAddress=str(list({row[4]})[0])
        yesno=input("Continue ?(Y/n)")
        if(yesno=="Y" or yesno=="y"):
            cursor.execute(quer3)
            results=cursor.fetchall()
            for row in results:
                walletBal = list({row[7]})[0]
            cursor.execute(quer2)
            results=cursor.fetchall()
            for row in results:
                if(walletBal>=list({row[2]})[0]):
                    ord_ins="INSERT INTO `ordera` (`cart_index`, `order_time`, `fin_val`, `shipping_address`) VALUES ("+str(cust_id)+", now(), '"+str(list({row[2]})[0])+"', 'Molestiae quia laudantium fuga.');"
                    orderid+=1
                    cursor.execute(ord_ins)
                    print("Ordera table updated")
                    newBal = walletBal-list({row[2]})[0]
                    update_wallet = "UPDATE customer SET cust_wallet ="+str(newBal)+" WHERE customer.cust_id = "+str(cust_id)+";"
                    cusor.execute(update_wallet)
                    print("Your new wallet balance is: ", newBal)
                else:
                    print("Insufficient wallet balance!")
                    cust_menu(cust_id)
            print("Reached Here")
            cursor.execute(quer)
            print("Reached here 2")
            results=cursor.fetchall()    
            for row in results:
                ins="INSERT INTO `order_items` (`order_id`,`cart_index`, `prod_id`, `quantity`) VALUES ("+str(orderid)+", "+str(cust_id)+", "+str(list({row[2]})[0])+", "+str(list({row[3]})[0])+");"
                cursor.execute(ins)
                shipment_update="INSERT INTO `shipper` (`shipper_id`, `order_id`, `order_time`, `del_date`, `shipping_address`) VALUES ("+str(random.choice(shippers))+", "+str(orderid)+", now(), now()+1, '"+str(custAddress)+"');"
                cursor.execute(shipment_update)
            finv="UPDATE cart SET fin_val=0 WHERE cust_id="+str(cust_id)+";"
            cursor.execute(finv)
            clr="DELETE FROM CartItems WHERE CartItems.cart_index="+str(cust_id)+";"
            cursor.execute(clr)
            print("Order Placed Successfully!")


def cust_menu(cust_id):
    menu = {
        1: "Browse Products",
        2: "Add products to cart",
        3: "Remove products from cart",
        4: "Apply coupons",
        5: "View previous orders",
        6: "Checkout",
        7: "Logout",
    }
    for key, value in menu.items():
        print(f"{key}. {value}")
    choice = input("Enter your choice: ")
    if choice == "1":
        browse_products()
        cust_menu(cust_id)
    elif choice == "2":
        add_to_cart(cust_id)
    elif choice == "3":
        remove_from_cart(cust_id)
        cust_menu(cust_id)
    elif choice == "4":
        apply_coupon(cust_id)
        cust_menu(cust_id)
    elif choice == "5":
        past_orders(cust_id)
        cust_menu(cust_id)
    elif choice == "6":
        place_order(cust_id)
        cust_menu(cust_id)
    elif choice == "7":
        main_fun()
    else:
        print("Invalid choice. Please enter a valid input (1-6)")
        cust_menu(cust_id)

def past_orders(cust_id):
    query = "SELECT * FROM ordera WHERE ordera.cart_index = "+str(cust_id)+";"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Order ID\tCustomer ID\tOrder Time\tFinal Value\tShipping Address")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
        
def view_shipper():
    query = "SELECT * FROM shipper;"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Shipment ID\tShipper ID\tOrder ID\tOrder_time\tOrder_time\tDelivery Date\tShipping Address")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}")
    

def view_shipment(cust_id):
    query = "SELECT s.shipment_id, s.shipper_id, s.order_id, s.order_time, s.del_date, s.shipping_address FROM shipper s INNER JOIN ordera ON s.order_id = ordera.order_id WHERE cust_id = "+str(cust_id)+";"
    cursor.execute(query)
    results = cursor.fetchall()
    print("Shipment ID\tShipper ID\tOrder ID\tOrder_time\tDelivery Date\tShipping Address")
    for row in results:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")


def add_shipper():
    new_shipper = int(input("Enter new shipper ID: "))
    shippers.append(new_shipper)
    print(f"Added{new_shipper}!")

    

def main_fun():
    while True:
        print("\n---- OLAP Queries Menu ----")
        for key, value in menu.items():
            print(f"{key}. {value}")
        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            browse_products()
            main_fun()
        elif choice == "2":
            customer_login()
        elif choice == "3":
            admin_login()
        elif choice == "4":
            employee_login()
        elif choice == "5":
            customer_sign_up()
        elif choice == "6":
            cursor.close()
            cnx.close()
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice, please enter a number between 1 and 8.")


main_fun() 
