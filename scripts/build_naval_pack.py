#!/usr/bin/env python3
"""Generate the Naval plugin skills and shared references.

This intentionally stores paraphrased operating knowledge, coverage maps,
and workflows, not the full copyrighted book text.
"""

from __future__ import annotations

from pathlib import Path
import json
import re
import textwrap


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REFERENCES_DIR = ROOT / "references"


CHAPTER_SUMMARIES = {
    "front-matter": """# Front Matter And Context

The book is a curated collection of Naval Ravikant's public talks, interviews, tweets, and writing. It is edited and rearranged, so the pack should treat it as an operating map, not a primary-source quote archive.

Core constraints for this plugin:

- Paraphrase by default.
- Use only short excerpts when necessary.
- Mention page ranges or source sections when useful.
- Verify exact phrasing against a primary source before helping the user cite Naval.
- Interpret generously because the source material is intentionally non-linear and context has shifted across media.

The opening frames Naval as an immigrant, reader, founder, investor, and philosophical operator. His background matters because the book treats wealth, judgment, and happiness as learned skills rather than fixed traits.
""",
    "wealth": """# Wealth

Coverage: Building Wealth, pages 29-92.

The wealth section argues that wealth is not money or status. Wealth is productive ownership: assets, equity, code, media, IP, products, capital, or systems that can earn without a direct hour-for-hour trade.

Major ideas:

- Seek wealth, not money or status.
- Ethical wealth creation is possible.
- Do not rent out time as the primary path to freedom.
- Give society something it wants but does not yet know how to get, at scale.
- Build specific knowledge through curiosity, obsession, apprenticeship, and lived traits.
- Escape competition through authenticity.
- Play long-term games with long-term people.
- Compound capital, reputation, relationships, learning, and trust.
- Take accountability under your own name.
- Own equity or upside.
- Use leverage: labor, capital, code, media, brand, distribution, and automation.
- Learn to build or sell; doing both is powerful.
- Get paid for judgment rather than input.
- Value time aggressively.
- Avoid status games and short-term games.
- Engineer luck through motion, preparedness, reputation, and unique character.
- Be patient, but avoid risk of ruin.
- Money solves money problems; it does not automatically produce peace.

Default output for wealth skills:

- Identify the current wealth game.
- Separate wealth, money, and status.
- Identify ownership and leverage gaps.
- Name the compounding surface.
- Recommend one concrete experiment that increases specific knowledge, accountability, leverage, or ownership.
""",
    "judgment": """# Judgment

Coverage: Building Judgment, pages 93-126.

The judgment section treats wisdom as knowing long-term consequences and judgment as applying that wisdom to external decisions. In a leveraged age, small differences in judgment create large differences in outcome.

Major ideas:

- Clear thinking matters more than sounding smart.
- Understand basics deeply enough to rederive ideas.
- Fancy language can hide weak understanding.
- Reality is easiest to see when ego, identity, and desired outcomes are quiet.
- Suffering can reveal reality when denial stops working.
- Empty calendar space is required for clear thought.
- Shed inherited identity bundles and tribal packages.
- Be radically honest without being needlessly harsh.
- Use mental models: evolution, game theory, complexity, economics, principal-agent, compounding, basic math, probability, tail risk, falsifiability, and inversion.
- If you cannot decide on a major yes/no life commitment, default to no.
- If split between two hard choices, choose short-term pain with long-term gain.
- Reading is a meta-skill. Read by curiosity, reread, drop weak books, and build foundations.

Default output for judgment skills:

- State the decision or claim plainly.
- Identify hidden desires, identity, incentives, and time horizons.
- Apply 2-4 mental models.
- Show what would falsify the conclusion.
- Recommend the next action or information needed.
""",
    "happiness": """# Happiness

Coverage: Learning Happiness, pages 127-156.

The happiness section treats happiness as a trainable baseline. It is less about positive emotion and more about peace, presence, acceptance, and reducing needless desire.

Major ideas:

- Happiness is learned and can be trained like fitness.
- Happiness is what remains when the sense of missing something drops away.
- Positive thoughts are not the whole answer; desire and mental motion create suffering.
- Presence matters because regret and anticipation pull attention away from reality.
- Peace is more stable than excitement.
- Desires can become self-imposed unhappiness until reality changes.
- External success does not create lasting happiness.
- Hedonic adaptation keeps people playing games too long.
- Envy dissolves when you realize you cannot selectively swap lives.
- Happiness is built through habits, environment, people, exercise, sunlight, meditation, and reducing screens/news/stimulants where needed.
- In a stuck situation, choose: change it, accept it, or leave it.
- Death awareness can clarify what matters and reduce ego battles.

Default output for happiness skills:

- Identify the desire, expectation, comparison, or story creating suffering.
- Separate controllable action from acceptance.
- Pick a small practice for presence or peace.
- Suggest one environment or habit change.
""",
    "saving-yourself": """# Saving Yourself

Coverage: Saving Yourself, pages 157-192.

This section turns philosophy into responsibility. Doctors, teachers, mentors, and trainers can help, but they cannot save the user. The user must choose health, authenticity, self-observation, habits, and freedom.

Major ideas:

- Be yourself with intensity; do not copy someone else's checklist.
- Find the people, project, market, or art that needs you most.
- Health comes first: physical, mental, spiritual, family, then external work.
- Modern life pulls people away from evolved needs: movement, nature, family, sunlight, play, low processed food, and lower screen addiction.
- Diet is best simplified by subtracting processed food and avoiding appetite traps.
- Exercise should be daily and chosen for consistency.
- Meditation is mental fasting; it processes unresolved thoughts and creates distance from the mind.
- Awareness allows the user to watch thoughts instead of being owned by them.
- Habits and self-image shape behavior.
- Systems and environments beat abstract goals.
- Freedom evolves from freedom to do anything into freedom from reaction, anger, expectation, employment dependence, and uncontrolled thinking.

Default output for self-work skills:

- Identify the current responsibility gap.
- Name the environment, habit, or thought pattern driving the issue.
- Recommend a small system or practice.
- End with one commitment and one thing to remove.
""",
    "philosophy": """# Philosophy

Coverage: Philosophy, pages 193-206.

The philosophy section avoids one universal meaning and pushes the user to discover or create meaning directly. It joins practical values with rational inner work.

Major ideas:

- The meaning of life is personal, or absent, or a story created inside a vast indifferent universe.
- Values are what the user refuses to compromise.
- Naval emphasizes honesty, long-term thinking, peer relationships, and freedom from anger.
- Relationships work better when values line up.
- Rational Buddhism means keeping testable inner practices and rejecting unverifiable metaphysical claims as operating truths.
- Evolution explains many drives; Buddhism gives tools for internal freedom.
- The present moment is the only place life is actually experienced.
- Inspiration is perishable and should be acted on quickly.

Default output for philosophy skills:

- Clarify whether the user needs meaning, values, acceptance, or action.
- Refuse borrowed certainty.
- Turn abstract reflection into one behavior, boundary, or commitment.
""",
    "reading": """# Reading And Recommended Curriculum

Coverage: Naval's Recommended Reading, Naval's Writing, and Next On Naval, pages 207-228.

The reading section is not a generic book list. It reflects Naval's preference for foundations, original thinkers, science, math, economics, philosophy, mental models, and idea-dense fiction.

Major clusters:

- Science and explanation: David Deutsch, Richard Feynman, Carlo Rovelli, physics basics.
- History and progress: Yuval Harari, Will and Ariel Durant, Matt Ridley.
- Risk and mental models: Nassim Taleb, Charlie Munger, Farnam Street.
- Economics and strategy: microeconomics, game theory, cooperation, aggregation theory.
- Philosophy and inner work: Krishnamurti, Osho, Anthony de Mello, Marcus Aurelius, Kamal Ravikant, Kahlil Gibran, Jed McKenna, Kapil Gupta.
- Fiction and speculative thinking: Borges, Ted Chiang, Neal Stephenson, Asimov.
- Writing and web reading: Scott Adams, Kevin Simler, Ben Thompson, Idle Words, Hamming.

Default output for reading skills:

- Ask what the user wants to develop: wealth, judgment, peace, science, persuasion, or meaning.
- Choose a short reading path.
- Include classics/foundations before commentary.
- Encourage dropping weak books and rereading strong ones.
""",
}


