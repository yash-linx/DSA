# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector<string> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:

# vector<string> decode(string s) {
#     //... your code
#     return strs;
# }
# So Machine 1 does:

# string encoded_string = encode(strs);

# and Machine 2 does:

# vector<string> strs2 = decode(encoded_string);

# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# Example 1:
# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]

# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2

# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
# Example 2:

# Input: dummy_input = [""]

# Output: [""]

def encode(strs: list[str]) -> str:
    encoded_string = ""
    for i in strs:
        encoded_string += str(len(i)) + "#" + str(i)
    return encoded_string

def decode(s: str) -> list[str]:
    j = 0
    decoded_list = []
    i=0
    while i < len(s):
        if s[i]=="#":
            msg_length = int(s[j:i])
            msg = s[i+1:i+msg_length+1]
            decoded_list.append(msg)
            j = msg_length+1+i
            i = j
        i += 1
    return decoded_list


print(encode(["Hello","World", "!", "Good", "Morning"]))
print(decode(encode(["Hello","World", "!", "Good", "Morning"])))