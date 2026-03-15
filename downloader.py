#!/usr/bin/env python3
"""TikTok FHD Video Downloader

Downloads TikTok videos (without watermark where possible) using yt-dlp.

Usage:
    python downloader.py <tiktok_url> [output_directory]

Examples:
    python downloader.py https://vt.tiktok.com/ZSuSaLEdF/
    python downloader.py https://www.tiktok.com/@user/video/1234567890 ./downloads
"""

import os
import sys
import yt_dlp


def download_tiktok_video(url: str, output_dir: str = ".") -> str:
    """Download a TikTok video from the given URL.

    Args:
        url: The TikTok video URL (supports short URLs like vt.tiktok.com).
        output_dir: Directory where the video will be saved (default: current directory).

    Returns:
        The file path of the downloaded video.

    Raises:
        yt_dlp.utils.DownloadError: If the download fails.
    """
    os.makedirs(output_dir, exist_ok=True)

    output_template = os.path.join(output_dir, "%(uploader)s_%(id)s.%(ext)s")

    ydl_opts = {
        "outtmpl": output_template,
        # Prefer the best video quality available
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        # Use TikTok's API to get the watermark-free version when available
        "extractor_args": {"tiktok": {"api_hostname": "api22-normal-c-useast2a.tiktokv.com"}},
        "quiet": False,
        "no_warnings": False,
    }

    downloaded_file = None

    def progress_hook(d: dict) -> None:
        nonlocal downloaded_file
        if d["status"] == "finished":
            downloaded_file = d["filename"]

    ydl_opts["progress_hooks"] = [progress_hook]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return downloaded_file


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    print(f"Downloading TikTok video: {url}")
    print(f"Output directory: {os.path.abspath(output_dir)}")

    try:
        file_path = download_tiktok_video(url, output_dir)
        if file_path:
            print(f"\nDownload complete: {file_path}")
        else:
            print("\nDownload complete.")
    except yt_dlp.utils.DownloadError as e:
        print(f"\nError downloading video: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
