ELEMENTS = ["A", "C", "G", "T"]


def hamming_distance(str1, str2):
    counter = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            counter += 1
    return counter


def get_neighbors(pattern, d):
    neighbor = []

    if d == 0:
        return pattern

    if len(pattern) == 1:
        return ELEMENTS

    suffix = get_neighbors(pattern[1:], d)
    for text in suffix:
        if hamming_distance(pattern[1:], text) < d:
            for element in ELEMENTS:
                neighbor.append(element + text)
        else:
            neighbor.append(pattern[0] + text)
    return neighbor


def get_words(genome, k):
    words = []
    for start in range(len(genome) - k + 1):
        end = start + k
        words.append(genome[start:end])
    return words


def get_neighborhood(words, d):
    neighborhood = set()
    for word in words:
        neighborhood.update(set(get_neighbors(word, d)))
    return neighborhood


def find_frequent(genome, k, d):
    result = []
    max = 0

    words = get_words(genome, k)
    neighborhood = get_neighborhood(words, d)

    for neighbor in neighborhood:
        frequent = 0
        for word in words:
            if hamming_distance(neighbor, word) <= d:
                frequent += 1

        if max < frequent:
            max = frequent
            result = [neighbor]
        elif max == frequent:
            result.append(neighbor)
    return result


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


if __name__ == '__main__':
    Executor.execute(find_frequent, 'frequent_words_mismatch.txt')
