"""Memi Mallorca — practise your memory about Mallorca."""

import os

from memi_engine import MemiConfig, create_app

import memi_ml.providers  # noqa: F401

# The home page opens on the menu, and its empty card shows Mallorca's coastline in the island's flag above
# "pick a category". The engine has no setting for that, so this rides on
# analytics_html (raw HTML at the bottom of every page, after app.js); loading
# a category replaces the card's text, so the map goes with it.
# static/flag-map-mallorca.svg: the coastline from OpenStreetMap (ODbL), the flag from Wikimedia Commons (public domain).
HOME_CARD_HTML = """
<style>
    #status.home { width: 100%; text-align: center; }
    #status .home-map, #done-art .home-map { display: block; max-width: 80%; max-height: calc(min(500px, 90vw) * 0.6); margin: 0 auto 1.5rem; }
</style>
<script>
(function () {
    var status = document.getElementById('status');
    if (status && status.textContent.trim() === 'pick a category') {
        status.classList.add('home');
        status.insertAdjacentHTML('afterbegin', '<img class="home-map" src="/static/flag-map-mallorca.svg" alt="Mallorca">');
    }
})();
</script>
"""

config = MemiConfig(
    # Details panel beside the card on reveal: the Wikipedia intro and, for
    # places, a map.
    layout="enriched",
    analytics_html=(
        '<script data-goatcounter="https://memi-ml.goatcounter.com/count"'
        ' async src="//gc.zgo.at/count.js"></script>'
    ) + HOME_CARD_HTML,
    title="memi mallorca",
    subtitle="practise your memory",
    favicon_color="#DA121A",
    sponsor_url="https://github.com/sponsors/filias",
    sponsor_text="sponsor",
    # The memi.games landing page, then every other public edition (memi
    # mallorca is private), in the landing page's order.
    related_sites=[
        {"name": "memi.games", "url": "https://memi.games"},
        {"name": "memi", "url": "https://world.memi.games"},
        {"name": "memi portugal", "url": "https://pt.memi.games"},
        {"name": "memi lisboa", "url": "https://lx.memi.games"},
        {"name": "memi slovensko", "url": "https://sk.memi.games"},
        {"name": "memi united states", "url": "https://us.memi.games"},
        {"name": "memi pyrenees", "url": "https://py.memi.games"},
        {"name": "memi kraków", "url": "https://kr.memi.games"},
        {"name": "memi romania", "url": "https://ro.memi.games"},
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
            <li><strong>know more:</strong> appears on reveal and opens the
            Wikipedia article (or source page) for the item, so you can read
            further.</li>
            <li><strong>report:</strong> flag a card if the image doesn't match
            the answer (wrong picture, broken thumbnail, etc.).</li>
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
    # The "all done" card shows the same flag map as the home card.
    done_html='<img class="home-map" src="/static/flag-map-mallorca.svg" alt="Mallorca">',
)

instance_static = os.path.join(os.path.dirname(__file__), "..", "static")
app = create_app(config, instance_static=instance_static)

if __name__ == "__main__":
    app.run(debug=True, port=8089)
