import csv


class FileWriter:
    # header
    header_list = ['name', 'img_url']

    def __init__(self, csv_file_path):
        """
        initial object
        """
        self.csv_path = csv_file_path

    def write_header(self):
        """
        write header strings to csv
        """
        with open(self.csv_path, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow([self.header_list[0], self.header_list[1]])

    def write_actress_data(self, actress_data_list):
        """
        write name and url of actress data
        """
        writed_cnt = 0
        with open(self.csv_path, 'a') as f:
            writer = csv.writer(f, delimiter=',')
            for actress in actress_data_list:
                writer.writerow([actress['name'], actress['img_url']])
                writed_cnt+=1

        return writed_cnt
