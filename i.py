class PairElements:

    def twoSum(self, nums, target):
        lookup={}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target - num],i
            lookup[num]=i

        return None  

value=int(input("Enter sum for which you want to make this search: "))

result=PairElements().twoSum((10, 20, 30, 40, 50, 60, 70), value)

if result:
    print("index1=%d, index2=%d" % result)
else:
    print("No two elements found with the given sum")
