import docx2txt

filename = "/Users/NLNEW/Desktop/220110.docx"
file_txt = docx2txt.process(filename)

ascii_values = []
for character in file_txt:
    ascii_values.append(ord(character))
# print(ascii_values)

whitespace = "30"
backspace = "10"
num1 = 0
def1 = ["97", 
 "98",
 "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "195", "187", "195", "169", "195", "161", "197", "147", "195", "162", "195", "160", "195", "180", "46", "44", "39", "195", "175", "195", "164", "195", "182", "195", "188", "195", "168", "40", "41", "49", "50", "51", "52", "53", "54", "55", "56", "57", "48", "33"]
def2 = [97,
 98,
 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 195, 187, 195, 169, 195, 161, 197, 147, 195, 162, 195, 160, 195, 180, 46, 44, 39, 195, 175, 195, 164, 195, 182, 195, 188, 195, 168, 40, 41, 49, 50, 51, 52, 53, 54, 55, 56, 57, 48, 33]
defcount = []  

for x in def2:
    values = ascii_values.count(def2[num1])
    defcount.append(values)
    # print(def2[num1])

    # print(values)
    num1 += 1

# print(file_txt)

# print(defcount)

days = "lundi Lundi mardi Mardi mercredi Mercredi jeudi Jeudi vendredi Vendredi"
day_asci = []
for character in days:
    day_asci.append(ord(character))

lundi = [108, 117, 110, 100, 105]
Lundi = [76, 117, 110, 100, 105]

def charfind(characters, word_list, characters_number):
    if characters[characters_number] in word_list:
        character_index = word_list.index(characters[characters_number])
        print(character_index)
        next_chracter_index = character_index + 1
        print(next_chracter_index)
    else:
        next_chracter_index = False
    return next_chracter_index



def char(items, text):
    char_num = 0
    while True == True:
        charfind(items, text, char_num)
        char_num += 1

char(lundi, ascii_values)

