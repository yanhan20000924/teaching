def func(s):
    try:
        res = s.split('/')
        check = False
        if len(res) != 3:
            print('Not a valid date.')
            return None
        res[0], res[1] = res[1], res[0]

        if 0 < int(res[0]) <= 31 and 0 < int(res[1]) <= 12 and (0 <= int(res[2]) <= 99 or 1000 <= int(res[2]) <= 9999):
            check = True
        elif check == False and 0 < int(res[1]) <= 31 and 0 < int(res[0]) <= 12 and (
                0 <= int(res[2]) <= 99 or 1000 <= int(res[2]) <= 9999):
            print('Not a valid date. Did you mean to input {}/{}/{}?'.format(res[0], res[1], res[2]))
            return None
        else:
            print('Not a valid date.')
            return None
        if int(res[1]) == 2:
            if int(res[2]) % 4 != 0 and int(res[0]) >= 29:
                print('Not a valid date.')
                return None
            elif int(res[2]) % 4 == 0 and int(res[0]) > 29:
                print('Not a valid date.')
                return None
        if (res[1] == 4 or res[1] == 6 or res[1] == 9 or res[1] == 11) and res[0] > 30:
            print('Not a valid date.')
            return None
        # valid date
        if len(res[0]) == 1:
            res[0] = '0' + res[0]
        if len(res[1]) == 1:
            res[1] = '0' + res[1]
        if len(res[2]) == 2:
            if int(res[2]) <= 22:
                res[2] = '20' + res[2]
            else:
                res[2] = '19' + res[2]
        return '-'.join(res)
    except:
        print('Not a valid date.')
        return None
