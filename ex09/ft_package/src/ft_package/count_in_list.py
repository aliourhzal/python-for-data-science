
def count_in_list(arr: list, target: str) -> int:
    filter_obj = filter(lambda str: str == target, arr)
    filtered = list(filter_obj)
    return (len(filtered))
