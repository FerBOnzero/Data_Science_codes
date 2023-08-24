from collections import Counter
from itertools import combinations

# Transactions example
transactions = [
    {'pan', 'mantequilla', 'leche', 'gelatina', 'queso'},
    {'huevos', 'leche', 'yogurt', 'chocolate'},
    {'pan', 'queso', 'huevos', 'leche'},
    {'huevos', 'leche', 'galletas', 'pan'},
    {'queso', 'leche', 'galletas'},
    {'pan', 'huevo', 'cafe'},
    {'cafe', 'pan', 'yogurt'},
    {'galleta', 'pan', 'leche'},
    {'cafe', 'leche', 'queso', 'galletas', 'yogurt'}
]

min_support = 0.3
min_confidence = 0.4

def apriori(data, supmin, confmin): 
    data_len = len(data)
    max_length = max(len(s) for s in data)
    print(max_length)
    supports = []

    k = 1
    # Create a Counter to store the element counts
    element_counter = Counter()

    # Iterate through each dictionary in the list
    for transaction in transactions:
        element_counter.update(transaction)
    
    # Storage the element counts
    element_count_dict = dict(element_counter)
    keys_to_remove = []

    for i in element_count_dict.keys():
        element_count_dict[i] = element_count_dict[i] / data_len
        if element_count_dict[i] < supmin:
            keys_to_remove.append(i)

    for key in keys_to_remove:
        del element_count_dict[key]
    
    supports.append(element_count_dict)
    products = element_count_dict.keys()

    k += 1
    try:
        while k<=max_length:
            combinations_list = set(combinations(products, k))
            element_counter = Counter()
            # Count how many times each combination appears in transactions
            for combination in combinations_list:
                count = sum(1 for transaction in transactions if set(combination).issubset(transaction))
                element_counter[combination] = count
            element_count_dict = element_counter

            for i in element_count_dict.keys():
                element_count_dict[i] = element_count_dict[i] / data_len
                if element_count_dict[i] < supmin:
                    keys_to_remove.append(i)

            for key in keys_to_remove:
                del element_count_dict[key]
                
            if not element_count_dict:
                print(f'Aquí se detiene el algoritmo con k={k}')
                break 
            
            supports.append(dict(element_count_dict))
            products = combinations_list
            products = {element for tup in products for element in tup}

            k += 1
    except: 
        print(f'Terminó para k={k}')

    return supports

print(apriori(transactions, min_support, min_confidence))