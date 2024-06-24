def ci_date(value):
    if 0 < int(value[0:2]) < 99:
        if 1 <= int(value[2:4]) <= 12:
            if 1 <= int(value[4:6]) <= 31:
                return True
            else:
                return False
        else:
            return False
    else:
        return False