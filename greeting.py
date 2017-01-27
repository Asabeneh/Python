name =input("What is your name: ").lower()
lang = input("What language do you speak: ").lower()
live = input("Where do you live: ").lower()
def greet(lang,name,live):
    if(lang == 'eng'):
        print("Hello",name)
    elif(lang=='es'):
        print("Hola",name)
    elif(lang=='fr'):
        print("Bonjour",name)
    elif(lang=='fi'):
        print("Moi",name)
    elif(lang=='am'):
        print("Selam",name)
    else:
        print("Do you speak English?",name)
greet(lang,name,live)
