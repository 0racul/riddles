



alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

source_str = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj")

result_str = []

for str_symbol in source_str:

    if str_symbol not in [" ", ",", ".", "(", ")", "'"]:

        match = alphabet.index(str_symbol)
        match_plus = match + 2

        if match_plus < len(alphabet):
            result = result_str.append(alphabet[match_plus])

        elif match_plus >= len(alphabet):
            match_minus = match_plus - len(alphabet)
            result = result_str.append(alphabet[match_minus])

        else:
            result = result_str.append(alphabet[match_plus - 1])
    else:

        result = result_str.append(str_symbol)


print(*result_str)



