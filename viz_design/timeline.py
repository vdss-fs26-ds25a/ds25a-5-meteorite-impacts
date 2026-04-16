from shiny import ui


TIMELINE_EVENTS = [
    {
        "year": "860",
        "title": "First Recorded Meteorite",
        "name": "Nogata",
        "mass": "472 g",
        "composition": "Ordinary chondrite (historical record)",
        "location": "Nogata, Fukuoka, Japan",
        "status": "Fell",
        "wiki_url": "https://en.wikipedia.org/wiki/N%C5%8Dgata_meteorite",
        "image_url": "",
        "image_source": "",
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Campo_del_Cielo_meteorite%2C_El_Chaco_fragment%2C_N.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:Campo_del_Cielo_meteorite,_El_Chaco_fragment,_N.jpg",
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Ahnighito_AMNH%2C_34_tons_meteorite.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:Ahnighito_AMNH,_34_tons_meteorite.jpg",
        "notes": ["Ahnighito AMNH, Larges fragment fount 34t"],
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/39/Hoba_meteorite_%2815062762703%29.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:Hoba_meteorite_(15062762703).jpg",
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9d/2024-10-21_-_Tuscaloosa%2C_AL%2C_USA_-_Hodges_%28Sylacauga%29_Meteorite.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:2024-10-21_-_Tuscaloosa,_AL,_USA_-_Hodges_(Sylacauga)_Meteorite.jpg",
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c4/ALH84001.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:ALH84001.jpg",
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
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Meteorite_explosion_over_Chelyabinsk_on_February_15%2C_2013.gif",
        "image_source": "https://commons.wikimedia.org/wiki/File:Meteorite_explosion_over_Chelyabinsk_on_February_15,_2013.gif",
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
        "image_url": "",
        "image_source": "",
        "notes": [],
    },
]


def _meta_row(label, value):
    return ui.tags.li(
        ui.tags.span(label, class_="timeline-meta-label"),
        ui.tags.span(value, class_="timeline-meta-value"),
        class_="timeline-meta-row",
    )


