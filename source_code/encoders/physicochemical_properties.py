import pandas as pd
from joblib import Parallel, delayed
from utils_functions import utils_functions

class physicochemical_encoder(object):

    def __init__(self,
                 dataset,
                 property_encoder,
                 dataset_encoder,
                 constant_instance,
                 name_column_seq,
                 name_column_id,
                 name_column_response):

        self.dataset = dataset
        self.property_encoder = property_encoder
        self.dataset_encoder = dataset_encoder
        self.constant_instance = constant_instance
        self.name_column_seq = name_column_seq
        self.name_column_id = name_column_id
        self.name_column_response = name_column_response

        self.zero_padding = self.check_max_size()

    def __check_residues(self, residue):
        if residue in self.constant_instance.possible_residues:
            return True
        else:
            return False

    def __encoding_residue(self, residue):

        if self.__check_residues(residue):
            return self.dataset_encoder[self.property_encoder][residue]
        else:
            return False

    def check_max_size(self):
        size_list = [len(seq) for seq in self.dataset[self.name_column_seq]]
        return max(size_list)

    def __encoding_sequence(self, sequence, response, id_seq):

        sequence = sequence.upper()
        sequence_encoding = []
        for residue in sequence:
            response_encoding = self.__encoding_residue(residue)
            if response_encoding != False:
                sequence_encoding.append(response_encoding)

        # complete zero padding
        for k in range(len(sequence_encoding), self.zero_padding):
            sequence_encoding.append(0)

        sequence_encoding.append(response)
        sequence_encoding.insert(0, id_seq)
        return sequence_encoding

    def encoding_dataset(self, name_export, is_export):

        #print("Start encoding process")
        data_encoding = Parallel(n_jobs=self.constant_instance.n_cores, require='sharedmem')(delayed(self.__encoding_sequence)(self.dataset[self.name_column_seq][i], self.dataset[self.name_column_response][i], self.dataset[self.name_column_id][i]) for i in range(len(self.dataset)))

        print("Processing results")
        matrix_data = []
        for element in data_encoding:
            matrix_data.append(element)

        print("Creating dataset")
        header = ['p_{}'.format(i) for i in range(len(matrix_data[0])-2)]
        header.append(self.name_column_response)
        header.insert(0, self.name_column_id)
        print("Export dataset")
        df_data = pd.DataFrame(matrix_data, columns=header)

        if is_export:
            print(name_export)
            utils_functions().export_csv(df_data, name_export)
        return df_data
