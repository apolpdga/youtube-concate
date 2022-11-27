import os
import time

from pytube import YouTube

from .step import Step
from youtube_concate.utils import Utils
from .step import StepException



class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            if utils.caption_file_exists(url):
                print('caption is exists.')
                continue
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = en_caption.generate_srt_captions()
            except AttributeError:
                print('AttributeError when downloading caption for', url)
                continue
            #except KeyError:
            #    print('KeyError when downloading caption for', url)
            #    continue
            #save the caption to a file named Output.txt

            text_file = open(utils.get_caption_path(url), 'w', encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end-start, 'seconds')













