from shiny import ui


def build_meteor_introduction():
    comparison_cards = [
        {
            "title": "Meteoroid",
            "icon": "bi-hexagon-fill",
            "text": "A rocky or metallic body traveling through space, ranging from tiny dust grains to objects meters wide. Larger bodies are classified as asteroids or comets.",
        },
        {
            "title": "Meteor",
            "icon": "bi-stars",
            "text": "The luminous phenomenon when a meteoroid enters Earth's atmosphere at high speed, heating the surrounding air to incandescence. Commonly known as a 'shooting star'.",
        },
        {
            "title": "Meteorite",
            "icon": "bi-geo-alt-fill",
            "text": "The solid fragment that survives the fiery passage through the atmosphere and reaches Earth's surface. Less than 5% of meteoroids that enter the atmosphere make it to the ground.",
        },
    ]

    class_code_rows = [
        {
            "code": "H",
            "name": "Ordinary chondrite group H",
            "description": "High total iron content. Example: H5.",
        },
        {
            "code": "L",
            "name": "Ordinary chondrite group L",
            "description": "Lower iron than H group. Example: L6.",
        },
        {
            "code": "LL",
            "name": "Ordinary chondrite group LL",
            "description": "Low total iron and low metallic iron. Example: LL5.",
        },
        {
            "code": "CM",
            "name": "Carbonaceous chondrite group CM",
            "description": "Carbon-rich, primitive meteorites, often altered by water. Example: CM2.",
        },
        {
            "code": "E",
            "name": "Enstatite chondrite group",
            "description": "Very reduced meteorites dominated by enstatite. Example: E3.",
        },
        {
            "code": "Iron",
            "name": "Iron meteorite class",
            "description": "Metal-dominated meteorites (mostly iron-nickel). Example: Iron, IIIAB.",
        },
        {
            "code": "3",
            "name": "Petrologic type 3",
            "description": "Most primitive ordinary chondrites; least thermally altered.",
        },
        {
            "code": "4",
            "name": "Petrologic type 4",
            "description": "Moderate thermal metamorphism.",
        },
        {
            "code": "5",
            "name": "Petrologic type 5",
            "description": "Stronger thermal metamorphism than type 4.",
        },
        {
            "code": "6",
            "name": "Petrologic type 6",
            "description": "Strong thermal metamorphism; textures are more equilibrated.",
        },
        {
            "code": "2",
            "name": "Petrologic type 2 (common in carbonaceous classes)",
            "description": "Significant aqueous alteration on the parent body. Example: CM2.",
        },
        {
            "code": "4/5",
            "name": "Transitional subtype",
            "description": "Intermediate between two petrologic types. Example: H4/5.",
        },
        {
            "code": "IIIAB",
            "name": "Chemical subgroup for iron meteorites",
            "description": "Refines Iron meteorites by chemistry and structure. Example: Iron, IIIAB.",
        },
    ]

    intro_steps = [
        {
            "kind": "text",
            "title": "Meteoroid, Meteor, Meteorite, What's the Difference?",
            "text": "The same object can be called three different names depending on where it is in its journey. "
                    "These terms are often confused in everyday language, but scientists use them precisely "
                    "to describe each phase: drifting through space, blazing through our atmosphere, "
                    "and finally resting on the ground.",
        },
        {
            "kind": "text",
            "title": "From Space to Ground",
            "text": "The journey begins millions of kilometers away. A meteoroid is a fragment of rock or metal "
                    "broken off from an asteroid or comet it drifts silently through the solar system. "
                    "When it crosses paths with Earth, gravity pulls it into our atmosphere at speeds "
                    "between 11 and 72 km/s. The name it carries changes at each stage of that descent.",
        },
        {
            "kind": "cards",
            "title": "Meteoroid, Meteor, Meteorite",
            "text": "Three names, one object, here is how the terminology shifts as the space rock "
                    "travels from the void of space through our atmosphere to the surface of the Earth.",
        },
        {
            "kind": "text",
            "title": "Meteoroid",
            "text": "Meteoroids are the most numerous solid objects in the inner solar system. "
                    "They originate from collisions between asteroids, from cometary debris trails, "
                    "or even from material ejected off the Moon or Mars by past impacts. "
                    "Most are smaller than a grain of sand, though some reach several meters in diameter. "
                    "Earth sweeps up an estimated 100 tonnes of meteoroid material every single day.",
        },
        {
            "kind": "text",
            "title": "Meteor",
            "text": "As a meteoroid slams into Earth's atmosphere, friction compresses and superheats "
                    "the air in front of it to temperatures exceeding 1,600 °C. This causes the object "
                    "to ablate, its outer layers vaporize, producing the glowing streak we call a meteor. "
                    "Most meteors burn up completely within seconds at altitudes between 80 and 120 km. "
                    "Exceptionally bright meteors, brighter than Venus, are called fireballs or bolides "
                    "and can cast shadows on the ground.",
        },
        {
            "kind": "text",
            "title": "Meteorite",
            "text": "Meteorites are survivors. Only the most robust and sizable meteoroids withstand "
                    "the brutal passage through the atmosphere and reach the surface intact. "
                    "They are classified into three broad groups: stony meteorites (most common), "
                    "iron meteorites (dense, metallic), and stony-iron meteorites (rarest). "
                    "Upon landing, they are typically cool to the touch, the ablation process "
                    "strips away the heated outer shell, leaving the cold interior exposed.",
        },
        {
            "kind": "text",
            "title": "What Meteorites Tell Us",
            "text": "Meteorites are among the oldest materials on Earth, many formed over 4.5 billion years ago, "
                    "predating our planet itself. Their chemical composition, mineral structures, and isotopic "
                    "ratios act as a fossil record of the early solar system. By studying them, scientists "
                    "can reconstruct how planets formed, what the young Sun looked like, and whether "
                    "organic molecules, the building blocks of life, were delivered to early Earth from space.",
        },
        {
            "kind": "class_table",
            "title": "How To Read Meteorite Class Codes",
            "text": "The recclass value is built from a group code (letters) plus a subtype number or modifier. "
                    "Use this quick guide to decode labels like L6, LL5, CM2, H4/5, and Iron, IIIAB.",
        },
        {
            "kind": "text",
            "title": "Why This Matters Here",
            "text": "The timeline below traces key moments in humanity's relationship with meteorites "
                    "from ancient civilizations that worshipped fallen iron as gifts from the gods, "
                    "to the first scientific classifications in the 19th century, "
                    "to modern observed falls tracked by global camera networks. "
                    "Each event marks a milestone in how we understand our place in the solar system.",
        },
    ]

    blocks = []
    sentinels = []
    for i, step in enumerate(intro_steps):
        block_children = [
            ui.tags.h3(step["title"], class_="meteorite-intro-block-title"),
            ui.tags.p(step["text"], class_="meteorite-intro-block-text"),
        ]
        block_class = "meteorite-intro-block"

        if step["kind"] == "cards":
            block_class += " cards-step"
            term_cards = []
            for card in comparison_cards:
                term_cards.append(
                    ui.tags.article(
                        ui.tags.div(
                            ui.tags.i(class_=f"bi {card['icon']}"),
                            class_="meteorite-term-icon",
                            aria_hidden="true",
                        ),
                        ui.tags.h3(card["title"],
                                   class_="meteorite-term-title"),
                        ui.tags.p(card["text"], class_="meteorite-term-text"),
                        class_="meteorite-term-card",
                    )
                )
            block_children.append(ui.tags.div(
                *term_cards, class_="meteorite-term-grid"))
        elif step["kind"] == "class_table":
            table_rows = []
            for row in class_code_rows:
                table_rows.append(
                    ui.tags.tr(
                        ui.tags.td(row["code"], class_="meteorite-class-code"),
                        ui.tags.td(row["name"]),
                        ui.tags.td(row["description"]),
                    )
                )

            block_children.append(
                ui.tags.div(
                    ui.tags.table(
                        ui.tags.thead(
                            ui.tags.tr(
                                ui.tags.th("Code part"),
                                ui.tags.th("Official meaning"),
                                ui.tags.th("How to interpret it"),
                            )
                        ),
                        ui.tags.tbody(*table_rows),
                        class_="meteorite-class-table",
                    ),
                    class_="meteorite-class-table-wrap",
                )
            )

        blocks.append(
            ui.tags.article(
                *block_children,
                class_=block_class,
                **{"data-step": str(i)},
            )
        )
        sentinels.append(
            ui.tags.div(
                class_="meteorite-intro-sentinel",
                **{"data-step": str(i)},
            )
        )

    return ui.tags.section(
        ui.tags.style(
            """
            .meteorite-intro-section {
                position: relative;
                z-index: 11;
                background: #1f1f1f;
                padding: 64px 24px 140px;
            }

            .meteorite-intro-header {
                max-width: 860px;
                margin: 0 auto 34px auto;
            }

            .meteorite-intro-kicker {
                margin: 0 0 8px 0;
                color: #7f7f7f;
                font-size: 16px;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 1.6px;
            }

            .meteorite-intro-heading {
                margin: 0;
                color: #ffffff;
                font-size: clamp(1.5rem, 2.3vw, 2.1rem);
                font-weight: 800;
                letter-spacing: -0.02em;
            }

            .meteorite-intro-subtitle {
                margin: 10px 0 0 0;
                color: #a2a2a2;
                font-size: 18px;
                max-width: 64ch;
            }

            .meteorite-term-grid {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 14px;
                margin-top: 12px;
            }

            .meteorite-term-card {
                border: 1px solid rgba(255, 255, 255, 0.14);
                border-radius: 14px;
                background: rgba(25, 25, 25, 0.88);
                box-shadow: 0 16px 28px rgba(0, 0, 0, 0.24);
                padding: 16px;
                opacity: 0;
                transform: translateY(20px);
                transition: opacity 420ms ease, transform 420ms ease;
            }

            .meteorite-intro-block.cards-step.is-active .meteorite-term-card {
                opacity: 1;
                transform: translateY(0);
            }

            .meteorite-intro-block.cards-step.is-active .meteorite-term-card:nth-child(1) {
                transition-delay: 80ms;
            }

            .meteorite-intro-block.cards-step.is-active .meteorite-term-card:nth-child(2) {
                transition-delay: 220ms;
            }

            .meteorite-intro-block.cards-step.is-active .meteorite-term-card:nth-child(3) {
                transition-delay: 360ms;
            }

            .meteorite-term-icon {
                width: 40px;
                height: 40px;
                border-radius: 10px;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
                color: #cfe1ff;
                border: 1px solid rgba(159, 195, 255, 0.35);
                background: rgba(13, 110, 253, 0.16);
                margin-bottom: 10px;
            }

            .meteorite-term-title {
                margin: 0 0 6px 0;
                color: #f1f1f1;
                font-size: 1.02rem;
                letter-spacing: -0.01em;
            }

            .meteorite-term-text {
                margin: 0;
                color: #c0c0c0;
                line-height: 1.45;
                font-size: 14px;
            }

            .meteorite-class-table-wrap {
                margin-top: 12px;
                border: 1px solid rgba(255, 255, 255, 0.14);
                border-radius: 14px;
                background: rgba(25, 25, 25, 0.88);
                box-shadow: 0 16px 28px rgba(0, 0, 0, 0.24);
                overflow-x: auto;
            }

            .meteorite-class-table {
                width: 100%;
                min-width: 760px;
                border-collapse: collapse;
                font-size: 13px;
                line-height: 1.45;
                color: #c7c7c7;
            }

            .meteorite-class-table th {
                text-align: left;
                font-size: 11px;
                letter-spacing: 0.06em;
                text-transform: uppercase;
                color: #8fb5ef;
                padding: 12px 14px;
                background: rgba(13, 110, 253, 0.12);
                border-bottom: 1px solid rgba(255, 255, 255, 0.14);
            }

            .meteorite-class-table td {
                vertical-align: top;
                padding: 10px 14px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            }

            .meteorite-class-table tbody tr:last-child td {
                border-bottom: none;
            }

            .meteorite-class-code {
                color: #d6e6ff;
                font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
                font-weight: 700;
                white-space: nowrap;
            }

            .meteorite-intro-scrolly {
                position: relative;
                max-width: 860px;
                margin: 0 auto;
            }

            .meteorite-intro-stack {
                position: sticky;
                top: 50vh;
                transform: translateY(-50%);
                border: 1px solid rgba(255, 255, 255, 0.14);
                border-radius: 16px;
                background: rgba(25, 25, 25, 0.88);
                box-shadow: 0 16px 28px rgba(0, 0, 0, 0.32);
                overflow: hidden;
                transition: height 360ms ease;
            }

            .meteorite-intro-block {
                position: absolute;
                left: 0;
                right: 0;
                top: 0;
                padding: 26px 28px;
                opacity: 0;
                transform: translateY(20px);
                transition: opacity 360ms ease, transform 360ms ease;
                pointer-events: none;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }

            .meteorite-intro-block.is-active {
                opacity: 1;
                transform: translateY(0);
            }

            .meteorite-intro-block.is-before {
                opacity: 0;
                transform: translateY(-20px);
            }

            .meteorite-intro-block.is-after {
                opacity: 0;
                transform: translateY(20px);
            }

            .meteorite-intro-block-title {
                margin: 0 0 10px 0;
                color: #f3f3f3;
                font-size: clamp(1.15rem, 1.8vw, 1.45rem);
                letter-spacing: -0.01em;
            }

            .meteorite-intro-block-text {
                margin: 0;
                color: #c6c6c6;
                line-height: 1.65;
                max-width: 62ch;
            }

            .meteorite-intro-scrollspace {
                position: relative;
                margin-top: 10px;
            }

            .meteorite-intro-sentinel {
                height: 52vh;
            }

            .meteorite-intro-scroll-hint {
                position: fixed;
                left: 50%;
                top: 70vh;
                transform: translateX(-50%);
                z-index: 25;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                gap: 2px;
                margin: 0;
                color: #aeb9cc;
                font-size: 11px;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                pointer-events: none;
                opacity: 1;
                transition: opacity 180ms ease;
            }

            .meteorite-intro-scroll-hint.is-hidden {
                opacity: 0;
            }

            .meteorite-intro-scroll-hint-icon {
                font-size: 14px;
                color: #8fb5ef;
            }

            @media (max-width: 900px) {
                .meteorite-intro-section {
                    padding: 56px 18px 110px;
                }

                .meteorite-intro-stack {
                    top: 50vh;
                }

                .meteorite-intro-block {
                    padding: 20px 18px;
                }

                .meteorite-intro-sentinel {
                    height: 56vh;
                }

                .meteorite-term-grid {
                    grid-template-columns: 1fr;
                }
            }
            """
        ),
        ui.tags.div(
            ui.tags.p("Meteorite Basics", class_="meteorite-intro-kicker"),
            ui.tags.h2(
                "A Short Introduction To Meteorites",
                class_="meteorite-intro-heading",
            ),
            ui.tags.p(
                "Scroll through the key concepts before exploring the historical timeline.",
                class_="meteorite-intro-subtitle",
            ),
            class_="meteorite-intro-header",
        ),
        ui.tags.div(
            ui.tags.div(*blocks, class_="meteorite-intro-stack"),
            ui.tags.div(
                ui.tags.span("Scroll"),
                ui.tags.i(
                    class_="bi bi-chevron-down meteorite-intro-scroll-hint-icon", aria_hidden="true"),
                class_="meteorite-intro-scroll-hint",
            ),
            ui.tags.div(*sentinels, class_="meteorite-intro-scrollspace"),
            class_="meteorite-intro-scrolly",
        ),
        ui.tags.script(
            """
            (function() {
                function initMeteoriteIntro() {
                    var root = document.querySelector('.meteorite-intro-scrolly');
                    if (!root || root.dataset.enhanced === '1') return;
                    root.dataset.enhanced = '1';

                    var blocks = Array.prototype.slice.call(
                        root.querySelectorAll('.meteorite-intro-block')
                    );
                    var sentinels = Array.prototype.slice.call(
                        root.querySelectorAll('.meteorite-intro-sentinel')
                    );
                    var stack = root.querySelector('.meteorite-intro-stack');
                    var indicator = root.querySelector('.meteorite-intro-scroll-hint');
                    if (!blocks.length || blocks.length !== sentinels.length || !stack) return;

                    var currentStep = -1;
                    var ticking = false;

                    function syncStackHeight(stepIndex) {
                        var index = Math.max(0, Math.min(stepIndex, blocks.length - 1));
                        var activeBlock = blocks[index];
                        if (!activeBlock) return;
                        stack.style.height = activeBlock.offsetHeight + 'px';
                    }

                    function setStep(nextStep) {
                        if (nextStep === currentStep) return;
                        currentStep = nextStep;

                        blocks.forEach(function(block, index) {
                            block.classList.remove('is-active', 'is-before', 'is-after');
                            if (index === currentStep) {
                                block.classList.add('is-active');
                            } else if (index < currentStep) {
                                block.classList.add('is-before');
                            } else {
                                block.classList.add('is-after');
                            }
                        });

                        syncStackHeight(currentStep);
                    }

                    function updateIndicatorPosition() {
                        if (!indicator) return;
                        var viewportHeight = window.innerHeight || document.documentElement.clientHeight;
                        var stackRect = stack.getBoundingClientRect();
                        var stackVisible = stackRect.bottom > 0 && stackRect.top < viewportHeight;

                        indicator.style.left = (stackRect.left + (stackRect.width / 2)) + 'px';
                        indicator.style.top = (stackRect.bottom + 26) + 'px';
                        indicator.classList.toggle('is-hidden', !stackVisible);
                    }

                    function updateStep() {
                        var viewportMid = (window.innerHeight || document.documentElement.clientHeight) * 0.52;
                        var bestStep = 0;
                        var bestDistance = Infinity;

                        sentinels.forEach(function(sentinel, index) {
                            var rect = sentinel.getBoundingClientRect();
                            var center = rect.top + (rect.height / 2);
                            var distance = Math.abs(center - viewportMid);

                            if (distance < bestDistance) {
                                bestDistance = distance;
                                bestStep = index;
                            }
                        });

                        setStep(bestStep);
                    }

                    function onScrollOrResize() {
                        if (ticking) return;
                        ticking = true;
                        window.requestAnimationFrame(function() {
                            updateStep();
                            syncStackHeight(currentStep >= 0 ? currentStep : 0);
                            updateIndicatorPosition();
                            ticking = false;
                        });
                    }

                    setStep(0);
                    updateStep();
                    updateIndicatorPosition();
                    window.addEventListener('scroll', onScrollOrResize, { passive: true });
                    window.addEventListener('resize', onScrollOrResize);
                }

                if (document.readyState === 'loading') {
                    document.addEventListener('DOMContentLoaded', initMeteoriteIntro, { once: true });
                } else {
                    initMeteoriteIntro();
                }
            })();
            """
        ),
        class_="meteorite-intro-section",
    )
