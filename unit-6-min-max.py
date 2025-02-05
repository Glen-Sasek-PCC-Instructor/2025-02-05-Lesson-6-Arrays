def main():
    nums = [3, -2, 4, 10, -6]

    print("array:", nums)

    print("min:", findMin(nums))

def findMin(n):
    # in this function, the array is called n
    min = n[0] # always set min/max to cell 0!
    length = len(n) # get the number of elements

    # loop through all of the elements
    for index in range(length):
        if n[index] < min:
            min = n[index]

    return min

main()