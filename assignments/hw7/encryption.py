def encode(message, key):
    word = ""
    for i in range(len(message)):
        num_m = ord(message[i])
        letter = chr(num_m + key)
        word += letter
    return word

def encode_better(phrase, key_phrase, file_name):
   ret =" "
   for i in range(len(phrase)):
        num_m = ord(phrase[i]) - 65
        num_k = ord(key_phrase[i % len(key_phrase)]) - 65
        number = ((num_m + num_k) % 58) + 65
        cipher_text = chr(number)
        ret+=cipher_text
   file = open(file_name, "a")
   file.write(ret)