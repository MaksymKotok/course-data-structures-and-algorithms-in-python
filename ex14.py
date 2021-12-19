def collectStrings(obj):
    head = obj[obj.keys()[0]]
    obj.pop(obj.keys()[0])
    if type(head) is dict:
        return collectStrings(head)
    if type(head) is str:
        return [head] + (collectStrings(obj) if len(obj.keys()) > 0 else [])


obj = {
    'stuff': 'foo',
    'data': {
        'val': {
            'thing': {
                'info': 'bar',
                'moreInfo': {
                    'evenMoreInfo': {
                        'weMadeIt': 'baz'
                    }
                }
            }
        }
    }
}

print(collectStrings(obj))