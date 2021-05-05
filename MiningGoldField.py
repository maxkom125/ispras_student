 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 2021

@author: maksym
"""
simple_modulo = 1000000007
import numpy as np

def print_A(step): #step % 3 == 0 must be True!
    if step % 3 != 0:
        print ("Wrong step. step % 3 == 0 must be True!")
        return
    
    N = step + 10
    a = 1
    b = 2
    c = 1
    curr_N = N - 4

    ka = np.array([1, 0, 0])
    kb = np.array([0, 1, 0])
    kc = np.array([0, 0, 1])
    iteration = 0
    while curr_N >= 7:
        iteration += 1
            
        new_a = (a + b) % simple_modulo
        new_b = (a + b + c) % simple_modulo
        new_c = (a + c) % simple_modulo
        a, b, c = new_a, new_b, new_c
        ka, kb, kc = (ka + kb) % simple_modulo, (ka + kb + kc) % simple_modulo, (ka + kc) % simple_modulo
        if N - curr_N > step:
            print(ka % simple_modulo, kb % simple_modulo, kc % simple_modulo, "iteration: ", iteration)
        curr_N -= 3
    return

      
def Ans(N): # a Ans(n) + b Ans(n - 1) + c Ans(n - 2) =
            # (a + b) Ans(n - 3) + (a + b + c) Ans(n - 4) + (a + c) Ans(n - 5) =
            # A * vector(Ans(k), Ans(k - 1), Ans(k - 2))
    if N <= 1:
        return 0
    elif N <= 4:
        return 1
    elif N <= 6:
        return 2
    elif N == 7:
        return 3
    
    curr_N = N - 4

    new_koef = np.array([1, 2, 1]).reshape(3, 1)
    # print(new_koef)
    array_A = [ 
        np.array([[305366937, 181258272, 180539332],
                  [361797604, 305366937, 181258272],
                  [181258272, 180539332, 124827605]]), # 3 000 000 шагов, N -= 9 * 10**6 + 4
        
        np.array([[202085592, 571086465,  46766784],
                  [617853249, 202085592, 571086465],
                  [571086465,  46766784, 155318808]]), # 100 000 шагов, N -= 300 000 + 4
        
        np.array([[990385432, 461556644, 205524447],
                  [667081091, 990385432, 461556644],
                  [461556644, 205524447, 784860985]]), # 1000 шагов, N -= 3000 + 4
               
        np.array([[8745217,  6601569, 4983377], 
                  [11584946, 8745217, 6601569], 
                  [6601569,  4983377, 3761840]]), # 20 шагов, N -= 60 + 4
        
               np.array([[1, 1, 0],
                         [1, 1, 1],
                         [1, 0, 1]]) # 1 шаг, N -= 3 + 4
               ]
    i = 0
    steps = [9 * (10**6), 3 * (10**5), 3000, 60, 3] # steps from max to min
    # steps.reverse()
    for step in steps:
        A = array_A[i]
        i += 1
        while curr_N >= step + 4: # if can do step with curr size
            new_koef = np.dot(A, new_koef) % simple_modulo
            curr_N -= step
        
    if curr_N == 4:       
        return np.sum(new_koef) % simple_modulo
    elif curr_N == 5:
        return (np.sum(new_koef) + new_koef[0][0] % simple_modulo) # 2 * a + b + c
    elif curr_N == 6:
        return (np.sum(new_koef) + new_koef[0][0] + new_koef[1][0]) % simple_modulo # 2 * a + 2 * b + c
    
T = int(input()) # test count
N = 1

# print_A(300000)

for i in range(T):
    N = int(input())
    print (Ans(N) % simple_modulo)
    