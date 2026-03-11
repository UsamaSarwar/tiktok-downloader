# tiktok-downloader
TikTok FHD Video Downloader

A Python script to download TikTok videos (without watermark where possible).

## Requirements

- Python 3.8+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) ≥ 2026.2.21

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python downloader.py <tiktok_url> [output_directory]
```

### Examples

```bash
# Download to current directory
python downloader.py https://vt.tiktok.com/ZSuSaLEdF/

# Download to a specific folder
python downloader.py https://www.tiktok.com/@user/video/1234567890 ./downloads
```

Downloaded files are saved as `<uploader>_<video_id>.mp4` in the output directory.
