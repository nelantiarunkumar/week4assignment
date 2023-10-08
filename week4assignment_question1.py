def extract_key_value_pairs(ceo_items):
    key_value_pairs = []  
    
    
#Following that, the function will return a list of tuples containing all of the key-value pairs from the dictionary and its nested dictionaries.
    def recursive_fun(dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                recursive_fun(value)
            else:
                key_value_pairs.append((key, value))

    recursive_fun(ceo_items)
    return key_value_pairs

#Dictionary for CEO's to be return in valu key pairs
ceo_dict = {
    'arun': 'kumar',
    'pranav': {
        'sundhar': 'pichai',
        'kumar': {
            'sathya': 'Nadella',
            'Aman': 'Gupta'
        }
    }
}

#Printing key value pairs
keyValuePairs = extract_key_value_pairs(ceo_dict)
print(keyValuePairs)


#Output
'''
[('arun', 'kumar'), ('sundhar', 'pichai'), ('sathya', 'Nadella'), ('Aman', 'Gupta')]
>
'''
#Explanation
#To extract key-value pairs from a nested dictionary, use the Python script extract_key_value_pairs.py that is available in this repository. The script offers a flexible way of traversing through intricate nested dictionaries and extracting all key-value combinations, which can be helpful for a variety of data processing jobs.
