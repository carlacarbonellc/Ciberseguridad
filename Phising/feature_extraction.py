# feature_extraction.py

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import features


def extract_features(html, url):
    soup = BeautifulSoup(html, "html.parser")
    domain = urlparse(url).netloc

    feature_vector = {
        "num_links": features.count_links(soup),
        "num_forms": features.count_forms(soup),
        "num_inputs": features.count_inputs(soup),
        "num_scripts": features.count_scripts(soup),
        "has_password": features.has_password_input(soup),
        "num_iframes": features.count_iframes(soup),
        "num_images": features.count_images(soup),
        "num_external_links": features.count_external_links(soup, domain),
    }

    return feature_vector
