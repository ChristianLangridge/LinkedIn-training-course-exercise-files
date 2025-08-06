def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)


def square(num):
    if num == 1:
        return num 
    return triangle(num) + triangle(num - 1)


square(2)
