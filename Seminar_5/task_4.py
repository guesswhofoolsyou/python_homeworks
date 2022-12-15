# функции, списки, кортеже и rock'n'roll

def split(s):
    return [char for char in s]

def zip_list(lang_list, lang_num):
    for i in range(0,len(lang_list)):
        lang_list[i] = lang_list[i].upper()
    lang_zip = zip(lang_num, lang_list)
    zipped_list = list(lang_zip)
    print (zipped_list)


def uni_ziplist(lang_list, lang_num): 
    lang_uni = []
    for i in lang_list:
        temp = 0
        temp_sum = 0
        for j in i:
            temp = ord(j)
            temp_sum += temp
        lang_uni.append(temp_sum)
    uni_num = []
    uni_list = []
    for i in range(1, len(lang_num)+1):
        if str(i) in split(str(lang_uni[i-1])):
            uni_list.append(lang_list[i-1])
            uni_num.append(i)
    uni_zip = list(zip(uni_num, uni_list))
    print (uni_zip)

lang_list = ['c#', 'python', 'c++', 'turbo pascal', 'javascript', 'delphi']
lang_num = ['1', '2', '3', '4', '5', '6']

zip_list(lang_list, lang_num)
uni_ziplist(lang_list, lang_num)