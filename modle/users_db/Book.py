from utils.Utils import Constants


class Book:
    def __init__(self,id,tittle,description,author,status:Constants):
        self.__id=id
        self.__tittle = tittle
        self.__description = description
        self.__author = author
        self.__status= status


    def get_Book_id(self):
        return self.__id
    def set_Book_id(self,id):
        self.__id=id

    def get_Book_tittle(self):
            return self.__tittle

    def set_Book_tittle(self, tittle):
            self.__tittle = tittle
    def get_Book_description(self):
        return self.__description
    def set_Book_descriptioj(self,description):
        self.__description=description

    def get_Book_author(self):
            return self.__author

    def set_Book_author(self, author):
            self.__author = author
    def get_Book_status(self):
        return self.__status
    def set_Book_status(self,status):
        self.__status=status



    def __repr__(self):
         return f'   {self.__id}    , {self.__tittle}, {self.__description} ,              {self.__status}                 ,{self.__author}'
