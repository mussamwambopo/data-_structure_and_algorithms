import itertools
def two_indices(nums,target):  
    return
nums = [val for val in nums if val <= target]

combinations = list(itertools.combinations(nums, 2))

    
totals = [comb for comb in combinations if sum(comb) == target]

    
answerDict = {}

    
for i,answer in enumerate(totals):
        indexes = []
        for list_item in answer:
            indexes.append(nums.index(list_item))

        answerDict[i] = {"Values":answer,"Index":indexes}
if two_indices =="_main_":
        two_indices