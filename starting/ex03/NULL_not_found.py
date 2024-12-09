
def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if isinstance(object, float) and object != object:
        print(f"Cheese: {object} {obj_type}")
        return (0)
    elif object:
        print("Type not Found")
        return (1)
    if object is None:
        print(f"Nothing: {object} {obj_type}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {obj_type}")
    elif isinstance(object, int):
        print(f"Zero: {object} {obj_type}")
    elif isinstance(object, str):
        print(f"Empty: {object} {obj_type}")
    return (0)