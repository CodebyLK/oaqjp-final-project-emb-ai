'''Executing this function initiates the motion detection
analysis to be executed over the Flask channel and be deployed
on localhost:5000.
'''

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''Retrieve the text to analyze from the request arguments'''
    text_to_analyze = request.args.get('textToAnalyze')

    #Check for blank entries
    if not text_to_analyze or not text_to_analyze.strip():
        return jsonify({"error": "Invalid entry"}), 400

    #Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return jsonify({"error": "Invalid input! Try again"}), 400
    dominant_emotion = response['dominant_emotion']

    #Remove 'dominant_emotion' from the emotions dictionary for formatting
    emotions = {k: v for k, v in response.items() if k != 'dominant_emotion'}

    formatted_emotions = ', '.join([f"'{emotion}': {value}" for emotion, value in emotions.items()])

    #Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is {formatted_emotions}"\
        f"The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    '''function to render html'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
