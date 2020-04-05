#Made by https://github.com/HiteshKumarSaini/

from urllib.request import urlopen

keyword = str(input("Enter a keyword to search in youtube:")) #KEYWORD INPUT

page = str(urlopen(("https://www.youtube.com/results?search_query=%s&disable_polymer=1" %keyword)).read())
page_source = page.split()

temp = 0

link_output = [] #OUTPUT VIDEO LINKS FROM SEARCH
title_output = [] #OUTPUT TITLE LINKS FROM SEARCH


for index in range(0, len(page_source)-1, 1):
    element = page_source[index]
    element_next = page_source[index+1]
    if (element[0:23] == 'data-sessionlink="itct=') and (element_next[0:7] == 'title="'):
        buffer = ""
        init = page_source[index+1]
        buffer+=init
        sub_index = index+2
        end = index+22
        while sub_index<end:
            this_element = page_source[sub_index]
            next_element = page_source[sub_index+1]
            if (this_element[len(this_element)-1])== '"':
                if next_element == 'rel="spf-prefetch"':
                    buffer+=(" "+this_element)
                    title_output.append(buffer)
                    break
            else:
                buffer+=(" "+this_element)
            sub_index+=1


for element in page_source :
    if element[0:15] == 'href="/watch?v=' and len('www.youtube.com'+element[6:len(element)-1]) == 35:
        temp+=1
        if temp%2 ==0:
            link_output+=['www.youtube.com'+element[6:len(element)-1]]
            
            
for index in range(0,len(link_output)):
    print(link_output[index], title_output[index]) #SHOWING OUTPUT
