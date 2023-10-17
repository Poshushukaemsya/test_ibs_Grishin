words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']


def find_in_different_registers(words):
    str_tmp = []
    ans = []
    for i in words:
        str_tmp.append(i.lower())

    for i in set(str_tmp):
        if str_tmp.count(i) == 1:
            ans.append(i)

    for i in words:
        if (i in str) and (i.swapcase() in str):
            if (i not in ans) and (i.swapcase() not in ans):
                ans.append(i)
    return ans


print(find_in_different_registers(words))
