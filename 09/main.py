import random

import numpy


def gibbs_sampler(*var):
    k = var[0]
    t = var[1]
    N = var[2]
    dnas = var[3:]

    best_motifs = [k * t, None]
    for repeat in range(20):
        rand_ints = [random.randint(0, len(dnas[0]) - k) for a in range(t)]
        motifs = [dnas[i][r:r + k] for i, r in enumerate(rand_ints)]

        cur_motifs = [get_score(motifs), list(motifs)]
        for _ in range(N):
            rand_i = random.randint(0, t - 1)
            motif_list = [x for a, x in enumerate(motifs) if a != rand_i]
            current_profile = get_profile_with_pseudocounts(motif_list)
            motifs[rand_i] = get_profile_randomized_kmer(k, current_profile, dnas[rand_i])
            cur_score = get_score(motifs)
            if cur_score < cur_motifs[0]:
                cur_motifs = [cur_score, list(motifs)]

        if cur_motifs[0] < best_motifs[0]:
            best_motifs = cur_motifs
    result = best_motifs[1]
    return result


def get_score(motifs):
    score = 0
    letters = 'ACGT'
    for element in range(len(motifs[0])):
        motif_list = [motifs[i][element] for i in range(len(motifs))]
        motif = ''.join(motif_list)

        ham_dist_list = [hamming_distance(motif, letter * len(motif)) for letter in letters]
        score += min(ham_dist_list)
    return score


def get_profile_with_pseudocounts(motifs):
    profiles = []
    letters = 'ACGT'
    for element in range(len(motifs[0])):
        motif_list = [motifs[i][element] for i in range(len(motifs))]
        c = ''.join(motif_list)

        prof_list = [float(c.count(letter) + 1) / float(len(c) + 4) for letter in letters]
        profiles.append(prof_list)
    return profiles


def get_most_prob_k_mers(dna, k, prof):
    letters = 'ACGT'
    n_loc = {nuc: index for index, nuc in enumerate(letters)}
    max_prob = [-1, None]
    for element in range(len(dna) - k + 1):
        current_prob = 1
        for i, nuc in enumerate(dna[element:element + k]):
            current_prob *= prof[i][n_loc[nuc]]
        if current_prob > max_prob[0]:
            max_prob = [current_prob, dna[element:element + k]]
    result = max_prob[1]
    return result


def hamming_distance(word_1, word_2):
    count = 0
    for letter_1, letter_2 in zip(word_1, word_2):
        if letter_1 != letter_2:
            count += 1
    return count


def get_profile_randomized_kmer(k, profile, dna):
    letters = 'ACGT'
    n_loc = {nuc: index for index, nuc in enumerate(letters)}
    probs = []
    for element in range(len(dna) - k):
        current_prob = 1.0
        for i, nuc in enumerate(dna[element:element + k]):
            current_prob *= profile[i][n_loc[nuc]]
        probs.append(current_prob)

    element = numpy.random.choice(len(probs), p=numpy.array(probs) / numpy.sum(probs))
    result = dna[element:element + k]
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
    Executor.execute(gibbs_sampler, 'gibbs.txt')
