import math
import re


diferent_prf = 0 

def decimalToBinary(n):
    '''Convert each byte to binary and add them to the list'''
    n = n.split(".")  
    bin_ip = []
    for bajt in n:
        bajt = int(bajt)
        bajt = bin(bajt).replace("0b", "")
        if len(bajt) != 8: 
            # adding zeros if the byte is not 8 characters long
            rest = 8 - len(bajt) 
            nol = rest * "0"
            bajt = nol + str(bajt)
        bin_ip.append(bajt)
    return bin_ip

def pref(n):
    '''Take prefix and make string corresponding of converted prefix
     to binary plus rest of zeros after that it split it to bytes'''
    ones = n * "1"
    zero = (32 - n) * "0"
    ones_zeros = ones + zero
    first_bite, second_bite, third_bite, fourth_bite = "".join(ones_zeros[:8]), "".join(ones_zeros[8:16]), "".join(ones_zeros[16:24]), "".join(ones_zeros[24:32])
    # Spliting bits string to bytes
    ret = [first_bite, second_bite, third_bite, fourth_bite]
    return [ret, zero]

def suming(ip, pref):
    '''AND operation between ip adress bytes with bytes of prefix'''
    ls = []
    for sm in range(0, 4):
        sumed = bin(int(ip[sm], 2) & int(pref[sm], 2)).replace("0b", "")
        # AND operation
        if len(sumed) != 8:
            # adding zeros if the byte is not 8 characters long
            rest = 8 - len(sumed) 
            nol = rest * "0"
            sumed = nol + str(sumed)
        ls.append(sumed)
    return ls

def size_of_subnets(zeros, n_subnets):
    '''Host bits divide by number of subnets if the number of subnets is power of two'''
    size = (2 ** len(zeros)) / n_subnets
    return size

def finall_subnets(ip, size):
    '''Converting subnet bytes in binery to decimal and adding size of subnet
     and returning subnets ip adresses in list (used for size of subents in power of two)'''
    pre_sub = "".join(ip)
    subnets = []
    subnets.append(pre_sub)
    for _ in range(number_of_subnets - 1):
        pre_sub = bin(int(pre_sub,2) + int(size)).replace("0b", "")
        # adding number of hosts to ip
        pre_sub = list(pre_sub)
        if len(pre_sub) != 32:
            # Checking if the size is 32 if not, prepand zeros
            zb = 32 - len(pre_sub)
            pre_sub.insert(0, zb * '0')
        pre_sub = "".join(pre_sub)
        subnets.append(pre_sub)
    return subnets

def prefix_output(ls_divises):
    '''Counting prefixes and masks for each subnet'''
    ls_of_prf = []
    nt_full_finall = []
    for dv in ls_divises:
        nt_full = []
        # Counting prefix with logaritmus
        log = math.ceil(math.log(dv)/math.log(2))
        prf = 32 - log
        ls_of_prf.append(prf)
        full_bytes = int(prf / 8) 
        nt_full_bytes = prf % 8
        # counting full bytes
        nt_full.append(nt_full_bytes * "1")
        nt_full.append((8 - nt_full_bytes) * "0")
        # making last byte
        end_byte = int("".join(nt_full),2)
        nt_full_finall.append(full_bytes * "255." + str(end_byte))
        #prepending full bytes and last byte
    return ls_of_prf, nt_full_finall

def other_sizes_subnets(raw_ip, size):
    '''Converting subnet bytes in binery to decimal and adding size 
    of subnet and returning subnets ip adresses in list (used for not size of subents in power of two)'''
    ip = []
    conectit_raw_ip = "".join(raw_ip)
    ip.append(conectit_raw_ip)
    number_of_computers_plus_round.insert(0, int(0))
    for bin_plus in size[1:-1]:
        added = bin(int(conectit_raw_ip,2) + bin_plus).replace("0b", "")
        # adding number of hosts to ip
        added = list(added)
        if len(added) != 32:
            # Checking if the size is 32 if not, prepand zeros
            zb = 32 - len(added)
            added.insert(0, zb * '0')
        added = "".join(added)
        conectit_raw_ip = added
        ip.append(added)
    return ip

def mask(prf):
    '''Count mask from prefix'''
    ones_zeros = list((32 - prf) * "1" + prf * "0")
    # last byte
    first_bite, second_bite, third_bite, fourth_bite = "".join(ones_zeros[:8]), "".join(ones_zeros[8:16]), "".join(ones_zeros[16:24]), "".join(ones_zeros[24:32])
    # cuting to bytes
    sub_mask = [str(int(first_bite,2)), str(int(second_bite,2)), str(int(third_bite,2)), str(int(fourth_bite,2))]
    #converting from bunary to decimal
    sub_mask = ".".join(sub_mask)
    return sub_mask


