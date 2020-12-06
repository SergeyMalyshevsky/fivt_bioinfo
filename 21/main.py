def find_the_minimun_number_of_coins(*var):
    money = var[0]
    coin_list = var[1].split(',')

    coins = []
    for coin in coin_list:
        coins.append(int(coin))

    limit = money + 1
    minimum_number = [0 for _ in range(0, limit)]
    for element in range(1, limit):
        minimum_number[element] = 10**10
        for index in range(0, len(coins)):
            coin = coins[index]
            if coin <= element:
                if (minimum_number[element - coin] + 1) < minimum_number[element]:
                    minimum_number[element] = minimum_number[element - coin] + 1
    result = max(minimum_number)
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

        if isinstance(result, list):
            for element in result:
                print(element)
        elif isinstance(result, int):
            print(result)
        else:
            print(result)


if __name__ == "__main__":
    Executor.execute(find_the_minimun_number_of_coins, 'change_problem.txt')