def _build_timeline_scale(events):
    years = [int(event.get("year", "")) for event in events]
    years = [year for year in years if year is not None]
    if not years:
        return {
            "start": 0,
            "end": 0,
            "span": 10,
            "track_height_px": 3200,
            "top_pad_px": 260,
            "bottom_pad_px": 220,
        }

    start = (min(years) // 10) * 10
    end = ((max(years) + 9) // 10) * 10
    span = max(end - start, 10)
    top_pad_px = 260
    bottom_pad_px = 220
    breakpoints = sorted(
        {
            start,
            end,
            800,
            1500,
            1800,
            2026,
        }
    )

    segments = []
    weighted_span = 0.0
    for i in range(len(breakpoints) - 1):
        seg_start = breakpoints[i]
        seg_end = breakpoints[i + 1]
        if seg_end <= start or seg_start >= end:
            continue

        seg_start = max(seg_start, start)
        seg_end = min(seg_end, end)
        if seg_end <= seg_start:
            continue

        mid = (seg_start + seg_end) / 2
        if 800 <= mid < 1500:
            weight = 0.35
        elif 1500 <= mid < 1800:
            weight = 0.8
        elif 1800 <= mid < 2026:
            weight = 2.4
        else:
            weight = 1.0

        segments.append((seg_start, seg_end, weight))
        weighted_span += (seg_end - seg_start) * weight

    weighted_span = max(weighted_span, 1.0)
    track_height_px = max(
        3200, int(weighted_span * 2.4 + top_pad_px + bottom_pad_px))
    return {
        "start": start,
        "end": end,
        "span": span,
        "segments": segments,
        "weighted_span": weighted_span,
        "track_height_px": track_height_px,
        "top_pad_px": top_pad_px,
        "bottom_pad_px": bottom_pad_px,
    }


def _year_to_top_pct(year, scale):
    clamped_year = max(scale["start"], min(scale["end"], year))
    weighted_pos = 0.0
    for seg_start, seg_end, weight in scale["segments"]:
        if clamped_year >= seg_end:
            weighted_pos += (seg_end - seg_start) * weight
            continue
        if clamped_year > seg_start:
            weighted_pos += (clamped_year - seg_start) * weight
        break

    ratio = weighted_pos / max(scale["weighted_span"], 1.0)
    ratio = max(0.0, min(1.0, ratio))
    usable_px = max(scale["track_height_px"] -
                    scale["top_pad_px"] - scale["bottom_pad_px"], 1)
    y_px = scale["top_pad_px"] + ratio * usable_px
    return (y_px / scale["track_height_px"]) * 100.0


def _build_timeline_ticks(scale):
    start = scale["start"]
    end = scale["end"]

    ticks = []
    for year in range(start, end + 1, 10):
        if year % 100 == 0:
            tick_size = "big"
        elif year % 50 == 0:
            tick_size = "medium"
        else:
            tick_size = "small"

        top_pct = _year_to_top_pct(year, scale)
        label = (
            ui.tags.span(str(year), class_="timeline-tick-label")
            if tick_size == "big"
            else None
        )
        ticks.append(
            ui.tags.div(
                ui.tags.span(class_="timeline-tick-mark"),
                label,
                class_=f"timeline-tick {tick_size}",
                style=f"top: {top_pct:.4f}%;",
                **{"data-year": str(year)},
            )
        )

    return ui.tags.div(
        *ticks,
        ui.tags.div(
            ui.tags.span(class_="timeline-current-tick-mark"),
            ui.tags.span(class_="timeline-current-tick-label"),
            class_="timeline-current-tick",
        ),
        class_="timeline-ticks",
    )


def _timeline_item(event, index, top_pct):
    side = "left" if index % 2 == 0 else "right"
    year_value = int(event.get("year", ""))
    attrs = {}
    if year_value is not None:
        attrs["data-year"] = str(year_value)
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
        ) if event["image_url"] else ui.tags.p(
            "Image unavailable. Open Wiki link.",
            class_="timeline-image-fallback"
        ),
        details,
        ui.tags.ul(*entries, class_="timeline-entry-list") if entries else None,
        *notes,
        ui.tags.div(
            ui.tags.a("Image source", href=event["image_source"], target="_blank",
                      rel="noopener noreferrer", class_="timeline-link"),
            ui.tags.a("Wiki", href=event["wiki_url"], target="_blank",
                      rel="noopener noreferrer", class_="timeline-link"),
            class_="timeline-links",
        ),
        class_=f"timeline-item {side}",
        style=f"top: {top_pct:.4f}%;",
        **attrs,
    )


