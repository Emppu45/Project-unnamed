import keyboard
import math

print("Hello press enter to continue")
keyboard.wait('enter')
name = input("Hello and welcome to my test. What you want me to call you?")

print("Okay " + name + " This test has 5 questions. Are you ready?")

# Setting score

score = 0
score = int(score)

# QUestion 1

print("Question 1: what is 720/2?")

Q1answer = "360"
Q1response = input('Your answer : ')

if (Q1response != Q1answer):
    print("Oh thats bad, You're WRONG!")
    score = 0

else:
    print('Good job! ' + name + ' "." ' + Q1response + ' is CORRECT!')
    score = score + 1

print('Great your score is ' + str(score) + ' out of 10!')

# Question 2

print("Question 2!")
print("What is 123/123")

Q2answer = "1"
Q2response = input("Your answer : ")

if (Q2response != Q2answer):
    print("YOU GOT THIS wronng? you're probably 8-year old. Go back to school")

else:
    print("Noice! " + name + " " + Q1response + " is CORRECT!")
    score: int
    score = score + 1

# Question 3

print("Question 3!")

print("What is 92/2")

Q3answer = "42"
Q3response = input("Your answer : ")

if (Q3response != Q3answer):
    print("Sorry, that was incorrect")

else:
    print("Good job " " + name + !")
    score = score + 2


