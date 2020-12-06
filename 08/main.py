import random


def randomized_motif_search(*var):
    k = var[0]
    t = var[1]
    dna = var[2:]

    i = 0
    best_motifs = []
    for i in range(t):
        best_motifs.append(dna[i][:k])
    while i < 1000:
        motifs = []
        for word in dna:
            point = random.randint(0, len(word) - k)
            motifs.append(word[point:point + k])

        while True:
            profile = get_profile(motifs)
            temp_motifs = create_motifs(profile, dna)
            if score(temp_motifs) < score(motifs):
                motifs = temp_motifs
            else:
                break

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        i += 1
    return best_motifs


def create_motifs(profile, dna):
    motifs = []
    for i in dna:
        motifs.append(profile_most_probable(i, profile, len(profile)))
    return motifs


def get_best_motifs(dna, k, t):
    best_motifs = []
    for i in range(t):
        best_motifs.append(dna[i][:k])
    return best_motifs


def get_profile(motifs):
    profile = []
    letters = 'ACGT'
    motifs_len = len(motifs) + 4
    for i in range(len(motifs[0])):
        count = {}
        for letter in letters:
            count[letter] = 1
        for motif in motifs:
            if motif[i] in letters:
                count[motif[i]] += 1
        profile.append([count['A'] / motifs_len,
                        count['C'] / motifs_len,
                        count['G'] / motifs_len,
                        count['T'] / motifs_len])
    return profile


def get_prob(profile, word):
    prob = 1
    letters = 'ACGT'
    for element in range(0, len(word)):
        for letter_index in range(len(letters)):
            if word[element] == letters[letter_index]:
                prob = prob * profile[element][letter_index]
    return prob


def profile_most_probable(dna, profile, k):
    pattern = dna[0:k]
    best_prob = 0
    for i in range(len(dna) - k + 1):
        word = dna[i:i+k]
        new_prob = get_prob(profile, word)
        if new_prob > best_prob:
            pattern = word
            best_prob = new_prob
    return pattern


def hamming_distance(word_1, word_2):
    count = 0
    for letter_1, letter_2 in zip(word_1, word_2):
        if letter_1 != letter_2:
            count += 1
    return count


def score(motifs):
    cons = find_cons(motifs)
    score = 0
    for motif in motifs:
        score += hamming_distance(cons, motif)
    return score


def find_cons(motifs):
    cons = ''
    letters = 'ACGT'
    for element in range(len(motifs[0])):
        count = {}
        for letter in letters:
            count[letter] = 0
        for motif in motifs:
            for letter in letters:
                if motif[element] == letter:
                    count[letter] += 1

        if count['A'] >= max(count['C'], count['G'], count['T']):
            cons += "A"
        elif count['C'] >= max(count['A'], count['G'], count['T']):
            cons += "C"
        elif count['G'] >= max(count['A'], count['C'], count['T']):
            cons += "G"
        elif count['T'] >= max( count['A'], count['C'], count['T']):
            cons += "T"
    return cons


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


if __name__ == "__main__":
    Executor.execute(randomized_motif_search, 'randomized_motif_search.txt')
