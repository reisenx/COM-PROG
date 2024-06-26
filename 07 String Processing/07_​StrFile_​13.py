# Input a text
text = input().strip()

# Convert all character into lowercase
# Replace all symbol from a text with " "
# Split them to be a list of words
# Example: "Power of "love" 555"
# text = "power of "love" 555"
# new_text = "power of  love  555"
# word_list = ["power", "of", "love", "555"]
text = text.lower()
new_text = ""
for char in text:
    if("a" <= char <= "z"):
        new_text += char
    elif("0" <= char <= "9"):
        new_text += char
    else:
        new_text += " "
word_list = new_text.split()

# Output
# The first one will be all lower but the rest are all lowercase except the first letter
# Example: ["power", "of", "love", "555"] --> powerOfLove555
camelCase = ""
for i in range(len(word_list)):
    if(i == 0):
        camelCase += word_list[i]
    else:
        camelCase += word_list[i][0].upper() + word_list[i][1:]
print(camelCase)