WORKFLOWS = {
    "wealth-scorecard": """# Wealth Scorecard

Score each from 0-5:

- Specific knowledge: Is this based on hard-to-train curiosity, skill, or taste?
- Accountability: Is someone clearly taking risk under their own name?
- Ownership: Is there equity, IP, asset ownership, or upside?
- Leverage: Can code, media, capital, labor, brand, or distribution multiply the work?
- Long-term game: Can trust, reputation, learning, and relationships compound?
- Market want: Does society want this but not yet know how to get it?
- Authenticity: Does this fit the user's actual interests and temperament?
- Ruin control: Is catastrophic downside avoided?

Output: total score, weakest constraint, strongest compounding surface, one 7-day experiment.
""",
    "decision-scorecard": """# Decision Scorecard

Use for job, city, relationship, business, investment, or project choices.

Questions:

- What is the actual yes/no decision?
- Is the user deciding from desire, fear, identity, status, or reality?
- What happens if this compounds for ten years?
- What incentives are hidden?
- What would falsify the user's preferred answer?
- If the answer is not a clear yes, should it be no?
- If two options are tied, which has short-term pain and long-term gain?

Output: recommendation, uncertainty, one test, and one action now.
""",
    "desire-audit": """# Desire Audit

Use when the user feels restless, jealous, angry, or stuck.

Questions:

- What external condition is the user waiting on before being okay?
- What desire has become a contract for unhappiness?
- Is this desire worth keeping as the one big active desire?
- Can the user change it, accept it, or leave it?
- What would peace choose if ego were quiet?

Output: desire, cost, keep/drop/change/accept/leave, practice for today.
""",
    "meditation-protocol": """# Meditation Protocol

Use as a practical, non-mystical protocol.

Options:

- Choiceless awareness during walking or quiet time.
- Sit with eyes closed and do nothing.
- Watch thoughts as events, not commands.
- Use breath to settle the nervous system.
- Journal as written meditation.

Output: duration, time, method, resistance plan, and what to observe.
""",
    "reading-curriculum": """# Reading Curriculum

Build short tracks:

- Wealth: microeconomics, game theory, Munger, Taleb, technology strategy.
- Judgment: math, probability, science, Feynman, Farnam Street, originals.
- Happiness: Krishnamurti, Marcus Aurelius, de Mello, Tolle-adjacent presence work.
- Science and optimism: Deutsch, Ridley, Rovelli, Feynman.
- Fictional thinking: Borges, Ted Chiang, Stephenson, Asimov.

Keep paths short. Prefer one great book over ten impressive ones.
""",
    "daily-review": """# Daily Review

Ask:

- Did I protect health first?
- What did I do that compounds?
- What desire disturbed peace?
- Did I rent time, build assets, or improve judgment?
- Did I act from authenticity or status?
- What should be removed tomorrow?

Output: one win, one drag, one removal, one compounding action.
""",
    "weekly-compound-review": """# Weekly Compound Review

Review:

- Wealth: ownership, leverage, specific knowledge, reputation.
- Judgment: decisions, books, falsified beliefs, mental models.
- Health: exercise, diet, sleep, sunlight, screen discipline.
- Happiness: desires, presence, relationships, acceptance.
- Values: honesty, long-term behavior, anger, expectations.

Output: compounding gains, leaks, next week's one constraint.
""",
    "opportunity-scorecard": """# Opportunity Scorecard

Use for jobs, startups, projects, content, products, and investments.

Score:

- Market wants it.
- User has or can build specific knowledge.
- Leverage is available.
- Ownership/upside is available.
- Accountability is clear.
- Long-term people are involved.
- It feels like play enough to persist.
- Ruin risk is controlled.

Output: pursue, test, defer, or decline.
""",
    "relationship-scorecard": """# Relationship Scorecard

Use for collaborators, partners, friends, and teams.

Check:

- Integrity under small stakes.
- Long-term orientation.
- Energy and intelligence without cynicism.
- Values alignment.
- Ability to compound trust.
- Low maintenance, low drama.
- Whether the user can imagine working with them for life.

Output: deepen, keep light, set boundary, or exit.
""",
    "quote-safety": """# Quote Safety

Use when producing any quotation-like output from the book.

Rules:

- Paraphrase by default.
- Keep direct excerpts short.
- Cite page/section when available.
- Say if exact wording should be verified against a primary source.
- Do not reproduce long passages, chapter chunks, or the full text.
""",
}


