import time
import logging
from multiprocessing import Process, Queue

from googletrans import Translator

from gtranslate import utils


def translate(message, language, queue):
    logging.info('Requesting translation for {} to language {}'.format(message, language))
    translator = Translator()
    queue.put(translator.translate(message, dest=language).text)


def get_translation(data):
    messages = utils.deserialize(data)
    translations = []
    procs = []
    queue = Queue()
    before = int(round(time.time() * 1000))
    after = 0
    rate_limit = utils.get_rate_limit()
    requests_made = 0

    for message in messages["message"]:
        diff = after - before

        # check if there are more requests per second than allowed
        if diff > 1 and requests_made > rate_limit:
            logging.info('Rate limiting at {} requests/second'.format(rate_limit))
            time.sleep(1/rate_limit)
        proc = Process(target=translate, args=(message, messages["language"], queue))
        procs.append(proc)
        proc.start()
        requests_made += 1
        after = int(round(time.time() * 1000))

    for proc in procs:
        proc.join()
        translations.append(queue.get())
    logging.info('Finished translations: {}'.format(translations))

    return utils.serialize(translations)
