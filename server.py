'''Application deployed via Flask that offers a user interface to customers 
   with which they can have their input analyzed.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows 5 possible emotions
        and the dominant one.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # In case of empty input
    if len(text_to_analyze) == 0:
        return "Invalid input! Please try again!"

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the result is None or (FOR TASK 7B) the dominant emotion is None
    if response is None or response['dominant_emotion'] is None:
        return "Invalid input! Please try again!"
    # Return a formatted string with the emotions and dominant score
    return f'''For the given statement, the system response is 'anger': {response['anger']},
        'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}
        and 'sadness': {response['sadness']}.
        The dominant emotion is <strong>{response['dominant_emotion']}</strong>.'''

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel 
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
