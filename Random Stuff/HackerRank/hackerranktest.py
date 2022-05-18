def missingCharacters(s):
    # Write your code here
    alphanumeric = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chars = []
    missingchars = []
    for char in alphanumeric:
        if char in s:
            chars.append(char) 
        else:
            missingchars.append(char)
    str = ''.join(missingchars)
    print(str)
    # return(str)

missingCharacters("3aloha412")