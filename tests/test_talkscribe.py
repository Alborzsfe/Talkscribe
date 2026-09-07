import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest

from Talkscribe import build_parser, transcribe_audio


def test_parser_accepts_audio_and_output():
    args = build_parser().parse_args(
        ["sample.wav", "--output", "result.txt", "--model", "tiny"]
    )
    assert args.audio == Path("sample.wav")
    assert args.output == Path("result.txt")
    assert args.model == "tiny"


def test_missing_audio_fails_before_loading_model(tmp_path):
    with pytest.raises(FileNotFoundError):
        transcribe_audio(tmp_path / "missing.wav", tmp_path / "out.txt")


def test_transcription_is_saved_without_loading_real_whisper(tmp_path):
    audio = tmp_path / "sample.wav"
    audio.write_bytes(b"test")
    output = tmp_path / "out.txt"
    model = Mock()
    model.transcribe.return_value = {"text": " hello world "}
    fake_whisper = SimpleNamespace(load_model=Mock(return_value=model))

    with patch.dict(sys.modules, {"whisper": fake_whisper}):
        result = transcribe_audio(audio, output, "tiny")

    assert result == "hello world"
    assert output.read_text(encoding="utf-8") == "hello world\n"
