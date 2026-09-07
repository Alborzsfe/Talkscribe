from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any


def transcribe_audio(
    audio_path: Path,
    output_path: Path,
    model_name: str = "base",
) -> str:
    """Transcribe an audio file and write the resulting text."""
    if not audio_path.is_file():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    import whisper

    model: Any = whisper.load_model(model_name)
    result = model.transcribe(str(audio_path))
    transcript = str(result.get("text", "")).strip()
    output_path.write_text(transcript + "\n", encoding="utf-8")
    return transcript


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Transcribe an audio file locally with OpenAI Whisper."
    )
    parser.add_argument("audio", type=Path, help="Path to the input audio file")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("transcription.txt"),
        help="Output text file (default: transcription.txt)",
    )
    parser.add_argument(
        "-m",
        "--model",
        choices=("tiny", "base", "small", "medium", "large"),
        default="base",
        help="Whisper model size (default: base)",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        transcript = transcribe_audio(args.audio, args.output, args.model)
    except (FileNotFoundError, OSError, RuntimeError) as exc:
        print(f"Error: {exc}")
        return 1

    print(transcript)
    print(f"Transcript saved to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
