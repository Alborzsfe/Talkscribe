# TalkScribe

TalkScribe is a command-line tool that transcribes local audio files with the open-source OpenAI Whisper model. Processing runs locally after the model has been downloaded.

## Features

- Accepts the audio path from the command line—no source-code editing required.
- Supports Whisper's `tiny`, `base`, `small`, `medium`, and `large` model sizes.
- Lets you select the output text file.
- Returns a clear error for missing or unreadable input files.
- Includes unit tests and a GitHub Actions workflow.

## Requirements

- Python 3.10 or newer
- FFmpeg available on your system
- Enough memory and storage for the selected Whisper model

## Installation

```bash
git clone https://github.com/Alborzsfe/Talkscribe.git
cd Talkscribe
python -m venv .venv
pip install -r requirements.txt
```

Whisper also requires FFmpeg. Install it through your operating system's package manager.

## Usage

```bash
python Talkscribe.py path/to/audio.mp3
python Talkscribe.py path/to/audio.mp3 --model small --output interview.txt
```

Use `python Talkscribe.py --help` for all options.

## Tests

The unit tests do not download a Whisper model.

```bash
pip install -r requirements-dev.txt
pytest
```

## Privacy

Audio is processed locally by Whisper. The initial model download requires internet access, but audio is not uploaded by this script.

## License

MIT
