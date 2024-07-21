import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import font as tkfont

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")

        # Custom Fonts
        self.title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=12)
        self.button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

        # Frame for main content
        self.main_frame = tk.Frame(root, padx=20, pady=20, bg="#f5f5f5")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.folder_path = tk.StringVar()
        self.video_url = tk.StringVar()
        self.video_format = tk.StringVar()
        self.formats = []

        # Title
        tk.Label(self.main_frame, text="YouTube Video Downloader", font=self.title_font, bg="#f5f5f5").grid(row=0, column=0, columnspan=3, pady=10)

        # URL Entry
        tk.Label(self.main_frame, text="YouTube URL:", font=self.label_font, bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.url_entry = tk.Entry(self.main_frame, width=50, textvariable=self.video_url, font=self.label_font)
        self.url_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Folder Path
        tk.Label(self.main_frame, text="Save to folder:", font=self.label_font, bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(self.main_frame, textvariable=self.folder_path, width=50, font=self.label_font).grid(row=2, column=1, padx=10, pady=5, sticky="w")
        tk.Button(self.main_frame, text="Browse", command=self.open_file_dialog, font=self.button_font, bg="#4CAF50", fg="white").grid(row=2, column=2, padx=10, pady=5)

        # Format Selection
        tk.Label(self.main_frame, text="Select Format:", font=self.label_font, bg="#f5f5f5").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.format_combobox = ttk.Combobox(self.main_frame, textvariable=self.video_format, state="readonly", font=self.label_font)
        self.format_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Buttons
        tk.Button(self.main_frame, text="Get Formats", command=self.get_formats, font=self.button_font, bg="#2196F3", fg="white").grid(row=3, column=2, padx=10, pady=5)
        tk.Button(self.main_frame, text="Download", command=self.download_video, font=self.button_font, bg="#FFC107", fg="white").grid(row=4, columnspan=3, pady=20)

        # Progress Bar
        self.progress = ttk.Progressbar(self.main_frame, orient="horizontal", length=400, mode="determinate")
        self.progress.grid(row=5, columnspan=3, pady=20)

        # Center align the main frame
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def open_file_dialog(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def get_formats(self):
        url = self.video_url.get()
        if not url:
            messagebox.showerror("Error", "Please provide a valid URL.")
            return

        ydl_opts = {}

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                self.formats = info_dict.get('formats', [])
                if not self.formats:
                    raise ValueError("No formats found.")
                format_list = [f'{f["format_id"]} - {f["ext"]} - {f.get("format_note", "unknown")} - {f.get("resolution", "audio only")}' for f in self.formats if f['ext'] == 'mp4']
                self.format_combobox['values'] = format_list
                if format_list:
                    self.format_combobox.current(0)
                else:
                    messagebox.showerror("Error", "No suitable formats found.")
        except youtube_dl.utils.DownloadError as e:
            messagebox.showerror("Error", f"DownloadError: {e}")
        except youtube_dl.utils.ExtractorError as e:
            messagebox.showerror("Error", f"ExtractorError: {e}")
        except youtube_dl.utils.GeoRestrictedError as e:
            messagebox.showerror("Error", f"GeoRestrictedError: {e}")
        except youtube_dl.utils.UnavailableVideoError as e:
            messagebox.showerror("Error", f"UnavailableVideoError: {e}")
        except youtube_dl.utils.MaxDownloadsReached as e:
            messagebox.showerror("Error", f"MaxDownloadsReached: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def download_video(self):
        url = self.video_url.get()
        save_path = self.folder_path.get()
        selected_format = self.video_format.get().split(' ')[0]

        if not url or not save_path or not selected_format:
            messagebox.showerror("Error", "Please provide a valid URL, select a folder, and choose a format.")
            return

        ydl_opts = {
            'format': selected_format,
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'progress_hooks': [self.progress_hook],
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download video: {e}")

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d['_percent_str']
            percent = float(percent.replace('%', '').strip())
            self.progress['value'] = percent
            self.root.update_idletasks()
        elif d['status'] == 'finished':
            self.progress['value'] = 100
            self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
