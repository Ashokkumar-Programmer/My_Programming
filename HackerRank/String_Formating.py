def print_formatted(number):
    for i in range(1, number + 1):
            width = len(f"{number:b}")
            print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")
n = int(input())
print_formatted(n)