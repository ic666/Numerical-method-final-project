#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

def gauss_seidel(a, b):   
    #a為初始矩陣 b為對應解矩陣  
    m, n = a.shape
    #x矩陣為各xi之對應矩陣
    x = np.zeros(m)
    x = x.astype(float)
    times = 0          
    #times計算蝶帶次數
    print("Iteration results") 
    print("k,\tx1,\tx2,\tx3 ") 
    condition = True
    while condition:  #condition=>等進入error容許範圍再跳出
        error = 0
        print(times+1,end='\t') 
        for i in range(n):
            x_temp = x[i] #取x_temp計算誤差
            sum_left = (a[i,:i]*x[:i]).sum()  #該變數值左邊和
            sum_right = (a[i,i+1:]*x[i+1:]).sum()  #該變數值右邊和
            x[i] = 1/a[i,i]*(b[i]-sum_left-sum_right) #iteration計算
            error += abs(x[i] - x_temp)  #計算error
            print("%.4f"%(x[i]),end='\t') #print x1,x2,x3
        print("\n")
        times+=1
        condition =  error > 0.0001  #error=0.0001
    print("Converged!")


# In[9]:


a = np.array([[8, 4, -3], [-2, -8, 5], [3, 5, 10]])
y = np.array([14, 5, -8])
gauss_seidel(a, y)


# In[10]:


a = np.array([[12, 3, -5], [1, 5, 3], [3, 7, 13]])
y = np.array([10, 6, 3])
gauss_seidel(a, y)


# In[ ]:




