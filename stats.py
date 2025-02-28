def word_count(text):
    return len(text.split())

def character_count(text):
    #count = text.lower().count('c')
    #return count
    letters = {}
    for s in text.lower():
        # If the character is in the dictionary, increment its count
        if s in letters:
            letters[s] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            letters[s] = 1
    return letters

def sorted_list(char_dict):
    # First, we need to create a list of dictionaries from our character dictionary
    char_list = []
    
    # For each character and count in the dictionary
    for char, count in char_dict.items():
        # Add a new dictionary to our list
        char_list.append({"char": char, "count": count})
    
    # Now we can sort the list
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list