import whisper

# Path to your audio file
audio_path = r"path"

# Load Whisper model
model = whisper.load_model("base")

# Transcribe the audio
print("🎙️ Transcribing audio...")
result = model.transcribe(audio_path)

# Print the transcript
print("\n📄 Transcript:")
print(result["text"])

# Save the transcript to a text file
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("\n✅ Transcript saved to 'transcription.txt'")