SKILLS = [
    ("n-router", "Naval Router", "meta", "Route vague user situations to the right Naval skill and reference path.", "Use Naval to analyze this career decision."),
    ("n-source-fidelity", "Naval Source Fidelity", "front-matter", "Keep interpretations faithful to the book, avoid over-quoting, and flag when exact phrasing needs verification.", "Check this Naval idea before I cite it."),
    ("n-biographical-context", "Naval Biographical Context", "front-matter", "Use Naval's background and timeline to explain why a principle appears in the book.", "What life context explains this Naval idea?"),
    ("n-wealth-map", "Naval Wealth Map", "wealth", "Create an end-to-end wealth strategy using specific knowledge, accountability, ownership, leverage, and patience.", "Build me a Naval-style wealth plan."),
    ("n-wealth-vs-money-status", "Naval Wealth Vs Money Status", "wealth", "Separate wealth creation from income, cash, approval, prestige, and social hierarchy.", "Am I chasing wealth, money, or status here?"),
    ("n-specific-knowledge", "Naval Specific Knowledge", "wealth", "Identify hard-to-train strengths, obsessions, taste, and authentic edges.", "Help me identify my specific knowledge."),
    ("n-authenticity-positioning", "Naval Authenticity Positioning", "wealth", "Escape competition by positioning around what is natural, rare, and hard to copy.", "How do I make this product more authentically mine?"),
    ("n-long-term-games", "Naval Long Term Games", "wealth", "Evaluate whether work, relationships, and markets can compound for years.", "Is this a long-term game with long-term people?"),
    ("n-integrity-partner-filter", "Naval Integrity Partner Filter", "wealth", "Assess collaborators for integrity, optimism, energy, and long-term fit.", "Should I work with this person?"),
    ("n-accountability-risk", "Naval Accountability Risk", "wealth", "Decide when to put reputation, name, capital, and responsibility behind an action.", "Should I take public accountability for this?"),
    ("n-equity-ownership", "Naval Equity Ownership", "wealth", "Move from wage or service work toward ownership, IP, assets, and upside.", "How do I get equity or upside here?"),
    ("n-leverage-stack", "Naval Leverage Stack", "wealth", "Find code, media, capital, labor, brand, distribution, and automation leverage.", "What leverage can I add to this project?"),
    ("n-build-or-sell", "Naval Build Or Sell", "wealth", "Choose whether to learn building, selling, or both for a tech or business path.", "Should I learn to build, sell, or both?"),
    ("n-judgment-compensation", "Naval Judgment Compensation", "wealth", "Move from being paid for hours to being paid for judgment under leverage.", "How do I become paid for judgment?"),
    ("n-time-value-focus", "Naval Time Value Focus", "wealth", "Apply personal hourly-rate thinking, ruthless prioritization, and calendar clearing.", "What should I stop doing this week?"),
    ("n-status-game-detector", "Naval Status Game Detector", "wealth", "Detect zero-sum approval, politics, prestige, and comparison traps.", "Is this actually a status game?"),
    ("n-big-life-decisions", "Naval Big Life Decisions", "wealth", "Think through city, partner, job, company, and life-direction choices.", "Help me decide whether to take this job."),
    ("n-work-as-play", "Naval Work As Play", "wealth", "Find work that feels like play to the user but looks like work to others.", "What work feels like play to me?"),
    ("n-retirement-freedom-design", "Naval Retirement Freedom Design", "wealth", "Design freedom through passive income, low burn, or loved work.", "What is my real path to retirement?"),
    ("n-luck-engineering", "Naval Luck Engineering", "wealth", "Create conditions for luck through motion, skill, reputation, and unique character.", "How do I make luck find me?"),
    ("n-reputation-networking", "Naval Reputation Networking", "wealth", "Replace shallow networking with craft, generosity, and visible reputation.", "How should I build relationships without networking?"),
    ("n-patience-compounding", "Naval Patience Compounding", "wealth", "Balance impatience with action against patience for compounding results.", "Where do I need patience versus action?"),
    ("n-risk-of-ruin", "Naval Risk Of Ruin", "wealth", "Identify legal, health, financial, relationship, and reputation ruin risks.", "What could ruin me in this plan?"),
    ("n-judgment-builder", "Naval Judgment Builder", "judgment", "Improve decision quality in leveraged work and life choices.", "Improve my judgment on this bet."),
    ("n-clear-thinking", "Naval Clear Thinking", "judgment", "Simplify confused thinking down to basics, first principles, and plain language.", "Make my thinking clearer here."),
    ("n-reality-ego-audit", "Naval Reality Ego Audit", "judgment", "Reveal where desire, ego, or fear is blocking reality.", "What am I refusing to see?"),
    ("n-identity-shedding", "Naval Identity Shedding", "judgment", "Drop inherited labels, tribes, packages, and stale self-images.", "What identity is trapping my thinking?"),
    ("n-decision-rules", "Naval Decision Rules", "judgment", "Apply Naval's major decision heuristics to hard choices.", "Apply Naval's decision rules to this choice."),
    ("n-mental-models", "Naval Mental Models", "judgment", "Use compounding, incentives, evolution, game theory, complexity, inversion, and probability.", "Which mental models apply here?"),
    ("n-inversion-filter", "Naval Inversion Filter", "judgment", "Find what will fail, what to avoid, and which mistakes matter most.", "How could this fail?"),
    ("n-falsifiability-truth", "Naval Falsifiability Truth", "judgment", "Test whether claims have predictive power and can be falsified.", "Is this claim actually testable?"),
    ("n-foundational-learning", "Naval Foundational Learning", "judgment", "Build foundations in math, science, economics, persuasion, and learning.", "Build me a foundation learning plan."),
    ("n-reading-system", "Naval Reading System", "judgment", "Design curiosity-led reading habits, rereading, skimming, and dropping weak books.", "Design my reading system."),
    ("n-happiness-baseline", "Naval Happiness Baseline", "happiness", "Train happiness as a baseline using peace, habits, presence, and acceptance.", "Help me raise my happiness baseline."),
    ("n-desire-audit", "Naval Desire Audit", "happiness", "Identify desires that create suffering and decide whether to keep, drop, change, accept, or leave.", "What desire is making me unhappy?"),
    ("n-presence-practice", "Naval Presence Practice", "happiness", "Reduce rumination and anticipation by returning attention to present reality.", "Help me return to the present."),
    ("n-peace-over-joy", "Naval Peace Over Joy", "happiness", "Prefer stable peace over stimulation, bliss chasing, or externally dependent moods.", "Am I optimizing for peace or excitement?"),
    ("n-success-game-exit", "Naval Success Game Exit", "happiness", "Notice when the user has outgrown a game with big rewards.", "Have I outgrown this game?"),
    ("n-envy-antidote", "Naval Envy Antidote", "happiness", "Dissolve jealousy, comparison, and external scorecards.", "Help me dissolve envy around this person."),
    ("n-happiness-habits", "Naval Happiness Habits", "happiness", "Build daily habits that support mood stability and long-term happiness.", "Create a happiness habit plan."),
    ("n-accept-change-leave", "Naval Accept Change Leave", "happiness", "Force stuck situations into acceptance, change, or exit.", "Should I accept, change, or leave this?"),
    ("n-death-awareness", "Naval Death Awareness", "happiness", "Use mortality to clarify priorities and reduce ego battles.", "Use mortality to clarify this decision."),
    ("n-self-responsibility", "Naval Self Responsibility", "saving-yourself", "Stop outsourcing responsibility to gurus, mentors, doctors, teachers, or tools.", "Where am I outsourcing responsibility?"),
    ("n-be-yourself", "Naval Be Yourself", "saving-yourself", "Find original contribution by being oneself with intensity.", "Help me stop copying others."),
    ("n-health-first", "Naval Health First", "saving-yourself", "Reorder life around physical, mental, and spiritual health before work.", "Reorder my life around health first."),
    ("n-diet-simplifier", "Naval Diet Simplifier", "saving-yourself", "Simplify diet by subtracting processed food and appetite traps.", "Simplify my diet Naval-style."),
    ("n-exercise-priority", "Naval Exercise Priority", "saving-yourself", "Make daily exercise consistent and priority-driven.", "Make exercise non-negotiable."),
    ("n-meditation-system", "Naval Meditation System", "saving-yourself", "Create a practical awareness, sitting, walking, or journaling meditation protocol.", "Design a 60-day meditation protocol."),
    ("n-mental-debugging", "Naval Mental Debugging", "saving-yourself", "Watch thoughts, reactions, fear, desire, and ego as debuggable processes.", "Debug my internal monologue."),
    ("n-habit-change", "Naval Habit Change", "saving-yourself", "Replace vague goals with identity, triggers, substitutes, tracking, and commitment.", "Help me replace this habit."),
    ("n-systems-not-goals", "Naval Systems Not Goals", "saving-yourself", "Turn goals into environments and systems that make success likely.", "Turn this goal into a system."),
    ("n-grow-yourself", "Naval Grow Yourself", "saving-yourself", "Support self-change through self-image, learning, and internal readiness.", "How do I become the kind of person who does this?"),
    ("n-freedom-from-expectations", "Naval Freedom From Expectations", "saving-yourself", "Set boundaries around expectations, obligations, and others' imagined claims.", "Where am I living by others' expectations?"),
    ("n-anger-release", "Naval Anger Release", "saving-yourself", "Treat anger as self-punishment and find a cleaner response.", "Help me process this anger."),
    ("n-employment-freedom", "Naval Employment Freedom", "saving-yourself", "Reduce dependence on employment through burn-rate, ownership, and independence choices.", "How do I become less dependent on employment?"),
    ("n-uncontrolled-thinking", "Naval Uncontrolled Thinking", "saving-yourself", "Turn the mind from master into tool by reducing compulsive inner narration.", "Help me stop compulsive thinking."),
    ("n-modern-addiction-defense", "Naval Modern Addiction Defense", "saving-yourself", "Audit screens, news, processed food, games, porn, stimulants, and dopamine traps.", "Audit my environment for modern traps."),
    ("n-meaning-maker", "Naval Meaning Maker", "philosophy", "Explore personal meaning without pretending there is a universal borrowed answer.", "Help me find my current meaning."),
    ("n-values-filter", "Naval Values Filter", "philosophy", "Apply values: honesty, long-term thinking, peer relationships, low anger, and freedom.", "What values are being violated here?"),
    ("n-rational-buddhism", "Naval Rational Buddhism", "philosophy", "Use testable inner work while rejecting unverifiable claims as operating truth.", "Give me a rational inner-work frame."),
    ("n-wisdom-long-term", "Naval Wisdom Long Term", "philosophy", "Evaluate long-term consequences as the basis of wisdom.", "What are the long-term consequences?"),
    ("n-present-moment", "Naval Present Moment", "philosophy", "Return to the present and act on perishable inspiration.", "What should I do immediately?"),
    ("n-reading-curriculum", "Naval Reading Curriculum", "reading", "Build book paths across science, mental models, philosophy, economics, and fiction.", "Build me a Naval reading curriculum."),
    ("n-life-formulas", "Naval Life Formulas", "reading", "Use Naval's formula-style writing for health, wealth, happiness, income, and learning.", "Show the formula behind this area."),
    ("n-rules", "Naval Rules", "reading", "Apply compact Naval rules and maxims as reminders, not substitutes for reasoning.", "Give me the relevant Naval rule."),
    ("n-next-sources", "Naval Next Sources", "reading", "Point users to deeper Naval resources, podcasts, essays, and source trails.", "Where should I go deeper on this topic?"),
    ("n-coverage-auditor", "Naval Coverage Auditor", "meta", "Check whether all book sections are represented by skills and references.", "Audit whether the Naval plugin missed anything."),
    ("n-principle-to-action", "Naval Principle To Action", "meta", "Convert a principle into a concrete behavior, experiment, or operating rule.", "Turn this Naval principle into action."),
    ("n-daily-review", "Naval Daily Review", "meta", "Run a daily health, work, desire, focus, and freedom review.", "Run my daily Naval review."),
    ("n-weekly-compound-review", "Naval Weekly Compound Review", "meta", "Review weekly compounding across wealth, judgment, health, happiness, relationships, and values.", "Run my weekly compound review."),
    ("n-opportunity-scorecard", "Naval Opportunity Scorecard", "meta", "Score jobs, startups, projects, products, content, and investments.", "Score this opportunity Naval-style."),
    ("n-relationship-scorecard", "Naval Relationship Scorecard", "meta", "Score collaborators, friends, partners, and teams for long-term compounding fit.", "Score this collaborator Naval-style."),
    ("n-quote-safety", "Naval Quote Safety", "meta", "Keep quotations short, attributed, and compliant while preferring paraphrase.", "Make this Naval quote safe to use."),
    ("n-socratic-coach", "Naval Socratic Coach", "meta", "Ask precise questions before advising when the user's situation is under-specified.", "Coach me through this without jumping to advice."),
    ("n-flashcards", "Naval Flashcards", "meta", "Turn principles into recall prompts, reflection cards, or spaced repetition items.", "Make flashcards from this Naval topic."),
    ("n-book-club", "Naval Book Club", "meta", "Discuss chapters, exercises, takeaways, and reading reflections.", "Run a book club discussion for the wealth section."),
]


