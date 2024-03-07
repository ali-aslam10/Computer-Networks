#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.patches as pat
def TwoB1Q(bitstring):
    li=list(bitstring)
    result=[]
    length=len(li)
    i=0
    while i<length:
        if(li[i]=='0' and li[i+1]=='0'):
            result.append(-3)
            i+=2
        elif(li[i]=='0' and li[i+1]=='1'):
            result.append(-1)
            i+=2
        elif(li[i]=='1' and li[i+1]=='0'):
            result.append(3)
            i+=2
        elif(li[i]=='1' and li[i+1]=='1'):
            result.append(1)
            i+=2
    result.insert(0,result[0])    
    return result
def plot_2B1Q(bitstring):
    plt.plot(TwoB1Q(bitstring),drawstyle='steps-pre',marker='o')
    plt.xticks([])
    plt.title("2B1Q")
    plt.xlabel("Time")
    info=pat.Patch(label='00--->-3\n01--->-1\n10--->+3\n11--->+1')
    plt.legend(handles=[info],title="Rules")
    plt.show()
    
def AMI(bitstring):
    li=list(bitstring)
    result=[]
    length=len(li)
    upper=False  #True will indicate last 1 binary represented by +1
    i=0
    while i<length:
        if(li[i]=='0'):
            result.append(0)
            i+=1
        else:
            if(not upper):
                result.append(1)
                i+=1
                upper=True
            else:
                result.append(-1)
                i+=1
                upper=False
    result.insert(0,result[0])
    return result
def plot_AMI(bitstring):
    plt.plot(AMI(bitstring),drawstyle='steps-pre',marker='o')
    plt.xticks([])
    plt.title("AMI")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    info=pat.Patch(label='1--->Alternate +ve & -ve\n0--->0')
    plt.legend(handles=[info],title="Rules")
    plt.show()
    
def pseudoternary(bitstring):
    li=list(bitstring)
    result=[]
    length=len(li)
    upper=False  #True will indicate last 0 binary represented by +1
    i=0
    while i<length:
        if(li[i]=='1'):
            result.append(0)
            i+=1
        else:
            if(not upper):
                result.append(1)
                i+=1
                upper=True
            else:
                result.append(-1)
                i+=1
                upper=False
    result.insert(0,result[0])
    return result
def plot_pseudoternary(bitstring):
    plt.plot(pseudoternary(bitstring),drawstyle='steps-pre',marker='o')
    plt.xticks([])
    plt.title("Pseudoternary")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    info=pat.Patch(label='0--->Alternate +ve & -ve\n1--->0')
    plt.legend(handles=[info],title="Rules")
    plt.show()
    
def Manchester(bitstring):
    li=list(bitstring)
    result=[]
    length=len(li) 
    i=0
    while i<length:
        if(li[i]=='1'):
            result.append(-1)
            result.append(1)
            i+=1
        else:
            result.append(1)
            result.append(-1)
            i+=1
               
    result.insert(0,result[0])
    return result
def plot_Manchester(bitstring):
    plt.plot(Manchester(bitstring),drawstyle='steps-pre',marker='o')
    plt.xticks([])
    plt.title("Manchester")
    plt.xlabel("Time")
    plt.show()
    
def Differential_Manchester(bitstring):
    li=list(bitstring)
    result=[]
    length=len(li)
    upper=False  #True will indicate last signal end on +1.It help to present next signal
    i=0
    while i<length:
        if(li[i]=='1'):
            if(not result):  #if list empty, it is first signal
                result.append(1)
                result.append(-1)
                i+=1
            else:
                if(upper):    #if end on upper means start from lower.As it is 1 binary so now it should  start from upper
                    result.append(1)
                    result.append(-1)
                    i+=1
                    upper=False
                else:
                    result.append(-1)
                    result.append(1)
                    i+=1
                    upper=True
        else:
            if(not result):  #if list empty, it is first signal
                result.append(-1)
                result.append(1)
                i+=1
                upper=True
            else:
                if(upper):     #if end on upper means start from lower.As it is 0 binary so it should also start from lower
                    result.append(-1)
                    result.append(1)
                    i+=1
                else:
                    result.append(1)
                    result.append(-1)
                    i+=1
    result.insert(0,result[0])
    return result
