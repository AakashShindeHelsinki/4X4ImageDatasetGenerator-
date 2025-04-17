import dataval_constructor


def main():
    #Default Values
    number_of_value = 20
    pixel_diff = 0.99 # Greater than 0, Less than 1
    greator_val = None # Linear / Diagonal
    data_percent_split=0.5 # Between 0 and 1 needs greator val argument else useless
    shuffle = False # True / False
    X,y = dataval_constructor.dataval_constructor(number_of_value, pixel_diff, greator_val, data_percent_split, shuffle)
    print(X)
    return X,y

if __name__ == "__main__":
    main()