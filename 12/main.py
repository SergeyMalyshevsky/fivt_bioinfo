from itertools import product


def k_universal_string_problem(*var):
    k = var[0]

    k_mers = []
    s = []
    path = []

    universe = ["0", "1"]
    k_mers = ["".join(el) for el in product(universe, repeat=k)]
    patterns = sorted(k_mers)

    for pattern in patterns:
        pattern_len = len(pattern)
        k_mers += suffix_compose(pattern_len, pattern)
    k_mers = set(k_mers)
    k_mers_dict = {}
    for k_mer in k_mers:
        k_mers_dict[k_mer] = []
    for pattern in patterns:
        k_mers_dict[pattern[0:-1]].append(pattern[1:])

    rand_v = sorted(k_mers_dict.keys())[0]
    s.append(rand_v)
    while s:
        x = s[-1]
        try:
            y = k_mers_dict[x][0]
            s.append(y)
            k_mers_dict[x].remove(y)
        except:
            path.append(s.pop())

    c = path[::-1]
    c = c[:-(k - 1)]
    genome = c[0][:-1]
    for element in c:
        genome += element[-1]
    return genome


def suffix_compose(k, words):
    k_mers = []
    for element in range(len(words) + 1 - k):
        k_mers.append(words[element:element + k - 1])
    return sorted(list(k_mers))


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
        else:
            print(result)


if __name__ == "__main__":
    Executor.execute(k_universal_string_problem, 'universal_string.txt')
