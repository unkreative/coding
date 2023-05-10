import docx2txt
import subprocess

def listToString(s): 
    str1 = " "  
    return(str1.join(s))

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

filename = "/Users/NLNEW/Desktop/220110.docx"
file_txt = docx2txt.process(filename)
write_to_clipboard(file_txt)
ascii_values = []
for character in file_txt:
    value = ord(character)
    ascii_values.append(f"{value}")

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

ascii_values2 = listToString(ascii_values)

def words(input, words):
    if "10" in input:
        input = input.replace(" 10 ", " ")
        print()
        print(type(input))
        print()
        print(input)

words(ascii_values2, def1)