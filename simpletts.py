import os
from gtts import gTTS
import re

def read_text_from_file(input_file_path):
    """
    Read text from a file.

    :param input_file_path: Path to the input text file.
    :return: Text content of the file.
    """
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        return None

def text_to_speech(text, output_audio_path, lang='en', slow=False):
    """
    Convert text to speech using the gTTS API and save it as an MP3 file.

    :param text: Text to convert to speech.
    :param output_audio_path: Path to save the output MP3 file.
    :param lang: The language for the speech (default is English).
    :param slow: Boolean indicating whether the speech should be slow.
    """
    try:
        # Initialize gTTS with the extracted text
        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save(output_audio_path)
        print(f"Audio has been saved to '{output_audio_path}'.")
    except Exception as e:
        print(f"An error occurred while converting text to speech: {e}")

def main():
    input_file_path = "input.txt"    # Path to the input text file
    output_audio_path = "output.mp3"
    language = 'en'                  # Change language code if needed
    speech_speed = False             # Set to True for slower speech

    try:
        # Read text from the input file
        input_text = read_text_from_file(input_file_path)
        if input_text is None:
            return

        # Remove unnecessary line breaks
        input_text = re.sub(r'\s+', ' ', input_text).strip()

        # Convert the text to speech
        text_to_speech(input_text, output_audio_path, lang=language, slow=speech_speed)

        # Play the audio file
        try:
            if os.name == 'nt':
                os.startfile(output_audio_path)
            elif os.uname().sysname == 'Darwin':
                os.system(f"open {output_audio_path}")
            else:
                os.system(f"xdg-open {output_audio_path}")
            print("Playing the audio file...")
        except Exception as e:
            print(f"An error occurred while trying to play the audio: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
