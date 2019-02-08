import util.Constant as Constants
import os
import requests
from tqdm import tqdm


class DatasetDownloader:
    def __init__(self, output_path=Constants.ARCHIVE_PATHS, urls=Constants.URL_LIST):
        self.output_path = output_path
        self.urls = urls

    def download_dataset(self):
        if self.output_path is None or self.urls is None or len(self.urls) == 0:
            return

        for url in self.urls:
            file_name = url.split('/')[-1]
            destination = os.path.join(self.output_path, file_name)

            print("Downloading %s -> %s" % (url, destination))

            response = requests.get(url, stream=True)

            with open(destination, "wb") as handle:
                for data in tqdm(response.iter_content()):
                    handle.write(data)
