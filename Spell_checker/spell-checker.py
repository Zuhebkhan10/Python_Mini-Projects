from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            corrected = self.spell.correction(word)
            if corrected != word.lower():
                print(f'Correcting "{word}" to "{corrected}"')
            corrected_words.append(corrected if corrected else word)
        return ' '.join(corrected_words)


    def run(self):
        print("\n---Spell Checker---")
        while True:
            text = input("Enter text to check: ")
            if text.lower() == 'exit':
                print("Closing the program")
                break
            corrected_text = self.correct_text(text)
            print(f"Corrected text: {corrected_text}")

if __name__ == '__main__':
    s = SpellCheckerApp()
    s.run()