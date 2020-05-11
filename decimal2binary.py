def reverse(binary):
    temp = ""
    for i in range(len(binary)-1,-1,-1):
        #print(binary[i])
        temp = temp + str(binary[i])
    return temp


def binary(num):

    bin = []

    if num!=0: #if decimal is not zero

        while num != 1:

            #print("num is ",num)
            bin.append(int(num%2))
            num = int(num/2)

            if num == 1:
                bin.append(1)

    # fill in remaining space with 0
    i = len(bin)
    while i < 8:
        bin.append(0)
        i = i+1

    bin = reverse(bin)
    return bin

def decimal(binary):

    decimal = 0
    bit = 7
    for i in range(8):
        #print("binary[{}] is {}".format(i,binary[i]))
        if binary[i] == '1':
            decimal = decimal + 2 ** bit #8-i
            bit = bit-1
        else:
            decimal = decimal + 0
            bit = bit-1
       
    return str(decimal)

def and_of(ip,mask):
    
    network = []
    for i in range(8):
        if ip[i] == mask[i]:
            network.append(ip[i])
        else:
            network.append('0')

    network = "".join(network)
    #print(network)
    return network

def ip_notation_to_binary(ip_notation):

    ip = ip_notation.split('.')
    ip_binary = []
    for i in ip:
        ip_binary.append(binary(int(i)))
    return ip_binary


if __name__ == "__main__":
    
    #print(binary(192))
    ip_address = "192.11.6.9"
    subnet_mask = "255.128.0.0"

    ip_address = input("Enter IP address : ")
    subnet_mask = input("Enter Subnet mask : ")


    #Convert ip address to binary
    ip_binary = ip_notation_to_binary(ip_address)
    print("\n\n\nip address {} is {}".format(ip_address,".".join(ip_binary)))

    #Convert subnet mask to binary
    sub_binary = ip_notation_to_binary(subnet_mask)
    print("Subnet mask {} is {}".format(subnet_mask,".".join(sub_binary)))

    #Perform AND Operation on each octet to find subent id
    network_bin = []
    for i in range(4):
        network_bin.append(and_of(ip_binary[i],sub_binary[i]))

    print("\n\nNetwork id is  ",".".join(network_bin))

    #Convert Subnet id to decimal
    network_id = []
    for i in range(4):
        network_id.append(decimal(network_bin[i]))
    print(".".join(network_id),"\n\n")

    #subnet_mask = "255.128.0.0"
    # block size

    
    subnet_octet = subnet_mask.split(".")
    octet = 0

    for i in subnet_octet:

        if i != '255':
            block_size = 256 - int(i)
            octet = octet + 1
            break
        else:
            octet = octet + 1

    print("block_size = ", block_size)

    print("Next subent id = ", (int(network_id[octet]) + block_size))



