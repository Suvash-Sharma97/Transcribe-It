from pydub import AudioSegment
import speech_recognition as sr
import os

# Language mapping dictionary
LANGUAGE_CODES = {
    "english": "en-US",
    "german": "de-DE",
    "french": "fr-FR",
    "spanish": "es-ES",
    "italian": "it-IT",
    "portuguese": "pt-PT",
    "hindi": "hi-IN",
    "japanese": "ja-JP",
    "chinese": "zh-CN",
    "russian": "ru-RU",
    "korean": "ko-KR",
    "dutch": "nl-NL",
}

# Get language input from user
user_lang = input("Enter the language of the audio files (e.g., 'English', 'German'): ").strip().lower()

# Get language code
lang_code = LANGUAGE_CODES.get(user_lang)

if not lang_code:
    print("Error: Unsupported language. Please enter a valid language name.")
    print("Supported languages:", ", ".join(LANGUAGE_CODES.keys()))
    exit(1)

# Initialize recognizer
recognizer = sr.Recognizer()

# Create a temporary folder for WAV files
wav_dir = "converted_wavs"
os.makedirs(wav_dir, exist_ok=True)

# Get all .mp3 files in the current working directory
mp3_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.mp3')]

if not mp3_files:
    print("No MP3 files found in the directory.")
    exit(1)

# Convert MP3 to WAV
for mp3_file in mp3_files:
    mp3_path = os.path.join(os.getcwd(), mp3_file)
    wav_path = os.path.join(wav_dir, os.path.splitext(mp3_file)[0] + ".wav")

    # Convert only if WAV doesn't already exist
    if not os.path.exists(wav_path):
        try:
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format="wav")
        except Exception as e:
            print(f"Error processing {mp3_file}: {e}")
            continue

# Process WAV files
wav_files = [f for f in os.listdir(wav_dir) if f.endswith(".wav")]

for wav_file in wav_files:
    wav_path = os.path.join(wav_dir, wav_file)

    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)

        # Transcribe audio
        try:
            transcription = recognizer.recognize_google(audio_data, language=lang_code)
            print(f"Transcription ({wav_file}): {transcription}")

            # Optional: Save transcription to a text file
            with open(wav_path.replace(".wav", ".txt"), "w", encoding="utf-8") as txt_file:
                txt_file.write(transcription)

        except sr.UnknownValueError:
            print(f"Unable to transcribe {wav_file}: Speech not recognized.")
        except sr.RequestError as e:
            print(f"Error with Google Speech Recognition API: {e}")
        except Exception as e:
            print(f"Unexpected error processing {wav_file}: {e}")

    # Remove WAV file after processing
    try:
        os.remove(wav_path)
    except PermissionError:
        print(f"Permission error: Could not delete {wav_path}")

print("Processing complete!")
