import random
import math
import statistics
import string

def RanInt(minimum, maximum, quantity = 1, avg = None):

# Conditions for testing validity of arguments    
    
    try:
        quantity = int(quantity)
    except:
        raise ValueError("non integer arg for 'quantity'")

    if minimum >= maximum:
        raise ValueError("argument 'minimum' cannot be smaller or equal to 'maximum'")
    
    if quantity < 1:
        raise ValueError("argument 'quantity' cannot be less than 1")
    
    if minimum is None and not maximum is None:
        raise TypeError("RanInt() missing 1 required positional argument: 'minimum'")
    
    if not minimum is None and maximum is None:
        raise TypeError("RanInt() missing 1 required positional argument: 'maximum'")
    
    if not minimum is None and not maximum is None:
        
        if avg is None or avg == "":
            
            # Direct generation of random number(s)

            ranints = []
            
            while quantity > 0:
                ranints.append(random.randint(int(minimum), int(maximum)))
                quantity -= 1
            
            return ranints
        
        else:
            
            # Validity check for avg

            valid = "|" in avg
            
            if valid == False:
                raise ValueError("invalid argument for 'avg'; missing '|'")

            # Taking average of several random numbers
            
            else:
                avg = str(avg)
                ranints = []
                avgl = avg.split("|")
                atype = avgl[1]
            
            # Value validity check
            
                try:
                    iterations = int(avgl[0])
                except:
                    raise ValueError("invalid argument for 'avg'")
            
                real_iterations = iterations
            
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
                
                # Random average

                    if atype == "rand":
                        a = random.randint(1, 3)
                    else:
                        a = 4
                
                # Mean taken
                
                    if atype == "mean" or a == 1:
                        deci = str(sum(numlist) / len(numlist))
                        if int(deci[-1:]) >= 5:
                            ranints.append(math.ceil(float(deci)))
                        else:
                            ranints.append(math.floor(float(deci)))
                
                # Median taken

                    elif atype == "median" or a == 2:
                        ranints.append(round(statistics.median(numlist)))
                
                # Mode taken

                    elif atype == "mode" or a == 3:
                        ranints.append(max(set(numlist), key = numlist.count))
                
                    else:
                        raise ValueError("invalid argument for 'avg'")
                    
                    quantity -= 1
                
                return ranints
