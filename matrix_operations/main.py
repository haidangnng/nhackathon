import enum
import numpy as np

operation_lookup = {
    "+": lambda x, y: np.add(x, y),
    "*": lambda x, y: np.matmul(x, y),
}

precendence_lookup = {
    "*": 1,
    "+": 0,
}

with open("./input.txt", "r") as f:
    input = f.readlines()


def parse_line_number(string):
    line_array = []
    nums = string.split()
    for element in range(0, len(nums)):
        line_array.append(int(nums[element]))

    return line_array


# Not expecting any parentheses soooooo let's simplify this
# with just addition and multiplication
def simplify_shunting_yard(line_array):
    stack, queue = [], []
    for index, element in enumerate(line_array):
        if element.isalpha():
            queue.append(element)
        else:
            if (
                len(stack) > 0
                and precendence_lookup[stack[len(stack) - 1]]
                > precendence_lookup[element]
            ):
                last_stack = stack.pop()
                queue.append(last_stack)
            stack.append(element)
        if index == len(line_array) - 1 and len(stack) > 0:
            for i in range(len(stack) - 1, -1, -1):
                queue.append(stack[i])

    return queue


def execute_operation(matrices, operation):
    stack = []
    post_fix = simplify_shunting_yard(operation.split())
    for element in post_fix:
        if element.isalpha():
            stack.append(matrices.get(element))
        else:
            second = stack.pop()
            first = stack.pop()
            result = operation_lookup[element](first, second)
            stack.append(result)
    print(operation)
    for i in stack[0]:
        print(" ".join(str(x) for x in i.tolist()))
    print()
    return


def get_parameters(file_input):
    matrices = {}
    line_index = 0
    current_matrix = ""
    tmp = []
    initializing = True

    while line_index < len(file_input):
        cur_line = file_input[line_index].strip()
        if not cur_line and current_matrix != "":
            matrices[current_matrix] = np.array(tmp)
            current_matrix = ""
            tmp = []
        if cur_line:
            # break initializing parts
            if cur_line == "operations":
                initializing = False
                line_index += 1
                continue
            if cur_line == "matrices":
                line_index += 1
                continue
            if not initializing:
                execute_operation(matrices, cur_line)
                line_index += 1
                continue

            # initializing matrices
            if cur_line.isalpha():
                current_matrix = cur_line
                line_index += 1
                continue
            if current_matrix:
                current_dimensions = parse_line_number(cur_line)
                tmp.append(current_dimensions)

        else:
            current_matrix = ""
        line_index += 1

    print("Initializing done")


get_parameters(input)
