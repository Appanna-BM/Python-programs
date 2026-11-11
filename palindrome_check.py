def plaindrome_check(nums):
    if nums<0 or nums%10==0:
        return False
    if int(str(nums)[::-1]):
        return True
    else:
        return False
r=plaindrome_check(1)
print(r)