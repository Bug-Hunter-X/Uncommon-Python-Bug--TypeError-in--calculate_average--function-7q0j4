def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    return total / len(numbers)

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"Average: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"Average of empty list: {average_empty}")

my_list_with_strings = [10, 20, "thirty", 40, 50]
average_mixed = calculate_average(my_list_with_strings)