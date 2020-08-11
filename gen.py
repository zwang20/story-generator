import pickle
import random

with open('Data/dict.txt', 'rb') as input_file:
    word_dict = pickle.load(input_file)
with open('Data/end_dict.txt', 'rb') as input_file:
    end_word_dict = pickle.load(input_file)

for i in range(1):
    sentence_length = 0
    output_text = ''
    current_token = 'the'
    output_text = output_text+current_token+' '
    sentence_length += 1
    word_count = 0
    while True:
        try:
            if sentence_length > 10:
                try:
                    current_token = random.choice(end_word_dict[current_token])
                    output_text = output_text+current_token+' '
                    sentence_length = 0
                except KeyError:
                    pass
            current_token = random.choice(word_dict[current_token])
            output_text = output_text+current_token+' '
            if any([
                '.' in current_token,
                '!' in current_token,
                '?' in current_token,
            ]):
                sentence_length = 0
            else:
                sentence_length += 1
            if len(output_text) > 1000:
                break
            word_count += 1
        except IndexError:
            break
        except KeyError:
            break
        # if sentence_length == 0:
        #     break
        # if word_count > 100:
        #     break
    print(output_text)
