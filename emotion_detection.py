import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json=input_json, headers=headers)

    # convert json to dict:
    emo_dict = json.loads(response.text)

    # new_emo_dict is created to isolate the emotions with their scores
    # {'anger': 0.0132405795, 'disgust': 0.0020517302, 'fear': 0.009090992, 'joy': 0.9699522, 'sadness': 0.054984167}
    new_emo_dict = emo_dict["emotionPredictions"][0]["emotion"]

    # Select the emotion with the dominant score from new_emo_dict
    dominant_emotion = max(new_emo_dict, key=new_emo_dict.get)

    # Add dominant_score to new_emo_dict
    new_emo_dict['dominant_emotion'] = dominant_emotion
    
    return new_emo_dict
