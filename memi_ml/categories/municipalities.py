"""53 municipalities of Mallorca, grouped by region.

Region breakdown follows the standard 6-region division used on
es.wikipedia.org/wiki/Comarcas_de_Mallorca.

Locator maps come from Wikimedia Commons under the canonical pattern
``Localització de <Municipi> respecte de Mallorca.svg`` (with the Catalan
elision ``de`` -> ``d'`` before vowels). All 53 files exist and were
batch-verified via the Commons API.
"""

# Region display name -> ordered list of member municipalities.
REGIONS = {
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

ALL = [m for munis in REGIONS.values() for m in munis]

# Reverse lookup: municipality -> region display name.
REGION_BY_MUNICIPALITY = {m: c for c, munis in REGIONS.items() for m in munis}

# URL-safe filter keys -> member municipalities (mirrors REGIONS in memi-us states).
FILTER = {
    "palma": REGIONS["Palma"],
    "tramuntana": REGIONS["Serra de Tramuntana"],
    "raiguer": REGIONS["Raiguer"],
    "pla": REGIONS["Pla de Mallorca"],
    "migjorn": REGIONS["Migjorn"],
    "llevant": REGIONS["Llevant"],
}


def locator_filename(municipality: str) -> str:
    """Build the Commons filename for a municipality's locator map.

    Catalan elides ``de`` to ``d'`` before vowels (a, e, i, o, u).
    The lowercase Mallorcan articles ``sa``/``ses`` start with ``s``,
    so they take ``de`` like any consonant.
    """
    article = "d'" if municipality[0].lower() in "aeiou" else "de "
    return f"Localització {article}{municipality} respecte de Mallorca.svg"

# English Wikipedia article for each municipality (the details panel).
WIKIPEDIA = {
    "Palma": "Palma de Mallorca",
    "Andratx": "Andratx",
    "Banyalbufar": "Banyalbufar",
    "Bunyola": "Bunyola",
    "Calvià": "Calvià",
    "Deià": "Deià",
    "Escorca": "Escorca",
    "Esporles": "Esporles",
    "Estellencs": "Estellencs",
    "Fornalutx": "Fornalutx",
    "Pollença": "Pollença",
    "Puigpunyent": "Puigpunyent",
    "Sóller": "Sóller",
    "Valldemossa": "Valldemossa",
    "Alaró": "Alaró",
    "Alcúdia": "Alcúdia",
    "Binissalem": "Binissalem",
    "Búger": "Búger",
    "Campanet": "Campanet",
    "Consell": "Consell",
    "Inca": "Inca, Spain",
    "Lloseta": "Lloseta",
    "Mancor de la Vall": "Mancor de la Vall",
    "Marratxí": "Marratxí",
    "sa Pobla": "Sa Pobla",
    "Santa Maria del Camí": "Santa Maria del Camí",
    "Selva": "Selva, Mallorca",
    "Algaida": "Algaida",
    "Ariany": "Ariany, Spain",
    "Costitx": "Costitx",
    "Lloret de Vistalegre": "Lloret de Vistalegre",
    "Llubí": "Llubí",
    "Maria de la Salut": "Maria de la Salut",
    "Montuïri": "Montuïri",
    "Muro": "Muro, Mallorca",
    "Petra": "Petra, Spain",
    "Porreres": "Porreres",
    "Sant Joan": "Sant Joan",
    "Santa Eugènia": "Santa Eugènia, Mallorca",
    "Santa Margalida": "Santa Margalida",
    "Sencelles": "Sencelles",
    "Sineu": "Sineu",
    "Vilafranca de Bonany": "Vilafranca de Bonany",
    "Campos": "Campos, Spain",
    "Felanitx": "Felanitx",
    "Llucmajor": "Llucmajor",
    "ses Salines": "Ses Salines",
    "Santanyí": "Santanyí",
    "Artà": "Artà",
    "Capdepera": "Capdepera",
    "Manacor": "Manacor",
    "Sant Llorenç des Cardassar": "Sant Llorenç des Cardassar",
    "Son Servera": "Son Servera",
}
