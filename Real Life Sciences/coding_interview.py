import re #regular expressions
import os #system and files

def get_frequency_of_words(input_file, output_file):
    """
    Assuming nothing wrong with file like the problem suggests.
    This returns the frequency of all words in the file.
    """
    freq = {}

    """
    open file and lowercase everything to make easy matching
    (O)n - read in each letter, and then 
    (O)n - lower every letter
    """
    data =  open('{}'.format(input_file), 'r').read().lower()

    """
    (O)n - only needs to go through each character once to find boundaries.

    Regular Expression
    1. \b (word boundary) 
        - excludes all the unecessary space, punctuations and breaks.
    2. [a-z0-9]
        - I lower cased everything so we only need to match numbers and letters
    3. {1,}
        - assuming we want all words lengths, {1,} should give all words of length 1 or higher.
    """
    match_pattern = re.findall(r'\b[a-z0-9]{1,}\b', data)


    """
    Alternative to the next section:
    from collections import Counter
    Counter(match_pattern)

    no package solution:
    (O)n' - iterate through list
    (O)n' - search dict
    """
    for word in match_pattern:
        count = freq.get(word, 0)
        freq[word] = count + 1

    """
    Remove file if it exists because it will append.
    """
    try:
        os.remove(output_file)
    except OSError:
        pass
    
    # Open file to write
    f = open("{}".format(output_file), "a")
    
    """
    (O)n' - iterations, but only once through dict to sort and etc.
    we could have easily just taken the key as well
    e.g.
    for key in sorted(freq.keys()):
        f.write("{} : {}\n".format(key, freq[key]))
        
    TOTAL TIME COMPLEXITY: (O)n
    """
    for key, value in sorted(freq.items()):
        f.write("{} : {}\n".format(key, value))