CATEGORY_REFERENCES = {
    "front-matter": ["front-matter"],
    "wealth": ["wealth"],
    "judgment": ["judgment"],
    "happiness": ["happiness"],
    "saving-yourself": ["saving-yourself"],
    "philosophy": ["philosophy"],
    "reading": ["reading"],
    "meta": ["wealth", "judgment", "happiness", "saving-yourself", "philosophy", "reading"],
}


CATEGORY_WORKFLOWS = {
    "wealth": ["wealth-scorecard", "opportunity-scorecard"],
    "judgment": ["decision-scorecard"],
    "happiness": ["desire-audit"],
    "saving-yourself": ["meditation-protocol", "daily-review"],
    "philosophy": ["decision-scorecard"],
    "reading": ["reading-curriculum"],
    "front-matter": ["quote-safety"],
    "meta": ["daily-review", "weekly-compound-review", "opportunity-scorecard", "relationship-scorecard", "quote-safety"],
}


BOOK_MAP = """# Naval Almanack Book Map

Source: Eric Jorgenson, The Almanack of Naval Ravikant, 2020 PDF.

This plugin covers the whole book as a set of operational skills. It does not store the full book text. Use the user's local PDF or primary web sources for exact quotation checks.

## Sections

- Important Notes / Disclaimer, pages 9-11: edited compilation, interpret generously, verify exact phrasing before citation.
- Foreword, pages 13-16: Naval as independent thinker, tester, long-term operator.
- Eric's Note, pages 17-19: why this book exists and how to use it as a guide.
- Timeline / Background, pages 21-25: immigrant upbringing, books, Stuyvesant, Dartmouth, Epinions, AngelList, investing.
- Wealth, pages 29-92: wealth creation, specific knowledge, long-term games, accountability, equity, leverage, judgment, focus, work as play, luck, patience.
- Judgment, pages 93-126: clear thinking, reality, identity shedding, decision-making, mental models, reading.
- Happiness, pages 127-156: happiness as skill, choice, presence, peace, desire, success, envy, habits, acceptance.
- Saving Yourself, pages 157-192: self-responsibility, authenticity, health, diet, exercise, meditation, habits, growth, freedom.
- Philosophy, pages 193-206: meaning, values, rational Buddhism, present moment.
- Recommended Reading / Writing / Next Sources, pages 207-228: books, blogs, other recommendations, formulas, rules, source trail.
- Appreciation / Sources / About, pages 229-242: acknowledgments, citations, author note.

## Usage Principle

Prefer skill-specific action over generic inspiration. Each skill should ask for missing context, apply the relevant Naval lens, and end with a decision, scorecard, practice, experiment, or next action.
"""


