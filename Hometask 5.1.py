import keyword
import string

def is_valid_variable_name(name: str) -> bool:
    if name in keyword.kwlist:
        return False
    if name[0].isdigit():
        return False
    for char in name:
        if char.isupper() or char in string.punctuation.replace("_", "") or char.isspace():
            return False
    if name.count("_") > 1:
        return False

    return True

variable_names = ["_", "__", "___", "x", "get_value", "get value", "get!value", "some_super_puper_value",
                  "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"]

for name in variable_names:
    result = is_valid_variable_name(name)
    print(f"{name} => {result}")