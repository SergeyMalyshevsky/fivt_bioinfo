AMINOS = {'G': 57,
          'A': 71,
          'S': 87,
          'P': 97,
          'V': 99,
          'T': 101,
          'C': 103,
          'I': 113,
          'N': 114,
          'D': 115,
          'K': 128,
          'E': 129,
          'M': 131,
          'H': 137,
          'F': 147,
          'R': 156,
          'Y': 163,
          'W': 186
          }

mass = {}


def count_peptide(m):
    count = 0
    for element in AMINOS.keys():
        if (m - AMINOS[element]) in mass.keys():
            count += mass[(m - AMINOS[element])]
        elif m - AMINOS[element] < 0:
            break
        elif m - AMINOS[element] == 0:
            count += 1
            return count
        elif m - AMINOS[element] > 0:
            count += count_peptide(m - AMINOS[element])
    mass[m] = count
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
            for element in result:
                print(element)
        elif isinstance(result, int):
            print(result)
        else:
            print(result)


if __name__ == '__main__':
    Executor.execute(count_peptide, 'counting_peptides.txt')
