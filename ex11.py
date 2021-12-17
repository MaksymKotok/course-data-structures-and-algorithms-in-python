def nestedEvenSum(obj, sum=0):
    return (nestedEvenSum(obj[obj.keys()[0]]) if type(obj[obj.keys()[0]]) is dict else sum if type(obj[obj.keys()[0]]) is not int else sum + 1 if obj[obj.keys()[0]] % 2 == 0 else sum) + (nestedEvenSum({k: obj[k] for k in obj.keys()[1:]}) if len(obj.keys()) > 1 else 0)
