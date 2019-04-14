from multiprocessing import Process, Queue

from googletrans import Translator

from gtranslate import utils


def translate(message, language, queue):
    translator = Translator()
    queue.put(translator.translate(message, dest=language).text)


def get_translation(data):
    messages = utils.deserialize(data)
    translations = []
    procs = []
    queue = Queue()

    for message in messages["message"]:
        proc = Process(target=translate, args=(message, messages["language"], queue))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
        translations.append(queue.get())
    return utils.serialize(translations)
