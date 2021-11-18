[101, 102, 103, 105, 106, 107, 108, 109, 110, 115, 116, 100000000101]

def binary_search(list1, item_to_search):
    """
    This is "docstring" aka document string.
    This function searches for item in list1.
    Returns True if present, False if absent.
    """
    #print (item_to_search)
    low = 0
    high = len(list1) - 1
    #if (item_to_search < list1[low]) or (item_to_search > list1[high - 1]):
    #    return False
    while high >= low:
        mid_index = (high + low) // 2
        #print (low, mid_index, high)
        mid_item = list1[mid_index]
        if item_to_search == mid_item:
            return True
        elif item_to_search > mid_item:
            low = mid_index + 1
        else: # item_to_search < mid_item
            high = mid_index - 1
    return False

assert binary_search([1,2,3,4,5,6,7], 1) == True, "1 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 2) == True, "2 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 3) == True, "3 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 4) == True, "4 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 5) == True, "5 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 6) == True, "6 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 7) == True, "7 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 8) == False, "8 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 3.5) == False, "3.5 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 4.5) == False, "4.5 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 5.5) == False, "5.5 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 0) == False, "0 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 100) == False, "100 working incorrectly"
assert binary_search([1,2,3,4,5,6,7], 6.5) == False, "6.5 working incorrectly"


def binary(list,mynumber):
    list = sorted(list)
    print(list)
    while True:
        
        a = int(len(list)//2)
        cislo_a = list[a]
        over = None        
        if cislo_a == mynumber:
           list = [mynumber]
           over = True           
           print("got it")
           return True       
        if cislo_a > mynumber:
           list = list[:a]
           min_number = cislo_a
           print(list)
        if cislo_a < mynumber:
           list = list[a:]
           max_number = cislo_a
           print(list)
        if len(list) <= 1 and over is not True:
           print("number not found")
           return False

assert binary([1,2,3,4,5,6,7], 1) == True, "1 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 2) == True, "2 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 3) == True, "3 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 4) == True, "4 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 5) == True, "5 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 6) == True, "6 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 7) == True, "7 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 8) == False, "8 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 3.5) == False, "3.5 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 4.5) == False, "4.5 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 5.5) == False, "5.5 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 0) == False, "0 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 100) == False, "100 working incorrectly in new algorithm"
assert binary([1,2,3,4,5,6,7], 6.5) == False, "6.5 working incorrectly in new algorithm"