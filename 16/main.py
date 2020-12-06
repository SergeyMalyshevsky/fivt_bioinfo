RNA_CODONS = {
    'AAA': 'K',
    'AAC': 'N',
    'AAG': 'K',
    'AAU': 'N',
    'ACA': 'T',
    'ACC': 'T',
    'ACG': 'T',
    'ACU': 'T',
    'AGA': 'R',
    'AGC': 'S',
    'AGG': 'R',
    'AGU': 'S',
    'AUA': 'I',
    'AUC': 'I',
    'AUG': 'M',
    'AUU': 'I',
    'CAA': 'Q',
    'CAC': 'H',
    'CAG': 'Q',
    'CAU': 'H',
    'CCA': 'P',
    'CCC': 'P',
    'CCG': 'P',
    'CCU': 'P',
    'CGA': 'R',
    'CGC': 'R',
    'CGG': 'R',
    'CGU': 'R',
    'CUA': 'L',
    'CUC': 'L',
    'CUG': 'L',
    'CUU': 'L',
    'GAA': 'E',
    'GAC': 'D',
    'GAG': 'E',
    'GAU': 'D',
    'GCA': 'A',
    'GCC': 'A',
    'GCG': 'A',
    'GCU': 'A',
    'GGA': 'G',
    'GGC': 'G',
    'GGG': 'G',
    'GGU': 'G',
    'GUA': 'V',
    'GUC': 'V',
    'GUG': 'V',
    'GUU': 'V',
    'UAA': '',
    'UAC': 'Y',
    'UAG': '',
    'UAU': 'Y',
    'UCA': 'S',
    'UCC': 'S',
    'UCG': 'S',
    'UCU': 'S',
    'UGA': '',
    'UGC': 'C',
    'UGG': 'W',
    'UGU': 'C',
    'UUA': 'L',
    'UUC': 'F',
    'UUG': 'L',
    'UUU': 'F'
}


def peptide_encoding_problem(*var):
    dna = var[0]
    peptide = var[1]

    seq = []

    limit = ((len(dna) - 3) * len(peptide) + 1)

    for i in range(limit):

        if translation(dna[i:i + len(peptide) * 3].replace('T', 'U')) == peptide or translation(reverse_seq(dna[i:i + len(peptide) * 3]).replace('T', 'U')) == peptide:
            seq.append(dna[i:i + len(peptide) * 3])
    return seq


def translation(rna):
    protein = ""
    for i in range(0, len(rna), 3):
        if rna[i:i + 3] in RNA_CODONS:
            if isinstance(RNA_CODONS[rna[i:i + 3]], str):
                protein += RNA_CODONS[rna[i:i + 3]]
    return protein


def reverse_seq(seq):
    sequence = ''
    seq_dict = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }
    for letter in seq:
        sequence += seq_dict[letter]

    result = sequence[::-1]
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
    Executor.execute(peptide_encoding_problem, 'peptide_encoding.txt')