CONCEPT_GRAPH = {
    "wealth": ["specific knowledge", "accountability", "ownership", "leverage", "judgment", "long-term games", "patience"],
    "judgment": ["clear thinking", "reality", "identity", "mental models", "decision rules", "reading", "falsifiability"],
    "happiness": ["desire", "presence", "peace", "habits", "acceptance", "envy", "death awareness"],
    "self_work": ["health", "diet", "exercise", "meditation", "habits", "freedom", "responsibility"],
    "philosophy": ["meaning", "values", "rational Buddhism", "present moment", "wisdom"],
    "reading": ["foundations", "originals", "science", "economics", "philosophy", "fiction", "rereading"],
}


ROUTER_GUIDE = """# Router Guide

Use this when the user says "use Naval", "n-", or gives a vague life/work situation without naming a specific skill.

## Fast Routing

- Money, work, business, leverage, equity, career, startup: start with `n-wealth-map`.
- Unique strengths, niche, unfair advantage, competition: start with `n-specific-knowledge`.
- Product, project, company, content, investment: start with `n-opportunity-scorecard`.
- Hard yes/no choice: start with `n-decision-rules`.
- Confusion, ego, denial, bad assumptions: start with `n-reality-ego-audit`.
- Mental models, incentives, risk, probability: start with `n-mental-models`.
- Restlessness, wanting, jealousy, anxiety: start with `n-desire-audit`.
- Stuck situation: start with `n-accept-change-leave`.
- Health, exercise, diet, meditation: start with `n-health-first`, then route narrower.
- Values, boundaries, anger, expectations: start with `n-values-filter`.
- Books or learning path: start with `n-reading-curriculum`.
- Exact wording, citation, quote use: start with `n-source-fidelity` or `n-quote-safety`.

## Routing Output

Return:

- Primary skill
- Secondary skills
- Why this route
- First question to ask
- Best next action format: decision, scorecard, practice, experiment, or reading path

Prefer one primary skill. Use secondary skills only when they add a different lens.
"""


