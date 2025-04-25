# #  coditional and loops //vvclass and obect and inheritance // List 
# # Data Structure and algorithm
# #  1. array and string 
# #  2. Linked list 
# #  3. Stack and queue 
# #  4. Function and Recursion and backtrakking 
# #  5. Searching algorithm 
# #  6. Sorting algorithm 
# #  7. Hashing 


#Condition statement:
# n=7
# if (n%2==0):
#     print(f"The number {n} is even")
# else:
#     print(f"THe number is {n} is odd ")

# Conditional loop 
# for loop 
# while loop 
# n=10
# for i in range(1,n-1):
#     print(i)
# list=[1,2,4,"Raju"]
# # print(list[0],list[1],list[2],list[3])
# print(list[-1:])
# # x=len(list) # 4
# # print(x)
# # for i in range(x):
# #     print(i)
 
# for i in list:
#     print(i)      
 

 



# # if, elif, else example

# x = 10
# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is equal to 5")
# else:
#     print("x is less than 5")
# i=1 # intialization 
# while(i<=5): # condition 
#     print(i)
#     i =i+1   # Increment/decrement

# CLass and Object :
# class is blueprint and it is not real # ghar banauda naksha ready
# object real version of class # Gives real output

# # For loop example
# for i in range(5):
#     print(f"Iteration {i}")

# # While loop example
# count = 0
# while count < 5:
#     print(f"Count is {count}")
#     count += 1
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def speak(self):
        print(f"Hi {self.name} and your age={self.age}")
ani=Animal("Hari",5)
ani.speak()
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print(f"{self.name} says hello!")
        
# # Creating an object of the Animal class
# dog = Animal("Buddy", 3)
# dog.speak()


# # Inheriting from the Animal class
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)
#         self.breed = breed
        
#     def speak(self):
#         print(f"{self.name} barks!")
        
# # Creating an object of the Dog class
# dog = Dog("Buddy", 3, "Golden Retriever")
# dog.speak()


# # Creating a list
# fruits = ["apple", "banana", "cherry"]

# # Adding an element to the list
# fruits.append("orange")

# # Removing an element from the list
# fruits.remove("banana")

# # Accessing elements by index
# print(fruits[1])  # Output: cherry

# # Iterating through the list
# for fruit in fruits:
#     print(fruit)


# # Array example
# arr = [1, 2, 3, 4, 5]

# # String example
# string = "Hello, World!"
# print(string[7:12])  # Output: World


# #Linked list:
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
        
#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
        
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# # Using the LinkedList class
# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.append(30)
# ll.display()


# # Stack and Queue

# stack = []

# # Push operation
# stack.append(10)
# stack.append(20)

# # Pop operation
# print(stack.pop())  # Output: 20

# #Queue (using collections.deque)

# from collections import deque

# queue = deque()

# # Enqueue operation
# queue.append(10)
# queue.append(20)

# # Dequeue operation
# print(queue.popleft())  # Output: 10
    
   

# #Function

# def add(a, b):
#     return a + b

# print(add(2, 3))  # Output: 5 

# #Recursion (Factorial)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))  # Output: 120


# #Searching Algorithm
# #Linear Search

# def linear_search(arr, target):
#     for i, num in enumerate(arr):
#         if num == target:
#             return i
#     return -1

# arr = [10, 20, 30, 40, 50]
# print(linear_search(arr, 30))  # Output: 2