# def toString(List): 
#     return ''.join(List) 
  
# # Function to print permutations of string 
# # This function takes three parameters: 
# # 1. String 
# # 2. Starting index of the string 
# # 3. Ending index of the string. 
# def permute(a, l, r): 
#     if l==r: 
#         print toString(a) 
#     else: 
#         for i in xrange(l,r+1): 
#             a[l], a[i] = a[i], a[l] 
#             print('a', a)
#             permute(a, l+1, r)
#             print('backtrack', 'l', l, 'i', i, 'r', r) 
#             a[l], a[i] = a[i], a[l] # backtrack 

class Solution: 
    
    def __init__(self, answers):
        self.answers = answers

    def printAnswer(self):
        for answer in self.answers:
            print(answer)

    def permute(self,a,l,r):
        
        if l==r:
            self.answers.append(a.copy())
        else:
            for i in range(l, r+1):
                a[l], a[i] = a[i], a[l]
                print(a)
                self.permute(a, l+1, r)
                a[l], a[i] = a[i], a[l]


# Driver program to test the above function 
answers = []
string = "ABC"
sol = Solution(answers)
n = len(string) 
a = list(string) 
sol.permute(a, 0, n-1)


