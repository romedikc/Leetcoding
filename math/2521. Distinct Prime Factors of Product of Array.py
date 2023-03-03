from typing import List


def distinctPrimeFactors(nums: List[int]) -> int:
    def get_prime_factors(n):
        i = 2
        prime_factors = []
        while i * i <= n:
            if n % i == 0:
                prime_factors.append(i)
                n //= i
            else:
                i += 1

        if n > 1:
            prime_factors.append(n)

        return prime_factors

    pms = set()
    for i in nums:
        get_prime = get_prime_factors(i)
        for p in get_prime:
            pms.add(p)
    return len(pms)


nums = [2, 4, 3, 7, 10, 6]
print(distinctPrimeFactors(nums))
