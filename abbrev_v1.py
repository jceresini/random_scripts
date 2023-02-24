from typing import List

def abbreviate(in_str: str, keep_len: int=None)-> List[str]:


    
    abbrevs = []

    if keep_len is None:
        keep_len = len(in_str)
        
    if len(in_str) < keep_len:
        raise ValueError("Bad input")

    for i in range(len(in_str) - keep_len + 1) :
        start_char = i
        end_char = i + keep_len
        mid_chars = in_str[start_char:end_char]
        start_ones_count = start_char
        end_ones_count = len(in_str) - start_ones_count - keep_len

        abbrev_str = (
            "1"*start_ones_count +
            mid_chars +
            "1"*end_ones_count
        )


        abbrevs.append(abbrev_str)

    if keep_len > 1:
        abbrevs += abbreviate(in_str, keep_len-1)
    else:
        # Also include the case where we replace ever character with '1'
        abbrevs.append('1' * len(in_str))

    # We no longer need to convert to a set because we don't get duplicates
    return abbrevs
