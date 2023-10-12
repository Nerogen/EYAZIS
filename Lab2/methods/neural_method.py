import langid

def lang(text: str):  
    #text = "i love my cat"
    language, confidence = langid.classify(text)

    print("Обнаружен язык:", language)
    print("Уверенность:", confidence)
    if language == 'ru':
        return 'Russian'
    elif language == 'en':
        return 'English'
    else:
        return 'Unable to recognize'
