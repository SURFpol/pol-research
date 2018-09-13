import os
import soundfile
import random


class WaveSampler(object):

    def __init__(self, source, destination):
        self.source = source
        self.dest = destination

    def __call__(self, sample_length=60):
        for entry in os.scandir(self.source):
            if not entry.is_file or not entry.path.endswith("wav"):
                continue
            print("Sampling: {}".format(entry.path))
            path, file = os.path.split(entry.path)
            sample, sample_rate = self.get_sample(entry.path, sample_length)
            destination = os.path.join(self.dest, file)
            soundfile.write(destination, sample, samplerate=sample_rate)

    def get_sample(self, file_path, length=60):
        wave_info = soundfile.info(file_path)
        if wave_info.duration <= 60:
            return soundfile.read(file_path)
        start = random.uniform(0, int(wave_info.duration - length) * wave_info.samplerate)
        start = int(start)
        stop = start + length * wave_info.samplerate
        return soundfile.read(file_path, start=start, stop=stop)


if __name__ == "__main__":
    sampler = WaveSampler("data/samples/sources", "data/samples")
    sampler()
