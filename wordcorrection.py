#step 1. import the necessary libraries
from spellchecker import SpellChecker

#Step 2 creating the app class
class SpellCheckerApp:
    def __init__(self):
        self.spell=SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words= []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f'correcting"{word}" to "{corrected_word}"')
                corrected_words.append(corrected_word)

#step 4 Returning the corrected Text
def run(self):
    print("\n ___Spell Checker___")

    while True:
        text = input("enter text to check(or 'exit' to quit): ")

        if text.lower() ==' exit':
            break
        
        corrected_text = self.corrected_text(text)
        print(f'corrected text: {corrected_text}')

#Stwep 5 running the program
if __name__ == "__main__":
    SpellCheckerApp().run()


        
