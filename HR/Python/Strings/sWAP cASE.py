def swap_case(s):
    output = '';
    for char in s:
        if(char.isupper() == True):
            output += (char.lower());
        elif(char.islower() == True):
            output += (char.upper());
        else:
            output += char;
    return output