def ceaser_cipher(str,coding_type,k):
    new_str = ""
    if(coding_type=="encoding"):
        for i in str:
            if(i.isupper()):
                new_str += chr((ord(i)-k-65)%26+65)
            else:
                new_str += chr((ord(i)-k-97)%26+97)
        return new_str
    elif(coding_type=="decoding"):
        for i in str:
            if(i.isupper()):
                new_str += chr((ord(i)+k-65)%26+65)
            else:
                new_str += chr((ord(i)+k-97)%26+97)
        return new_str

print(ceaser_cipher("narasimha","encoding",3))
print(ceaser_cipher("lahari","decoding",3))
