from Auth.Auth import Auth
from modle.users_db.Book import Book
from modle.users_db.Client import Client
from modle.users_db.Librarian import Librarian
from modle.users_db.Order import Order
from utils.Utils import App_utils, Constants

at=Auth()





print("welcome to our library\nif you are a client enter 1\nif you are a librarian enter 2 ")
user_type=input("enter here:")
App_utils.check_input_is_empty(user_type)

if user_type!="1" and user_type!="2":
    print("error")

if user_type=="1":
     print("enter 1 to log in\nenter 2 to register")
     log_type=input("enter here:")
     App_utils.check_input_is_empty(log_type)


     if log_type=="1":
      log_client_full_name=input("enter your full name:")
      log_client_id=input("enter your id:")
      App_utils.check_input_is_digit(log_client_full_name)
      if at.login_Client(log_client_full_name, log_client_id):
          pass
      else:
          print("wrong name or id")
          exit()
      App_utils.check_input_is_empty(log_client_full_name,log_client_id)


     if log_type=="2":
      client_full_name=input("enter your full name:")
      age =input("enter your age:")
      phone_number =input("enter your phone number:")
      id_no=input("enter your id number:")
      App_utils.check_input_is_digit(client_full_name)
      App_utils.check_input_is_empty(client_full_name, age,phone_number,id_no)

      at.register_new_client(Client(full_name = client_full_name,age = age,phone_number = phone_number,id_no=id_no,id= int(at.get_client_last_id())+1))
      print("this is your id number",str(at.get_client_last_id()))



     client_operation=input("choose what do you want to do \n1- borrow a book\n2- return a book\n3-show the orders you have made\nenter here:")
     App_utils.check_input_is_empty(client_operation)
     if client_operation == "1" or client_operation == "borrow a book":
        print("here is the avalibale books we have")
        print("id,tittle,description ")
        at.show_avalibale_books_list_for_client()
        borrowed_book_id=input("enter the id of the book that you want to borrow:")
        client_id=input("enter your id:")
        date=input("enter the date dd/mm/yyyy:")
        librarian_id=input("enter the id of the librarian that you want to deal with:")
        App_utils.check_input_is_empty(borrowed_book_id,client_id,date,librarian_id)
        at.check_if_the_client_exist(client_id=client_id)
        at.check_if_the_librarian_exist(librarian_id=librarian_id)
        at.check_if_the_book_is_avalibalee(book_id=borrowed_book_id)
        at.new_order(Order(book_id=borrowed_book_id,client_id=client_id,date=date,librarian_id=librarian_id,status=Constants.order_active,id=int(at.get_order_last_id())+1))
        at.change_status_of_book_inactive(book_id=borrowed_book_id)
        at.append_a_new_borrowed_book(book_id=borrowed_book_id)
        at.delete_a_book_from_avalibale(book_id=borrowed_book_id)


        print(" the order has been successfully completed and this is your order id ", at.get_order_last_id())

     if client_operation=="2" or client_operation=="return a book":
        order_id=input("enter the order id: ")
        client_id= input("enter your id:")
        book_id=input("enter the book id ")
        App_utils.check_input_is_empty(order_id,client_id,book_id)
        at.check_if_order_exist(order_id=order_id)
        at.check_if_order_is_active(order_id=order_id)
        at.check_if_book_is_borrowed(book_id=book_id)
        at.chang_status_of_order_to_expired(order_id=order_id)
        at.change_status_of_book_to_active(book_id=book_id)
        print("the operation has been done sucessfully")
     if client_operation=="3" or client_operation=="show the orders you have made":
        client_id=input("enter your id")
        client_name=input("enter your full name")
        App_utils.check_input_is_digit(client_name)
        App_utils.check_input_is_empty(client_id,client_name)
        if at.login_Client(client_name, client_id):
            pass
        else:
            print("wrong name or id")
            exit()
        at.check_if_the_client_exist(client_id=client_id)
        print("order id , client id ,librarian id,book id,status(2'active' 3'expired' 4'canceled'),date")
        at.show_the_client_orders(client_id=client_id)







