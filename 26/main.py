def greedy_sort(input_array):
    permutations = []
    distance = 0
    start = 1
    end = len(input_array) + 1

    for element in range(start, end):
        if input_array[element - 1] != element:
            if input_array[element - 1] != -element:
                index = 0
                if element in input_array:
                    index = input_array.index(element)
                elif -element in input_array:
                    index = input_array.index(-element)
                t = input_array[element - 1:index + 1]
                t = [-k for k in t]
                input_array[element - 1:index + 1] = t[::-1]
                permutations.append(input_array[:])
                distance += 1
            if input_array[element - 1] == -element:
                input_array[element - 1] = element
                permutations.append(input_array[:])
                distance += 1
    return permutations


class Executor:
    @staticmethod
    def _read_input_file(filename):
        with open(filename) as f:
            data = f.read()

        input_list = data.split()

        input_data = []
        for element in input_list:
            if 'input' in element.lower():
                continue
            elif 'output' in element.lower():
                break
            else:
                input_data.append(element)

        return input_data

    @staticmethod
    def execute(func, filename):
        input_data = Executor._read_input_file(filename)

        converted_input_data = []
        for element in input_data:
            if element.isdigit():
                converted_input_data.append(int(element))
            else:
                converted_input_data.append(element)

        result = func(*converted_input_data)
        print(*result)

    @staticmethod
    def print_result(func, filename):
        with open(filename) as f:
            lines = f.readlines()

        for line in lines:
            if 'input' in line.lower():
                continue
            elif 'output' in line.lower():
                break
            input_array = line.replace("(", "").replace(")", "").split()
            input_data = [int(element) for element in input_array]

        permutations = func(input_data)

        for permutation in permutations:
            str_array = ['+' + str(number) if number > 0 else str(number) for number in permutation]
            arr = ' '.join(str_array)
            print(f'({arr})')


if __name__ == '__main__':
    Executor.print_result(greedy_sort, 'GreedySorting.txt')
