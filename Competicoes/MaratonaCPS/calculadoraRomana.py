def converteR(num) -> int:
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0

    for i in range(len(num)):
        valor = nums[num[i]]
        if i + 1 < len(num) and nums[num[i + 1]] > valor:
            # numero com precedente(IV), subtrai-se o precedente e o numero debita o valor desconto
            sum -= valor
        else:
            sum += valor
    return sum


def converteA(num) -> str:
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = []

    for i in range(len(ints)):
        count = int(num / ints[i])
        result.append(nums[i] * count)
        num -= ints[i] * count
    return ''.join(result)


while True:
    lin = list(map(converteR, input().split("+")))
    if lin[0] == '0': break

    print(converteA(sum(lin)))
