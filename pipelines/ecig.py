from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
# from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import Normalizer

from pipelines.helpers import ItemGetter
# from pipelines.user import UserAgeMonths, UserEgoVectorizer
# from pipelines.time import Timestamp2DatetimeIndex, DatetimeIndexAttr
# from pipelines.text import Gensim


class ECigPipeline:
    def __init__(self, global_features=None, lsi=False, lsi_n=1000):
        """
        :param time_features: default(["dayofweek", "hour", "hourofweek"])
        :param global_features: default(["text", "time", "user", "age"])
        :param lsi: if true, includes the TruncatedSVD() piece
        """
        self.lsi = lsi
        self.lsi_n = lsi_n

        self.global_features = {
            "text"
        } if not global_features else global_features

    def feature_textpipe(self):
        """
        :return: Pipeline(ItemGetter -> TfidfVectorizer)
        """
        textpipe = [
            # ("getter", ItemGetter(
            #     "realdonaldtrump_foxandfriends_smoke_blowing_up_your_orange_ass")),
            ("tfidf", TfidfVectorizer(analyzer="char")),
        ]
        if self.lsi:
            textpipe.append(("lsi", TruncatedSVD(n_components=self.lsi_n)))
        return Pipeline(textpipe)

    def features(self):
        """
        :return: FeatureUnion([
            ("text", Pipeline(textpipe))
        ])
        """

        dd = {
            "text": self.feature_textpipe()
        }

        features = list(map(lambda feature: (
            feature, dd[feature]), self.global_features))
        return FeatureUnion(features)

    def pipeline(self, clf):
        """
        :param clf: sklearn.classifer
        :return: Pipeline([
            ("exploder", exploder),
            ("features", features),
        ])
        """
        pipeline = [
            # ("features", self.features()),
            # ("scaler", Normalizer()),
            ("tfidf", TfidfVectorizer(analyzer="word", ngram_range=(1, 3))),
            ("clf", clf)
        ]
        return Pipeline(pipeline)
