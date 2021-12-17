def flatten(arr):
    return (flatten(arr[0]) if type(arr[0]) is list else [arr[0]]) + (flatten(arr[1:]) if len(arr) > 1 else [])
