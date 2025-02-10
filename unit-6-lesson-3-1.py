#Written by Gayathri Iyer
#Notice we print the 5 elements one at a time.

def main():
    nums = [2, -3, 10, -1, 7]

    print(nums)
    print(0, nums[0])
    print(1, nums[1])
    print(2, nums[2])
    print(3, nums[3])
    print(4, nums[4])

    print("")
    print(nums)
    print("nums[0] ", nums[0])
    print("nums[1] ", nums[1])
    print("nums[2] ", nums[2])
    print("nums[3] ", nums[3])
    print("nums[4] ", nums[4])

    print("")
    print(nums)
    for i in range(0, len(nums)):
        print(i, nums[i])

main()