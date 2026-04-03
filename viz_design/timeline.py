from shiny import ui


TIMELINE_EVENTS = [
    {
        "year": "ca. 860",
        "title": "First Recorded Meteorite",
        "name": "Nogata",
        "mass": "472 g",
        "composition": "Ordinary chondrite (historical record)",
        "location": "Nogata, Fukuoka, Japan",
        "status": "Fell",
        "wiki_url": "https://en.wikipedia.org/wiki/N%C5%8Dgata_meteorite",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Meteorite_NWA_869.jpg/640px-Meteorite_NWA_869.jpg",
        "notes": [],
    },
    {
        "year": "1575",
        "title": "One of the Biggest Meteorites",
        "name": "Campo del Cielo",
        "mass": "50 t",
        "composition": "Iron meteorite (IAB complex)",
        "location": "Gran Chaco region, Argentina",
        "status": "Found",
        "wiki_url": "https://en.wikipedia.org/wiki/Campo_del_Cielo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Meteorito_Campo_del_Cielo.jpg/640px-Meteorito_Campo_del_Cielo.jpg",
        "notes": [],
    },
    {
        "year": "1818",
        "title": "One of the Biggest Meteorites",
        "name": "Cape York",
        "mass": "58.2 t",
        "composition": "Iron meteorite (coarse octahedrite)",
        "location": "Savissivik, Greenland",
        "status": "Found",
        "wiki_url": "https://en.wikipedia.org/wiki/Cape_York_meteorite",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Cape_York_Meteorite.jpg/640px-Cape_York_Meteorite.jpg",
        "notes": [],
    },
    {
        "year": "1920",
        "title": "Biggest Known Meteorite",
        "name": "Hoba",
        "mass": "60 t",
        "composition": "Iron meteorite (ataxite)",
        "location": "Grootfontein, Namibia",
        "status": "Found",
        "wiki_url": "https://en.wikipedia.org/wiki/Hoba_meteorite",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Hoba_meteorite%2C_Grootfontein%2C_Namibia%2C_2018.jpg/640px-Hoba_meteorite%2C_Grootfontein%2C_Namibia%2C_2018.jpg",
        "notes": ["Weight equivalent: 60 t / 12 t = 5 London double-decker buses."],
    },
    {
        "year": "1954",
        "title": "Meteorite Hit House and Person",
        "name": "Sylacauga meteorite",
        "mass": "5.56 kg",
        "composition": "Ordinary chondrite",
        "location": "Sylacauga, Alabama, USA",
        "status": "Fell",
        "wiki_url": "https://en.wikipedia.org/wiki/Sylacauga_(meteorite)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Sylacauga_meteorite.jpg/640px-Sylacauga_meteorite.jpg",
        "notes": [],
    },
    {
        "year": "1984",
        "title": "Mars Meteorite",
        "name": "Allan Hills 84001",
        "mass": "1.9309 kg",
        "composition": "Orthopyroxenite (Martian meteorite)",
        "location": "Allan Hills, Antarctica",
        "status": "Found",
        "wiki_url": "https://en.wikipedia.org/wiki/Allan_Hills_84001",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/ALH84001_in_museum.jpg/640px-ALH84001_in_museum.jpg",
        "notes": [],
    },
    {
        "year": "2013",
        "title": "Chelyabinsk Exploding Meteor",
        "name": "Chelyabinsk meteor",
        "mass": "100 kg (large recovered fragment)",
        "composition": "LL5 ordinary chondrite",
        "location": "Chelyabinsk Oblast, Russia",
        "status": "Fell",
        "wiki_url": "https://en.wikipedia.org/wiki/Chelyabinsk_meteor",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Chelyabinsk_meteor.jpg/640px-Chelyabinsk_meteor.jpg",
        "notes": [],
    },
    {
        "year": "2003",
        "title": "Peak of Recorded Distribution",
        "name": "Most meteorites recorded in one year",
        "mass": "n/a",
        "composition": "Mixed compositions",
        "location": "Global",
        "status": "3323 sightings",
        "wiki_url": "https://en.wikipedia.org/wiki/Meteorite_fall",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Meteor_crater_barringer.jpg/640px-Meteor_crater_barringer.jpg",
        "notes": [],
    },
]


def _meta_row(label, value):
    return ui.tags.li(
        ui.tags.span(label, class_="timeline-meta-label"),
        ui.tags.span(value, class_="timeline-meta-value"),
        class_="timeline-meta-row",
    )


