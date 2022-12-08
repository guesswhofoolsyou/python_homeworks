# RLE алгоритм

nums = '12345679'

def rle_enc(data):
    data_list = []
    for i in data:
        data_list.append(i)
    result = ''
    current = data_list.pop(0)
    counter = 1
    for i in data_list:
        if i == current:
            counter += 1
        else:
            result += f'{counter}{current}'
            current = i
            counter = 1
    result += f'{counter}{current}'
    return result

def rle_dec(data):
    data_list = []
    for i in data:
        data_list.append(i)
    result = ''
    for j in range (0, len(data_list)):
        if data_list[j].isdigit() == True:
            times = int(data_list[j])
            for k in range(1, times):
                result += f'{data_list[j+1]}'
        else:
            result += f'{data_list[j]}'
    return result

# data = open('Homeworks/Seminar_4/rle-enc.txt','w')
# enc_txt=input('Введите текст:\n')
# data.writelines(enc_txt)
# data.close()

# encoding = open('Homeworks/Seminar_4/rle-enc.txt','r')
# enc_mssg = encoding.read()
# enc_mssg = rle_enc(enc_mssg)
# print (enc_mssg)

decoding_txt = open('Homeworks/Seminar_4/rle-dec.txt','r')
dec_text = decoding_txt.readline()
print (dec_text)
print (rle_dec(dec_text))

