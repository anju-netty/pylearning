

def find_word_count(words_list):
    word_count_map = {}
    for i in words_list:
        if i in word_count_map:
            word_count_map[i] = word_count_map[i]+1
        else:
            word_count_map[i] = 1

    max_occurence_words = findmaxwords(word_count_map)
    return max_occurence_words

def findmaxwords(word_count_map):

    max_value = max(word_count_map.values())
    max_occurence_words = []
    for k in word_count_map:

        if word_count_map[k] == max_value:
            max_occurence_words.append(k)

    return max_occurence_words
if __name__ == "__main__":
    
    string = "Rocky is a dog and cat cat cat cat and dog and cat and dog dog dog 123"

    words_list = string.split(" ")

    print(find_word_count(words_list))

    
    