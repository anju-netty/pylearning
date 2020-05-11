




def find_phrase_in_sentence(s,p):
    len_s = len(s)
    len_p = len(p)

    print(len_s) #20
    print(len_p) #7

    found = False
    i = 0 
    j = 0

    while (j!=len_p or len_s-i > len_p ) and i != len_s: #j=0,i=0, 15-0 > 7
        if p[j] == s[i]: 
            print("p[{}] = {} and s[{}] is {}".format(j,p[j],i,s[i]))
            if j == len_p-1:
                found = True
                break
            
            j = j+1 #8
            i = i+1 #5
        else:
            print("p[{}] = {} and s[{}] is {}".format(j,p[j],i,s[i]))

            if j !=0:
                j = 0
                i = i-1
                #i = i+1
            else:
                j = 0
                i = i+1

    return found, i

def find_phrase(s,p):

    #loop through each letter of the sentence
    #for each letter will compare the first letter of the phase
    

if __name__ == "__main__":


    #s = "My name is Anju"
    #p = "name"

    s = input("Enter sentence : ")
    p = input("Enter phrase : ")

    found,i = find_phrase_in_sentence(s,p)

    if found == True:   
        index = i-(len(p)-1)
        print("Found and index is ",index)