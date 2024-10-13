from typing import Dict, List

# quick_sort: IN-PLACE Quick Sort that takes a list of clash cards and sorts them based on the sort key.
# Stores results into the original cards list.
# **************************************** 
# cards: a list of dictionaries that represent cards with keys "Name" and "Cost"
# sort_key: name of the key to sort on (either "Name" or "Cost")
# return: None - sorts in place
def quick_sort(cards:List[Dict], sort_key: str)->None:
    quick_sort_extra(cards, sort_key, 0, len(cards)-1)



# new cooler method
def quick_sort_extra(cards, sort_key, start, end):

    # BASE CASE
    if start >= end:
        return
    
    # Select pivot
    pivot_index = start
    pivot_value = cards[pivot_index][sort_key]

    i = start + 1
    j = end
    
    # keep going until i and j have crossed
    while i <= j:

        # increment until something larger than the pivot value
        while (i <= j) and (cards[i][sort_key] <= pivot_value):
            i += 1

        # increment until something smaller than the pivot value
        while (i <= j) and (cards[j][sort_key] > pivot_value):
            j -= 1

        if i < j:
            temp:int = cards[i]
            cards[i] = cards[j]
            cards[j] = temp

    # Swap pivot
    temp:int = cards[pivot_index]
    cards[pivot_index] = cards[j]
    cards[j] = temp
    
    # Recurse.
    quick_sort_extra(cards, sort_key, start, j-1)
    quick_sort_extra(cards, sort_key, j+1, end)

