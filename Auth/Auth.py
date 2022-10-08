from _ast import Constant

from modle.users_db.Book import Book
from modle.users_db.Client import Client
from modle.users_db.F1 import F1
from modle.users_db.Librarian import Librarian
from modle.users_db.Order import Order
from utils.Utils import Constants




class Auth:

    librarian_list : list[Librarian]=[Librarian(full_name="Ahmed Khaled",id="0", employment_type=Constants.full,age="50",id_no="420406332"),
                                      Librarian(full_name="Anas Anwar",id="1", employment_type=Constants.full,age="43",id_no="942576632"),
                                      Librarian(full_name="Amjad Fadi",id="2", employment_type=Constants.part,age="37",id_no="957259553"),
                                      Librarian(full_name="Hazem Anwar",id="3", employment_type=Constants.part,age="39",id_no="978663841")]
    client_list : list[Client]=[Client(id="0",full_name="Fayez Samer",age="25",id_no="942579923",phone_number="0599324457"),
                                Client(id="1",full_name="Mohammed Ali",age="20",id_no="954866435",phone_number="0598325423"),
                                Client(id="2",full_name="Kareem Mahir",age="29",id_no="943535753",phone_number="0597794362"),
                                Client(id="3",full_name="Murad Nabil",age="33",id_no="988463146",phone_number="0597799182")]
    avaliable_books_list: list[Book]=[Book(tittle="Math", id="0",author="Ahmed",status=Constants.book_active,description="(a math book for new students)"),
                                     (Book(tittle="English", id="1", author="Mohammed", status=Constants.book_active,description=" (English latters)")),
                                      Book(tittle="Habits", id="2", author="Mark", status=Constants.book_active,description="(how to build good habits)")]
    borrowed_books_list :list[Book]=[Book(tittle="Physics",id="3",author="ali",status=Constants.book_inactive,description="(physics basics)"),
                                     Book(tittle="History",id="4",author="Mostafa",status=Constants.book_inactive,description="(the history of palestine)"),
                                     Book(tittle="Arabic",id="5",author="Shaker",status=Constants.book_inactive,description="(arabic latters)")]
    orders_list :list[Order]=[Order(id="0",date="12/10/2022",client_id="0",book_id="0",status=Constants.order_expired,librarian_id="0"),
                              Order(id="1",date="30/12/2019",client_id="0",book_id="2",status=Constants.order_active,librarian_id="1"),
                              Order(id="2",date="5/8/2011",client_id="1",book_id="2",status=Constants.order_active,librarian_id="1")]

    def login_librarian(self,full_name:str,id:str) -> bool:
        for item in self.librarian_list:
            if item.get_id() == id and item.get_full_name() ==full_name:
                return True
            else:
                pass

    def login_Client(self,full_name:str, id:str) -> bool:
        for item in self.client_list:
            if item.get_id()==id and item.get_full_name()==full_name:
                return True
            else:
                pass

    def register_new_client(self,client:Client):
        self.client_list.append(client)

    def register_new_librarian(self, librarian: Librarian):
            self.librarian_list.append(librarian)

    def get_client_last_id(self) -> int:
       return self.client_list[len(self.client_list) - 1 ].get_id()

    def get_librarian_last_id(self)-> int:
        return self.librarian_list[len(self.librarian_list)-1].get_id()
    def show_avalibale_books_list_for_client(self):
        for item in self.avaliable_books_list:
            print (item.get_Book_id(),item.get_Book_tittle(),item.get_Book_description())
    def show_borrowed_books_list(self):
        for item in self.borrowed_books_list:
            print (item.get_Book_id(), item.get_Book_tittle(), item.get_Book_description())

    def new_order(self,order:Order):
        self.orders_list.append(order)
    def check_if_the_client_exist(self,client_id) :
        for item in self.client_list:
            if int(client_id)== int(item.get_id()):
                return True
        else:
               print("wrong client id")
               exit()

    def check_if_the_librarian_exist(self,librarian_id):
        for item in self.librarian_list:
             if librarian_id == item.get_id():
                break
        else:
                 print("wrong librarian id ")
                 exit()

    def get_order_last_id(self) -> int:
        return self.orders_list[len(self.orders_list) - 1].get_id()

    def check_if_the_book_is_avalibalee(self,book_id):
        for item in self.avaliable_books_list:
             if book_id == item.get_Book_id():
                break
        else:
                 print("wrong book id ")
                 exit()
    def delete_a_book_from_avalibale(self,book_id:str):
        self.avaliable_books_list= [Book for Book in self.avaliable_books_list if Book.get_Book_id() == book_id]
    def append_a_new_borrowed_book(self,book_id):
        for item in self.avaliable_books_list:
         if item.get_Book_id()==book_id:
            self.borrowed_books_list.append(item)
    def change_status_of_book_inactive(self,book_id):
        for item in self.avaliable_books_list:
            if item.get_Book_id()==book_id:
                item.set_Book_status(Constants.book_inactive)
    def chang_status_of_order_to_expired(self,order_id):
        for item in self.orders_list:
            if item.get_id()== order_id:
                item.set_status(Constants.order_expired)
    def change_status_of_book_to_active(self,book_id):
        for item in self.borrowed_books_list:
            if item.get_Book_id()==book_id:
                item.set_Book_status(Constants.book_active)
                self.avaliable_books_list.append(item)
    def check_if_order_is_active(self,order_id):
        for item in self.orders_list:
            if item.get_id()== order_id:
                if item.get_status()==Constants.order_active:
                    break
                else:
                    print("the order is not active")
                    exit()
    def check_if_book_is_borrowed(self,book_id):
        for item in self.borrowed_books_list:
            if item.get_Book_id()==book_id:
                break
            else:
                print("the book is not borrowed")
                exit()
    def show_the_client_orders(self,client_id):
        for item in self.orders_list:
            if item.get_client_id()== client_id:
               print(item)
            else:
                pass
    def check_if_order_exist(self,order_id):
        for item in self.orders_list:
            if item.get_id()==order_id:
                break
        else:
            print("order not found")
            exit()
    def librarian_specific_book(self,book_id):
        for item in self.avaliable_books_list:
            if item.get_Book_id()==book_id:
                print(item)
        else:
            for item in self.borrowed_books_list:
                if item.get_Book_id()==book_id:
                    print(item)
    def check_if_the_book_exist(self,book_id):
        for item in self.avaliable_books_list:
            if item.get_Book_id() == book_id:
                return True
        else:
            for item in self.borrowed_books_list:
                if item.get_Book_id() == book_id:
                    return True

    def show_the_specific_book_details(self,book_id):
        for item in self.avaliable_books_list:
            if item.get_Book_id() == book_id:
                print(item)

        else:
            for item in self.borrowed_books_list:
                if item.get_Book_id() == book_id:
                    print(item)

    def add_a_new_book(self,book : Book):
        self.avaliable_books_list.append(book)

    def get_last_book_id_from_avalibale(self)->int:
        return self.avaliable_books_list[len(self.avaliable_books_list)-1].get_Book_id()

    def get_last_book_if_from_borrowed(self)->int:
        return self.borrowed_books_list[len(self.borrowed_books_list)-1].get_Book_id()

    def set_new_book_id(self)->int:
        if int(self.get_last_book_id_from_avalibale())> int(self.get_last_book_if_from_borrowed()):
            return self.get_last_book_id_from_avalibale()
        elif int(self.get_last_book_if_from_borrowed())> int(self.get_last_book_id_from_avalibale()):
            return self.get_last_book_if_from_borrowed()
    def show_all_orders(self):
        for item in self.orders_list:
            print(item)
    def show_specific_order(self,order_id):
        for item in self.orders_list:
            if item.get_id()==order_id:
                return item
    def show_all_clients(self):
        for item in self.client_list:
            print(item)
    def show_specific_client(self,client_id):
        for item in self.client_list:
            if item.get_id()==client_id:
                return item




