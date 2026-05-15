"""Iconic Mallorca monuments and historic sites."""

ALL = [
    "Catedral de Palma",
    "Castell de Bellver",
    "Palau de l'Almudaina",
    "Cartoixa de Valldemossa",
    "Santuari de Lluc",
    "Castell de Capdepera",
    "Es Baluard",
    "Cap de Formentor",
    "Capocorb Vell",
    "Ses Païsses",
    "Coves del Drac",
    "Creu de Santa Ponsa",
]

# Display name -> English Wikipedia article title.
WIKIPEDIA = {
    "Catedral de Palma": "Palma Cathedral",
    "Castell de Bellver": "Bellver Castle",
    "Palau de l'Almudaina": "Royal Palace of La Almudaina",
    "Cartoixa de Valldemossa": "Valldemossa Charterhouse",
    "Santuari de Lluc": "Santuari de Lluc",
    "Castell de Capdepera": "Castle of Capdepera",
    "Es Baluard": "Es Baluard",
    "Cap de Formentor": "Cap de Formentor",
    "Capocorb Vell": "Capocorb Vell",
    "Ses Païsses": "Ses Païsses",
    "Coves del Drac": "Cuevas del Drach",
}

# Display name -> Wikimedia Commons filename, for items without an English
# Wikipedia article. Checked before WIKIPEDIA.
COMMONS_FILES = {
    "Creu de Santa Ponsa": "Calvià. Santa Ponça. Creu del Desembarcament (1).jpg",
}