if user_type=="2":
    print("enter 1 to log in\nenter 2 to register")
    log_type = input("enter here:")
    App_utils.check_input_is_empty(log_type)

    if log_type=="1":
        librarian_full_name=input("enter your full name:")
        librarian_id=input("enter your id:")
        App_utils.check_input_is_digit(librarian_full_name)
        if at.login_librarian(librarian_full_name,librarian_id):
            pass
        else:
            print("wrong name or id")
            exit()
        if App_utils.check_input_is_empty(librarian_id,librarian_full_name):
            pass
    if log_type=="2":
        librarian_full_name = input("enter your full name:")
        age = input("enter your age:")
        employment_type=input('enter your employment type (enter 0 to full ,enter 1 to part)')
        App_utils.check_input_is_digit(librarian_full_name)
        if employment_type=="0":
            emp_type=Constants.full
        elif employment_type=="1":
            emp_type=Constants.part
        else:
            print("wrong employment type")
            exit()

        id_no = input("enter your id number:")
        App_utils.check_input_is_empty(librarian_full_name, age, employment_type, id_no)

        at.register_new_librarian(Librarian(full_name= librarian_full_name, age=age,id_no=id_no,employment_type=emp_type,id=int(at.get_librarian_last_id()) + 1))
        print("this is your id number", str(at.get_librarian_last_id()))


    librarian_operation=input("choose what do you want to do\n1- show all the books\n2- add a new book\n3- show all the orders\n4- show all the clients\nenter here:")
    App_utils.check_input_is_empty(librarian_operation)
    if librarian_operation=="1"or librarian_operation=="show all the books":
       print("avalibale books:")
       print("(id,tittle,description)")
       at.show_avalibale_books_list_for_client()
       print("borrowed books:")
       at.show_borrowed_books_list()

       second_librarian_operation=input("1- if you want to search for a specific book\n2- exit\nenter here:")
       App_utils.check_input_is_empty(second_librarian_operation)
       if second_librarian_operation=="1" or second_librarian_operation=="if you want to search for a specific book":
           specific_book_id=input("enter the book id:")
           App_utils.check_input_is_empty(specific_book_id)
           if at.check_if_the_book_exist(book_id=specific_book_id):
               pass
           else:
               print("the book doesnt exist")
               exit()
           print("book id , tittle ,   description   , status(false'inactive',true'active'),author")
           at.show_the_specific_book_details(book_id=specific_book_id)
       elif second_librarian_operation=="2" or second_librarian_operation=="exit":
           exit()
       else:
           print("wrong input")
           exit()
    if librarian_operation=="2" or librarian_operation=="add a new book":
       book_tittle=input("enter the book tittle:")
       book_description=input("enter the book description:")
       book_author=input("enter the book author:")
       App_utils.check_input_is_digit(book_author,book_description,book_tittle)
       App_utils.check_input_is_empty(book_author,book_description,book_author)
       at.add_a_new_book(Book(tittle=book_tittle,description=book_description,author=book_author,status=Constants.book_active,id=int(at.set_new_book_id())+1))
       print("the operation has been done successfully and here is the new book id ",at.set_new_book_id())
    if librarian_operation=="3" or librarian_operation=="show all the orders":
        print("order id, client id, librarian id, book id, status(2'active'3'expired'4'canceled'  , date")
        at.show_all_orders()
        second_librarian_operation=input("1-if you want to search for a specific order\n2-exit\nenter here:")
        App_utils.check_input_is_empty(second_librarian_operation)
        if second_librarian_operation=="1"or second_librarian_operation=="if you want to search for a specific order":
           order_id=input("enter the order id:")
           at.check_if_order_exist(order_id=order_id)
           print("order id, client id, librarian id, book id, status(2'active'3'expired'4'canceled'  , date")
           print(at.show_specific_order(order_id=order_id))
        elif second_librarian_operation == "2" or second_librarian_operation == "exit":
            exit()
        else:
            print("wrong input")
            exit()
    if librarian_operation=="4" or librarian_operation=="show all the clients":
        print(" id,    name    ,  age , id number , phone number")
        at.show_all_clients()
        second_librarian_operation = input("1-if you want to search for a specific client\n2-exit\nenter here:")
        App_utils.check_input_is_empty(second_librarian_operation)
        if second_librarian_operation=="1"or second_librarian_operation=="f you want to search for a specific client":
            client_id=input("enter the client id:")
            App_utils.check_input_is_empty(client_id)
            at.check_if_the_client_exist(client_id=client_id)
            print(" id,    name    ,  age , id number , phone number")
            print(at.show_specific_client(client_id=client_id))
        elif second_librarian_operation== "2" or second_librarian_operation== "exit":
            exit()
        else:
            print("wrong input")
            exit()










