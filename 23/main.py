def find_the_highest_scoring_alignmen(sequence_1, sequence_2, matrix, penalty):
    length_1 = len(sequence_1)
    length_2 = len(sequence_2)
    s = [[0] * (length_2 + 1) for _ in range(length_1 + 1)]
    backtrack = [[0] * (length_2 + 1) for _ in range(length_1 + 1)]

    for i in range(1, length_1 + 1):
        s[i][0] = - i * penalty

    for j in range(1, length_2 + 1):
        s[0][j] = - j * penalty

    for i in range(1, length_1 + 1):
        for j in range(1, length_2 + 1):
            score_list = [s[i - 1][j] - penalty, s[i][j - 1] - penalty, s[i - 1][j - 1] + matrix[sequence_1[i - 1], sequence_2[j - 1]]]
            s[i][j] = max(score_list)
            backtrack[i][j] = score_list.index(s[i][j])

    insert = lambda seq, i: seq[:i] + '-' + seq[i:]
    align_1, align_2 = sequence_1, sequence_2
    a = length_1
    b = length_2
    max_score = str(s[a][b])
    while a * b != 0:
        if backtrack[a][b] == 0:
            a -= 1
            align_2 = insert(align_2, b)
        elif backtrack[a][b] == 1:
            b -= 1
            align_1 = insert(align_1, a)
        else:
            a -= 1
            b -= 1

    for _ in range(a):
        align_2 = insert(align_2, 0)

    for _ in range(b):
        align_1 = insert(align_1, 0)

    result = max_score, align_1, align_2

    return result


def read_dataset(filename):
    input_data = []
    with open(filename) as f:
        for element in f.readlines():
            if 'input' in element.lower():
                continue
            elif 'output' in element.lower():
                break
            else:
                input_data.append(element.strip())
    return input_data


def read_BLOSUM62(filename):
    with open('BLOSUM62.txt') as f1:
        lines = [line.strip().split() for line in f1.readlines()]
        score_matrix = {(line[0], line[1]): int(line[2]) for line in lines}
    return score_matrix


if __name__ == '__main__':
    sequence = read_dataset('global_alignment.txt')
    matrix = read_BLOSUM62('BLOSUM62.txt')
    for line in find_the_highest_scoring_alignmen(sequence[0], sequence[1], matrix, 5):
        print(line)
