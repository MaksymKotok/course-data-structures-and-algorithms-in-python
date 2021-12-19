def stringifyNumbers(obj):
    # print(obj)
    keys = list(obj.keys())
    if len(keys) == 0:
        return {}
    if type(obj[keys[0]]) is dict:
        obj[keys[0]] = stringifyNumbers(obj[keys[0]])
    if type(obj[keys[0]]) in (int, float, complex):
        obj[keys[0]] = str(obj[keys[0]])
    if len(keys) == 1:
        return obj
    elif len(keys) > 1:
        _obj = obj.copy()
        _obj.pop(keys[0])
        res = stringifyNumbers(_obj)
        obj.update(res)
        return obj


obj1 = {
    'num': 1,
    'test': [],
    'data': {
        'val': 4,
        'info': {
            'isRight': True,
            'random': 66
        }
    }
}

print(stringifyNumbers(obj1))
