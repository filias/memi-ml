"""Iconic Mallorca monuments and historic sites."""

ALL = [
    "Catedral de Palma",
    "Castell de Bellver",
    "Palau de l'Almudaina",
    "Cartoixa de Valldemossa",
    "Santuari de Lluc",
    "Castell de Capdepera",
    "Es Baluard",
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
    "Capocorb Vell": "Capocorb Vell",
    "Ses Païsses": "Ses Païsses",
    "Coves del Drac": "Cuevas del Drach",
}

# Display name -> /static/... path, for items without a usable Wikipedia image.
# Checked before WIKIPEDIA.
STATIC_FILES = {
    "Creu de Santa Ponsa": "/static/monuments/creu-santa-ponsa.webp",
}
