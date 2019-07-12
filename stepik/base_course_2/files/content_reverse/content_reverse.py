with open('in.txt', 'r') as input, open('out.txt', 'w') as out:
    input_list = [i.rstrip() for i in input][::-1]
    out.write("\n".join(input_list))