from gensim.models import TfidfModel
from gensim.models import LdaMulticore
from gensim.models import LdaModel
import gensim.corpora as corpora
from gensim.utils import ClippedCorpus
from gensim.models import CoherenceModel
from gensim.utils import simple_preprocess
from gensim import matutils
import pyLDAvis.gensim
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import itertools
import sys
import os
import mlflow
from mlflow import log_metric, log_param, log_artifact

sys.path.append("packages/utils")
import defaults
import credentials

class Classifier():

    def __init__(self, tracking_uri, args):

        with mlflow.start_run():
            self.tracking_uri = credentials.TRACKING_URI
            log_param("mode", args.mode)

            return

    def getSampleData():
        data = pd.read_csv(os.path.join(defaults.DATA_PATH, "test.data.csv"))
        return data

    def preProcess():
        return

    def train():
        return

    def predict():
        return

    def run(self, args):
    
    # Get data


    #
        return