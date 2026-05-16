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

        <h2>How to play</h2>
        <p>Pick a category, look at the image, and try to guess what it is
        before revealing the answer. No accounts, no scores, no time
        limits.</p>
        <p>A few helpers sit in the bottom row:</p>
        <ul>
            <li><strong>clues:</strong> toggle progressive letter hints &mdash;
            reveals the first letter, then the next, and so on. Handy when
            the name is on the tip of your tongue.</li>
            <li><strong>report:</strong> flag a card if the image doesn't match
            the answer (wrong picture, broken thumbnail, etc.).</li>
            <li><strong>know more:</strong> appears on reveal and opens the
            Wikipedia article (or source page) for the item, so you can read
            further.</li>
        </ul>
        <p>You can play it two ways:</p>
        <ul>
            <li><strong>To learn:</strong> when you don't recognise an item,
            reveal the answer and follow the <em>know more</em> link to read
            about it. Each exposure strengthens the link between the image
            and the name.</li>
            <li><strong>To test yourself:</strong> once a category feels
            familiar, cycle through it and see how many you can name
            without revealing.</li>
        </ul>

        <h2>Why it works</h2>
        <p>This is a simple form of <em>active recall</em> &mdash; pulling
        information out of memory instead of re-reading it. The
        <em>testing effect</em>, well documented in cognitive psychology,
        shows that retrieval practice builds more durable memory traces
        than re-exposure alone.</p>
        <p>Because each prompt is a picture, the game also leverages the
        <em>picture superiority effect</em>: images are encoded more richly
        than words and are easier to retrieve later. Naming the item is a
        form of <em>cued recall</em>, sitting between simple recognition
        (&ldquo;have I seen this before?&rdquo;) and unaided <em>free
        recall</em>.</p>
        <p>Short, frequent sessions outperform long ones &mdash; the
        <em>spacing effect</em>. A few minutes a day is enough.</p>
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
