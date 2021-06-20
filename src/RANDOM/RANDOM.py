import random, math
def RanInt(minimum, maximum, quantity = 1, iterations = None, atype = None):
    real_iterations = iterations
    try:
        iterations = int(iterations)
    except:
        raise ValueError("non-integer arg for 'iterations'")
    try:
        quantity = int(quantity)
    except:
        raise ValueError("non integer arg for 'quantity'")
    if quantity < 1:
        raise ValueError("argument 'quantity' cannot be less than 1")
    if minimum is None and not maximum is None:
        raise TypeError("RanInt() missing 1 required positional argument: 'minimum'")
    if not minimum is None and maximum is None:
        raise TypeError("RanInt() missing 1 required positional argument: 'maximum'")
    if not minimum is None and not maximum is None:
        if iterations is None and atype is None:
            ranints = []
            while quantity > 0:
                ranints.append(random.randint(int(minimum), int(maximum)))
                quantity -= 1
            return ranints
        else:
            if iterations is None and not atype is None:
                raise TypeError("RanInt() missing 1 required positional argument: 'iterations'")
            elif not iterations is None and atype is None:
                raise TypeError("RanInt() missing 1 required positional argument: 'atype'")
            else:
                ranints = []
                while quantity > 0:
                    numlist = [1]
                    iterations = real_iterations
                    while iterations > 0:
                        try:
                            numlist.append(random.randint(int(minimum), int(maximum)))
                        except:
                            raise ValueError("non-integer arg for 'minimum' or 'maximum'")
                        iterations -= 1
                    del numlist[0]
                    if atype == "rand":
                        a = random.randint(1, 3)
                    else:
                        a = 4
                    if atype == "mean" or a == 1:
                            deci = str(sum(numlist) / len(numlist))
                            if int(deci[-1:]) >= 5:
                                ranints.append(math.ceil(float(deci)))
                            else:
                                ranints.append(math.floor(float(deci)))
                    elif atype == "median" or a == 2:
                            n = len(numlist)
                            for i in range(n-1):
                                for j in range(0, n-i-1):
                                    if numlist[j] > numlist[j + 1] :
                                        numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
                            if len(numlist) % 2 == 0:
                                # Zero indexing (+1-1) for 2nd one in next line so omitted
                                ranints.append((numlist[len(numlist) // 2 - 1] + numlist[len(numlist) // 2]) // 2)
                            else:
                                # Zero indexing so the following should be math.ceil(...-1) but that's same as math.floor(...)
                                ranints.append(numlist[math.floor(len(numlist) / 2)])
                    elif atype == "mode" or a == 3:
                            ranints.append(max(set(numlist), key = numlist.count))
                    else:
                        raise ValueError("invalid argument for 'atype'")
                    quantity -= 1
                return ranints
