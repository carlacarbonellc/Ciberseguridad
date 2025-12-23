# data_collector.py

import requests
import pandas as pd
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from feature_extraction import extract_features

disable_warnings(InsecureRequestWarning)


def normalize_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return "http://" + url


def collect_data(input_csv, output_csv, label, limit=50):
    df = pd.read_csv(input_csv)
    urls = df["url"].tolist()[:limit]

    rows = []

    for url in urls:
        try:
            url = normalize_url(url)
            response = requests.get(url, timeout=5, verify=False)
            if response.status_code == 200:
                features = extract_features(response.text, url)
                features["URL"] = url
                features["label"] = label
                rows.append(features)
                print(f"[OK] {url}")
        except Exception as e:
            print(f"[ERROR] {url} -> {e}")

    result_df = pd.DataFrame(rows)
    result_df.to_csv(output_csv, index=False)
    print(f"Dataset guardado en {output_csv}")


if __name__ == "__main__":
    # LEGÍTIMOS
    collect_data(
        input_csv="top-1m.csv",
        output_csv="structured_data_legitimate.csv",
        label=0
    )

    # PHISHING
    collect_data(
        input_csv="verified_online.csv",
        output_csv="structured_data_phishing.csv",
        label=1
    )
