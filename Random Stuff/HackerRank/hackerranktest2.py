def transformSentence(sentence):
    # Write your code here
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newstring = ""
    position1 = ""
    position2 = ""
    sentence = sentence.lower()
    lensentence = len(sentence)
    sentencelist = list(sentence)
    for i in range(0,lensentence):
        position1 = lensentence[i]
        position2 = lensentence[i+1]
    print(position1)

transformSentence("Blue Moon")