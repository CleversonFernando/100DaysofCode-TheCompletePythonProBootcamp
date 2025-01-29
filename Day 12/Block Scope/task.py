def is_prime(num):
    item = num
    count = 0
    for _ in range(num):
        if num % item == 0 and num != 1:
            count += 1
        item -= 1
    if count == 2:
        return True
    else:
        return False


continueTrue = True
while continueTrue:
    num = int(input("Type:"))
    is_prime(num)