def wrap(text: str) -> str:
    return textwrap.dedent(text).strip() + "\n"


def yaml_quote(value: str) -> str:
    return json.dumps(value)


def display_name(slug: str, title: str) -> str:
    if title.startswith("Naval"):
        return title.replace("Naval", "N", 1)
    return title


def short_description(title: str, focus: str) -> str:
    text = f"{title}: {focus}"
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) < 25:
        text = f"{text} guidance"
    if len(text) > 64:
        text = text[:64].rsplit(" ", 1)[0]
    if len(text) < 25:
        text = f"{title} operating guidance"
    return text


def skill_lookup() -> dict[str, tuple[str, str, str, str]]:
    return {slug: (title, category, focus, example) for slug, title, category, focus, example in SKILLS}


def skill_catalog() -> str:
    lines = [
        "# Naval Skill Catalog",
        "",
        "Every callable skill uses the `n-` prefix for search. Use `n-router` when unsure.",
        "",
        "| Skill | Area | Use When | Example |",
        "|---|---|---|---|",
    ]
    for slug, title, category, focus, example in SKILLS:
        lines.append(f"| `{slug}` | {category} | {focus} | {example} |")
    lines.extend(
        [
            "",
            "## Better Than A Quote Pack",
            "",
            "These skills should not stop at summarizing Naval. Each one should turn the relevant principle into one of: a decision, scorecard, experiment, daily practice, boundary, reading path, or removal.",
            "",
            "## Search Tips",
            "",
            "- Search `n-wealth` for wealth and work questions.",
            "- Search `n-judgment` or `n-decision` for choices.",
            "- Search `n-desire`, `n-happiness`, or `n-accept` for inner-state questions.",
            "- Search `n-health`, `n-exercise`, `n-diet`, or `n-meditation` for self-care.",
            "- Search `n-values`, `n-meaning`, or `n-present` for philosophy.",
            "- Search `n-reading` for book paths.",
        ]
    )
    return "\n".join(lines) + "\n"


