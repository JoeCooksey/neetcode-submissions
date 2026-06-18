class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""

        for word in strs:
            # Format: "length + # + string" -> e.g., "5#hello"
            encodedString += str(len(word)) + "#" + word 
        
        return encodedString
    def decode(self, s: str) -> List[str]:
        decodedString = []
        i = 0

        while i < len(s):
            #Find where # is
            j = i
            while s[j] != '#':
                j += 1
            #Determine length of word
            length = int(s[i:j])
            #Determine start and end of word
            startofWord = j+1
            endofWord = startofWord + length
            #Append individual word and update i
            decodedString.append(s[startofWord:endofWord])
            i = endofWord
        return decodedString