def _timeline_item(event, index):
    side = "left" if index % 2 == 0 else "right"
    details = ui.tags.ul(
        _meta_row("Mass", event["mass"]),
        _meta_row("Composition", event["composition"]),
        _meta_row("Location", event["location"]),
        class_="timeline-meta",
    )

    entries = []
    for line in event.get("entries", []):
        entries.append(ui.tags.li(line, class_="timeline-entry-item"))

    notes = []
    for note in event.get("notes", []):
        notes.append(ui.tags.p(note, class_="timeline-note"))

    return ui.tags.article(
        ui.tags.div(
            ui.tags.span(event["year"], class_="timeline-year"),
            ui.tags.span(event["status"], class_="timeline-status"),
            class_="timeline-topline",
        ),
        ui.tags.h3(event["name"], class_="timeline-title"),
        ui.tags.p(event["title"], class_="timeline-event-type"),
        ui.tags.img(
            src=event["image_url"],
            alt=f"{event['name']} meteorite",
            class_="timeline-image",
            loading="lazy",
        ),
        ui.tags.p("Image unavailable. Open Wiki link.", class_="timeline-image-fallback"),
        details,
        ui.tags.ul(*entries, class_="timeline-entry-list") if entries else None,
        *notes,
        ui.tags.div(
            ui.tags.a("Image (Wiki)", href=event["image_url"], target="_blank", rel="noopener noreferrer", class_="timeline-link"),
            ui.tags.a("Wiki", href=event["wiki_url"], target="_blank", rel="noopener noreferrer", class_="timeline-link"),
            class_="timeline-links",
        ),
        class_=f"timeline-item {side}",
    )


