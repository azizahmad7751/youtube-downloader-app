# YouTube Video Downloader

A simple and user-friendly Tkinter-based application for downloading YouTube videos. This application allows you to select a folder for saving the video, choose from available resolutions, and displays download progress.

## Features

- **User Interface**: Built with Tkinter for a modern and interactive GUI.
- **Resolution Selection**: Lists available video resolutions for download.
- **Download Progress**: Displays a progress bar indicating the download status.
- **Error Handling**: Provides detailed error messages for troubleshooting.


## Installation

### Prerequisites

Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

### Required Packages

1. **yt-dlp**: A fork of youtube-dl for downloading videos.

   Install it using pip:

   ```bash
   pip install yt-dlp
2. **tkinter**: Usually included with Python installations, but ensure it’s available.
   
###Clone the Repository
Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repository.git

Navigate to the project directory:

'''bash
cd your-repository

###Usage
1. Run the Application:

'''bash
python app.py
2. Enter YouTube URL:

Provide the URL of the YouTube video you want to download.

3. Select Save Folder:

Click "Browse" to choose the folder where the video will be saved.

4. Get Available Formats:

Click "Get Formats" to retrieve and display the available resolutions for the video.

5. Select Format:

Choose the desired video resolution from the dropdown list.

6. Start Download:

Click "Download" to begin downloading the video. The progress bar will show the download progress.

###Design and Styling
* Fonts: Custom fonts are used for titles, labels, and buttons to enhance readability.
* Colors: Buttons and background colors are chosen for a modern and visually appealing look.
* Layout: The application uses a grid layout for organized and responsive design.

### Contributing
Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue on the GitHub repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
yt-dlp: A powerful tool for downloading videos from YouTube and other sites.
Tkinter: Python's standard GUI library used for creating the application interface.

