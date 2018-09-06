import subprocess
from itertools import islice

from readers.wur import WurLibrary4Learning


if __name__ == "__main__":
    wur_sources = WurLibrary4Learning("data/wur")
    for source in islice(wur_sources, 3):
        subprocess.run([
            "youtube-dl",
            "--extract-audio",
            "--audio-format=wav",
            "--postprocessor-args='-acodec pcm_s16le -ac 1 -ar 8000'",
            "-o 'data/wur/downloads/ - %(title)s.%(ext)s'",
            source["url"]
        ])