def build_scroll_timeline_section():
    return ui.tags.section(
        ui.tags.style(
            """
            .scroll-timeline-section {
                position: relative;
                z-index: 10;
                background:
                    radial-gradient(circle at 15% 0%, rgba(13, 110, 253, 0.16), transparent 35%),
                    radial-gradient(circle at 85% 100%, rgba(255, 120, 80, 0.10), transparent 35%),
                    #121212;
                padding: 64px 24px 86px;
                border-top: 1px solid #1a1a1a;
                border-bottom: 1px solid #1a1a1a;
            }

            .timeline-header {
                max-width: 860px;
                margin: 0 auto 34px auto;
            }

            .timeline-kicker {
                margin: 0 0 8px 0;
                color: #7f7f7f;
                font-size: 11px;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 1.6px;
            }

            .timeline-heading {
                margin: 0;
                color: #ffffff;
                font-size: clamp(1.5rem, 2.3vw, 2.1rem);
                font-weight: 800;
                letter-spacing: -0.02em;
            }

            .timeline-subtitle {
                margin: 10px 0 0 0;
                color: #a2a2a2;
                font-size: 15px;
                max-width: 64ch;
            }

            .scroll-timeline {
                position: relative;
                max-width: 860px;
                margin: 0 auto;
                padding: 10px 0;
            }

            .scroll-timeline::before {
                content: "";
                position: absolute;
                top: 0;
                bottom: 0;
                left: 50%;
                width: 2px;
                background: linear-gradient(to bottom, #2c2c2c, #4f4f4f, #2c2c2c);
                transform: translateX(-50%);
            }

            .timeline-item {
                width: calc(50% - 34px);
                margin: 0 0 28px 0;
                padding: 16px 18px 18px;
                border: 1px solid rgba(255, 255, 255, 0.14);
                border-radius: 14px;
                background: rgba(25, 25, 25, 0.88);
                box-shadow: 0 16px 28px rgba(0, 0, 0, 0.32);
                position: relative;
                opacity: 0;
                transform: translateY(26px);
                pointer-events: none;
                transition: opacity 380ms ease, transform 380ms ease;
            }

            .timeline-item.left {
                margin-right: auto;
            }

            .timeline-item.right {
                margin-left: auto;
            }

            .timeline-item::before {
                content: "";
                position: absolute;
                top: 22px;
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: #0d6efd;
                border: 2px solid #9fc3ff;
            }

            .timeline-item.left::before {
                right: -41px;
            }

            .timeline-item.right::before {
                left: -41px;
            }

            .timeline-item.is-current {
                opacity: 1;
                transform: translate(0, 0);
                pointer-events: auto;
            }

            .timeline-item.is-past {
                opacity: 0;
                transform: translateY(-26px);
            }

            .timeline-item.is-future {
                opacity: 0;
                transform: translateY(26px);
            }

            .timeline-topline {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 10px;
            }

            .timeline-year {
                display: inline-block;
                color: #8ab4ff;
                font-family: monospace;
                font-size: 13px;
                font-weight: 700;
                letter-spacing: 0.06em;
            }

            .timeline-status {
                color: #d2d2d2;
                font-size: 11px;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                border: 1px solid rgba(255, 255, 255, 0.16);
                border-radius: 999px;
                padding: 2px 8px;
            }

            .timeline-title {
                margin: 10px 0 10px 0;
                color: #f5f5f5;
                font-size: 1.05rem;
                line-height: 1.3;
            }

            .timeline-event-type {
                margin: -3px 0 10px 0;
                color: #9b9b9b;
                font-size: 12px;
                letter-spacing: 0.04em;
                text-transform: uppercase;
            }

            .timeline-image {
                width: 100%;
                max-height: 190px;
                object-fit: cover;
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.12);
                margin-bottom: 10px;
                display: block;
            }

            .timeline-image-fallback {
                display: none;
                margin: 0 0 10px 0;
                color: #8f8f8f;
                font-size: 12px;
            }

            .timeline-meta {
                list-style: none;
                margin: 0;
                padding: 0;
                display: grid;
                gap: 6px;
            }

            .timeline-meta-row {
                display: grid;
                grid-template-columns: 110px 1fr;
                align-items: baseline;
                gap: 8px;
                font-size: 13px;
            }

            .timeline-meta-label {
                color: #9a9a9a;
                text-transform: uppercase;
                letter-spacing: 0.06em;
                font-size: 11px;
            }

            .timeline-meta-value {
                color: #d6d6d6;
            }

            .timeline-entry-list {
                margin: 10px 0 0 0;
                padding-left: 18px;
                color: #d6d6d6;
                font-size: 13px;
                line-height: 1.45;
            }

            .timeline-entry-item {
                margin-bottom: 3px;
            }

            .timeline-note {
                margin: 8px 0 0 0;
                color: #9f9f9f;
                font-size: 12px;
                line-height: 1.4;
            }

            .timeline-links {
                margin-top: 12px;
                display: flex;
                gap: 8px;
                flex-wrap: wrap;
            }

            .timeline-link {
                color: #9fc3ff;
                text-decoration: none;
                border: 1px solid rgba(159, 195, 255, 0.45);
                border-radius: 8px;
                padding: 4px 8px;
                font-size: 12px;
            }

            .timeline-link:hover {
                color: #d6e7ff;
                border-color: rgba(214, 231, 255, 0.75);
            }

            @media (max-width: 900px) {
                .scroll-timeline::before {
                    left: 24px;
                    transform: none;
                }

                .timeline-item,
                .timeline-item.left,
                .timeline-item.right {
                    width: calc(100% - 54px);
                    margin-left: 54px;
                }

                .timeline-item::before,
                .timeline-item.left::before,
                .timeline-item.right::before {
                    left: -37px;
                    right: auto;
                }

                .timeline-meta-row {
                    grid-template-columns: 1fr;
                    gap: 1px;
                }
            }
            """
        ),
        ui.div(
            ui.tags.p("Historic Impact Timeline", class_="timeline-kicker"),
            ui.tags.h2("Meteorite Events Through Time", class_="timeline-heading"),
            ui.tags.p(
                "Scroll to reveal major meteorite moments and records.",
                class_="timeline-subtitle",
            ),
            class_="timeline-header",
        ),
        ui.div(
            *[_timeline_item(event, idx) for idx, event in enumerate(TIMELINE_EVENTS)],
            class_="scroll-timeline",
        ),
        ui.tags.script(
            """
            (function() {
                function initScrollTimeline() {
                    var root = document.querySelector('.scroll-timeline');
                    if (!root || root.dataset.enhanced === '1') return;
                    root.dataset.enhanced = '1';

                    var items = Array.prototype.slice.call(root.querySelectorAll('.timeline-item'));
                    if (!items.length) return;

                    items.forEach(function(item) {
                        var img = item.querySelector('.timeline-image');
                        var fallback = item.querySelector('.timeline-image-fallback');
                        if (img && fallback) {
                            img.addEventListener('error', function() {
                                img.style.display = 'none';
                                fallback.style.display = 'block';
                            }, { once: true });
                        }

                        item.classList.add('is-future');
                    });

                    var ticking = false;

                    function updateCurrentItem() {
                        var viewportMid = (window.innerHeight || document.documentElement.clientHeight) * 0.5;
                        var current = null;
                        var bestDistance = Infinity;

                        items.forEach(function(item) {
                            var rect = item.getBoundingClientRect();
                            var isVisible = rect.bottom > 0 && rect.top < (window.innerHeight || document.documentElement.clientHeight);
                            if (!isVisible) return;

                            var center = rect.top + (rect.height / 2);
                            var distance = Math.abs(center - viewportMid);
                            if (distance < bestDistance) {
                                bestDistance = distance;
                                current = item;
                            }
                        });

                        if (!current) {
                            items.forEach(function(item) {
                                var rect = item.getBoundingClientRect();
                                var center = rect.top + (rect.height / 2);
                                var distance = Math.abs(center - viewportMid);
                                if (distance < bestDistance) {
                                    bestDistance = distance;
                                    current = item;
                                }
                            });
                        }

                        items.forEach(function(item) {
                            item.classList.remove('is-current', 'is-past', 'is-future');
                            if (item === current) {
                                item.classList.add('is-current');
                                return;
                            }

                            var rect = item.getBoundingClientRect();
                            var center = rect.top + (rect.height / 2);
                            if (center < viewportMid) {
                                item.classList.add('is-past');
                            } else {
                                item.classList.add('is-future');
                            }
                        });
                    }

                    function onScrollOrResize() {
                        if (ticking) return;
                        ticking = true;
                        window.requestAnimationFrame(function() {
                            updateCurrentItem();
                            ticking = false;
                        });
                    }

                    updateCurrentItem();
                    window.addEventListener('scroll', onScrollOrResize, { passive: true });
                    window.addEventListener('resize', onScrollOrResize);
                }

                if (document.readyState === 'loading') {
                    document.addEventListener('DOMContentLoaded', initScrollTimeline, { once: true });
                } else {
                    initScrollTimeline();
                }
            })();
            """
        ),
        class_="scroll-timeline-section",
    )
