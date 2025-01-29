import requests
import json

def emotion_detector(text_to_analyze):
    """Function to analyze emotion input"""
    if not text_to_analyze.strip():
        return 'Error: Blank entry provided Status Code: 400'
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    obj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=obj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant emotion': None
        }
    else:
        result = 'Error: Unexpected response. Status Code: {}'.format(response.status_code)

    return result