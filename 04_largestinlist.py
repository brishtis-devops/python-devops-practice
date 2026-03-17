#Program to find the largest number in a list

#Define a list
numbers = [10, 45, 23, 67, 12, 89,34]

#Assue first number is the largest
largest = numbers[0]

#Loop though the list
for num in numbers:
    if num > largest:
        largest = num
print("The largest number is:", largest)

#Alternate
print("The largest number in the list is:", max(numbers))
