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
        curr_answer += C(type1_count + type2_count, type1_count) # ways to arrange C(n, k)
        # print(curr_answer, "!!!!")
        type2_count += 2
        type1_count -= 3
        
    print(curr_answer % simple_modulo)
    
# for i in answer:
#     print(i % simple_modulo)