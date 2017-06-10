scores = list(range(0, 42))
lst = [(score, [0]*300) for score in scores]
dic1 = dict(lst)

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

def parse_fastq(path):
	quality = []
	handle = open(path, 'rU')
	for ln, line in enumerate(handle):
		position = ln % 4
		if position == 0 and line.startswith('@'):
			continue
		elif position == 1:
			continue
		elif position == 2 and line.startswith('+'):
			continue  # do nothing
		elif position == 3:
			score = convert_quality(line)
			quality.append(score)
		else:
			print ('ERROR: Failed to parse FASTQ at line:\n', line)
	yield(quality)
