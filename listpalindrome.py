list=[]
list.append(input("enter a number"))
list.append(input("enter a number"))
list.append(input("enter a number"))
list_copy=list.copy()
list_copy.reverse()
if(list_copy==list):
    print("given list is palindrome")
else:
    print("not a palindrome")