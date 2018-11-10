

def new():
    string = 'AATATT'

    string1 = string + '$'

    suffixes = []

    count = 0

    while count < len(string1):
        if count == 0:
            suffixes.append(string1)
            count += 1
        else:
            suffixes.append(string1[(count * -1):])
            count += 1

    suffixes.sort(key=lambda s: len(s))
    # print(suffixes[0])

    # print("".join(suffixes[2].rsplit(suffixes[0])))

    substrings = []

    count = 0
    span = len(suffixes)

    while count < span:
        back = count
        while back >= 0:

            if back == count:
                substrings.append(suffixes[back])

            else:
                substrings.append("".join(suffixes[count].rsplit(suffixes[back])))

            back -= 1

            ## substrings.append("".join(suffix.rsplit(other)))

        count += 1

    print(substrings)

def old():
    string = 'AATATT'

    string1 = string + '$'

    suffixes = []

    count = 0

    while count < len(string1):
        if count == 0:
            suffixes.append(string1)
            count += 1
        else:
            suffixes.append(string1[(count * -1):])
            count += 1

    suffixes.sort(key=lambda s: len(s))
    # print(suffixes[0])

    # print("".join(suffixes[2].rsplit(suffixes[0])))

    substrings = []

    for suffix in suffixes:
        if suffix not in substrings:
            substrings.append(suffix)

        ## better way here -- don't check length on every element -- use counter so you never get to longer suffixes
        ## will improve runtime

        for other in suffixes:
            if len(other) < len(suffix):
                substrings.append("".join(suffix.rsplit(other)))

    print(substrings)

def main():
    new1 = new()
    old1 = old()

    print(str(new1 == old1))

if __name__ == "__main__":
    main()

