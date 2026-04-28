# TalkScribe – Voice to Text Transcription Tool

## 📌 Overview

TalkScribe is a simple Python-based tool for converting audio files into text using OpenAI's Whisper model. It provides an easy way to transcribe spoken content into written format with minimal setup.

This project demonstrates the integration of a state-of-the-art speech recognition model into a practical application.

---

## ⚙️ Features

* 🎙️ Audio-to-text transcription
* 🧠 Powered by Whisper (pretrained speech recognition model)
* 📄 Automatic saving of transcription to a text file
* ⚡ Simple and minimal implementation

---

## 🚀 How It Works

1. Load a pre-trained Whisper model
2. Provide the path to an audio file
3. Run transcription
4. Display the result in the terminal
5. Save output to `transcription.txt`

---

## 🧪 Example Workflow

```id="n4k29d"
audio_path = "your_audio_file.mp3"
model = whisper.load_model("base")
result = model.transcribe(audio_path)
print(result["text"])
```

---

## 📂 Project Structure

```id="a92ldk"
.
├── Talkscribe.py        # Main script
├── transcription.txt    # Output file (generated)
└── README.md
```

---

## 🛠️ Requirements

* Python 3.x
* whisper

Install dependencies:

```id="k3ld9s"
pip install openai-whisper
```

---

## ▶️ Usage

1. Open `Talkscribe.py`
2. Set your audio file path:

```id="p9d2ls"
audio_path = "path_to_your_audio_file"
```

3. Run the script:

```id="z8s1kd"
python Talkscribe.py
```

---

## 📊 Output

* Console: Printed transcription
* File: `transcription.txt` containing full text

---

## 💡 Use Cases

* Podcast transcription
* Lecture note generation
* Voice memo conversion
* Content creation workflows

---

## 🔧 Future Improvements

* Support for multiple audio formats
* Add language selection
* GUI interface
* Batch processing for multiple files

---

## 👤 Author

* Alborz Seifaei

---

## 📜 License

This project is for educational and personal use.
