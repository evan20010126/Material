# import random
# print(random.randrange(1, 10))  # 1~9

# str1 = """
#     hello
#     my
#     friend
# """
# print(len(str1))

# print("hello" in str1)

# if "eeee" not in str1:
#     print("Yes, eeee is not in str1", end="\n")


# a = "   Hello, world   "
# a = a.strip()
# print(a)  # returns "Hello, world"

# a = a.replace("l", "0")
# print(a)

# x = a.split(",")
# print(x)

# #  But we can combine strings and numbers by using the format() method!

# # places them in the string where the placeholders {}
# age = 36
# txt = "My name is evan, and I am {}"
# txt = txt.format(age)
# print(txt)

# # quantity = 3
# # itemno = 567
# # price = 49.95
# # myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# # print(myorder.format(quantity, itemno, price))

# txt = "HELLO wORLD e"
# print(txt.center(99, "O"))


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# # thislist.sort(reverse=True)
# # print(thislist)
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# # To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# thislist.insert(2, "watermelon")
# print(thislist)


# # To add an item to the end of the list, use the append() method:

# # To append elements from another list to the current list, use the extend() method.
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# # he remove() method removes the specified item.
# # .remove("element名稱")
# # The pop() method removes the specified index.
# # .pop(int) 若沒有指定index 刪除last  // del list[int]

# # The clear() method empties the list.
# # The list still remains, but it has no content.

# '''
# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.
# '''
# # thislist = ["banana", "Orange", "Kiwi", "cherry"]
# # thislist.reverse()
# # print(thislist)


# fruits = ("apple", "banana", "cherry")

# (x, y, z) = fruits

# # print(x)
# # print(y)
# # print(z)


# def my_function(foods):
#     foods[0] = "a"


# arr = ["z", "z", "z"]
# my_function(arr)

# print(arr)


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# try:
#     print("hello")
#     raise Exception
# except:
#     print("here")

import sys
import bs4


class Square:
    def __init__(self, width):
        self.width = width

    @property
    def area(self):
        print("hi")
        return self.width**2

    @area.setter
    def area(self, value):
        value1, value2 = value
        print("hi2")
        self.width = value1**0.5 - value2

    @area.deleter
    def area(self):
        print("you actually del this width")
        del self.width

    def __add__(self, another):
        print("answer: {} + {}".format(self.width, another))
        return self.width + another


a = Square(10)
a.area = (100, 2)

a = a + 3
print(a)

print(dir(bs4.BeautifulSoup))

print(sys.argv)
