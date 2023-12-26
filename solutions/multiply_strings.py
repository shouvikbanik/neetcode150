def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if num1 == '0' or num2 == '0':
        return '0'

    def decode(num):
        ans = 0
        for i in num:
            ans = ans * 10 + (ord(i) - ord('0'))
        return ans

    def encode(s):
        new_str = ''
        while s:
            a = s % 10
            s = s // 10
            new_str = chr(ord('0') + a) + new_str
        return new_str

    return encode(decode(num1) * decode(num2))
