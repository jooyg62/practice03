# 문제2.
# range() 함수와 유사한 frange() 함수를 작성해 보세요. frange() 함수는 실수 리스트를 반환합니다

def frange(val, base=0.0, step=0.1):
    if val < base:
        start = val
        stop = base
    else:
        start = base
        stop = val

    start = float(start)

    result = []

    result.append(start)

    while True:
        if start >= stop:
            break

        start = float(format(start + step, '.1f'))
        result.append(start)

    return result



print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))