def plot_Differential_Manchester(bitstring):
    plt.plot(Differential_Manchester(bitstring),drawstyle='steps-pre',marker='o')
    plt.xticks([])
    plt.title("Differential Manchester")
    plt.xlabel("Time")
    plt.show()
    
def NRZ_I(bitstring):
    li=list(bitstring)
    result=[]
    length=len(li)
    upper=False  #True will indicate last signal end on +1.It will help to present next signal
    i=0
    while i<length:
        if(li[i]=='1'):
            if(not result):  #if list empty, it is first signal
                result.append(1)
                i+=1
            else:
                if(upper):    #if last signal represent on  upper side.As it is 1 binary so now it should  represent by -1
                    result.append(-1)
                    i+=1
                    upper=False
                else:
                    result.append(1)
                    i+=1
                    upper=True
        else:
            if(not result):  #if list empty, it is first signal
                result.append(1)
                i+=1
                upper=True
            else:
                if(upper):     #if last signal represent on  upper side.As it is 0 binary so now it should  represent by 1
                    result.append(1)
                    i+=1
                else:
                    result.append(-1)
                    i+=1
    result.insert(0,result[0])
    return result
def plot_NRZ_I(bitstring):
    plt.plot(NRZ_I(bitstring),drawstyle='steps-pre',marker='o')
    plt.xticks([])
    plt.title("NRZ-I")
    plt.xlabel("Time")
    info=pat.Patch(label='0--->No Change\n1--->Change')
    plt.legend(handles=[info],title="Rules")
    plt.show()
    
def NRZ_L(bitstring):
    li=list(bitstring)
    result=[]
    length=len(li)
    i=0
    while i<length:
        if(li[i]=='1'):
            result.append(-1)
            i+=1
        else:
            result.append(1)
            i+=1
    result.insert(0,result[0])
    return result
def plot_NRZ_L(bitstring):
    plt.plot(NRZ_L(bitstring),drawstyle='steps-pre',marker='o')
    plt.xticks([])
    plt.title("NRZ-L")
    plt.xlabel("Time")
    info=pat.Patch(label='0--->+1\n1--->-1')
    plt.legend(handles=[info],title="Rules")
    plt.show()
    
def NRZ(bitstring):
    li=list(bitstring)
    result=[]
    length=len(li)
    i=0
    while i<length:
        if(li[i]=='1'):
            result.append(1)
            i+=1
        else:
            result.append(0)
            i+=1
    result.insert(0,result[0])
    return result
def plot_NRZ(bitstring):
    plt.plot(NRZ(bitstring),drawstyle='steps-pre',marker='o')
    plt.xticks([])
    plt.title("NRZ")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    info=pat.Patch(label='0--->0\n1--->1')
    plt.legend(handles=[info],title="Rules")
    plt.show()

    

#Main

while(True):
    binary_string=input("Enter Binary String:")
    while(not all(binary in '01' for binary in binary_string)):
        print("Invalid binary string! Try again.")
        binary_string=input("Enter Binary String:")
    print("Select Line Coding Scheme:\n1.NRZ\n2.NRZ-L\n3.NRZ-I\n4.Manchester\n5.Differential Manchester\n6.AMI\n7.Pseudoternary\n8.2B1Q")
    choice=int(input("Choice:"))
    while(choice<1 or choice>8):
        print("Invalid Choice! Try Again.")
        choice=int(input("Choice:"))
    if(choice==1):
        plot_NRZ(binary_string)
    elif(choice==2):
        plot_NRZ_L(binary_string)
    elif(choice==3):
        plot_NRZ_I(binary_string)
    elif(choice==4):
        plot_Manchester(binary_string)
    elif(choice==5):
        plot_Differential_Manchester(binary_string)
    elif(choice==6):
        plot_AMI(binary_string)
    elif(choice==7):
        plot_pseudoternary(binary_string)
    else:
        plot_2B1Q(binary_string)


    print("Select option:\n1.Continue\n2.Exit")
    choice=int(input("Choice:"))
    while(choice<1 or choice>2):
        print("Invalid Choice! Try Again.")
        choice=int(input("Choice:"))
    if(choice==2):
        break
    
    
    


# In[ ]:




