ELEMENTS = ["A", "C", "G", "T"]
COMPLEMENT_TABLE = {'A': 'T',
                    'T': 'A',
                    'C': 'G',
                    'G': 'C'}


def hamming_distance(word_1, word_2):
    count = 0
    for letter_1, letter_2 in zip(word_1, word_2):
        if letter_1 != letter_2:
            count += 1
    return count


def get_neighbors(pattern, d):
    neighbors = []

    if d == 0:
        return pattern

    if len(pattern) == 1:
        return ELEMENTS

    suffix = get_neighbors(pattern[1:], d)
    for text in suffix:
        if hamming_distance(pattern[1:], text) < d:
            for element in ELEMENTS:
                neighbors.append(element + text)
        else:
            neighbors.append(pattern[0] + text)
    return neighbors


def get_words(genome, k):
    words = []
    for start in range(len(genome) - k + 1):
        end = start + k
        words.append(genome[start:end])

    for start in range(len(genome) - k + 1):
        end = start + k
        words.append(reverse_complement(genome[start:end]))
    return words


def reverse_complement(word):
    element_list = []
    for element in range(len(word) - 1, -1, -1):
        element_list.append(COMPLEMENT_TABLE[word[element]])
    result = ''.join(element_list)
    return result


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
    Executor.execute(find_frequent, 'frequent_words_mismatch_complements.txt')
