class Analyzer:
    """log analyzer

    The program reads the file and outputs
    the number of NOK events per minute
    to another file in a convenient format,
    having previously grouped by hours, months, years.

        Input data
    file_name -------------- filename to scan
    write_file_name -------- filename to write

    """

    def __init__(self, file_name, write_file_name=None):
        self.file_name = file_name
        self.write_file_name = write_file_name
        self.stat = {}

    # Creating a dictionary with specified conditions
    def creating_a_list_of_events(self):

        with open(self.file_name, 'r', encoding='UTF8') as file:
            for line in file:
                data = line[1:17]
                not_ok = line[-4:-1]
                if not_ok == 'NOK':
                    if data in self.stat:
                        self.stat[data] += 1
                    else:
                        self.stat[data] = 1

    # Writing a sorted dictionary to a file
    def write_to_file(self):
        if self.write_file_name == None:
            self.write_file_name = 'NOK_' + self.file_name
        with open(self.write_file_name, 'w', encoding='UTF8') as file:
            for key, value in self.stat.items():
                file.write('[' + str(key) + '] ' + str(value) + '\n')

    def grouping_by_hour(self):
        start_to_cut = 11
        end_cut = 13
        self.grouping(start_to_cut, end_cut)

    def grouping_by_month(self):
        start_to_cut = 5
        end_cut = 7
        self.grouping(start_to_cut, end_cut)

    def grouping_by_year(self):
        start_to_cut = 0
        end_cut = 4
        self.grouping(start_to_cut, end_cut)

    def grouping(self, start_to_cut, end_cut):
        grouped_data = {}
        for i in self.stat.keys():
            sort_value = i[start_to_cut: end_cut]

            if sort_value in grouped_data.keys():
                grouped_data[sort_value].update({i: self.stat[i]})
            else:
                grouped_data[sort_value] = {}
                grouped_data[sort_value].update({i: self.stat[i]})

        self.write_grouping(grouped_data)

    def write_grouping(self, dict):
        dict = dict
        with open(self.write_file_name, 'w') as file:
            for key, dict_2 in dict.items():
                for key_dict2, value in dict_2.items():
                    file.write(
                        str(key) + '-> [' + (
                                str(key_dict2) + '] ' + str(value) + '\n'))


test = Analyzer(file_name='events.txt')
test.creating_a_list_of_events()
test.write_to_file()
test.grouping_by_hour()
