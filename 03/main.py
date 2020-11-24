def get_starting_positions(pattern, genome, max_error):
    positions = []
    k = len(pattern)
    for start in range(len(genome) - k + 1):
        end = start + k
        word = "".join(genome[start:end])
        if get_position(word, pattern, max_error):
            positions.append(start)
    return positions


def get_position(word, pattern, max_error):
    count = 0
    if (len(word) != len(pattern)):
        return False
    else:
        for i in range(len(word)):
            if (word[i] != pattern[i]):
                count += 1
            if count > max_error:
                return False
    return True


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
    Executor.execute(get_starting_positions, 'approximate_match.txt')