def finall_convertor(ones_zeros):
    '''Formating nad printing out ip adesses and their prefix'''
    print("--------" * 7)
    for i in ones_zeros:
        bites = [int(i[:8],2), int(i[8:16],2), int(i[16:24],2), int(i[24:32],2)]
        # Converting binary bytes to decimal 
        if diferent_prf == 0:
            if len(f"{bites[3]}") == 1:
                print(f"IP: {bites[0]}.{bites[1]}.{bites[2]}.{bites[3]}   | Prefix: /{prf[0][ones_zeros.index(i)]} | Mask: {prf[1][ones_zeros.index(i)]}") 
            if len(f"{bites[3]}") == 2:
                print(f"IP: {bites[0]}.{bites[1]}.{bites[2]}.{bites[3]}  | Prefix: /{prf[0][ones_zeros.index(i)]} | Mask: {prf[1][ones_zeros.index(i)]}") 
            if len(f"{bites[3]}") == 3:
                print(f"IP: {bites[0]}.{bites[1]}.{bites[2]}.{bites[3]} | Prefix: /{prf[0][ones_zeros.index(i)]} | Mask: {prf[1][ones_zeros.index(i)]}") 
            # Printing formated ip and prefix
        else:
            if len(f"{bites[3]}") == 1:
                print(f"IP: {bites[0]}.{bites[1]}.{bites[2]}.{bites[3]}   | Prefix: /{32 - prf} | Mask: {mask}")
            if len(f"{bites[3]}") == 2:
                print(f"IP: {bites[0]}.{bites[1]}.{bites[2]}.{bites[3]}  | Prefix: /{32 - prf} | Mask: {mask}")
            if len(f"{bites[3]}") == 3:
                print(f"IP: {bites[0]}.{bites[1]}.{bites[2]}.{bites[3]} | Prefix: /{32 - prf} | Mask: {mask}")
            # Printing formated ip and prefix 
    print("--------" * 7)


ip_addres = input("Zadejte ip adresu sítě: ")
while True:
    match_ip = re.search('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', ip_addres)
    # Checking corect ip adress form
    if match_ip == None:
        # Checking valid input (ip adress)
        ip_addres = input("Zadejte prosím správně formátovanou ip adresu sítě: ")
    else:
        break


prefix = int(input("Zadejte prefix základní sítě: /"))
while True:
    # Checking valid input (prefix)
    if prefix >= 30 or prefix < 8:
        prefix = int(input("Zadejte prosím max. prefix 30! "))
    else:
        break


number_of_subnets = int(input("Zadejte počet pod/sítí: "))
while True:
    # Checking valid number of subnets
    if number_of_subnets > 32 or number_of_subnets <= 0:
        number_of_subnets = int(input("Zadejte prosím max. 32 a min. 1 podsítí! "))
    else:

        ip_in_bin = decimalToBinary(ip_addres)
        pref_plus_zeros_pref = pref(prefix)[0]
        pref_plus_zeros_zeros = pref(prefix)[1]

        if number_of_subnets in [1, 2, 4, 8, 16, 32]:
            #Checking if the number of subnets is a power of two 
            diferent_prf = 1
            prf = math.ceil(math.log(size_of_subnets(pref_plus_zeros_zeros, number_of_subnets))/math.log(2))
            mask = mask(prf)
            finall_convertor(finall_subnets(suming(ip_in_bin, pref_plus_zeros_pref), size_of_subnets(pref_plus_zeros_zeros, number_of_subnets))) # final function
            break

        else:
            # If it's not power of two
            number_of_computers_plus_round = []
            number_of_computers = str(input("Zadejte velikosti podsítí ve formátu x, y, z,... sestupně!:")).split(",") # Asking for size of subnets
            while True:
                if len(number_of_computers) > number_of_subnets:
                    number_of_computers = str(input("Zadejte správný počet velikostí podsítí ve formátu x, y, z,... sestupně!:")).split(",")
                else:
                    break
            for plus in number_of_computers:
                # Rounding number of hosts to power of two
                plus = int(plus) + 2
                power = math.ceil(math.log(plus)/math.log(2))
                plus = 2 ** power
                number_of_computers_plus_round.append(plus)
            if sum(number_of_computers_plus_round) > 2 ** len(pref_plus_zeros_zeros):
                # checking if the number of hosts is not bigger then size of space for hosts 
                print("Více hostů než je místa!!!")
                break
            else:
                prf = prefix_output(number_of_computers_plus_round)    
                finall_convertor(other_sizes_subnets(suming(ip_in_bin, pref_plus_zeros_pref), number_of_computers_plus_round)) # final function
                break



if __name__ == "__main__":
    pass