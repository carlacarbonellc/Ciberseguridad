# features.py
"""
Definición de las características basadas en contenido HTML
Cada función devuelve un valor numérico
"""

def count_links(soup):
    """Cuenta el número de enlaces <a>"""
    return len(soup.find_all("a"))


def count_forms(soup):
    """Cuenta el número de formularios"""
    return len(soup.find_all("form"))


def count_inputs(soup):
    """Cuenta campos de entrada"""
    return len(soup.find_all("input"))


def count_scripts(soup):
    """Cuenta scripts"""
    return len(soup.find_all("script"))


def has_password_input(soup):
    """Detecta si hay inputs tipo password"""
    for inp in soup.find_all("input"):
        if inp.get("type") == "password":
            return 1
    return 0


def count_iframes(soup):
    """Cuenta iframes"""
    return len(soup.find_all("iframe"))


def count_images(soup):
    """Cuenta imágenes"""
    return len(soup.find_all("img"))


def count_external_links(soup, domain):
    """Cuenta enlaces externos al dominio"""
    external = 0
    for link in soup.find_all("a", href=True):
        if domain not in link["href"]:
            external += 1
    return external
