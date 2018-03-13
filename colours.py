# colours.py facilitates conversion between the hex RGB format to dec and binary

# a hex number in the format #RRGGBB to decimal
def hex_to_dec(col):
    answer = []
    answer.append(["red", int(col[1:3], 16)])
    answer.append(["green", int(col[3:5], 16)])
    answer.append(["blue",int(col[5:7], 16)])
    return answer


# a hex number in the format #RRGGBB to 8bit binary
def hex_to_bin(col):
    answer = hex_to_dec(col)
    for x in range(0,3):
        answer[x][1] = bin(answer[x][1])[2:]
        bin_len = len(answer[x][1])
        if bin_len != 8:
            str = (8-bin_len)*"0"
            answer[x][1] = str + answer[x][1]

    return answer


# calling the functions, output:
col = raw_input("Give a hex colour in the form of #RRGGBB:  ")
print "In decimal: ", hex_to_dec(col)
print 'In binary: ', hex_to_bin(col)
