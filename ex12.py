def capitalizeWords(arr):
    return [arr[0].upper()] + (capitalizeWords(arr[1:]) if len(arr) > 1 else [])
