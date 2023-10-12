from langdetect import detect


def lang(text: str):

    try:
        language = detect(text)
        if language == 'ru':
            return 'Russian'
        elif language == 'en':
            return 'English'
        else:
            return 'Unable to recognize'
    except Exception as e:
        return str(e)

