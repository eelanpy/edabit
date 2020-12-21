# 64_Fizz_buzz_interview_question:
import os

def fizz_buzz_interview(num):
    saying = ""
    if num % 3 == 0:
        saying = 'Fizz!'
    if num % 5 == 0:
        saying = 'Buzz!'

    if num % 3 == 0 and num % 5 == 0:
        saying = 'You are hired back!'
    
    os.system("say '{}'".format(saying))

fizz_buzz_interview(30)