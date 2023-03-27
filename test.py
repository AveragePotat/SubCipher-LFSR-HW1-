# TITLE: Test File
# DEDICATED USE:
#   To understand how something works

# imported libraries
import numpy
from pylfsr import LFSR as L

# initializing variables
test_str = "hello how are you doing today"
# empty freq array 
az_freq = {}
# length of inputted char array
len_test = len(test_str.replace(" ", ""))

# finds the letter frequency in the given text
def letter_freq(cipher, freq_arr):
    for char in cipher:
        if char in freq_arr:   
            freq_arr[char] += 1
        else:
            freq_arr[char] = 1

    # print result
    #print("Letter frequency in the ciphertext is: \n " 
    #      + str(freq_arr))
    
    return freq_arr

# find the percentage of each letter
def freq_perc(freq_arr, freq_len):
    # placeholders variables
    perc_str = "%"
    # runs through the array and calculates the percentages
    for char, amt in freq_arr.items():
        freq_arr[char] = str(round(amt/freq_len*100)) + perc_str
        print(str(freq_arr[char]))
    
    #print("Letter frequency percentage in the ciphertext is: \n " 
    #     + str(freq_arr))

def count_lfsr():
    # initializing count variable
    cnt = 0
    # for __ in ___:
    #   if ___ in ___:
    print("The period is: " + str(cnt))

# test functions
# ------------------------------------------------------------------------
# freq = letter_freq(test_str, az_freq)
# lett_perc = freq_perc(freq, len_test)


# REFERENCES #
# ------------------------------------------------------------------------

# UNDERSTANDING TRY & EXPECT FUNCTIONS 
# chars = {}
# for char in test_str:
#     try:chars[char] += 1
#     except:chars[char] = 1

# UNDERSTANDING .format() function
# for key, value in chars.items():
#     print("{} -> {}%".format(key, value/len(test_str)*100))