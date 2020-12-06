def distance_between_pattern_and_strings(*var):
    pattern = var[0]
    dna = var[1:]

    k = len(pattern)
    distance = 0
    for each in dna:
        ham_dist = float("inf")
        for element in range(len(each) - k + 1):
            if ham_dist > hamming_distance(pattern, each[element:element + k]):
                ham_dist = hamming_distance(pattern, each[element:element + k])
        distance += ham_dist
    return distance


def hamming_distance(word_1, word_2):
    count = 0
    for letter_1, letter_2 in zip(word_1, word_2):
        if letter_1 != letter_2:
            count += 1
    return count


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

        if isinstance(result, list):
            print(*result)
        elif isinstance(result, int):
            print(result)


if __name__ == '__main__':
    Executor.execute(distance_between_pattern_and_strings, 'distance_between_pattern_and_strings.txt')
