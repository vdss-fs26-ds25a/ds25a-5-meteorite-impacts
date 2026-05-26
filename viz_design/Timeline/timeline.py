from shiny import ui


TIMELINE_EVENTS = [
    {
        "id": "16988",
        "year": "860",
        "title": "First Recorded Meteorite",
        "description": "In the year 860, a stone fell from the sky near Nogata in present-day Fukuoka, Japan. Local records preserved the event, making it the oldest documented meteorite fall still recognized today. The meteorite itself survived and became an extraordinary bridge between ancient observation and modern planetary science.",
        "name": "Nogata",
        "mass": "472 g",
        "composition": "Ordinary chondrite (L6)",
        "location": "Nogata, Fukuoka, Japan",
        "status": "Fell",
        "wiki_url": "https://en.wikipedia.org/wiki/N%C5%8Dgata_meteorite",
        "image_url": "",
        "image_source": "",
        "lat": 33.725,
        "lon": 130.75,
        "notes": []
    },
    {
        "id": "5247",
        "year": "1575",
        "title": "Third Biggest Meteorite",
        "description": "Scattered across Argentina’s Gran Chaco region lies Campo del Cielo, a field of iron meteorites left behind by a massive impact thousands of years ago. Known to Indigenous communities long before scientific study, its enormous fragments revealed one of Earth’s largest and most famous meteorite discoveries.",
        "name": "Campo del Cielo",
        "mass": "50 t",
        "composition": "Iron meteorite (IAB-MG)",
        "location": "Gran Chaco region, Argentina",
        "status": "Found",
        "wiki_url": "https://en.wikipedia.org/wiki/Campo_del_Cielo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/1c/Campo_del_Cielo_meteorite%2C_El_Chaco_fragment%2C_N.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:Campo_del_Cielo_meteorite,_El_Chaco_fragment,_N.jpg",
        "lat": -27.46667,
        "lon": -60.58333,
        "notes": []
    },
    {
        "id": "5262",
        "year": "1818",
        "title": "Second Biggest Meteorite",
        "description": "Near Savissivik in Greenland, explorers encountered giant iron masses unlike ordinary rocks. These pieces belonged to the Cape York meteorite, used for generations by Inuit communities as a source of metal. Its largest fragment, Ahnighito, became one of the most iconic meteorites ever displayed.",
        "name": "Cape York",
        "mass": "58.2 t",
        "composition": "Iron meteorite (IIIAB)",
        "location": "Savissivik, Greenland",
        "status": "Found",
        "wiki_url": "https://en.wikipedia.org/wiki/Cape_York_meteorite",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Ahnighito_AMNH%2C_34_tons_meteorite.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:Ahnighito_AMNH,_34_tons_meteorite.jpg",
        "lat": 76.13333,
        "lon": -64.93333,
        "notes": ["Ahnighito AMNH, Larges fragment fount 34t"]
    },
    {
        "id": "11890",
        "year": "1920",
        "title": "Biggest Known Meteorite",
        "description": "Discovered on a farm near Grootfontein, Namibia, Hoba remains the largest single meteorite ever found on Earth. Unlike many impactors, it never formed a visible crater and still rests where it landed. Its immense iron mass has made it both a scientific treasure and landmark.",
        "name": "Hoba",
        "mass": "60 t",
        "composition": "Iron meteorite (IVB)",
        "location": "Grootfontein, Namibia",
        "status": "Found",
        "wiki_url": "https://en.wikipedia.org/wiki/Hoba_meteorite",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/39/Hoba_meteorite_%2815062762703%29.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:Hoba_meteorite_(15062762703).jpg",
        "lat": -19.58333,
        "lon": 17.91667,
        "notes": ["Weight equivalent: 60 t / 12 t = 5 London double-decker buses."]
    },
    {
        "id": "23773",
        "year": "1954",
        "title": "Meteorite Hit House and Person",
        "description": "On a quiet afternoon in Alabama, a meteorite crashed through the roof of a house, bounced off furniture, and struck Ann Hodges while she rested. She survived with bruises, creating one of the only confirmed cases of a person being injured by a meteorite.",
        "name": "Sylacauga meteorite",
        "mass": "5.56 kg",
        "composition": "Ordinary chondrite (H4)",
        "location": "Sylacauga, Alabama, USA",
        "status": "Fell",
        "wiki_url": "https://en.wikipedia.org/wiki/Sylacauga_(meteorite)",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/9/9d/2024-10-21_-_Tuscaloosa%2C_AL%2C_USA_-_Hodges_%28Sylacauga%29_Meteorite.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:2024-10-21_-_Tuscaloosa,_AL,_USA_-_Hodges_(Sylacauga)_Meteorite.jpg",
        "lat": 33.18836,
        "lon": -86.2945,
        "notes": []
    },
    {
        "id": "",
        "year": "1979",
        "title": "Peak of Recorded Distribution",
        "description": "The year 1979 stands out in this dataset not for a single famous impact, but because it recorded the highest number of meteorite observations. Improved monitoring, reporting, and collection efforts created a sharp peak, capturing thousands of sightings and expanding the historical record.",
        "name": "Most meteorites recorded in one year",
        "mass": "",
        "composition": "",
        "location": "Global",
        "status": "3323 sightings",
        "wiki_url": "",
        "image_url": "",
        "image_source": "",
        "lat": None,
        "lon": None,
        "notes": []
    },
    {
        "id": "604",
        "year": "1984",
        "title": "Mars Meteorite",
        "description": "Recovered from the Antarctic ice fields, Allan Hills 84001 was eventually identified as a rock blasted from Mars millions of years ago. Decades later, scientists proposed it might contain traces linked to ancient microbial life, sparking worldwide debate and renewed interest in planetary exploration.",
        "name": "Allan Hills 84001",
        "mass": "1.9309 kg",
        "composition": "Orthopyroxenite (Martian meteorite)",
        "location": "Allan Hills, Antarctica",
        "status": "Found",
        "wiki_url": "https://en.wikipedia.org/wiki/Allan_Hills_84001",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c4/ALH84001.jpg",
        "image_source": "https://commons.wikimedia.org/wiki/File:ALH84001.jpg",
        "lat": -76.92031,
        "lon": 156.77355,
        "notes": []
    },
    {
        "id": "57165",
        "year": "2013",
        "title": "Chelyabinsk Exploding Meteor",
        "description": "A brilliant fireball streaked across the skies over Chelyabinsk, Russia, before exploding high in the atmosphere. The shockwave shattered windows across the region and injured thousands, mostly indirectly. Captured by countless cameras, it became the most documented meteor event in modern history.",
        "name": "Chelyabinsk meteor",
        "mass": "100 kg (large recovered fragment)",
        "composition": "LL5 ordinary chondrite",
        "location": "Chelyabinsk Oblast, Russia",
        "status": "Fell",
        "wiki_url": "https://en.wikipedia.org/wiki/Chelyabinsk_meteor",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Meteorite_explosion_over_Chelyabinsk_on_February_15%2C_2013.gif",
        "image_source": "https://commons.wikimedia.org/wiki/File:Meteorite_explosion_over_Chelyabinsk_on_February_15,_2013.gif",
        "lat": 54.81667,
        "lon": 61.11667,
        "notes": []
    }
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


def _timeline_item(event, top_pct):
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

    link_buttons = []
    image_source = event.get("image_source", "")
    wiki_url = event.get("wiki_url", "")
    if image_source:
        link_buttons.append(
            ui.tags.a(
                "Image source",
                href=image_source,
                target="_blank",
                rel="noopener noreferrer",
                class_="timeline-link",
            )
        )
    if wiki_url:
        link_buttons.append(
            ui.tags.a(
                "Wiki",
                href=wiki_url,
                target="_blank",
                rel="noopener noreferrer",
                class_="timeline-link",
            )
        )

    lat = event.get("lat")
    lon = event.get("lon")
    map_card = None
    if lat is not None and lon is not None:
        map_card = ui.tags.div(
            ui.tags.div(
                class_="timeline-map-plot",
                **{"aria-label": f"Satellite map around {event['location']}"},
            ),
            ui.tags.p(f"Lat {lat:.5f}, Lon {lon:.5f}",
                      class_="timeline-map-coords"),
            class_="timeline-map",
            **{"data-lat": f"{lat:.6f}", "data-lon": f"{lon:.6f}"},
        )

    media_block = None
    if event["image_url"]:
        media_block = ui.tags.div(
            ui.tags.img(
                src=event["image_url"],
                alt=f"{event['name']} meteorite",
                class_="timeline-image",
                loading="lazy",
            ),
            ui.tags.p(
                "Image unavailable. Open Wiki link.",
                class_="timeline-image-fallback"
            ),
            class_="timeline-media",
        )

    content_block = ui.tags.div(
        ui.tags.div(
            ui.tags.span(event["year"], class_="timeline-year"),
            ui.tags.span(event["status"], class_="timeline-status"),
            class_="timeline-topline",
        ),
        ui.tags.h3(event["name"], class_="timeline-title"),
        ui.tags.p(event["title"], class_="timeline-event-type"),
        ui.tags.p(event.get("description", ""),
                  class_="timeline-description") if event.get("description") else None,
        details,
        ui.tags.ul(*entries, class_="timeline-entry-list") if entries else None,
        *notes,
        ui.tags.div(*link_buttons,
                    class_="timeline-links") if link_buttons else None,
        class_="timeline-card-content",
    )

    top_section_children = [content_block]
    if media_block is not None:
        top_section_children.append(media_block)

    return ui.tags.article(
        ui.tags.div(
            *top_section_children,
            class_=f"timeline-card-top {'has-media' if media_block is not None else 'no-media'}",
        ),
        map_card,
        class_="timeline-item",
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
        positioned_items.append(_timeline_item(event, top_pct))

    return ui.tags.section(
        ui.tags.style(
            """
            .scroll-timeline-section {
                position: relative;
                z-index: 10;
                --timeline-max-width: 1120px;
                background: #1f1f1f;
                padding: 64px 24px 600px;
            }

            .timeline-header {
                max-width: var(--timeline-max-width);
                margin: 0 auto 34px auto;
            }

            .timeline-kicker {
                margin: 0 0 8px 0;
                color: #7f7f7f;
                font-size: 16px;
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
                font-size: 18px;
                max-width: 64ch;
            }

            .scroll-timeline {
                position: relative;
                max-width: var(--timeline-max-width);
                margin: 0 auto;
                height: var(--timeline-track-height, 3200px);
                --timeline-axis-x: 0%;
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
                font-size: 14px;
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
                font-size: 16px;
                letter-spacing: 0.08em;
                text-shadow: 0 0 8px rgba(122, 166, 240, 0.45);
            }

            .timeline-current-tick.is-visible {
                opacity: 1;
            }

            .timeline-item {
                width: min(860px, calc(100% - var(--timeline-axis-x) - 74px));
                margin: 0;
                padding: 16px 18px 18px;
                border: 1px solid rgba(255, 255, 255, 0.14);
                border-radius: 14px;
                background: rgba(25, 25, 25, 0.88);
                box-shadow: 0 16px 28px rgba(0, 0, 0, 0.32);
                position: absolute;
                left: calc(var(--timeline-axis-x) + 100px);
                opacity: 0;
                transform: translateY(26px);
                pointer-events: none;
                transition: opacity 380ms ease, transform 380ms ease;
                z-index: 2;
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

            .timeline-card-top {
                display: grid;
                gap: 12px;
                align-items: start;
                margin-bottom: 10px;
            }

            .timeline-card-top.has-media {
                grid-template-columns: minmax(0, 1fr) clamp(150px, 34%, 220px);
            }

            .timeline-card-top.no-media {
                grid-template-columns: minmax(0, 1fr);
            }

            .timeline-card-content {
                min-width: 0;
            }

            .timeline-media {
                align-self: stretch;
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

            .timeline-description {
                margin: -2px 0 10px 0;
                color: #d6d6d6;
                font-size: 13px;
                line-height: 1.45;
            }

            .timeline-image {
                width: 100%;
                height: 100%;
                min-height: 160px;
                max-height: 260px;
                object-fit: cover;
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.12);
                display: block;
            }

            .timeline-image-fallback {
                display: none;
                margin: 0;
                min-height: 160px;
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.12);
                background: rgba(255, 255, 255, 0.03);
                align-items: center;
                justify-content: center;
                text-align: center;
                padding: 10px;
                color: #8f8f8f;
                font-size: 12px;
            }

            .timeline-map {
                position: relative;
                margin: 0;
            }

            .timeline-map-plot {
                width: 100%;
                height: 300px;
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.12);
                overflow: hidden;
                background: #0f0f0f;
            }

            .timeline-map-coords {
                margin: 6px 0 0 0;
                color: #9f9f9f;
                font-size: 11px;
                font-family: monospace;
                letter-spacing: 0.03em;
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

                .timeline-item {
                    width: calc(100% - 54px);
                    left: 54px;
                }

                .timeline-item::before {
                    left: -37px;
                }

                .timeline-meta-row {
                    grid-template-columns: 1fr;
                    gap: 1px;
                }

                .timeline-card-top.has-media {
                    grid-template-columns: minmax(0, 1fr);
                }

                .timeline-image,
                .timeline-image-fallback {
                    min-height: 180px;
                    max-height: 230px;
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
                function ensurePlotlyLoaded(onReady) {
                    if (window.Plotly && typeof window.Plotly.newPlot === 'function') {
                        onReady();
                        return;
                    }

                    var existing = document.getElementById('timeline-plotly-loader');
                    if (existing) {
                        existing.addEventListener('load', onReady, { once: true });
                        return;
                    }

                    var script = document.createElement('script');
                    script.id = 'timeline-plotly-loader';
                    script.src = 'https://cdn.plot.ly/plotly-2.35.2.min.js';
                    script.async = true;
                    script.addEventListener('load', onReady, { once: true });
                    document.head.appendChild(script);
                }

                function initSatelliteMaps(root) {
                    var maps = Array.prototype.slice.call(root.querySelectorAll('.timeline-map'));
                    if (!maps.length) return;

                    ensurePlotlyLoaded(function() {
                        function englishSatelliteLayers() {
                            return [
                                {
                                    sourcetype: 'raster',
                                    source: ['https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'],
                                    below: 'traces',
                                },
                                {
                                    sourcetype: 'raster',
                                    source: ['https://services.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}'],
                                    below: 'traces',
                                }
                            ];
                        }

                        maps.forEach(function(mapNode) {
                            if (mapNode.dataset.interactive === '1') return;

                            var lat = parseFloat(mapNode.dataset.lat);
                            var lon = parseFloat(mapNode.dataset.lon);
                            var target = mapNode.querySelector('.timeline-map-plot');
                            if (!target || Number.isNaN(lat) || Number.isNaN(lon)) return;

                            var trace = {
                                type: 'scattermap',
                                mode: 'markers',
                                lat: [lat],
                                lon: [lon],
                                marker: {
                                    size: 14,
                                    color: '#ff4d4d',
                                    line: { color: '#ffffff', width: 2 },
                                },
                                hovertemplate: 'Lat %{lat:.5f}<br>Lon %{lon:.5f}<extra></extra>',
                            };

                            var layout = {
                                margin: { l: 0, r: 0, t: 0, b: 0 },
                                paper_bgcolor: 'rgba(0,0,0,0)',
                                dragmode: 'zoom',
                                map: {
                                    style: 'white-bg',
                                    center: { lat: lat, lon: lon },
                                    zoom: 3.5,
                                    layers: englishSatelliteLayers(),
                                },
                                showlegend: false,
                            };

                            var config = {
                                responsive: true,
                                scrollZoom: true,
                                displaylogo: false,
                                modeBarButtonsToRemove: ['select2d', 'lasso2d', 'toImage'],
                            };

                            function markError() {
                                target.innerHTML = '';
                                target.textContent = 'Map failed to load';
                                target.style.display = 'grid';
                                target.style.placeItems = 'center';
                                target.style.color = '#9f9f9f';
                                target.style.fontSize = '12px';
                            }

                            window.Plotly.newPlot(target, [trace], layout, config)
                                .then(function() {
                                    mapNode.dataset.interactive = '1';
                                })
                                .catch(function() {
                                    // Fallback for environments that only support mapbox traces.
                                    trace.type = 'scattermapbox';
                                    layout.mapbox = {
                                        style: 'white-bg',
                                        center: { lat: lat, lon: lon },
                                        zoom: 3.5,
                                        layers: englishSatelliteLayers(),
                                    };
                                    delete layout.map;
                                    window.Plotly.newPlot(target, [trace], layout, config)
                                        .then(function() {
                                            mapNode.dataset.interactive = '1';
                                        })
                                        .catch(markError);
                                });
                        });
                    });
                }

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
                                fallback.style.display = 'flex';
                            }, { once: true });
                        }

                        item.classList.add('is-future');
                    });

                    initSatelliteMaps(root);

                    var ticking = false;
                    var TRIGGER_RATIO = 1 / 3;

                    function getItemTopPct(item) {
                        var raw = parseFloat(item.style.top || '0');
                        return Number.isNaN(raw) ? 0 : raw;
                    }

                    function getItemAnchorY(item, rootRect) {
                        return rootRect.top + (getItemTopPct(item) / 100) * rootRect.height;
                    }

                    function updateCurrentItem() {
                        var triggerY = (window.innerHeight || document.documentElement.clientHeight) * TRIGGER_RATIO;
                        var rootRect = root.getBoundingClientRect();
                        var current = null;
                        var bestPastAnchor = -Infinity;

                        items.forEach(function(item) {
                            var anchorY = getItemAnchorY(item, rootRect);
                            if (anchorY <= triggerY && anchorY > bestPastAnchor) {
                                bestPastAnchor = anchorY;
                                current = item;
                            }
                        });

                        var currentTop = current ? getItemTopPct(current) : null;

                        items.forEach(function(item) {
                            item.classList.remove('is-current', 'is-past', 'is-future');
                            if (item === current) {
                                item.classList.add('is-current');
                                return;
                            }

                            if (currentTop !== null && getItemTopPct(item) < currentTop) {
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