def build_scroll_timeline_section():
    scale = _build_timeline_scale(TIMELINE_EVENTS)
    positioned_items = []
    total_items = len(TIMELINE_EVENTS)
    for idx, event in enumerate(TIMELINE_EVENTS):
        year_value = int(event.get("year", ""))
        if year_value is not None:
            top_pct = _year_to_top_pct(year_value, scale)
        else:
            top_pct = ((idx + 1) / (total_items + 1)) * 100
        positioned_items.append(_timeline_item(event, idx, top_pct))

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
                padding: 64px 24px 300px;
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
                height: var(--timeline-track-height, 3200px);
                --timeline-axis-x: 50%;
            }

            .scroll-timeline::before {
                content: "";
                position: absolute;
                top: 0;
                bottom: 0;
                left: var(--timeline-axis-x);
                width: 2px;
                background: linear-gradient(to bottom, #2c2c2c, #4f4f4f, #2c2c2c);
                transform: translateX(-50%);
                z-index: 0;
            }

            .timeline-ticks {
                position: absolute;
                top: 0;
                bottom: 0;
                left: var(--timeline-axis-x);
                width: 0;
                pointer-events: none;
                z-index: 1;
            }

            .timeline-tick {
                position: absolute;
                left: 0;
                transform: translate(-50%, -50%);
            }

            .timeline-tick-mark {
                display: block;
                background: #5f5f5f;
                opacity: 0.35;
                transition: opacity 240ms ease, background-color 240ms ease, transform 240ms ease;
            }

            .timeline-tick.small .timeline-tick-mark {
                width: 10px;
                height: 1px;
            }

            .timeline-tick.medium .timeline-tick-mark {
                width: 16px;
                height: 1px;
            }

            .timeline-tick.big .timeline-tick-mark {
                width: 26px;
                height: 2px;
                background: #8ab4ff;
            }

            .timeline-tick-label {
                position: absolute;
                left: 30px;
                top: 50%;
                transform: translateY(-50%);
                color: #8ea5c7;
                font-size: 10px;
                font-family: monospace;
                letter-spacing: 0.08em;
                opacity: 0.38;
                transition: opacity 240ms ease, color 240ms ease;
            }

            .timeline-current-tick {
                position: absolute;
                left: 0;
                transform: translate(-50%, -50%);
                opacity: 0;
                pointer-events: none;
                transition: opacity 200ms ease;
            }

            .timeline-current-tick-mark {
                display: block;
                width: 34px;
                height: 2px;
                background: #dce9ff;
                box-shadow: 0 0 10px rgba(122, 166, 240, 0.45);
            }

            .timeline-current-tick-label {
                position: absolute;
                left: 42px;
                top: 50%;
                transform: translateY(-50%);
                color: #dce9ff;
                font-family: monospace;
                font-size: 11px;
                letter-spacing: 0.08em;
                text-shadow: 0 0 8px rgba(122, 166, 240, 0.45);
            }

            .timeline-current-tick.is-visible {
                opacity: 1;
            }

            .timeline-item {
                width: calc(50% - 34px);
                margin: 0;
                padding: 16px 18px 18px;
                border: 1px solid rgba(255, 255, 255, 0.14);
                border-radius: 14px;
                background: rgba(25, 25, 25, 0.88);
                box-shadow: 0 16px 28px rgba(0, 0, 0, 0.32);
                position: absolute;
                opacity: 0;
                transform: translateY(26px);
                pointer-events: none;
                transition: opacity 380ms ease, transform 380ms ease;
                z-index: 2;
            }

            .timeline-item.left {
                left: 0;
            }

            .timeline-item.right {
                right: 0;
            }

            .timeline-item::before {
                content: "";
                position: absolute;
                top: 0;
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: #0d6efd;
                border: 2px solid #9fc3ff;
                transform: translateY(-50%);
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
                color: #6f8fbd;
                font-family: monospace;
                font-size: 13px;
                font-weight: 700;
                letter-spacing: 0.06em;
                transition: color 240ms ease, text-shadow 240ms ease;
            }

            .timeline-item.is-current .timeline-year {
                color: #cfe1ff;
                text-shadow: 0 0 10px rgba(122, 166, 240, 0.45);
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
                    left: var(--timeline-axis-x);
                    transform: none;
                }

                .scroll-timeline {
                    --timeline-axis-x: 24px;
                }

                .timeline-item,
                .timeline-item.left,
                .timeline-item.right {
                    width: calc(100% - 54px);
                    left: 54px;
                    right: auto;
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

                .timeline-tick-label {
                    left: -54px;
                    text-align: right;
                }

                .timeline-current-tick-label {
                    left: -92px;
                    text-align: right;
                }
            }
            """
        ),
        ui.div(
            ui.tags.p("Historic Impact Timeline", class_="timeline-kicker"),
            ui.tags.h2("Meteorite Events Through Time",
                       class_="timeline-heading"),
            ui.tags.p(
                "Scroll to reveal major meteorite moments and records.",
                class_="timeline-subtitle",
            ),
            class_="timeline-header",
        ),
        ui.div(
            _build_timeline_ticks(scale),
            *positioned_items,
            class_="scroll-timeline",
            style=f"--timeline-track-height: {scale['track_height_px']}px;",
        ),
        ui.tags.script(
            """
            (function() {
                function initScrollTimeline() {
                    var root = document.querySelector('.scroll-timeline');
                    if (!root || root.dataset.enhanced === '1') return;
                    root.dataset.enhanced = '1';

                    var items = Array.prototype.slice.call(root.querySelectorAll('.timeline-item'));
                    var currentTick = root.querySelector('.timeline-current-tick');
                    var currentTickLabel = root.querySelector('.timeline-current-tick-label');
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
                        var viewportMid = (window.innerHeight || document.documentElement.clientHeight) * 0.58;
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

                        if (currentTick && currentTickLabel) {
                            if (current) {
                                currentTickLabel.textContent = current.getAttribute('data-year') || '';
                                currentTick.style.top = current.style.top || '0%';
                                currentTick.classList.add('is-visible');
                            } else {
                                currentTick.classList.remove('is-visible');
                            }
                        }
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
