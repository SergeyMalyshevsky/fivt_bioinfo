def find_minimizing_skew(genome):
    FIRST_LETTER = 'C'
    SECOND_LETTER = 'G'

    result = []
    skew = []
    position = 0

    for i in genome:
        if i == FIRST_LETTER:
            position += -1
        elif i == SECOND_LETTER:
            position += 1
        skew.append(position)

    minimum = min(skew)

    for i in range(len(skew)):
        if skew[i] == minimum:
            result.append(i + 1)
    return result


class Executor:
    @staticmethod
    def _read_input_file(filename):
        with open(filename) as f:
            data = f.read()

        input_list = data.split()

        input_data = []
        for element in input_list:
            if element.lower() == 'input':
                continue
            elif element.lower() == 'output':
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


if __name__ == '__main__':
    Executor.execute(find_minimizing_skew, 'minimum_skew.txt')
