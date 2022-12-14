import os

from youtube_concate.settings import DOWNLOADS_DIR
from youtube_concate.settings import VIDEOS_DIR
from youtube_concate.settings import CAPTIONS_DIR

class Utils:
    def __int__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v')[-1]

    def get_caption_path(self, url):
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url) + '.txt')

    def caption_file_exists(self, url):
        path = self.get_caption_path(url)
        return os.path.exists(path) and os.path.getsize(path) > 0










