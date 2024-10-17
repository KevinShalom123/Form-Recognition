import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert speech in an MP3 file to text
def mp3_to_text(file_path):
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)  # Using Google Speech Recognition
            print("Text:", text)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# Path to the MP3 file
file_path = "path_to_your_mp3_file.mp3"

# Call the function to convert MP3 to text
mp3_to_text(file_path)
