'''
Exercise 13: Fibonacci

Write a program that asks the user how many Fibonnaci numbers
to generate and then generates them. Take this opportunity to
think about how you can use functions. Make sure to ask the
user to enter the number of numbers in the sequence to
generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous
two numbers in the sequence. The sequence looks like this: 1, 1,
2, 3, 5, 8, 13, …)

'''

# Solution
'''
Exercise 13: Fibonacci

Write a program that asks the user how many Fibonnaci numbers
to generate and then generates them. Take this opportunity to
think about how you can use functions. Make sure to ask the
user to enter the number of numbers in the sequence to
generate.(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous
two numbers in the sequence. The sequence looks like this: 1, 1,
2, 3, 5, 8, 13, …)

'''

# Solution
input_number = input("How many numbers do you want to generate? ")
number_checked = 0
while number_checked == 0:
    try:
        input_number = int(input_number)
        number_checked = 1
    except:
        number_checked = 0
        print("Enter a valid Integer")
        input_number = input("How many numbers do you want to generate? ")
sequence = [1, 1]
for count in range(0, input_number - 2):
    sequence.append(sequence[count] + sequence[count+1])
print(sequence)


# Test Part
# How many Fibonnaci numbers do you want to generate?5
# [1, 1, 2, 3, 5]
# How many Fibonnaci numbers do you want to generate?10
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
