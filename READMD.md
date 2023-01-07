# Python tips

## Note
- 我的pip路徑:
    > C:\Users\User\AppData\Local\Programs\Python\Python37\Scripts

- keras預設下載路徑:
    > C:\Users\User\.keras

- 下載模組:
    > pip install ...

## Contents 
- [Python tips](#python-tips)
  - [Note](#note)
  - [Contents](#contents)
    - [frequently used built-in modules.](#frequently-used-built-in-modules)
    - [String method](#string-method)
    - [Most Values are True](#most-values-are-true)
    - [list comprehension](#list-comprehension)
    - [list sort](#list-sort)
    - [Copy list](#copy-list)
    - [Asterisk *](#asterisk-)
    - [Set {}](#set-)
    - [Dictionary { : , :, ...}](#dictionary-----)
    - [Class](#class)
    - [Iterator: __iter__() and __next__()](#iterator-iter-and-next)
    - [JSON](#json)
    - [python string format](#python-string-format)
    - [file accessing](#file-accessing)
    - [with](#with)
    - [decorator 參考網站](#decorator-參考網站)
---

### frequently used built-in modules.

1. os module
2. random module
3. math module
4. time module
5. sys module
6. collections module
7. statistics module

---

### String method 
[參考網址](https://www.w3schools.com/python/python_ref_string.asp)

1. capitalize()
    > Converts the first character to upper case
2. casefold()
    > Converts string into lower case
3. center(length, character)
4. count(value, start, end)

---

### Most Values are True
1. Almost any value is evaluated to True if it has some sort of content.

2. Any string is True, except empty strings.

3. Any number is True, except 0.

4. Any list, tuple, set, and dictionary are True, except empty ones.

isinstance(x, float) //determine if an object is of a certain data type

###  list comprehension

---

- syntax
    newlist = [expression for item in iterable if condition == True]
- example        
    ```
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

    newlist = [x for x in fruits if "a" in x]

    print(newlist)
    ```

### list sort

---

- syntax
    list.sort(key=..., reverse=...)
    > reverse - If True, the sorted list is reversed (or sorted in Descending order)

    > key - function that serves as a key for the sort comparison

### Copy list

---

- method1: Make a copy of a list with the copy() method:
    ```
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)
    ```
- method2: Make a copy of a list with the list() method:
    ```
    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist)
    ```

### Asterisk *

---

- introduction: If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

- Example: 
    ```python
    fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

    (green, yellow, *red) = fruits

    print(green)  # apple
    print(yellow) # banana
    print(red)    # ['cherry', 'strawberry', 'raspberry']
    ```
- Example2:
    If the number of arguments is unknown, add a * before the parameter name
    ```python
    def my_function(*kids):
    print("The youngest child is " + kids[2])

    my_function("Emil", "Tobias", "Linus")
    ```

### Set {}

---

- method
    1. set.add("element")
    2. set.update(iterable object)
        > iteraable object: tuples, lists, dictionaries etc. 

        > 會直接修改原本set
    3. set.remove("element") // same function: .discard
        > If the item to remove does not exist, discard() will NOT raise an error.
    4. set.clear()
    5. del set
        > delete the set completely
    6. set.union(set) method that returns a new set

### Dictionary { : , :, ...}

---

- Duplicate values will overwrite existing values

- .pop("key")

### Class

---

- function 第一個parameter: 傳入 object 的記憶體位址
- class properties
    ```python
    class Person:
        TITLES = ('Dr','Mr', 'Mrs') # class attribute
        # def ... ():
    ```
- object's method:
    - getattr(object, attribute_name, default_value)
    - setattr(object, attribute_name, new_value)
    - hasattr(object, attribute_name)
    - delattr(object, attribute_name)
    > getattr & delattr 若為不存在的屬性, raise AttributeError
- @property, @property_name.setter, @property.deleter
    - @property: 當read此method時觸發
    - @property_name.setter: 當write此method時觸發
    - @property.deleter: 當del此method時觸發
    - Example:
        ```python
        class Square:
        def __init__(self,width):
            self.width = width

        @property
        def area(self):
            print("invoke 1")
            return self.width**2

        @area.setter
        def area(self, value):
            value1, value2 = value
            print("invoke 2")
            self.width = value1**0.5 - value2

        @area.deleter
        def area(self):
            print("invoke 3")
            print("you actually del this width")
            del self.width

        a = Square(10)
        b = a.area # invoke 1 and b = 100
        a.area = (4, 1) # invoke 2 and a.width = 4**0.5 - 1 
        del a.area # invoke 3 and del a.width
        ```

    - Magic method
        > 以特殊符號呼叫function
        - Example: Fractional number class
            ```python
            class FractionalNumber:
            def __init__(self, numer, denom):
                self.n = numer
                self.d = denom
            def __add__(self, other):
                return FractionalNumber(self.d*other.n+self.n*other.d,self.d*other.d)
            def __sub__(self, other):
                return FractionalNumber(self.d*other.n-self.n*other.d,self.d*other.d)
            def __mul__(self,other):
                return FractionalNumber(self.n*other.n,self.d*other.d)
            def __truediv__(self,other):
                return FractionalNumber(self.n*other.d,self.d*other.n)
            def __str__(self):
                return str(self.n)+"/"+str(self.d)
            def __repr__(self): 
                # Tell Python how to represent FractionalNumber. 
                # The output string must be able to be evaluated by eval.
                return "FractionalNumber({},{}..................)".format(self.n,self.d)
            def __iadd__(self,other):
                self.n = self.n*other.d+other.n*self.d
                self.d = self.d*other.d
                return self
            ```
- @staticmethod [參考文章](https://ji3g4zo6qi6.medium.com/python-tips-5d36df9f6ad5)
    > 靜態函數，被綁定在class中，不需要建立object就可使用。\
    > 無法存取物件資料，只能對傳入的參數做處理。
    - syntax:
        ```python
        @staticmethod
        #def func(args, ...):
        ```

- @classmethod
    > 綁定的對象為class，不需要建立object就可以使用。
    > 彈性的創造物件，不局限於限定的建構子參數。
    - syntax:
        ```python
        @classmethod    #cls為該類別的記憶體位置
        #def func(cls, ...):
        ```
        
    


### Iterator: __iter__() and __next__()

---

- String, Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

- for 與 iterator 的關係
    > The for loop actually creates an iterator object and executes the next() method for each loop.


### JSON

---

- import json
- method:
    1. json.loads("json字串") # return python's dictionary
        > json.load(file_object) # return python's object #file_object open("路徑")
    1. json.dumps(python's object, indent = int) # return json
        > json.dump(json_obj, file_object) #file_object open("路徑", "w")
        > 1. dict
        > 2. list
        > 3. tuple
        > 4. string
        > 5. int
        > 6. float
        > 7. True
        > 8. False
        > 9. None
    1. python's object & json    
        | Python | JSON   |
        | ------ | ------ |
        | dict   | Object |
        | list   | Array  |
        | tuple  | Array  |
        | str    | String |
        | int    | Number |
        | float  | Number |
        | True   | true   |
        | False  | false  |
        | None   | null   |

### python string format

---

- table:
    | word | effect                                                                         |
    | ---- | ------------------------------------------------------------------------------ |
    | :<   | Left aligns the result (within the available space)                            |
    | :>   | Right aligns the result (within the available space)                           |
    | :^   | Center aligns the result (within the available space)                          |
    | :=   | Places the sign to the left most position                                      |
    | :+   | Use a plus sign to indicate if the result is positive or negative              |
    | :-   | Use a minus sign for negative values only                                      |
    | :    | Use a space to insert an extra space before positive numbers (and a            | minus sign before negative numbers) |
    | :,   | Use a comma as a thousand separator                                            |
    | :_   | Use a underscore as a thousand separator                                       |
    | :b   | Binary format                                                                  |
    | :c   | Converts the value into the corresponding unicode character                    |
    | :d   | Decimal format                                                                 |
    | :e   | Scientific format, with a lower case e                                         |
    | :E   | Scientific format, with an upper case E                                        |
    | :f   | Fix point number format ({:.2f})                                               |
    | :F   | Fix point number format, in uppercase format (show inf and nan as INF and NAN) |
    | :g   | General format                                                                 |
    | :G   | General format (using a upper case E for scientific notations)                 |
    | :o   | Octal format                                                                   |
    | :x   | Hex format, lower case                                                         |
    | :X   | Hex format, upper case                                                         |
    | :n   | Number format                                                                  |
    | :%   | Percentage format                                                              |


### file accessing

---

- Syntax
    f = open("file_name", "mode", encoding = '')
- 

### with

---

- target: Python 會自動進行資源的建立、清理、回收，方便使用各種資源
- syntax:
    ```python
    # 使用with開啟檔案時，會將開啟的檔案放在 f variable中，而 f variable 只有在這個with範圍內可以使用，離開範圍時f variable 就會自動被關閉，回收相關的資源
    with open("file_name", "mode") as f:
        # statements
    ```
- with 與 class 的 \__enter__ 與 \__exit__
    > with剛開始執行時，會先執行__enter__ function return 回配給的資源\
    > with結束時，會自動呼叫__exit__ function 釋放資源

---

### decorator [參考網站](https://www.maxlist.xyz/2019/12/07/python-decorator/)
- target: 降低程式碼重複率、易讀性高、靈活度高
- syntax: @ 要裝飾的function_name
