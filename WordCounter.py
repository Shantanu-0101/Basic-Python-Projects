def word_counter(text):
    words = text.split()
    return len(words)

def main():
    this = input("Enter text : ")
    print("length of your text :", word_counter(this)) 

main()
