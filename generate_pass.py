import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
"""def generate_password():
    data_password=""
    for i in range(3):
        p_index=random.randint(0,len(word_list)-1)
        print(p_index,word_list[p_index])
        data_password +=word_list[p_index]
# It should return a string consisting of three random words 
    return data_password
# concatenated together without spaces"""



"""def generate_password():
    data_password=""
    data_password=''.join(random.sample(word_list,3))
    return data_password
# concatenated together without spaces"""

def generate_password():
    data_password=""
    for i in range(3):
        
        data_password +=random.choice(word_list)
    return data_password
# concatenated together without spaces

# test your function
print(generate_password())
