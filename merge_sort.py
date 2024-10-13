from typing import Dict, List

# merge_sort: takes a list of clash cards and sorts them based on the sort key.
# Merges results into the original cards list
# **************************************** 
# cards: a list of dictionaries that represent cards with keys "Name" and "Cost"
# sort_key: name of the key to sort on (either "Name" or "Cost")
# return: None - sorted results are stored directly in cards
def merge_sort(cards: List[Dict], sort_key: str)->None:

    # BASE CASE
    if len(cards) <= 1:
        return


    # RECURSIVE CASE

    # split the list of cards into two halves
    mid = len(cards) // 2
    first_half = cards[:mid]
    second_half = cards[mid:]

    # recurse for both halves
    merge_sort(first_half, sort_key)
    merge_sort(second_half, sort_key)


    i: int = 0
    j: int = 0
    k: int = 0

    # do until one of the halves is used up
    while (i < len(first_half)) and (j < len(second_half)):
        if first_half[i][sort_key] < second_half[j][sort_key]:
            cards[k] = first_half[i]
            i += 1
        else:
            cards[k] = second_half[j]
            j += 1
        k += 1


    # finish using up second half
    while j < len(second_half):
        cards[k] = second_half[j]
        j += 1
        k += 1

    # finish using up first half
    while i < len(first_half):
        cards[k] = first_half[i]
        i += 1
        k += 1


    

    
