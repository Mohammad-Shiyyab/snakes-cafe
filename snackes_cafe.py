# **************************************
# **    Welcome to the Snakes Cafe!   **
# **    Please see our menu below.    **
# **
# ** To quit at any time, type "quit" **
# **************************************

def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')

Appetizers=["wings","cookies","spring rolls"]
Entrees=["salmon","steak","meat Tornado","a literal garden"]
Desserts=["ice cream","cake","pie"]
Drinks=["coffee","tea","unicorn tears"]
def user_insertion():
    user_input=input(">")
    return user_input

def main():
    intro()
    user_input = ""
    w=[]
    while(user_input.lower() != "quit"):
        x = 0
        user_input = user_insertion()
        w.append(user_input.lower())
        for a in w:
            if user_input.lower() == a:
                x = x + 1
        if user_input.lower() in Appetizers or user_input.lower() in Entrees or user_input.lower() in Desserts or user_input.lower() in Drinks:
            print('*',x , "order of", user_input,"has been add to your meal *")
        else:       
            print("sorry we dint hane this items !")
            user_input = user_insertion()

    end_application()

def end_application():
    print("thanks for using snackes cafe applecation !")

if __name__=="__main__":
    
    main()