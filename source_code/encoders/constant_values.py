import multiprocessing as mp

class constant_values(object):

    def __init__(self):
        self.n_cores = mp.cpu_count()
        self.possible_residues = [
            'A',
            'C',
            'D',
            'E',
            'F',
            'G',
            'H',
            'I',
            'N',
            'K',
            'L',
            'M',
            'P',
            'Q',
            'R',
            'S',
            'T',
            'V',
            'W',
            'Y'
        ]

