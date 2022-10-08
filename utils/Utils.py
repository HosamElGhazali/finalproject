class Constants:
    full=0
    part=1
    book_active=True
    book_inactive= False
    order_active=2
    order_expired=3
    order_canceled=4








class App_utils:

    @staticmethod
    def check_input_is_empty(*input):
        for item in input:
            if item.isspace() or item=="":
                print("empty input")
                exit()
            else :
                pass


    def check_input_is_digit(*input):
        for item in input:
            if str(item).isdigit():
                print("wrong input,please try again")
                exit()

