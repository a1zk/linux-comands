#!/usr/bin/python3

while True:
 print("Options:")
 print("Введите 'add'для додавания двух чисел:")
 print("Введите 'subtract'для вычитания двух чисел:")
 print("Введите 'multiply'для умножения двух чисел:")
 print("Введите 'divide' для деления двух чисел:")
 print("Введите 'quit'для выхода с калькулятора:")
 user_input=input(":")

if user_input =="quit":break
elif user_input=="add":
 num1= float(input("первое число"))
 num2= float(input("второе число"))
 result = str(num1 + num2)
 print("Ответ" + result)

#elif user_input == "subtract":

#elif user_input == "multiply":

#elif user_input == "divide":

else:
 print("Unknow input!")

