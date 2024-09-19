TRANSLATION = {
    "salom": {
        "uz": "Salom",
        "ru": "Privet",
        "en": "Hello",
      
    },
    "bot_salom": {
        "uz": "Assalamu alaykum\nBotimizga xush kelibsiz!",
        "ru": "Privet, Dobro pojalovat v nash bot",
        "en": "Hello, welcome to our bot",
    },
    "change_language": {
        "uz": "UZ Til o'zgartirildi",
        "ru": "RU Til o'zgartirildi",
        "en": "EN Til o'zgartirildi",
    },
    "books": {
        "uz": "📚 Kitoblar",
        "ru": "📚 Knigi",
        "en": "📚 Books",
    }
}

def get_translation(word, language):
    if not language:
        language = "uz"
    text = TRANSLATION.get(word, {}).get(language)
    return text if text else word