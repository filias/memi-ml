"""53 municipalities of Mallorca, grouped by comarca.

Comarca breakdown follows the standard 6-comarca division used on
es.wikipedia.org/wiki/Comarcas_de_Mallorca.

Locator maps come from Wikimedia Commons under the canonical pattern
``Localització de <Municipi> respecte de Mallorca.svg`` (with the Catalan
elision ``de`` -> ``d'`` before vowels). All 53 files exist and were
batch-verified via the Commons API.
"""

# Comarca display name -> ordered list of member municipalities.
COMARQUES = {
    "Palma": ["Palma"],
    "Serra de Tramuntana": [
        "Andratx", "Banyalbufar", "Bunyola", "Calvià", "Deià", "Escorca",
        "Esporles", "Estellencs", "Fornalutx", "Pollença", "Puigpunyent",
        "Sóller", "Valldemossa",
    ],
    "Raiguer": [
        "Alaró", "Alcúdia", "Binissalem", "Búger", "Campanet", "Consell",
        "Inca", "Lloseta", "Mancor de la Vall", "Marratxí", "sa Pobla",
        "Santa Maria del Camí", "Selva",
    ],
    "Pla de Mallorca": [
        "Algaida", "Ariany", "Costitx", "Lloret de Vistalegre", "Llubí",
        "Maria de la Salut", "Montuïri", "Muro", "Petra", "Porreres",
        "Sant Joan", "Santa Eugènia", "Santa Margalida", "Sencelles",
        "Sineu", "Vilafranca de Bonany",
    ],
    "Migjorn": ["Campos", "Felanitx", "Llucmajor", "ses Salines", "Santanyí"],
    "Llevant": [
        "Artà", "Capdepera", "Manacor", "Sant Llorenç des Cardassar",
        "Son Servera",
    ],
}

ALL = [m for munis in COMARQUES.values() for m in munis]

# Reverse lookup: municipality -> comarca display name.
COMARCA_BY_MUNICIPALITY = {m: c for c, munis in COMARQUES.items() for m in munis}

# URL-safe filter keys -> member municipalities (mirrors REGIONS in memi-us states).
FILTER = {
    "palma": COMARQUES["Palma"],
    "tramuntana": COMARQUES["Serra de Tramuntana"],
    "raiguer": COMARQUES["Raiguer"],
    "pla": COMARQUES["Pla de Mallorca"],
    "migjorn": COMARQUES["Migjorn"],
    "llevant": COMARQUES["Llevant"],
}


def locator_filename(municipality: str) -> str:
    """Build the Commons filename for a municipality's locator map.

    Catalan elides ``de`` to ``d'`` before vowels (a, e, i, o, u).
    The lowercase Mallorcan articles ``sa``/``ses`` start with ``s``,
    so they take ``de`` like any consonant.
    """
    article = "d'" if municipality[0].lower() in "aeiou" else "de "
    return f"Localització {article}{municipality} respecte de Mallorca.svg"
