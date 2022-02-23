def ternary(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    if n == 2:
        return '2'
    nums = []
    while n:
        r = n % 3
        n //= 3
        nums.append(str(r))
    return ''.join(reversed(nums))
