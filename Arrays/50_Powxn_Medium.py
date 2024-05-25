class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        The O(n) solution is giving Time Limit Exceeded
        """
        # prod=1.0
        # if n<0:
        #     prod=1
        #     j=n*-1
        #     for i in range(j):
        #         prod*=1/x
        # else:
        #     for i in range(n):
        #         prod*=x
        # return prod
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        current_product = x
        while n > 0:
            if n % 2 == 1: 
                result *= current_product
            current_product *= current_product 
            n //= 2 
        return result

def main():
    x=float(input('Enter the value of x: '))
    n=int(input('Enter the value of n: '))
    sol=Solution()
    result=sol.myPow(x, n)
    print(result)

if __name__=="__main__":
    main()