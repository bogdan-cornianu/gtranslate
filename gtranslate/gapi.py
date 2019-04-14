from googletrans import Translator

from gtranslate import utils


def get_translation(data):
    messages = utils.deserialize(data)
    translator = Translator()
    translations = []
    for message in messages:
        translations.append(translator.translate(message).text)

    return utils.serialize(translations)
