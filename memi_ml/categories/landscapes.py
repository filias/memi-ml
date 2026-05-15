"""Famous Mallorca landscapes — beaches, coves (cales), capes, peaks, caves."""

ALL = [
    "Es Trenc",
    "Sa Calobra",
    "Cala Agulla",
    "Cala Millor",
    "Cala d'Or",
    "Cala Bona",
    "Cala Tuent",
    "Cala Figuera",
    "Cala Llombards",
    "Port de Sóller",
    "Cap de Formentor",
    "Puig Major",
    "Puig de Massanella",
    "Puig Tomir",
    "Puig de Galatzó",
    "Coves del Drac",
]

# Display name -> English Wikipedia article title.
WIKIPEDIA = {
    "Es Trenc": "Es Trenc",
    "Sa Calobra": "Sa Calobra",
    "Cala Agulla": "Cala Agulla",
    "Cala Millor": "Cala Millor",
    "Cala d'Or": "Cala d'Or",
    "Cala Bona": "Cala Bona",
    "Cala Tuent": "Cala Tuent",
    "Cala Figuera": "Cala Figuera",
    "Cala Llombards": "Cala Llombards",
    "Port de Sóller": "Port de Sóller",
    "Cap de Formentor": "Cap de Formentor",
    "Puig Major": "Puig Major",
    "Puig de Massanella": "Puig de Massanella",
    "Puig Tomir": "Puig Tomir",
    "Puig de Galatzó": "Galatzó",
    "Coves del Drac": "Cuevas del Drach",
}

# Display name -> Wikimedia Commons file, when the Wikipedia article's lead
# image is a map / town shot instead of the landscape itself. Checked first.
COMMONS_FILES = {
    "Cala Millor": "Cala Millor Beach 1.JPG",
    "Cala d'Or": "Cala d'Or (Cala d'Or) 14.jpg",
    "Coves del Drac": "Covas del Drac - lit stalagmites and stalagtites 01.jpg",
}

# Display name -> altitude string (shown as tag on reveal). Peaks only.
ALTITUDES = {
    "Puig Major": "1,445 m",
    "Puig de Massanella": "1,367 m",
    "Puig Tomir": "1,103 m",
    "Puig de Galatzó": "1,026 m",
}
