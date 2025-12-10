import re
import pathlib
import yaml
import requests

# Filer och mappar vi jobbar med
VIDEOS_YAML = pathlib.Path("videos.yml")
VIDEOBANK = pathlib.Path("docs/videobank.md")
SNIPPET_DIR = pathlib.Path("docs/includes/videos")
SNIPPET_DIR.mkdir(parents=True, exist_ok=True)


def extract_video_id(url: str) -> str:
    """
    Plockar ut YouTube-video-ID från olika URL-varianter.
    Funkar för:
      - https://youtu.be/ID
      - https://www.youtube.com/watch?v=ID
      - https://youtube.com/shorts/ID
    """
    # youtu.be/ID
    m = re.search(r"youtu\.be/([^?&/]+)", url)
    if m:
        return m.group(1)

    # watch?v=ID
    m = re.search(r"v=([^?&/]+)", url)
    if m:
        return m.group(1)

    # shorts/ID
    m = re.search(r"shorts/([^?&/]+)", url)
    if m:
        return m.group(1)

    raise ValueError(f"Kunde inte hitta video-ID i URL: {url}")


def fetch_title(url: str) -> str:
    """
    Hämtar videotitel via YouTubes oEmbed (ingen API-nyckel behövs).
    """
    oembed_url = "https://www.youtube.com/oembed"
    params = {"url": url, "format": "json"}
    resp = requests.get(oembed_url, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return data.get("title", "YouTube-video")


def load_videos():
    """
    Läser in listan med URL:er från videos.yml.
    """
    with VIDEOS_YAML.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def generate_snippets(urls):
    """
    Skapar små .md-snuttar i docs/includes/videos/ med thumbnail + länk.
    """
    for url in urls:
        vid = extract_video_id(url)
        thumb_url = f"https://img.youtube.com/vi/{vid}/hqdefault.jpg"

        try:
            title = fetch_title(url)
        except Exception as e:
            print(f"Varning: kunde inte hämta titel för {url}: {e}")
            title = f"YouTube-video ({vid})"

        key = f"video-{vid}"
        md = f"""### {title}

[![{title}]({thumb_url})]({url})

"""

        out_path = SNIPPET_DIR / f"{key}.md"
        out_path.write_text(md, encoding="utf-8")
        print(f"Skrev snippet: {out_path}")


def update_videobank(urls):
    """
    Lägger till nya rader i videobank-tabellen med tomma bedömningsfält.
    Antagande: docs/videobank.md har redan en tabell med rubrikrad.
    """
    text = VIDEOBANK.read_text(encoding="utf-8")

    # Hitta alla URL:er som redan finns i filen
    existing_urls = set(re.findall(r"https?://[^\s|]+", text))

    # Hitta högsta # i tabellen
    last_num = 0
    for line in text.splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|", line)
        if m:
            last_num = max(last_num, int(m.group(1)))

    new_lines = []
    current_num = last_num

    for url in urls:
        if url in existing_urls:
            print(f"Hoppar över (finns redan i videobank): {url}")
            continue

        vid = extract_video_id(url)

        try:
            title = fetch_title(url)
        except Exception as e:
            print(f"Varning: kunde inte hämta titel för {url}: {e}")
            title = f"YouTube-video ({vid})"

        current_num += 1
        # Lämna längd, svårighetsgrad, rekommenderad användning, med i kursen? tomma
        row = (
            f"| {current_num} | {title} | {url} | "
            f" |  |  |  |\n"
        )
        new_lines.append(row)

    if not new_lines:
        print("Inga nya videor att lägga till i videobank.md")
        return

    # Lägg till rader i slutet av filen
    if not text.endswith("\n"):
        text += "\n"
    text += "".join(new_lines)

    VIDEOBANK.write_text(text, encoding="utf-8")
    print(f"La till {len(new_lines)} rader i {VIDEOBANK}")


def main():
    urls = load_videos()
    if not urls:
        print("Inga URL:er i videos.yml")
        return

    generate_snippets(urls)
    update_videobank(urls)


if __name__ == "__main__":
    main()
