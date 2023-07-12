# Utility functions for CC type game engine

def join_str_list(str_list):
    # return string list as a string in the format 'a' or 'a' and 'b' or 'a, b and c'
    if len(str_list) == 1:
        return str_list[0]
    else:
        return f"{', '.join(str_list[:-1])} and {str_list[-1]}"



