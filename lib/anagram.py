class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        matches = []
        # Convert the word to lowercase for case-insensitive comparison
        word_lower = self.word.lower()
        # Sort the letters of the word for comparison
        sorted_word = sorted(word_lower)
        
        # Iterate over each possible anagram
        for anagram in possible_anagrams:
            # Convert the anagram to lowercase for case-insensitive comparison
            anagram_lower = anagram.lower()
            # Sort the letters of the anagram for comparison
            sorted_anagram = sorted(anagram_lower)
            
            # Check if the sorted letters of the word and anagram are equal
            if sorted_word == sorted_anagram:
                # If they are equal, add the anagram to the matches list
                matches.append(anagram)

        return matches
