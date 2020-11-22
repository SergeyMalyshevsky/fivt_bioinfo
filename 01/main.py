import itertools
from collections import Counter


def frequent(genome, k):
    words = []

    for start in range(len(genome) - k + 1):
        end = start + k
        word = "".join(genome[start:end])
        words.append(word)

    return Counter(words).most_common()


def clump_finding(genome, k, L, t):
    words = []

    for start in range(len(genome) - L + 1):
        end = start + L
        strings = genome[start:end]
        words.append(frequent(strings, k))

    pattern = list(itertools.chain(*words))
    result = set(x[0] for x in pattern if x[1] >= t)
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
    Executor.execute(clump_finding, 'clump_finding.txt')
