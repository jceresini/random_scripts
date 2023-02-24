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

        start_chars = in_str[:start_char]
        end_chars = in_str[start_char+keep_len:]

        abbrev_str = f"{start_chars}{len(mid_chars)}{end_chars}"

        abbrevs.append(abbrev_str)

    if keep_len > 1:
        abbrevs += abbreviate(in_str, keep_len-1)
    else:
        # Treating this as a special case so we don't merge all combinations of
        # start/end chars when there are 0 inbetween
        abbrevs.append(str(len(in_str)))

    return abbrevs
