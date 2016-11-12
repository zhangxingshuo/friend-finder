'''
Given the raw html file, the script will find all the names and profile urls
of the Facebook profiles contained within the html file
'''

import re

raw_html = open('sel_out_andy.txt','r').read()

# Find the string 'Add [<name>] as a friend', which is unique to friends
starts = [m.start() for m in re.finditer('aria-label="Add ', raw_html)]
url_starts = [m.start() for m in re.finditer('div class="fsl fwb fcb"', raw_html)]

name_chunks = []

for start in starts[:-1]:
    # slice out start
    start_index = start+16
    end_index = start_index
    # find the end
    while raw_html[end_index] != '"':
        end_index += 1
    # slice out end
    end_index -= 12
    name_chunks.append(raw_html[start_index:end_index])

# get the urls of the profiles
urls = []
for start in url_starts:
    start_index = start+33
    end_index = start_index
    while raw_html[end_index] != '"':
        end_index += 1
    end_index -= 36
    urls.append(raw_html[start_index:end_index])

names = {}
for i in range(len(name_chunks)):
    names[name_chunks[i]] = urls[i]