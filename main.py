import math
import random

# constants
space = ' '
aplha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
freq = (8.167, 1.492, 2.202, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 1.292, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.356, 2.758, 0.978, 2.560, 0.150, 1.994, 0.077)
startFreq = (102785, 38613, 35932, 24843, 18803, 34629, 16856, 68651, 58960, 5349, 5759, 27756, 34128, 19132, 56031, 26237, 2244, 17378, 67495, 134614, 11037, 5193, 61851, 68, 14433, 85)
midFreq = (234203, 22704, 79409, 55316, 352993, 28552, 52118, 179095, 243526, 2455, 22153, 134806, 56163, 224666, 240950, 46560, 2062, 182761, 110952, 172644, 110220, 35314, 27850, 6828, 18519, 2307)
endFreq = (25611, 823, 2595, 110313, 185535, 33250, 32897, 24134, 9073, 64, 12046, 27020, 18609, 73871, 43176, 8156, 13, 56940, 108052, 94241, 9421, 221, 10593, 713, 51777, 80)
wordLengths = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
lengthFreq = (2.998, 17.651, 20.511, 14.787, 10.700, 8.388, 7.939, 5.943, 4.437, 3.076, 1.761, 0.958, 0.518, 0.222, 0.076)
maxSentenceLength = 25
maxVowelBias = 2
minVowelBias = -1

vowelRatio = 1
commaChance = 4 
topPercent = 0.20

# gen word

def SmartWord():
    wLen = random.choices(wordLengths, weights=lengthFreq, k=1)
   # return ''.join(random.choices(aplha, weights=freq, k= length)) Simpler one line generation using all of letter frequencies, reguardless of pos
    length = wLen[0]
    word = []
    word.extend(random.choices(aplha, weights=startFreq, k=1))  # first letter
    if length > 3:
        word.extend(random.choices(aplha, weights=midFreq, k=length - 2))  # mid letters
    if length > 2:
        word.extend(random.choices(aplha, weights=endFreq, k=1))  # last letter

    return ''.join(word)

# gen dicitonary

def GenDict(wordCount): 
    maxOccurance = wordCount * topPercent
    txt = []
    for x in range(wordCount):
        word = SmartWord()
        ratio = 1 / (x + 1)
        occurance = math.ceil(maxOccurance * ratio)
        for i in range(occurance):
            txt.append(word)
            if len(txt) >= wordCount:
                break
    random.shuffle(txt)
    return Sentences(txt)


# join txt list together and add punctuation


def Sentences(txt):
    startIndexes = [0]
    commas = []
    index = 0
    x = 0
    while index < len(txt):
        sentenceLength = random.randint(1, maxSentenceLength)
        sentenceLength = min(sentenceLength, len(txt) - startIndexes[x])
        commaSlots = [*range(index, index + sentenceLength - 2)]
        if len(commaSlots) > 0:
            commaAmt = random.randint(0, len(commaSlots))
            commas.extend(random.sample(commaSlots, k=commaAmt))
        index += sentenceLength
        startIndexes.append(index)
        x += 1

    for i in startIndexes:
        if i > 0:
            txt[i - 1] = fullStop(txt[i - 1])
        if i < len(txt):
            txt[i] = txt[i].capitalize()
    for c in commas:
        txt[c] = comma(txt[c])

    return space.join(txt)


def fullStop(s):
    return s + "."


def comma(s):
    return s + ","


 if __name__ == "__main__":
     GenDict()
