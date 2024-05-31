import pyfiglet

def generate_ascii_art(text):
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art

user_text = input("Enter a word or phrase: ")
ascii_art = generate_ascii_art(user_text)
print(ascii_art)
