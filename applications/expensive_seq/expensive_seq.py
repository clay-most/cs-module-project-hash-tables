import codecs
print(codecs.decode(
    "Va Clguba, n qvpg xrl pna or nal vzzhgnoyr glcr... vapyhqvat n hcyr.", "rot_13"))

store = {}


def expensive_seq(x, y, z):
    result = 0
    if (x, y, z) in store:
        result = store[(x, y, z)]
    elif(x <= 0):
        store[(x, y, z)] = y+z
    elif(x > 0):
        store[(x, y, z)] = expensive_seq(x-1, y+1, z) + \
            expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    result = store[(x, y, z)]
    return result


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
