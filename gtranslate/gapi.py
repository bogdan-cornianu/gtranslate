from googletrans import Translator

from gtranslate import utils


def get_translation(data):
    messages = utils.deserialize(data)
    translator = Translator()
    translations = []
    for message in messages["message"]:
        translations.append(translator.translate(message, dest=messages["language"]).text)

    return utils.serialize(translations)
