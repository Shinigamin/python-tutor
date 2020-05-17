

even = []
for num in range(15):
    if num % 2 == 0:
        even.append(num)



even = [num for num in range(15) if num % 2 == 0] # list
even = (num for num in range(15) if num % 2 == 0) # gen
even = {num: num for num in range(15) if num % 2 == 0} # dict
even = {num for num in range(15) if num % 2 == 0} # set


print(even)