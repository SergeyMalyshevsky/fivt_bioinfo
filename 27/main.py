def get_number_of_breakpoints(p):
    a = 0
    start = 0
    end = len(p) - 1

    for element in range(start, end):
        if p[element + 1] == p[element] + 1:
            a += 1

    if p[0] == 1:
        a += 1

    if p[-1] == len(p):
        a += 1

    number_of_breakpoints = len(p) + 1 - a
    return number_of_breakpoints


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

        number_of_breakpoints = func(input_data)
        print(number_of_breakpoints)


if __name__ == '__main__':
    Executor.print_result(get_number_of_breakpoints, 'rosalind_ba6b.txt')
