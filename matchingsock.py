
ar = [1,2,1,4,4,1,2,3,3,1,1]
ar.sort()

total_pair=0
seen = []
#

for i in ar:

    pair = 0 #local pair counter for the seen sack
#ar=[1,1,2,2,3,4,4]

    if seen == []:
        seen.append(i)
    else:
        for j in seen: #seen=[]
            
            if j == i: #j = 4, i =4
                    #pair = 2
                #print(seen,"pair = ",pair)
                print(seen)
                seen.pop()
                total_pair = total_pair + 1 # 2
            else:
                seen.pop()
                print(seen)
                seen.append(i)
                

print(total_pair)

#pair_of_color_socks = 0
#
#    #find the distinct colors in list
#    #unique_color_list = list(set(ar))
#
#    for i in unique_color_list:
#        pair_of_color_socks = pair_of_color_socks + int(ar.count(i)/2)
#
#    return pair_of_color_socks
#
#