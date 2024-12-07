
def NULL_not_found(object: any) -> int:
    if object:
        return (1)
    obj_type = object.__class__
    if object is None:
        print(f"Nothing: {object} {obj_type}")
    elif obj_type is float:
        print(f"Cheese: {object} {obj_type}")
    elif obj_type is int:
        print(f"Zero: {object} {obj_type}")
    elif obj_type is str:
        print(f"Empty: {object} {obj_type}")
    elif obj_type is bool:
        print(f"Fake: {object} {obj_type}")
    else:
        print("Type not Found")
    return (0)

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

print(Garlic is None)

# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))