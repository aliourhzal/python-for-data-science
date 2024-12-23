
def all_thing_is_obj(object: any) -> int:
    #your code here
    obj_type = type(object)
    types_set = (list, dict, set, tuple)
    if isinstance(object, str):
        print(f"{object} is in the kitchen : {obj_type}")
    elif obj_type in types_set:
        print(f"{obj_type.__name__.capitalize()} : {obj_type}")
    else:
        print("Type not found")
    return (42)
