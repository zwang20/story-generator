import os
import pickle

# generate normal dictionary
out_dict = {}
# for i in os.listdir("SStories"):
for i in ['simplewiki.txt']:
    if 'txt' in i:
        with open("SStories/"+i, 'rb') as input_file:
            word_list = pickle.load(input_file)
            for j in range(len(word_list)-1):
                try:
                    out_dict[word_list[j]].append(word_list[j+1])
                except KeyError:
                    out_dict[word_list[j]] = [word_list[j+1]]
with open('Data/dict.txt', 'wb') as output_file:
    pickle.dump(out_dict, output_file)

# generate ending dictionary
out_dict = {}
# for i in os.listdir("SStories"):
for i in ['simplewiki.txt']:
    if 'txt' in i:
        with open("SStories/"+i, 'rb') as input_file:
            word_list = pickle.load(input_file)
            for j in range(len(word_list)-1):
                if any([
                    '.' in word_list[j],
                    '?' in word_list[j],
                    '!' in word_list[j],
                ]):
                    try:
                        out_dict[word_list[j]].append(word_list[j+1])
                    except KeyError:
                        out_dict[word_list[j]] = [word_list[j+1]]
with open('Data/end_dict.txt', 'wb') as output_file:
    pickle.dump(out_dict, output_file)
