def convert_quality(line):
    line = line.strip('\n')  # just in case we forgot
    result = []  # prepare a container
    for letter in line:
        score = ord(letter)-33
        if score < 0 or score > 41:
            print ("ERROR: Unexpected integer value in convert_quality(): ", score)
            return None
        result.append(score)
    return(result)
