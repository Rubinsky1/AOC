from collections import Counter

def text_to_binary(text):
    binary_representation = []
    for char in text:
        # Convert each character to its binary representation
        binary_representation.append(format(ord(char), '08b'))
    return binary_representation

def binary_to_decimal(binary_list):
    decimal_representation = []
    for binary in binary_list:
        # Convert each binary string to its decimal equivalent
        decimal_representation.append(int(binary, 2))
    return decimal_representation

def save_array_to_file(array, filename):
    with open(filename, "w") as file:
        for element in array:
            file.write(str(element) + "\n")

# Test de functie met een spatie
text = "5!$7u(6B#@zq()!x4&2y35e7uw@s^8*(tqkzxe@65y)30y2!^1&73u) wqLyi&50@#82^)4x$78@q6w*k51z(z32!uy&05s3#a,xqw2k^$ (u@#6*680Geq37w#)4!31(@z2x^k5f50ue&q@^l*z*)$*k78yi(09c&x5#(((!6qu^23)*@#1kiw2^q(*t9ek5&15$0e@qu2y!6)#&4wyrz^3x(kd9y*& @0j689@)$68w^!k#q5^94u5*(2781z6&)0^5@z@6ewx3##!^ 80*$bew(2k)7q8903#15&)u4n@6@^*82z!()zxyt a84$kwa92z)0#^wu*76@801&ng5k(36)1!z$^9e5y*nxu4)k2#om@87xz(y4&63**^1q$)e!n.u9)k1 w84#^6H))(0*y@q72xe!t &$u^li1969)*q38(zgwt #4o@u1zx$^94)&!(p3 977*)dexz v9)^y1@l#kieq($w4rk!&$^^71x&in9g3w$(y4"
binary_result = text_to_binary(text)
binary_to_decimal(binary_result)
ascii = binary_to_decimal(binary_result)
save_array_to_file(ascii, "test.txt")


