def convert_F_to_C(tempF):
    return (tempF -32) * 5/9

def convert_F_to_K(tempF):
    tempC = convert_F_to_C(tempF)
    return convert_C_to_K(tempC)

def convert_C_to_F(tempC):
    return tempC * 9/5 + 32

def convert_C_to_K(tempC):
    return tempC + 273.15

def convert_K_to_F(tempK):
    tempC = convert_K_to_C(tempK)
    return convert_C_to_F(tempC)

def convert_K_to_C(tempK):
    return tempK - 273.15

conversions = {
    ('c','k'): convert_C_to_K,
    ('c','f'): convert_C_to_F,
    ('f','c'): convert_F_to_C,
    ('f','k'): convert_F_to_K,
    ('k','c'): convert_K_to_C,
    ('k','f'): convert_K_to_F,
}

def convert(temp, from_unit, to_unit):
    if from_unit.lower() == 'k' and temp < 0:
        temp = -1 * temp
    return conversions[from_unit.lower(), to_unit.lower()](temp)
    
