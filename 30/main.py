import numpy as np


def get_2_break_on_genome(genome, i, j, k, l):
    g = mark_edges(genome)

    rem = ((i, j), (j, i), (k, l), (l, k))
    bg = [t for t in g if t not in rem]
    bg.append((i, k))
    bg.append((j, l))
    g = bg

    genome = []
    visited = []
    adj = np.zeros(len(g) * 2, dtype=np.int)
    for t in g:
        adj[t[0] - 1] = t[1] - 1
        adj[t[1] - 1] = t[0] - 1

    for t in g:
        orig = t[0]
        if orig in visited:
            continue
        visited.append(orig)
        if orig % 2 == 0:
            closing = orig - 1
        else:
            closing = orig + 1
        p = []
        i = 0
        while True:
            if orig % 2 == 0:
                p.append(orig // 2)
            else:
                p.append(-(orig + 1) // 2)
            dest = adj[orig - 1] + 1
            i = i + 1
            if (i > 100):

                return
            visited.append(dest)
            if dest == closing:
                genome.append(p)
                break
            if (dest % 2 == 0):
                orig = dest - 1
            else:
                orig = dest + 1
            assert orig > 0
            visited.append(orig)

    fs = []
    for element in genome:
        ps = []
        for i in element:
            if i > 0:
                ps.append('+' + str(i))
            elif i == 0:
                ps.append('0')
            elif i < 0:
                ps.append(str(i))
        fs.append('(' + ' '.join(ps) + ')')

    result = ''.join(fs)
    return result


def mark_edges(genome):
    g = []
    for p in genome:
        nodes = []
        for i in p:
            if i > 0:
                nodes.append(2 * i - 1)
                nodes.append(2 * i)
            else:
                nodes.append(-2 * i)
                nodes.append(-2 * i - 1)
        for j in range(len(nodes) // 2):
            head = 1 + 2 * j
            tail = (2 + 2 * j) % len(nodes)
            e = (nodes[head], nodes[tail])
            g.append(e)
    return g


def permutation_list_to_str(p):
    ps = []
    for i in p:
        if i > 0:
            ps.append('+' + str(i))
        elif i == 0:
            ps.append('0')
        elif i < 0:
            ps.append(str(i))
    return '(' + ' '.join(ps) + ')'


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

    @staticmethod
    def print_result(func, filename):
        with open(filename) as f:
            lines = f.readlines()

        count = 0
        for line in lines:
            if 'input' in line.lower():
                continue
            elif 'output' in line.lower():
                break

            if count == 0:
                g = [list(map(int, line.strip().lstrip('(').rstrip(')').split(' ')))]
            if count == 1:
                a, b, c, d = list(map(int, line.strip().split(', ')))
            count += 1

        result = func(g, a, b, c, d)
        print(result)


if __name__ == '__main__':
    Executor.print_result(get_2_break_on_genome, 'rosalind_ba6k.txt')
