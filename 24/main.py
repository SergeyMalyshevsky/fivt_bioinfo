def find_the_highest_scoring_local_alignment(sequence_1, sequence_2, matrix, penalty):
    max_a = 0
    max_b = 0
    length_1 = len(sequence_1)
    length_2 = len(sequence_2)

    s = [[0 for _ in range(length_2 + 1)] for _ in range(length_1 + 1)]
    backtrack = [[0 for _ in range(length_2 + 1)] for j in range(length_1 + 1)]
    max_score = -1

    for i in range(1, length_1 + 1):
        for j in range(1, length_2 + 1):
            score_list = [s[i - 1][j] - penalty, s[i][j - 1] - penalty,
                          s[i - 1][j - 1] + matrix[sequence_1[i - 1], sequence_2[j - 1]], 0]
            s[i][j] = max(score_list)
            backtrack[i][j] = score_list.index(s[i][j])
            if s[i][j] > max_score:
                max_score = s[i][j]
                max_a, max_b = i, j

    insert = lambda seq, i: seq[:i] + '-' + seq[i:]

    align_1 = sequence_1[:max_a]
    align_2 = sequence_2[:max_b]

    while backtrack[max_a][max_b] != 3 and max_a * max_b != 0:
        if backtrack[max_a][max_b] == 0:
            max_a -= 1
            align_2 = insert(align_2, max_b)
        elif backtrack[max_a][max_b] == 1:
            max_b -= 1
            align_1 = insert(align_1, max_a)
        elif backtrack[max_a][max_b] == 2:
            max_a -= 1
            max_b -= 1

    align_1 = align_1[max_a:]
    align_2 = align_2[max_b:]
    result = str(max_score), align_1, align_2

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


def read_table(filename):
    with open(filename) as f1:
        lines = [line.strip().split() for line in f1.readlines()]
        matrix = {(line[0], line[1]): int(line[2]) for line in lines}
    return matrix


if __name__ == '__main__':
    sequence = read_dataset('local_alignment.txt')
    matrix = read_table('PAM250.txt')
    for line in find_the_highest_scoring_local_alignment(sequence[0], sequence[1], matrix, 5):
        print(line)
