from typing import List

def abbreviate(in_str: str, abbrev_len: int=None)-> List[str]:

    abbrevs = []

    if abbrev_len is None:
        abbrev_len = len(in_str)
        
    if len(in_str) < abbrev_len:
        raise ValueError("Bad input")

    for start_char_index in range(len(in_str) - abbrev_len + 1) :
        end_char_index = start_char_index + abbrev_len

        start_chars = in_str[:start_char_index]
        end_chars = in_str[start_char_index+abbrev_len:]

        abbrev_str = f"{start_chars}{str(abbrev_len)}{end_chars}"

        abbrevs.append(abbrev_str)

    if abbrev_len > 1:
        abbrevs += abbreviate(in_str, abbrev_len-1)
    else:
        # Treating this as a special case so we don't merge all combinations of
        # start/end chars when there are 0 inbetween
        abbrevs.append(in_str)

    return abbrevs
