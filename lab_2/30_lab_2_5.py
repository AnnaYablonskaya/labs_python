import argparse

def to_json(value) -> str:
    if type(value) not in (dict, list, int, float, type(None), bool, str, tuple):
        raise ValueError
    if type(value) == dict:
        s = ""
        for key, value in value.items():
            if type(key) not in (int, str):
                raise ValueError
            s += '"{}":{},'.format(key, to_json(value))
        return "{" + s[:-1] + "}"

    if type(value) in (list, tuple):
        s = ",".join(to_json(item) for item in value)
        return "[{}]".format(s)

    if type(value) in (int, float):
        return "{}".format(value)

    if value is None:
        return "null"

    if type(value) is str:
        return '"{}"'.format(value)


if __name__ == '__main__':
    a = {"check": 123, "check2": [123, "aaa"], "check3": None, "check4": {"a": 123}}
    print(to_json(a))
    parser = argparse.ArgumentParser(description='Inp.file name')
    parser.add_argument('-f',  
        help='Your file')
    args = parser.parse_args()
    try:
        if args.f:
            file = args.f
            file_f = open(file)
            file_d = "".join(file_f.readlines())
            file_f.close()
            print(to_json(file_d))
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("Your file wasn't found. Try again")