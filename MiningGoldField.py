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


T = int(input()) # test count
# answer = []
N = 1

for i in range(T):
    N = int(input())
    # N += 1
    curr_answer = 0
    
    if N < 2:
        print(0)
        break #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! breaks for
    
    if N % 2 == 0: # only 1 type
        type1_count = N // 2
        type2_count = 0
        previous_c = 1
    
    else:
        type1_count = (N - 3) // 2
        type2_count = 1
        previous_c = type1_count + 1
        
    print("type1 ", previous_c)
    n = type1_count + type2_count
    k = type2_count
    curr_answer += previous_c % simple_modulo
    # type2_count += 2
    # type1_count -= 3
    
        
    while n - k - 3 >= k + 2: # type1_count >= type2_count: # replace 3 type_1 and 2 type_2 (6 = 2 * 3 = 3 * 2)
    # (n * ... * (n - k - 1) ) / k! -> (n - 1) * .. * (n - k - 2) // (k + 2)!
        # print (n - k , k)
        # print (previous_c, (n - k), (n - k - 1), (n - k - 2), "//", n , (k + 1) , (k + 2))
        new_koef = previous_c * (n - k) * (n - k - 1) * (n - k - 2) // n // (k + 1) // (k + 2)
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
        
x = input()        

for i in range(T):
    N = int(input())
    curr_answer = 0
    
    if N < 2:
        print(0)
        break
    
    if N % 2 == 0: # only 1 type
        type1_count = N // 2
        type2_count = 0
    
    else:
        type1_count = (N - 3) // 2
        type2_count = 1
        
    while type1_count >= 0: # replace 3 type_1 and 2 type_2 (6 = 2 * 3 = 3 * 2)
        # curr_answer += C(type1_count + type2_count, type1_count) # ways to arrange C(n, k)
        numerator, denominator = C_modulo(type1_count + type2_count, type1_count)        
        print( numerator, denominator)
        # print("n , d ", numerator, denominator)
        factor_numerator = Factor(numerator)
        factor_denominator = Factor(denominator)
        print(factor_numerator, factor_denominator)
        for key in factor_numerator.keys():
            while factor_numerator[key] > 0:
                try:
                    if factor_denominator[key] > 0:
                        factor_denominator[key] -= 1
                        factor_numerator[key]   -= 1
                    else:
                        break
                    
                except KeyError:
                    break
                
        print(factor_numerator, factor_denominator)
        numerator, denominator = Get_number_from_factor(factor_numerator), Get_number_from_factor(factor_denominator)
        while numerator % denominator != 0:
            numerator += simple_modulo
        print("x")
            
        if numerator % denominator == simple_modulo:
            numerator = 0
            
        curr_answer += numerator // denominator
        # print(curr_answer, "!!!!")
        type2_count += 2
        type1_count -= 3
        
    print(curr_answer % simple_modulo)
    
# for i in answer: #######18!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#     print(i % simple_modulo)