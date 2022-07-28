'''
Given a string s, the task is to check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 

Example 1:

Input: s = "ababab"
Output: 1
Explanation: It is contructed by 
appending "ab" 3 times 

Example 2:

Input: s = "ababac"
Output: 0
Explanation: Not possible to construct
'''

def isRepeat(s):
    print (len(s)//2+1)
    for i in range(1,len(s)//2+1):
        if(len(s)%i!=0):
            continue
        if(s[:1]*(len(s)//i)==s):
            return "possible"
        return "not possible"
		    

s= "ababac"
print(isRepeat(s))
