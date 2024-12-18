def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    return total / len(numeric_numbers)

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"Average: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"Average of empty list: {average_empty}")

my_list_with_strings = [10, 20, "thirty", 40, 50]
average_mixed = calculate_average(my_list_with_strings)
print(f"Average of mixed list: {average_mixed}")

my_list_with_none = [10, 20, None, 40, 50]
average_none = calculate_average(my_list_with_none)
print(f"Average of list with None: {average_none}") 