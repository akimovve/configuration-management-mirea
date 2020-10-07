import json


# Класс для создания json
class JSONMaker:

    @staticmethod
    def print_json(data):
        resp_dictionary = dict()
        for i in range(len(data)):
            if type(data[i]) is tuple:
                resp_dictionary[data[i][0]] = data[i][1]
            elif (i < len(data) - 1) \
                    and (type(data[i + 1]) is list) \
                    and ((type(data[i]) is str)
                         or (type(data[i]) is int)):
                i += 1
                resp_dictionary[data[i - 1]] = JSONMaker.json_list(data[i])
        print(json
              .dumps(resp_dictionary,
                     ensure_ascii=False,
                     indent=6)
              .replace('"\\\"', '"')
              .replace('\\""', '"')
              )

    @staticmethod
    def json_list(data):
        resp_dictionary = dict()
        resp_list = []
        fl = True
        for d in data:
            if not (type(d) is tuple):
                fl = False
            else:
                continue
        if fl:
            for d in data:
                resp_dictionary[d[0]] = d[1]
            return resp_dictionary
        for d in data:
            if type(d) is list:
                resp_list.append(JSONMaker.json_list(d))
            if (type(d) is int) or (type(d) is str):
                resp_list.append(d)
        return resp_list
