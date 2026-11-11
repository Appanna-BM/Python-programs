'''def longest_prefix(list):
    first_str=list[0]
    print(first_str)
    output=""
    for i in range(len(first_str)):
        for words in list[1:]:
            if i>=len(words) or words[i]!=first_str[i]:
                return output
        output+=first_str[i]
    return output
list=["flower","flow","flight"]
r=longest_prefix(list)
print(r)
'''
#second method
def longest_prefix(list):
    srt_list=sorted(list)
    frst_word=srt_list[0]
    lst_word=srt_list[len(list)-1]
    output=""
    for i,j in zip(frst_word, lst_word):
        if i!=j:
            return output
        output+=i
    return output
list=["flower","flow","flight"]
r=longest_prefix(list)
print(r)