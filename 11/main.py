def string_reconstruction_problem(*var):
    patterns = var[1:]

    k_mers = []
    stack = []
    path = []
    genome = ''

    for pattern in patterns:
        pattern_len = len(pattern)
        k_mers += suffix_compose(pattern_len, pattern)
    k_mers = set(k_mers)
    k_mers_dict = {}
    for k_mer in k_mers:
        k_mers_dict[k_mer] = []
    for pattern in patterns:
        k_mers_dict[pattern[0:-1]].append(pattern[1:])

    st_list = [i for i, j in balance_count(k_mers_dict).items() if j == -1]
    stack.append(st_list[0])

    while stack:
        x = stack[-1]
        try:
            y = k_mers_dict[x][0]
            stack.append(y)
            k_mers_dict[x].remove(y)
        except:
            path.append(stack.pop())

    for k_mer in path[::-1]:
        genome += k_mer[0]
    genome += k_mer[1:]

    return genome


def suffix_compose(k, words):
    k_mers = []
    for element in range(len(words) + 1 - k):
        k_mers.append(words[element:element + k - 1])
    return sorted(list(k_mers))


def balance_count(adj_list):
    balanced_count = dict.fromkeys(adj_list.keys(), 0)
    for node in adj_list.keys():
        for out in adj_list[node]:
            balanced_count[node] -= 1
            try:
                balanced_count[out] += 1
            except:
                balanced_count[out] = 1
    return balanced_count


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
    Executor.execute(string_reconstruction_problem, 'StringReconstructionProblem.txt')
