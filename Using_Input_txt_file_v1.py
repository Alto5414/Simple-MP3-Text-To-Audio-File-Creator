# https://pypi.org/project/pyttsx3/
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)   # adjust speed
engine.setProperty("volume", 1.0)

# Hard-coded local file paths
input_file = r"C:\Users\user folder]\Documents\text file.txt"
output_file = r"C:\Users\user folder\Documents\audio file.mp3"

# Read the story from the uploaded file
with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

# Break into smaller chunks (to avoid engine limits)
chunk_size = 5000  # characters
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Save chunks into one MP3 file
for i, chunk in enumerate(chunks):
    engine.save_to_file(chunk, output_file)
engine.runAndWait()

print(f"✅ Done! Story saved as {output_file}")