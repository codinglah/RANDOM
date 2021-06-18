import random, math
def RanInt(minimum, maximum, iterations = None, atype = None):
    if not minimum == None and not maximum == None:
        if iterations == None and atype == None:
            if minimum == None and not maximum == None:
                raise TypeError("RanInt() missing 1 required positional argument: 'minimum'")
            elif not minimum == None and maximum == None:
                raise TypeError("RanInt() missing 1 required positional argument: 'maximum'")
            else:
                try:
                    return random.randint(int(minimum), int(maximum))
                except:
                    raise ValueError("non-integer arg for 'minimum' or 'maximum'")
        else:
            if iterations == None and not atype == None:
                raise TypeError("RanInt() missing 1 required positional argument: 'iterations'")
            elif not iterations == None and atype == None:
                raise TypeError("RanInt() missing 1 required positional argument: 'atype'")
            else:
                    numlist = []
                    try:
                        iterations = int(iterations)
                    except:
                        raise ValueError("non-integer arg for 'iterations'")
                    while iterations > 0:
                        try:
                            numlist.append(random.randint(int(minimum), int(maximum)))
                        except:
                            raise ValueError("non-integer arg for 'minimum' or 'maximum'")
                        iterations -= 1
                    if atype == "rand":
                        a = random.randint(1, 3)
                    else:
                        a = 4
                    if atype == "mean" or a == 1:
                        deci = str(sum(numlist) / len(numlist))
                        if int(deci[-1:]) >= 5:
                            return math.ceil(float(deci))
                        else:
                            return math.floor(float(deci))
                    elif atype == "median" or a == 2:
                        n = len(numlist)
                        for i in range(n-1):
                            for j in range(0, n-i-1):
                                if numlist[j] > numlist[j + 1] :
                                    numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
                        if len(numlist) % 2 == 0:
                            # Zero indexing (+1-1) for 2nd one in next line so omitted
                            return (numlist[len(numlist) // 2 - 1] + numlist[len(numlist) // 2]) // 2 
                        else:
                            # Zero indexing so the following should be math.ceil(...-1) but that's same as math.floor(...)
                            return numlist[math.floor(len(numlist) / 2)]
                    elif atype == "mode" or a == 3:
                        return max(set(numlist), key = numlist.count)
                    else:
                        raise ValueError("invalid argument for 'atype'")
