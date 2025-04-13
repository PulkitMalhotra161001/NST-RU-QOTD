https://my.newtonschool.co/playground/code/m89u6poqavwt


def removeOuterParentheses(S):
     
    res = ""
 
    count = 0
 
    for c in S:
         
        if (c == '(' and count > 0):
 
            res += c
 
        if (c == '('):
            count += 1
        if (c == ')' and count > 1):
 
            res += c
             
        if (c == ')'):
          count -= 1
     
    return res
 
if __name__ == '__main__':
     
    S = input()
     
    print(removeOuterParentheses(S))
