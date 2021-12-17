def isPalindrome(string):
    return (True if string[0] == string[-1] else False) and (isPalindrome(string[1:-1]) if len(string) > 1 else True)
