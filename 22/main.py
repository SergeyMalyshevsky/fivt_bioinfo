def find_the_length_of_the_longest_path(*var):
    n = var[0]
    m = var[1]
    d = var[2]
    r = var[3]

    s = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + d[i - 1][0]
    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + r[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + d[i - 1][j], s[i][j - 1] + r[i][j - 1])
    return s[n][m]


class Executor():
    @staticmethod
    def execute(func, filename):
        var = []
        with open(filename) as f:
            row = f.readline()
            if 'input' in row.lower():
                row = f.readline()

            line = row.strip().split()

            n = int(line[0])
            var.append(n)
            m = int(line[1])
            var.append(m)
            d = []
            for i in range(n):
                line = f.readline().strip().split()
                d.append([int(i) for i in line])
            var.append(d)
            f.readline()
            r = []
            for i in range(n + 1):
                line = f.readline().strip().split()
                r.append([int(i) for i in line])
            var.append(r)

        result = func(*var)

        if isinstance(result, list):
            for element in result:
                print(element)
        elif isinstance(result, int):
            print(result)
        else:
            print(result)


if __name__ == "__main__":
    Executor.execute(find_the_length_of_the_longest_path, 'Manhattan_tourist.txt')
