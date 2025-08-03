integer = 5
string = "John"
float_var = 3.7

print("===")
print(type(integer))

def type_to_str(variable):
    variable_type = type(variable)
    variable_str = str(variable_type)
    return variable_str

print("integer is " + type_to_str(integer))
print("string is " + type_to_str(string))
print("float is " + type_to_str(float_var))


