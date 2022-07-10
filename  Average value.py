 # Python program to find the average of ten numbers

# denotes total sum of ten numbers
total_sum = 0

for n in range (10):
    # take inputs
    num = float(input('Enter number: '))
    # calculate total sum of numbers
    total_sum += num

# calculate average of numbers
avg = total_sum / 10

# print average value
print('Average of numbers = %0.2f' %avg)