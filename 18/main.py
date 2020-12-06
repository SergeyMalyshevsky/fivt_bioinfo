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


def cyclopeptide_sequencing(*var):
    spectrum = list(var)

    cand_peptides = ['']
    result_peptides = []
    while cand_peptides:
        new_peptides = []
        for cand_peptide in cand_peptides:
            for amino in AMINOS:
                new_peptides.append(cand_peptide + amino)
        cand_peptides = new_peptides
        minus = []
        for i in range(len(cand_peptides)):
            peptide = cand_peptides[i]

            peptide_mass = 0
            for element in range(len(peptide)):
                peptide_mass += AMINOS[peptide[element]]

            if peptide_mass == max(spectrum):
                if get_cyclic_spectrum(peptide, AMINOS) == spectrum:
                    result_peptides.append(peptide)
                    minus.append(peptide)
            elif not is_consistent(peptide, spectrum):
                minus.append(peptide)
        for i in range(len(minus)):
            cand_peptides.remove(minus[i])

    mass_final_peptide = []
    for peptide in result_peptides:
        mass_peptides = []
        for i in range(len(peptide)):
            mass_peptides.append(AMINOS[peptide[i]])
        mass_final_peptide.append('-'.join(str(i) for i in mass_peptides))
    result = ' '.join(str(i) for i in mass_final_peptide)

    return result


def is_consistent(peptide, spectrum):
    mass = [0 for _ in range(len(peptide) + 1)]
    for element in range(len(peptide)):
        mass[element + 1] = mass[element] + AMINOS[peptide[element]]
    lin_spectrum = []
    for element in range(len(peptide)):
        for element_2 in range(element + 1, len(peptide) + 1):
            lin_spectrum.append(mass[element_2] - mass[element])
    lin_spectrum.append(0)
    lin_spectrum = sorted(lin_spectrum)

    for s in lin_spectrum:
        if lin_spectrum.count(s) > spectrum.count(s):
            return False
    return True


def get_cyclic_spectrum(peptide, AMINOS):
    mass = [0 for i in range(len(peptide) + 1)]
    for element in range(len(peptide)):
        mass[element + 1] = mass[element] + AMINOS[peptide[element]]
    peptideMass = mass[len(peptide)]
    cycl_spectrum = []
    for element in range(len(peptide)):
        for j in range(element + 1, len(peptide) + 1):
            cycl_spectrum.append(mass[j] - mass[element])
            if element > 0 and j < len(peptide):
                cycl_spectrum.append(peptideMass - (mass[j] - mass[element]))
    cycl_spectrum.append(0)
    result = sorted(cycl_spectrum)
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


if __name__ == '__main__':
    Executor.execute(cyclopeptide_sequencing, 'cyclopeptide_sequencing.txt')
