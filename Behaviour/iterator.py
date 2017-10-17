items = [1, 2, 3]
iterator = items.__iter__()
print(iterator.__next__())
print(iterator.__next__())

numbers = [1, 2, 3, 4, 5]
numbers_again = [n for n in numbers]
print(numbers_again)
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
odd_squares = [n**2 for n in numbers if n % 2 == 1]
print(odd_squares)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]
print(flat)
