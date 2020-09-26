"""Download Pretrained models."""
import requests
import coloredlogs
import logging
from os import path

# Create a logger object.
logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.DEBUG)


def download_dog_breed_model():
    """Download Pretrained model."""
    url = 'https://github.com/sravanrekandar/fastai-v2-exercises/blob/master/apps/dog_types/dog_learner.pkl?raw=true' # noqa
    target_url = 'downloaded-models/dog_learner.pkl'

    if path.exists(target_url):
        logger.info(target_url + ' exists, skipping download')
        return
    else:
        logger.info(target_url + ' not found.')
        logger.info('Downloading DogBreedModel file from ' + url)
        r = requests.get(url, allow_redirects=True)
        open(target_url, 'wb').write(r.content)
        logger.info('Stored the model to ' + target_url)
