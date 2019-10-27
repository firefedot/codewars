# my way
def flatten(*tmp_list, flat_list = None):
    if flat_list is None:
        flat_list = []
   # flat_list = [ [flatten(unlist) for unlist in sublist] if isinstance(sublist, (list)) else flat_list.append(sublist) for sublist in tmp_list]
    for sublist in tmp_list:
        # [flatten(unlist) for unlist in sublist] if isinstance(sublist,(list)) else flat_list.append(sublist)
        if isinstance(sublist,(list)):
            for unlist in sublist:
                flatten(unlist,flat_list=flat_list)
        else:
            flat_list.append(sublist)
    # flat_list.clear()
    a = flat_list.copy()
     # flat_list.clear()
    return flat_list

# BEST - practices
# def flatten(*args):
#     return [x for a in args for x in (flatten(*a) if isinstance(a, list) else [a])]

print(flatten(['hello',2,['text',[4,5]]],[[]],'[list]'))
print(flatten(['hello',2,['iuiui',[4,5]]],[[]],'[list]'))
