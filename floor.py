def floor_division(user_input1,user_input2):
    floor_division= user_input1//user_input2
    print(floor_division)
    
def string(user_input1,user_input2):
    string= user_input1+user_input2
    print(string)
    
def main():
    user_input1= float(input("enter first number"))
    user_input2= float(input("enter second number"))
    floor_division(user_input1, user_input2)
    
    # user_input1= input("first number")
    # user_input2= input("second number")
    # keep_string= string(user_input1,user_input2)


main()