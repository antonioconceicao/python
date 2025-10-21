import subprocess

filename = "audio.m4a"  # Replace with your audio file path
model_name = "base"  # Or 'tiny', 'base', 'small', 'large'

subprocess.run(
    [
        "whisper",
        "--language",
        "pt",  # Specify language (e.g., 'en' for English)
        "--word_timestamps",
        "True",
        "--model",
        model_name,
        "--output_dir",
        "output_transcriptions",  # Directory to save output
        filename,
    ]
)