def print_operation_table(operation, num_rows = 6, num_columns = 6):
    for i in range(num_columns):
        str = ""
        for j in range(num_rows):
            str += f"{operation(i+1, j+1)}\t"
        print(str)

print_operation_table(lambda x, y: x * y)