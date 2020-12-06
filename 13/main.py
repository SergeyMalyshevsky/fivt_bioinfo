def string_reconstruction_from_read_pairs_problem(*var):
    patterns = var[2:]

    k_mers_dict = {}
    s = []
    path = []
    genome = ''

    pairs = list(patterns)

    for pair in pairs:
        pair = pair.split('|')

        suffix = pair[0][:-1], pair[1][:-1]
        prefix = pair[0][1:], pair[1][1:]

        if prefix in k_mers_dict.keys():
            k_mers_dict[prefix].append(suffix)
        else:
            k_mers_dict[prefix] = [suffix]

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

    for k_mer in path[::-1]:
        genome += k_mer[0]

    return genome


def genome_path_problem(kmers):
    genome = ''
    for kmer in kmers:
        genome += kmer[0]
    return genome


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
    Executor.execute(string_reconstruction_from_read_pairs_problem, 'string_reconstruction_from_read_pairs.txt')
