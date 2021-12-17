def capitalizeFirst(arr):
    return [arr[0].capitalize()] + (capitalizeFirst(arr[1:]) if len(arr) > 1 else [])
