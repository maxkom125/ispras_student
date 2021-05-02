#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 2021

@author: maksym

First, let’s define a function, ord(ch) = the position of ch in the alphabet + 1, where ch can be any lowercase letter. So, ord(a) = 2, ord(b) = 3, ord(c) = 4, … ord(z) = 27.

Let fact(x) be x! or the factorial of x. A few examples, fact(1) = 1, fact(2) = 2, fact(3) = 6, fact(4) = 24, fact(5) = 120, etc. Given a string S of length N, consisting of lowercase letters only, the Faketorial Hashing of S, is defined as below:

fake_hash(S) = fact(ord(S[0])) × fact(ord(S[1])) × fact(ord(S[2])) × …… × fact(ord(S[N - 1]))

In other words, it is the product of the factorial of the ord() value of all the characters in S (That’s right, no modulus! Unlike the lame polynomial hashing). Not only that we have a new hashing mechanism in place, but we would also like to crack this now. Given a string S1 consisting of lowercase letters only, your task is to find a different string S2 consisting of lowercase letters, such that, fake_hash(S1) = fake_hash(S2) and S1 ≠ S2.

If there are multiple possible choices for S2, you need to find the lexicographically smallest one, or output the word “Impossible” without quotes, if it is not possible to find such a string.

Input
The first line contains an integer T, denoting the number of test cases. Each test case contains the string S1 consisting of lowercase letters (a-z) only.
Constraints
1 ≤ T ≤ 3000
1 ≤ |S1| ≤ 30


Except for the sample, the following constraints will hold:
1 ≤ |S1| ≤ 5, for 90% of the test cases
1 ≤ |S1| ≤ 15, for 99% of the test cases
Output
For each test case, output the case number followed by the required output. Please refer to the sample input/output section for the precise format. 
"""

def factorial(x): # x!
    fact = 1
    for i in range(2, x + 1): #2*3*...*x = x!
        fact *= i
        
    return fact


def Faketorial_hash(s): # Faketorial_hash(S) = factorial(ord(S[0]) - 95) × factorial(ord(S[1]) - 95) × …… × factorial(ord(S[N - 1]) - 95)
    fhash = 1
    for letter in s:
        x = ord(letter) - 95 # ord(a) == 97 
        fhash *= factorial(x) #
    
    return fhash


def HackFaketorialHash(hash_s, get_max_string = 1):
    if get_max_string == 1:
        
        search_s = ""
        print(hash_s)
        
        cur_hash   = hash_s
        greatest_num = 27 # z
        
        while greatest_num > 1 and cur_hash != 1:
            
            divider = greatest_num
            while divider > 1:
                
                while cur_hash % divider != 0: # Дошли до числа, на которое не делится, значит там нет factorial(greatest_num)          
                    print("Дошли до числа, на которое не делится: ", divider)
                    if divider != greatest_num: # Возврат к исходному хэшу, проверка greatest_num - 1 на текущей стадии (убираем только наибольший множитель)
                        cur_hash *= greatest_num
                        print("убираем только наибольший множитель: ", greatest_num)
                    else:
                        divider = greatest_num - 1 # Если текущий номер -- максимальный то будем исследовать следующий
                        print("текущий номер -- максимальный, будем исследовать следующий")
                        
                    greatest_num -= 1
                    
                    if greatest_num == 1:
                        print("IMPOSSIBLE!!!")
                        break
                    
                print(cur_hash, " //= ", divider)
                cur_hash //= divider
                divider -= 1
            # В hash_s нашли factorial(greatest_num)
            search_s += chr(greatest_num + 95) # chr(97) == a
            
        if cur_hash == 1:
            return search_s
        else:
            return "Impossible"
    
    else: # min string. write min symbol if possible do string without it factorial(ord())
        print("mem")
        


T = int(input())
for ttt in range(T):
    
    s = input()
    hash_s = Faketorial_hash(s)
    
    s_min = ""
    
    equivalent_replacements = {"c": "aab", "e": "abd", "g": "aaaf", "h": "abbf", "i": "bdf", "k": "abj", "o": "aaaan", "w": "aabv"}
    
    for letter in s:
        
        if letter in equivalent_replacements.keys():
            s_min += equivalent_replacements[letter]
        else:
            s_min += letter
        
    s_min = "".join(sorted(s_min))
    
    if s_min == s:
        for i in range(len(s_min) - 1, 0, -1):
            if s_min[i] != s_min[i - 1]:
                s_min[i], s_min[i + 1] = s_min[i + 1], s_min[i]
                break
            
    if s_min != s:
        print("Case ", ttt + 1,": ", s_min, sep = "")
    else:
        print("Case ", ttt + 1,": ", "Impossible", sep = "")

        
    #print(HackFaketorialHash(hash_s))

