def second_largest(nums):
    nums=list(set(nums))
    nums.sort(reverse=True)
    if len(nums)<2:
        return False
    else:
        return nums[1]
    
def main():
    numbers=list(map(int,input("enter a list of numbers: ").split()))
    secondlargest=second_largest(numbers)
    if secondlargest:
        print(f"the second largest number is {secondlargest}")
    else:
        print(f"there is no second largest number, all are unique")
        
main()