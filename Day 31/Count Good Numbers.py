https://my.newtonschool.co/playground/code/edryjggxevnb


def countGoodNumbers(n):
    MOD = 10**9+7	
    if n%2==0:
        ne=n//2
    else:
        ne=(n+1)//2
    no=n//2
    
    te = pow(5,ne,MOD)      #Total number of even places combinations.
    tp = pow(4,no,MOD)      #Total number of odd/prime combinations.
    return (tp*te)%MOD
