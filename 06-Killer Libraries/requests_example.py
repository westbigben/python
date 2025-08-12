"""Requests example — try a simple API call with a local fallback."""
import requests, json, os
from pathlib import Path

FALLBACK = Path(__file__).parent / "sample_api_response.json"

def main():
    url = "https://api.github.com"  # small, public API
    print("Requests demo — trying to GET", url)
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        data = r.json()
        print("Received keys from API:", list(data.keys())[:10])
        # show a sample key/value
        sample_key = next(iter(data.keys()))
        print("Sample:", sample_key, "=", data[sample_key])
    except Exception as e:
        print("Request failed — falling back to local sample JSON. Error:", e)
        with open(FALLBACK) as f:
            data = json.load(f)
        print("Loaded fallback keys:", list(data.keys()))

if __name__ == '__main__':
    main()
