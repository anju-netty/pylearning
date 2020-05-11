
def find_substring(input_string,substring):

    len_str = len(input_string)
    len_sub = len(substring)
    
    stop_search = len_str - (len_sub - 1)
    for i in range(stop_search):
        if input_string[i] == substring[0]: #0 0
            if input_string[i:i+len_sub] == substring:
                #return i for first index find
                last_matching_index = i
                
    return last_matching_index


if __name__ == "__main__":
    
    input_string = input("Enter the input string : ")
    substring = input("Enter substring : ")

    index = find_substring(input_string,substring)

    if index:
        print("The substring \"{}\" is present in \"{}\" at the last index \"{}\""
        .format(substring,input_string,index))
    else:
        print("Sorry not found!")
