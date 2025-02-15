# Create a function that receives three parameters
# and calculates a result depending on operator.
# The operator can be  'multiply', 'divide', 'add', 'subtract'.
# The input comes as three parameters – two integers and an operator as a string.

def calculation_with_operator(num_1, num_2, operator):
    result = None
    if operator == 'multiply':
        result = num_1 * num_2
    elif operator == 'divide':
        result = int(num_1 / num_2)
    elif operator == 'add':
        result = num_1 + num_2
    elif operator == 'subtract':
        result = num_1 - num_2
    return result


operator_data = input()
a = int(input())
b = int(input())

res = calculation_with_operator(a, b, operator_data)
print(res)
