"""
This module creates a Flask app for emotion detection from user input.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """
    Renders the index page for text input.
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def emote_detector():
    """
    Detects emotions from the user's input text and returns a response with 
    dominant emotion
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': "
        f"{response['anger']}, 'disgust': {response['disgust']}, 'fear': "
        f"{response['fear']}, 'joy': {response['joy']}, and 'sadness': "
        f"{response['sadness']}. The dominant emotion is {dominant_emotion}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
