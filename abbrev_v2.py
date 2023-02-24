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

        start = str(start_ones_count) if start_ones_count > 0 else ""
        end = str(end_ones_count) if end_ones_count > 0 else ""

        abbrev_str = f"{start}{mid_chars}{end}"

        abbrevs.append(abbrev_str)

    if keep_len > 1:
        abbrevs += abbreviate(in_str, keep_len-1)
    else:
        # Treating this as a special case so we don't merge all combinations of
        # start/end chars when there are 0 inbetween
        abbrevs.append(str(len(in_str)))

    return abbrevs
