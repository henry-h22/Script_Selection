
def dictInc(dictionary, key):
    # Special edge case because we don't care about sil_sil
    if (key == 'sil_sil'): return

    existingKeys = dictionary.keys()
    if (key in existingKeys) :
        dictionary[key] += 1
    else:
        dictionary[key] = 1


if __name__ == '__main__':
    quinn = {'b':3}
    dictInc(quinn, 'b')
    dictInc(quinn, 'a')
    print(quinn)