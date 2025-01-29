from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    emotions = {k: v for k, v in response.items()}
    
    formatted_emotions = ', '.join([f"'{emotion}': {value}" for emotion, value in emotions.items()])

    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is {formatted_emotions}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)