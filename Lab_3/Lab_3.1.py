


def sum_of_2_min(ls):
    if len(ls) < 4:
        raise ValueError("Список повинен містити мінімум 4 числа.")
    
    min1 = float('inf')
    min2 = float('inf')

    for x in ls:
        if x > 0 :
            if x < min1:

                min2 = min1 
                min1 = x

            elif x < min2:
                min2 = x


    return min1 + min2




ls = [1, 15, 14, 25, 13, 19, 21]

print(sum_of_2_min(ls))