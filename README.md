# YT-Downloader-Transcriber

An **AI-powered** YouTube audio downloader and transcriber with a simple GUI interface.

This tool uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to reliably download audio from any public YouTube video, then leverages OpenAI’s [Whisper](https://github.com/openai/whisper) model to transcribe the audio into text --> all offline and without any external GPT API or wrapper.


## Features

- Download audio stream from YouTube videos (mp3 format ONLY, no video)
  
- Transcribe audio with Whisper’s base model (high-quality speech recognition)
  
- Export transcript as a text file
  
- Simple Tkinter GUI for ease of use
  
- Cross-platform (Windows, macOS, Linux)


## Requirements

- Python 3.8 or higher
  
- ffmpeg installed and available in your system PATH
  
- Dependencies listed in `requirements.txt`


## Installation

1. Clone the repository:

       git clone https://github.com/anipaleja/YT-downloader-transcriber.git
   
       cd YT-down-transcribe

2. Create and activate a virtual environment (recommended):

       python -m venv venv
   
       source venv/bin/activate   # macOS/Linux
   
       venv\Scripts\activate      # Windows

3. Install dependencies:

       pip install -r requirements.txt

4. Make sure ffmpeg is installed:

   On macOS with Homebrew:

       brew install ffmpeg

   On Windows, download from ffmpeg.org and add to PATH

5. Run the application:

       python main.py

6. Next Steps:

- Enter the full valid YouTube video URL in the input box

- Click Download & Transcribe

- Wait for the audio download and transcription process to complete

- Transcript will appear in the GUI and be saved as transcript.txt in the YT-down-transcribe folder

    - Audio will appear in a new folder called Downloads withing the YT-down-transcribe folder
 
## Notes

- Transcription speed depends on your CPU/GPU and video length

- Use smaller Whisper models for faster transcription (modify main.py)
  
- For GPU support, install the appropriate PyTorch version with CUDA

## License

MIT License

## Acknowledgements

- **yt-dlp** for YouTube downloading

- **OpenAI Whisper** for transcription

**Feel free to open issues, pull requests to contribute!!**
