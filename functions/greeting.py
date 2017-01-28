name =input("What is your name: ").lower()
lang = input("What language do you speak: ").lower()
live = input("Where do you live(England,Spain, France,Finland, Ethiopia): ").lower()
def greet(lang,name,live):
    if(lang == 'eng'):
        if(live =="England"):
            print("Hello",name)
            print("You may speak English fluently")
        else:
            print("Hello",name)
            print("Your are proficient English user.")
    elif(lang=='es'):
        if(live =="Spain"):
            print("Holla",name)
            print("You may speak Spanish fluently")
        else:
            print("Hello",name)
            print("Your are proficient Spanish user.")
    elif(lang=='fr'):
        if(live =="France"):
            print("Bonjour",name)
            print("You may speak French fluently")
        else:
            print("Hello",name)
            print("Your are proficient English user.")
    elif(lang=='fi'):
        if(live =="Finland"):
            print("Moi",name)
            print("You may speak Finnish fluently")
        else:
            print("Moi",name)
            print("Your are proficient Finnish user.")
    elif(lang=='am'):
        if(live =="Ethiopia"):
            print("Selam",name)
            print("You may speak Amharic fluently")
        else:
            print("Hello",name)
            print("Your are proficient Amharic user.")
    else:
        print("Do you speak English?",name)
greet(lang,name,live)
