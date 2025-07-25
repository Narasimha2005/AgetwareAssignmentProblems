def convert_num(num):
    [int_part,decimal_part] = str(num).split(".")
    ans = ""
    k=0
    if(len(int_part)>3):
        ans += "," + int_part[-3:]
        for i in range(len(int_part)-4,-1,-1):
            if(k==2):
                ans = "," + ans
                k=0
            ans = int_part[i] + ans
            k+=1
    else:
        ans = int_part
    ans += "."+str(decimal_part)
    return ans


print(convert_num(1456.7891))
print(convert_num(17698323456.7891))
