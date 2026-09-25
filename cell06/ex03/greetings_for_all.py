def greetings(word=None):
    if word == None:
        print("Hello, noble stranger.")
    elif not isinstance(word,str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {word}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)