import os
import pickle
import string

for i in os.listdir("Stories"):
    if 'txt' in i:
        if not os.path.exists("SStories/"+i):
            with open("./SStories/"+i, 'wb') as output_file:
                with open("Stories/"+i) as input_file:
                    output_list = []
                    try:
                        for j in input_file:
                            for k in j.strip().split(' '):
                                if k.translate(str.maketrans('', '', string.punctuation)):
                                    try:
                                        k.decode('ascii')
                                    except UnicodeDecodeError:
                                        pass
                                    else:
                                        output_list.append(k.lower())
                    except UnicodeDecodeError:
                        pass
                    pickle.dump(output_list, output_file)
# print(os.listdir("Stories"))
