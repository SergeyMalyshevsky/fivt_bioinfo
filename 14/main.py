def generate_contigs(*var):
    patterns = var[0:]

    k_mers = []
    contigs = []
    degrees = {}

    for pattern in patterns:
        pattern_len = len(pattern)
        k_mers += suffix_compose(pattern_len, pattern)
    k_mers = set(k_mers)
    k_mers_dict = {}
    for k_mer in k_mers:
        k_mers_dict[k_mer] = []
    for pattern in patterns:
        k_mers_dict[pattern[0:-1]].append(pattern[1:])

    for k_mer in k_mers_dict.keys():
        neighbors = k_mers_dict[k_mer]
        out_degree = len(neighbors)

        if k_mer in degrees:
            degrees[k_mer][1] = out_degree
        else:
            degrees[k_mer] = [0, out_degree]

        for neighbor in neighbors:
            if neighbor in degrees:
                degrees[neighbor][0] += 1
            else:
                degrees[neighbor] = [1, 0]

    for k_mers_i in k_mers_dict.keys():
        if degrees[k_mers_i] == [1, 1]:
            continue
        for k_mers_j in k_mers_dict[k_mers_i]:
            contig = k_mers_i
            while True:
                contig += k_mers_j[-1]
                w_degree = degrees[k_mers_j]
                if w_degree != [1, 1]:
                    break
                else:
                    k_mers_j = k_mers_dict[k_mers_j][0]
            contigs.append(contig)
    result = sorted(contigs)

    return result


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
            for element in result:
                print(element)
        elif isinstance(result, int):
            print(result)
        else:
            print(result)


if __name__ == "__main__":
    Executor.execute(generate_contigs, 'contig_generation.txt')
