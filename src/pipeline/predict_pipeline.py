import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        danceability: float,
        energy: float,
        key,
        mode,
        time_signature,
        speechiness: float,
        acousticness: float,
        instrumentalness: float,
        liveness: float,
        valence: float,
        tempo: int,
        duration_ms: int,
        chorus_hit: int,
        sections: int,
        loudness: float):

        self.danceability = danceability

        self.energy = energy

        self.key = key

        self.mode = mode

        self.time_signature = time_signature

        self.speechiness = speechiness

        self.acousticness = acousticness

        self.instrumentalness = instrumentalness

        self.liveness = liveness

        self.valence = valence

        self.tempo = tempo

        self.duration_ms = duration_ms

        self.chorus_hit = chorus_hit

        self.sections = sections

        self.loudness = loudness

        

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "danceability": [self.danceability],
                "energy": [self.energy],
                "key": [self.key],
                "mode": [self.mode],
                "time_signature": [self.time_signature],
                "speechiness": [self.speechiness],
                "acousticness": [self.acousticness],
                "instrumentalness": [self.instrumentalness],
                "liveness": [self.liveness],
                "valence": [self.valence],
                "tempo": [self.tempo],
                "duration_ms": [self.duration_ms],
                "chorus_hit": [self.chorus_hit],
                "sections": [self.sections],
                "loudness": [self.loudness]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)