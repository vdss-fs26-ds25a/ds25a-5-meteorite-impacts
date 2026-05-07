from shiny import ui


def build_meteor_introduction():
    comparison_cards = [
        {
            "title": "Meteoroid",
            "icon": "bi-hexagon-fill",
            "text": "A rocky or metallic body traveling through space.",
        },
        {
            "title": "Meteor",
            "icon": "bi-stars",
            "text": "The bright streak created when it burns in the atmosphere.",
        },
        {
            "title": "Meteorite",
            "icon": "bi-geo-alt-fill",
            "text": "The surviving fragment that reaches Earth's surface.",
        },
    ]
    intro_steps = [
        {
            "kind": "text",
            "title": "Meteoroid, Meteor, Meteorite whats the difference?",
            "text": "Here is the sequence from space object to ground fragment.",
        },
        {
            "kind": "text",
            "title": "From Space To Ground",
            "text": "The same object gets a different name depending on where it is: \n"
            "in space, in the atmosphere, or on the ground.",
        },
        {
            "kind": "cards",
            "title": "Meteoroid, Meteor, Meteorite",
            "text": "Here is the sequence from space object to ground fragment.",
        },
        {
            "kind": "text",
            "title": "Meteoroid",
            "text": "Meteorites are time capsules from the early solar system. Their "
            "minerals and isotopes help scientists reconstruct planetary "
            "formation and cosmic history.",
        },
        {
            "kind": "text",
            "title": "Meteor",
            "text": "Meteorites are time capsules from the early solar system. Their "
            "minerals and isotopes help scientists reconstruct planetary "
            "formation and cosmic history.",
        },
        {
            "kind": "text",
            "title": "Meteorite",
            "text": "Meteorites are time capsules from the early solar system. Their "
            "minerals and isotopes help scientists reconstruct planetary "
            "formation and cosmic history.",
        },
        {
            "kind": "text",
            "title": "What Meteorites Tell Us",
            "text": "Meteorites are time capsules from the early solar system. Their "
            "minerals and isotopes help scientists reconstruct planetary "
            "formation and cosmic history.",
        },
        {
            "kind": "text",
            "title": "Why This Matters Here",
            "text": "The timeline below highlights key meteorite events, from early "
            "historical records to modern observed falls and major scientific "
            "discoveries.",
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
                        ui.tags.h3(card["title"], class_="meteorite-term-title"),
                        ui.tags.p(card["text"], class_="meteorite-term-text"),
                        class_="meteorite-term-card",
                    )
                )
            block_children.append(ui.tags.div(*term_cards, class_="meteorite-term-grid"))

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
                font-size: 11px;
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
                font-size: 15px;
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
                ui.tags.i(class_="bi bi-chevron-down meteorite-intro-scroll-hint-icon", aria_hidden="true"),
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
