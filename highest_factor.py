"""
Greatest commond divisor program
"""


class solution:

    def gcd(self, m, n):

        fm = []
        for i in range(1, m+1):
            if (m%i) == 0:
                fm.append(i)

        fn = []
        for j in range(1, n+1):
            if (n % j) ==0:
                fn.append(j)

        print(fm)
        print(fn)
        cf = []
        for f in fm:
            if f in fn:
                cf.append(f)

        print(cf)

        return (cf[-1])
    
    def gcd_optimized(self, m,n):

        cf  = []
        for i in range(1, min(m,n)+1):
            if m%i==0 and n%i==0:
                cf.append(i)
        return (cf[-1])
    
    def more_opt_gcd(self, m, n):

        for i in range(1, min(m, n)):
            if m%i ==0 and n%i==0:
                mrcf = i        #mcrf = most recent common factor
        return mrcf

    def scan_back(self, m, n):

        i = min(m,n)
        while i>0:
            if m%i ==0 and n%i ==0:
                return(i)
            else:
                i = i - 1

if __name__ == "__main__":

    solution = solution()
    common_factor = solution.gcd(10,15)
    common_factor_opt = solution.gcd_optimized(10, 15)
    most_recent = solution.more_opt_gcd(10, 15)
    backwards = solution.scan_back(10, 15)
    print(backwards)
