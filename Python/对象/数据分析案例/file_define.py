from data_define import Record
import json


class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件的数据,读到的每一条数据都转换成Record对象，将它们都封装到list内返回"""
        pass


class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        record_list = []
        f = open(self.path, "r", encoding="UTF-8")
        for line in f:
            line = line.strip()  # 消除读取到的每一行数据中的\n
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f:
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
        f.close()
        return record_list


if __name__ == "__main__":
    text_file_reader = TextFileReader("F:/程序学习/Python/对象/数据分析案例/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("F:/程序学习/Python/对象/数据分析案例/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for l in list1:
        print(l)
    for l in list2:
        print(l)