def skill_md(slug: str, title: str, category: str, focus: str, example: str) -> str:
    chapters = CATEGORY_REFERENCES[category]
    workflows = CATEGORY_WORKFLOWS[category]
    chapter_lines = "\n".join(f"- `../../references/chapter-summaries/{name}.md`" for name in chapters)
    workflow_lines = "\n".join(f"- `../../references/workflows/{name}.md`" for name in workflows)
    router_line = "- `../../references/router-guide.md`" if slug == "n-router" else "- `../../references/skill-catalog.md`"
    action_mode = {
        "wealth": "scorecard or 7-day wealth experiment",
        "judgment": "decision recommendation or falsifiable test",
        "happiness": "desire audit, acceptance choice, or daily practice",
        "saving-yourself": "habit system, environment change, or removal",
        "philosophy": "values clarification, boundary, or immediate action",
        "reading": "short reading path or learning system",
        "front-matter": "safe paraphrase, citation caveat, or source check",
        "meta": "router result, review, scorecard, or generated study artifact",
    }[category]
    description = (
        f"Use when applying The Almanack of Naval Ravikant to {focus.lower()} "
        f"Trigger for user requests involving Naval, n-, {title.lower()}, life design, wealth, judgment, happiness, health, values, or book-derived operating principles."
    )
    return wrap(
        f"""---
name: {slug}
description: {yaml_quote(description)}
---

# {title}

## Purpose

{focus}

## Read First

- `../../references/book-map.md`
- `../../references/coverage-matrix.yaml`
{router_line}
{chapter_lines}
{workflow_lines}

## Use When

- The user asks for `{slug}` directly.
- The user asks: "{example}"
- The user is dealing with: {focus.lower()}
- The situation would benefit from a {action_mode}.

## Workflow

1. Restate the user's situation in plain language.
2. Ask for missing context only when the decision would otherwise be unsafe or fake.
3. Apply the relevant Naval lens from the references.
4. Separate signal from status, desire, fear, identity, and generic self-help.
5. Convert the principle into a concrete decision, scorecard, experiment, practice, or next action.
6. Include a short caveat when the topic touches health, finance, legal risk, or exact citation.

## Output

Return concise sections:

- Situation
- Naval lens
- Diagnosis
- Options or scorecard
- Recommended action
- 7-day experiment or daily practice
- What to avoid

## Do Not

- Do not reproduce long book passages.
- Do not pretend Naval has one answer for every person.
- Do not give generic motivation when a decision, practice, or test is possible.
- Do not treat money, status, peace, health, and meaning as interchangeable.

## Example

User: "{example}"
Assistant: Apply this skill, cite the relevant reference section, and end with one concrete action.

## Quality Bar

- Make the answer specific to the user's actual situation.
- Prefer one sharp recommendation over a buffet of advice.
- Name the tradeoff or hidden cost.
- End with something the user can do, test, stop, or observe today.
"""
    )


def openai_yaml(slug: str, title: str, focus: str, example: str) -> str:
    return wrap(
        f"""interface:
  display_name: {yaml_quote(display_name(slug, title))}
  short_description: {yaml_quote(short_description(display_name(slug, title), focus))}
  default_prompt: {yaml_quote(example)}
"""
    )


