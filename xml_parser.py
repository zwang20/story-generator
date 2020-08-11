# import xml.etree.ElementTree as ET

# print('Parsing xml File')
# tree = ET.parse('simplewiki.xml')
# root = tree.geroot()
# print('Done')

import os
import pickle
import string

with open("Stories/"+'simplewiki.txt', 'wb') as output_file:
    with open('simplewiki.xml') as input_file:
        output_list = []
        try:
            for j in input_file:
                for k in j.strip().split(' '):
                    if k.translate(str.maketrans('', '', string.punctuation)):
                        # try:
                        #     k.decode('ascii')
                        # except UnicodeDecodeError:
                        #     pass
                        # else:
                            output_list.append(k.lower())
        except UnicodeDecodeError:
            pass
        pickle.dump(output_list, output_file)
