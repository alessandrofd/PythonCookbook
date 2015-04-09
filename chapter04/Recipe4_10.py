# Recipe 4.10. Iterating Over the Index-Value Pairs of a Sequence
#
# Problem: You want to iterate over a sequence, but would like to keep track of which element of the sequence is
#   currently being processed.
#
# Solution: The built-in enumerate() functions handles this quite nicely:

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# For printing output with canonical line numbers (where you typically start the numbering at 1 instead of 0), you can
# pass in a start argument:

print('\n### With start argument ###\n')

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):
    print(idx, val)

# This case is especially useful for tracking line numbers in files should you want a line number in an error message:

print("\n### Error message ###\n")

def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split
