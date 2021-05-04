 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 2021

@author: maksym
"""
simple_modulo = 1000000007

def fact_modulo_from(x, x_from):
    answer = dict()
        
    for i in range(x, x_from - 1, -1):
        if i % simple_modulo == 0:
            return 0
        else:      
            # answer = (answer * i)
            factor_i = Factor(i)
            # print("x = ", x, "i = ", i, "Factor_i = ", factor_i)
            for f in factor_i.keys():
                try:
                    answer[f] += factor_i[f] #!!!!!!
                except KeyError:
                    answer[f] = factor_i[f] 
        
    return answer


def C(n, k): # n! / ((n - k)! * k!) == (n * (n - 1) * ... * (max(n - k, k) + 1)/ (min (n - k, k))! )
    if k == 0 or n == 0:
        return 1
    elif k > n:
        return -1
    elif k == n:
        return 1
    # print(n , k)
    numerator = fact_modulo_from(n, max(n - k, k) + 1)
    # print(numerator)
    denominator = fact_modulo_from(min(n - k, k), 1)
    # print(denominator)
    if numerator  == 0:
        return 0
    else:
        #return numerator  // fact_modulo_minus(min(n - k, k), 0)
        ans_factor = dict()
        for f in numerator.keys():
            try:
                ans_factor[f] = numerator[f] - denominator[f]
            except KeyError:
                ans_factor[f] = numerator[f]
                
        return Get_number_from_factor(ans_factor)
    
    
    # if k == 0:
    #     return 1
    # elif k > n:
    #     return 0
    # else:
    #     return C(n - 1, k) + C(n - 1, k - 1)


def C_modulo(n, k): # n! / ((n - k)! * k!) == (n * (n - 1) * ... * (max(n - k, k) + 1)/ (min (n - k, k))! )
    numerator = 1
    denominator = 1
    # print(n, k)
    for i in range(n, max(n - k, k), -1):
        numerator = (numerator * i) % simple_modulo
        
    for j in range(min(n - k, k), 1, -1):
        denominator = (denominator * j) % simple_modulo

    return numerator, denominator

def Factor(n):
    Ans = dict()
    d = 2
    count = 1
    while d * d <= n:
        if n % d == 0:
            Ans[d] = count
            n //= d
            count += 1
        else:
            d += 1
            count = 1
    if n > 1:
        try:
            Ans[n] += 1
        except KeyError:
            Ans[n] = 1
    return Ans

def Get_number_from_factor(factor):
    xxx = 1
    for i in factor.keys():
        xxx *= i ** factor[i]
        
    return xxx

def Mul_factor_numbers(factor, array_of_numbers, multiply = 1): # change factor; if multiply != 1 => div
    for x in array_of_numbers:
        factor_x = Factor(x)
        # print(factor_x)
        Add_factors(factor, factor_x, multiply)
    return

def Add_factors(factor, add_factor, add = 1): # change factor; if add != 1 => subtract
    if add == 1:
        for f in add_factor.keys():
            try:
                factor[f] += add_factor[f]
            except KeyError:
                factor[f]  = add_factor[f]
    else:
        for f in add_factor.keys():
            try:
                factor[f] -= add_factor[f]
            except KeyError:
                print("Key Error, can't subtruct. Key: ", f)
    return
            
def Ans(N): #a Ans(n) + b Ans(n - 1) + c Ans(n - 2) =
            #(a + b) Ans(n - 3) + (a + b + c) Ans(n - 4) + (a + c) Ans(n - 5)
    if N <= 1:
        return 0
    elif N <= 4:
        return 1
    elif N <= 6:
        return 2
    elif N == 7:
        return 3
    
    a = 1
    b = 2
    c = 1
    curr_N = N - 4
    while curr_N >= 7:
        # print(a, b, c, "curr_N: ", curr_N)
        new_a = (a + b) % simple_modulo
        new_b = (a + b + c) % simple_modulo
        new_c = (a + c) % simple_modulo
        a, b, c = new_a, new_b, new_c
        # print(a, b, c, "curr_N: ", curr_N)
        curr_N -= 3
        
    if curr_N == 4:       
        return a + b + c
    elif curr_N == 5:
        return 2 * a + b + c
    elif curr_N == 6:
        return 2 * a + 2 * b + c
    
T = int(input()) # test count
# answer = []
N = 1


for i in range(T):
    N = int(input())
    print (Ans(N) % simple_modulo)
    continue
    # N += 1
    curr_answer = 0
    
    if N < 2:
        print(0)
        break #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! breaks for
    
    if N % 2 == 0: # only 1 type
        type1_count = N // 2
        type2_count = 0
        previous_c = 1
        curr_c = dict()
    
    else:
        type1_count = (N - 3) // 2
        type2_count = 1
        previous_c = type1_count + 1
        curr_c = Factor(type1_count + 1)
        
    print("type1 ", curr_c)
    n = type1_count + type2_count
    k = type2_count
    curr_answer += previous_c % simple_modulo
    # type2_count += 2
    # type1_count -= 3
    
        
    while n - k - 3 >= k + 2: # type1_count >= type2_count: # replace 3 type_1 and 2 type_2 (6 = 2 * 3 = 3 * 2)
    # (n * ... * (n - k - 1) ) / k! -> (n - 1) * .. * (n - k - 2) // (k + 2)!
        # print (n - k , k)
        # print (previous_c, (n - k), (n - k - 1), (n - k - 2), "//", n , (k + 1) , (k + 2))
        if (previous_c * (n - k) * (n - k - 1) * (n - k - 2) % (n * (k + 1) * (k + 2)) != 0):
            print("ERROR")
        new_koef = previous_c * (n - k) * (n - k - 1) * (n - k - 2) // n // (k + 1) // (k + 2)
        
        # Mul_factor_numbers(curr_c, [(n - k), (n - k - 1), (n - k - 2)]) # mul
        # Mul_factor_numbers(curr_c, [n , (k + 1) , (k + 2)], -1)         # div
        # print(curr_c, Get_number_from_factor(curr_c))
            
        previous_c = (new_koef) % simple_modulo
        # print(previous_c, "n and k: ", n - 1, k + 2)
        curr_answer = (curr_answer + previous_c) % simple_modulo
        # n = type1_count + type2_count
        # k = type2_count
        # type2_count += 2
        # type1_count -= 3
        n -= 1
        k += 2
        
    if N % 3 == 0: # only 2 type
        type1_count = 0 
        type2_count = N // 3
        previous_c = 1
    
    elif (N - 2) % 3 == 0: # one 1 type
        type2_count = (N - 2) // 3
        type1_count = 1
        previous_c = type2_count + 1
        
    else: # two 1_type
        type2_count = (N - 4) // 3
        type1_count = 2
        previous_c = (type2_count + type1_count) * (type2_count + type1_count - 1) // 2
    
    print("type2 ", previous_c)
    if type2_count > type1_count:
        curr_answer += previous_c % simple_modulo
    n = type1_count + type2_count
    k = type1_count
    # type2_count -= 2
    # type1_count += 3
        
    while n - k - 2 > k + 3: # type2_count > type1_count: # replace 3 type_1 and 2 type_2 (6 = 2 * 3 = 3 * 2) 
    # (n * ... * (n - k - 1) ) / k! -> ( (n + 1) * .. * (n - k - 1) / (k + 3)! ) 

        if (previous_c * (n + 1) * (n - k) * (n - k - 1) % ((k + 1) * (k + 2) * (k + 3)) != 0):
            print("ERROR")
        new_koef = previous_c * (n + 1) * (n - k) * (n - k - 1) // (k + 1) // (k + 2) // (k + 3)
        previous_c = (new_koef) % simple_modulo
        # print(previous_c, "n and k: ", n + 1, k + 3)
        curr_answer = (curr_answer + previous_c) % simple_modulo
        # n = type1_count + type2_count
        # k = type1_count
        # type2_count -= 2
        # type1_count += 3
        n += 1
        k += 3
        
    print(curr_answer)
        
    
# for i in answer: #######18!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     print(i % simple_modulo)