def write(path: Path, content: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    if executable:
        path.chmod(0o755)


def coverage_matrix() -> str:
    section_map = {
        "front_matter_disclaimer": ["n-source-fidelity", "n-quote-safety"],
        "foreword": ["n-biographical-context", "n-router"],
        "erics_note": ["n-router", "n-book-club"],
        "timeline_background": ["n-biographical-context"],
        "wealth_understand_creation": ["n-wealth-map", "n-wealth-vs-money-status"],
        "wealth_specific_knowledge": ["n-specific-knowledge", "n-authenticity-positioning"],
        "wealth_long_term_games": ["n-long-term-games", "n-integrity-partner-filter", "n-relationship-scorecard"],
        "wealth_accountability": ["n-accountability-risk"],
        "wealth_equity": ["n-equity-ownership"],
        "wealth_leverage": ["n-leverage-stack", "n-build-or-sell"],
        "wealth_judgment_compensation": ["n-judgment-compensation"],
        "wealth_focus": ["n-time-value-focus", "n-big-life-decisions"],
        "wealth_status_games": ["n-status-game-detector", "n-wealth-vs-money-status"],
        "wealth_work_as_play": ["n-work-as-play", "n-retirement-freedom-design"],
        "wealth_luck": ["n-luck-engineering", "n-reputation-networking"],
        "wealth_patience": ["n-patience-compounding", "n-risk-of-ruin"],
        "judgment_core": ["n-judgment-builder", "n-wisdom-long-term"],
        "judgment_clear_thinking": ["n-clear-thinking", "n-foundational-learning"],
        "judgment_reality_identity": ["n-reality-ego-audit", "n-identity-shedding"],
        "judgment_decision_making": ["n-decision-rules", "n-inversion-filter", "n-falsifiability-truth"],
        "judgment_mental_models": ["n-mental-models"],
        "judgment_reading": ["n-reading-system", "n-reading-curriculum"],
        "happiness_learned_choice": ["n-happiness-baseline"],
        "happiness_presence_peace": ["n-presence-practice", "n-peace-over-joy"],
        "happiness_desire": ["n-desire-audit"],
        "happiness_success_envy": ["n-success-game-exit", "n-envy-antidote"],
        "happiness_habits_acceptance": ["n-happiness-habits", "n-accept-change-leave", "n-death-awareness"],
        "saving_self_responsibility": ["n-self-responsibility"],
        "saving_be_yourself": ["n-be-yourself"],
        "saving_health": ["n-health-first", "n-diet-simplifier", "n-exercise-priority"],
        "saving_meditation": ["n-meditation-system", "n-mental-debugging"],
        "saving_build_grow": ["n-habit-change", "n-systems-not-goals", "n-grow-yourself"],
        "saving_freedom": ["n-freedom-from-expectations", "n-anger-release", "n-employment-freedom", "n-uncontrolled-thinking", "n-modern-addiction-defense"],
        "philosophy_meaning_values": ["n-meaning-maker", "n-values-filter"],
        "philosophy_rational_buddhism": ["n-rational-buddhism"],
        "philosophy_present": ["n-present-moment"],
        "recommended_reading": ["n-reading-curriculum", "n-next-sources"],
        "naval_writing": ["n-life-formulas", "n-rules", "n-principle-to-action"],
        "meta_review": ["n-coverage-auditor", "n-daily-review", "n-weekly-compound-review", "n-opportunity-scorecard", "n-flashcards", "n-socratic-coach"],
    }
    lines = ["# Coverage Matrix", "", "book_sections:"]
    for section, skills in section_map.items():
        lines.append(f"  {section}:")
        lines.append(f"    skills: [{', '.join(skills)}]")
    lines.append("")
    lines.append("all_skills:")
    for slug, *_ in SKILLS:
        lines.append(f"  - {slug}")
    return "\n".join(lines) + "\n"


def check_coverage_script() -> str:
    return wrap(
        """#!/usr/bin/env python3
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
skills_dir = root / "skills"
matrix = root / "references" / "coverage-matrix.yaml"
text = matrix.read_text(encoding="utf-8")
book_sections = text.split("\\nall_skills:", 1)[0]

actual = {p.name for p in skills_dir.iterdir() if (p / "SKILL.md").exists()}
listed = set(re.findall(r"\\b[n]-[a-z0-9-]+\\b", text))
mapped = set(re.findall(r"\\b[n]-[a-z0-9-]+\\b", book_sections))

missing_dirs = sorted(listed - actual)
unmapped = sorted(actual - mapped)
bad_prefix = sorted(name for name in actual if not name.startswith("n-"))
missing_links = []
missing_metadata = []
todo_files = []

for skill_dir in sorted(skills_dir.iterdir()):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        continue
    if not (skill_dir / "agents" / "openai.yaml").exists():
        missing_metadata.append(skill_dir.name)
    skill_text = skill_md.read_text(encoding="utf-8")
    if "TODO" in skill_text:
        todo_files.append(str(skill_md.relative_to(root)))
    for ref in re.findall(r"`(\\.\\./\\.\\./references/[^`]+)`", skill_text):
        target = (skill_dir / ref).resolve()
        if not target.exists():
            missing_links.append(f"{skill_dir.name}: {ref}")

for ref_file in sorted((root / "references").rglob("*")):
    if ref_file.is_file() and "TODO" in ref_file.read_text(encoding="utf-8", errors="ignore"):
        todo_files.append(str(ref_file.relative_to(root)))

if missing_dirs or unmapped or bad_prefix or missing_links or missing_metadata or todo_files:
    print("Coverage check failed")
    if missing_dirs:
        print("Missing skill directories:", ", ".join(missing_dirs))
    if unmapped:
        print("Skill directories not in coverage matrix:", ", ".join(unmapped))
    if bad_prefix:
        print("Skills without n- prefix:", ", ".join(bad_prefix))
    if missing_metadata:
        print("Skills without agents/openai.yaml:", ", ".join(missing_metadata))
    if missing_links:
        print("Missing reference links:")
        for link in missing_links:
            print(" -", link)
    if todo_files:
        print("TODO markers found:")
        for file in todo_files:
            print(" -", file)
    sys.exit(1)

print(f"Coverage check passed: {len(actual)} n-prefixed skills mapped with valid references.")
"""
    )


def main() -> None:
    REFERENCES_DIR.mkdir(parents=True, exist_ok=True)
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    write(REFERENCES_DIR / "book-map.md", BOOK_MAP)
    write(REFERENCES_DIR / "coverage-matrix.yaml", coverage_matrix())
    write(REFERENCES_DIR / "concept-graph.json", json.dumps(CONCEPT_GRAPH, indent=2) + "\n")
    write(REFERENCES_DIR / "router-guide.md", ROUTER_GUIDE)
    write(REFERENCES_DIR / "skill-catalog.md", skill_catalog())

    for name, content in CHAPTER_SUMMARIES.items():
        write(REFERENCES_DIR / "chapter-summaries" / f"{name}.md", content)
    for name, content in WORKFLOWS.items():
        write(REFERENCES_DIR / "workflows" / f"{name}.md", content)

    write(ROOT / "scripts" / "check_coverage.py", check_coverage_script(), executable=True)

    for slug, title, category, focus, example in SKILLS:
        skill_dir = SKILLS_DIR / slug
        write(skill_dir / "SKILL.md", skill_md(slug, title, category, focus, example))
        write(skill_dir / "agents" / "openai.yaml", openai_yaml(slug, title, focus, example))

    print(f"Generated {len(SKILLS)} n-prefixed Naval skills in {SKILLS_DIR}")


if __name__ == "__main__":
    main()
