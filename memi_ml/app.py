"""Memi Mallorca — practise your memory about Mallorca."""

import os

from memi_engine import MemiConfig, create_app

import memi_ml.providers  # noqa: F401

config = MemiConfig(
    title="memi Mallorca",
    subtitle="practise your memory",
    favicon_color="#DA121A",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="sponsor",
    related_sites=[
        {"name": "memi", "url": "https://memi.click"},
        {"name": "memi portugal", "url": "https://pt.memi.click"},
        {"name": "memi lisboa", "url": "https://lx.memi.click"},
        {"name": "memi slovensko", "url": "https://sk.memi.click"},
        {"name": "memi US", "url": "https://us.memi.click"},
    ],
    about_html="""
        <p>Memi Mallorca is a memory practice game about Mallorca.</p>
        <p>Pick a category, look at the image, and try to guess what it is
        before revealing the answer.</p>
    """,
    done_html="""
        <svg width="200" height="180" viewBox="0 0 80 72" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <clipPath id="heart-clip">
                    <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"/>
                </clipPath>
            </defs>
            <g clip-path="url(#heart-clip)">
                <rect x="0" y="0"  width="80" height="9" fill="#FCDD09"/>
                <rect x="0" y="9"  width="80" height="9" fill="#DA121A"/>
                <rect x="0" y="18" width="80" height="9" fill="#FCDD09"/>
                <rect x="0" y="27" width="80" height="9" fill="#DA121A"/>
                <rect x="0" y="36" width="80" height="9" fill="#FCDD09"/>
                <rect x="0" y="45" width="80" height="9" fill="#DA121A"/>
                <rect x="0" y="54" width="80" height="9" fill="#FCDD09"/>
                <rect x="0" y="63" width="80" height="9" fill="#DA121A"/>
            </g>
            <path d="M40 68 C40 68 4 44 4 22 C4 10 14 2 24 2 C30 2 36 6 40 12 C44 6 50 2 56 2 C66 2 76 10 76 22 C76 44 40 68 40 68Z"
                  fill="none" stroke="var(--subtle, #888)" stroke-width="1.5"/>
        </svg>
    """,
)

instance_static = os.path.join(os.path.dirname(__file__), "..", "static")
app = create_app(config, instance_static=instance_static)

if __name__ == "__main__":
    app.run(debug=True, port=8089)
