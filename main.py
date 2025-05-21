import os
import tkinter as tk
from tkinter import messagebox, scrolledtext
from yt_dlp import YoutubeDL
import whisper
import threading

class YouTubeTranscriberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NeuroCast - YouTube Transcriber")
        self.root.geometry("600x500")
        self.model = whisper.load_model("base")

        self.label = tk.Label(root, text="Enter YouTube Video URL:")
        self.label.pack(pady=10)

        self.url_entry = tk.Entry(root, width=60)
        self.url_entry.pack(pady=5)

        self.transcribe_btn = tk.Button(root, text="Download & Transcribe", command=self.run_thread)
        self.transcribe_btn.pack(pady=10)

        self.output = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=70)
        self.output.pack(pady=10)

    def run_thread(self):
        thread = threading.Thread(target=self.download_and_transcribe)
        thread.start()

    def download_and_transcribe(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a valid YouTube URL.")
            return

        try:
            self.append_output("[1] Downloading audio stream from YouTube using yt-dlp...")

            audio_path = self.download_audio_with_ytdlp(url)
            self.append_output(f"[2] Audio downloaded to: {audio_path}")

            self.append_output("[3] Transcribing with Whisper (this may take a while)...")
            result = self.model.transcribe(audio_path)
            transcript = result["text"]

            self.append_output("\n--- TRANSCRIPT ---\n")
            self.append_output(transcript)

            with open("transcript.txt", "w", encoding="utf-8") as f:
                f.write(transcript)

            self.append_output("\n Transcript saved to transcript.txt")

        except Exception as e:
            self.append_output(f"\n Error: {str(e)}")

    def download_audio_with_ytdlp(self, url, output_dir="downloads"):
        os.makedirs(output_dir, exist_ok=True)
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, 'temp.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
            'no_warnings': True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return os.path.join(output_dir, "temp.mp3")

    def append_output(self, text):
        self.output.insert(tk.END, text + "\n")
        self.output.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeTranscriberApp(root)
    root.mainloop()
