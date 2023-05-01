import itertools

def get_indexs_of_sum(search_list, search_val):  

    #remove any values higher than the search val
    search_list = [val for val in search_list if val <= search_val]

    #get all combinations with 2 elements    
    combinations = list(itertools.combinations(search_list, 2))

    def
    totals = [comb for comb in combinations if sum(comb) == search_val]

    
    answerDict = {}

    
    for i,answer in enumerate(totals):
        indexes = []
        for list_item in answer:
            indexes.append(search_list.index(list_item))

        answerDict[i] = {"Values":answer,"Index":indexes}
if sum_even_numbers =="_main_":
    return answerDict