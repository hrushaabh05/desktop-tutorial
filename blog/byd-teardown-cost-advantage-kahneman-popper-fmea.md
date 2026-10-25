---
title: "Stress-Testing the BYD Teardown Story: Bias, Falsification and a Modified FMEA Playbook for EV Makers"
slug: byd-teardown-cost-advantage-kahneman-popper-fmea
author: Hrushaabh Mishra
date: 2026-10-25
site: hrushaabhmishrablog.com
tags: [BYD, electric vehicles, teardown, cost engineering, Kahneman, Tversky, Karl Popper, DFMEA, PFMEA, manufacturing quality]
meta_description: "The Nikkei teardown says BYD wins on cost because of integration and in-house production. We test that claim with Kahneman & Tversky, try to falsify it with Popper, and turn the lessons into modified DFMEA/PFMEA guidelines for EV manufacturers."
---

# Stress-Testing the BYD Teardown Story: Bias, Falsification and a Modified FMEA Playbook for EV Makers

*By Hrushaabh Mishra · 25 October 2026 · ~15 min read*

> **TL;DR** — Teardowns of BYD vehicles keep returning the same verdict: Chinese EVs are cheaper mainly because of **part integration, vertical integration and scale**, not mainly because of subsidies or cheap labour. That claim is probably *largely right*, but the way it gets told is open to well-documented thinking errors. Below, I (1) summarise the evidence, (2) run it through Kahneman and Tversky's bias research, (3) restate it as hypotheses that could be proven wrong, in Popper's sense, and say what evidence would refute them, and (4) turn the lessons into a **modified DFMEA and PFMEA guideline** that EV manufacturers can use.

---

## 1. The claim we are testing

James Phang's recent post on the Nikkei BYD teardown and China's EV cost advantage [1] revisits a story that has been building since 2023. Japanese engineers, investment banks and think tanks have taken BYD cars apart, and they keep reaching the same conclusion.

Stated as one thesis:

> **"BYD's cost advantage is *structural*. It comes from fewer, more integrated parts, a high share of components made in-house, and scale. Subsidies and low labour costs explain only a small part of it, so Western and Japanese incumbents cannot close the gap with tariffs alone."**

What the teardown evidence says:

| Source | What it found |
|---|---|
| **Nikkei Asia, Nagoya EV teardown showcase (Oct 2024)** [2] | About 70 Japanese parts makers studied more than 90,000 parts from 16 foreign EVs, including the BYD Atto 3. Its conclusion: Chinese EV makers keep costs down "by integrating multiple components into one part and maximizing in-house production." |
| **Electrek / secondary coverage of the same event** [3][4] | The Atto 3's e-axle combines **eight functions** (motor, inverter, reducer, onboard charger, DC-DC converter, etc.) in one unit. Suppliers were "surprised at the small number of parts used by BYD and Tesla." |
| **Nikkei BP BYD Seal teardown book** [5] | A 350-page, step-by-step teardown of the Seal. Its price (about ¥67,000) shows how valuable this benchmarking is to Japanese industry. |
| **UBS Evidence Lab, BYD Seal teardown (Sept 2023)** [6][7] | About **75 % of components made in-house**, from batteries to power semiconductors. An estimated **~25 % cost advantage** over legacy OEMs in Europe *after* freight and tariffs, and ~15 % cheaper to build than a China-built Tesla Model 3. |
| **Rhodium Group, "Why Are Chinese EVs So Cheap?" (2026)** [8][9][10] | Vertical integration is the "most significant factor." BYD makes nearly **80 %** of its core components in-house. The Seal saves about **$2,369/vehicle in supplier mark-ups** compared with the Model 3, and about **$214/vehicle** from supplier payment timing (working capital). Subsidies matter but are **small** compared with these structural factors. |

The story is consistent across these sources, and it is persuasive. That is the reason to test it carefully.

---

## 2. A Kahneman & Tversky lens: how this story could mislead us

Daniel Kahneman and Amos Tversky showed that intuitive judgement relies on **heuristics**, mental shortcuts that are usually useful but cause predictable errors [11][12][13]. Teardown narratives are especially exposed to these errors because they are vivid, visual and easy to tell as a story.

### 2.1 "What you see is all there is" (WYSIATI)
A teardown shows you **the bill of materials (BOM)**. It does not show the costs that never reach the parts table: R&D amortisation, warranty reserves, payment terms with suppliers, capital costs, state-backed land and energy prices, or how much capacity a plant actually uses. Kahneman's System 1 builds a confident story from the evidence it has and ignores the evidence it lacks [13]. The Rhodium finding on *payment timing* [8] is exactly this kind of hidden cost: it is real money, and no teardown would ever find it.

> **Debias:** For every teardown claim, ask: *"What part of the total cost per vehicle is invisible on the bench?"*

### 2.2 Representativeness and the law of small numbers
Most conclusions rest on **one Seal (UBS, Nikkei BP)** or **one Atto 3 in a set of 16 cars (Nagoya)**. Tversky and Kahneman's "belief in the law of small numbers" [14] predicts that we treat small samples as more representative than they are. One car from one model year cannot tell us how BYD's costs vary across models, plants, years or cost-down cycles.

### 2.3 Anchoring on "25 %"
After UBS published "~25 %" [6], almost every later article repeated it. Anchoring [11] means later estimates are adjusted from that number and not rebuilt from first principles. Reported figures already range from 15 % (vs. Tesla China) to 25 % (vs. EU incumbents after tariffs) to 35 % (before tariffs) [7]. This **range** is the real finding, and quoting a single point hides it.

### 2.4 Availability and the affect heuristic
Headlines such as *"BYD teardown shocks Japan"* [3] make the story easy to recall and emotionally charged. The availability heuristic [11] and the affect heuristic [13] can push decision-makers toward panic responses, such as copying the 8-in-1 e-axle tomorrow, without checking whether that architecture suits their own volumes, supply base and regulators.

### 2.5 Loss aversion and framing
Prospect Theory [12] predicts that incumbents framed as *losing* will take more risk. That can be good, because it breaks inertia. It can also be bad, because it encourages aggressive cost-down that moves cost into **field failures**. The framing "we are 25 % behind" pushes toward risk-seeking. The framing "we can reach 90 % of their cost with 50 % of the integration risk" pushes toward measured action.

### 2.6 Narrative fallacy and the inside view
"Integration explains everything" is a clean causal story. Kahneman and Lovallo [15] showed that planners who take the **inside view**, reasoning from the specifics of their own case, routinely underestimate costs and risks. The **outside view** asks a different question: *across all the industries where a vertically integrated challenger beat modular incumbents, how long did the advantage last, and what eroded it?*

### 2.7 Survivorship bias
We tear down the *winners*. We rarely tear down the Chinese EV makers that failed despite using the same playbook: integration, in-house parts and subsidies. If dozens of firms copied BYD's model and went bankrupt, then "integration" cannot be a *sufficient* explanation.

**What this means in practice:** none of these biases proves the thesis wrong. They show where it is **over-confident**. The next step is to make it *testable*.

---

## 3. A Popperian lens: trying to falsify the claim

Karl Popper argued that a claim is scientific only if it says what evidence **would prove it wrong**, and that we gain knowledge by subjecting claims to **severe tests** and not by piling up confirmations [16][17]. A teardown supplies confirmations. Popper would ask: *what result would make you give the thesis up?*

The thesis breaks down into five **falsifiable hypotheses**:

| # | Hypothesis | What would **falsify** it | Current status (Oct 2026) |
|---|---|---|---|
| **H1** | Integration and vertical integration are the *main* cost drivers. | A non-Chinese OEM reaches comparable integration (e.g. Tesla's mega-castings and integrated drive units) and **still** shows a gap of roughly the same size, so something else must explain it. | **Partly survives, partly challenged.** UBS still finds a ~15 % gap even against Tesla China [7], and Tesla is itself highly integrated. Integration alone may not explain all of that gap. Labour, supply-base density and the cost of capital deserve more weight. |
| **H2** | Subsidies are a *minor* contributor. | Margins or volumes fall sharply when subsidies or tax exemptions are withdrawn, *beyond* what price competition explains. | **Open.** Rhodium judges subsidies small compared with structural factors [8][10]. Reports of BYD's first profit decline in four years [18] show the model is under pressure. Price war and subsidy phase-out are mixed together in that result, so the test is not clean yet. |
| **H3** | The advantage is *portable*: it survives outside China. | Vehicles built in BYD's overseas plants (Hungary, Türkiye, Brazil, Thailand) cost roughly the same as local incumbents once local labour, energy and supplier ecosystems apply. | **This is the most severe test available.** Its results will arrive as those plants reach volume. If the cost gap shrinks sharply abroad, the "structural design" story is refuted in favour of an "ecosystem/location" story. The fact that BYD is using a local assembler in Malaysia [19] is a small data point to watch. |
| **H4** | The cost advantage does **not** come at the expense of durability or safety. | Warranty claims, recalls or field failures per 1,000 vehicles are clearly higher than peers' over a 3–5-year horizon. | **Open.** It needs long-run field data (recall databases, warranty reserves in annual reports). A teardown shows the part *at time zero*. It cannot show degradation. |
| **H5** | Working-capital practices (supplier payment terms) are a *real but small* driver. | Supplier payment rules tighten and BYD's cost per vehicle rises more than about $200–300. | **Testable now** against changes in payment-term rules and BYD's reported payables days. |

### What Popper would warn against
- **Ad hoc rescue:** If H3 fails and someone says "well, the Hungarian plant is just immature," that is an *auxiliary hypothesis* added only to save the theory. It is allowed only if it makes **new, testable predictions**, for example: "costs will converge to within 10 % of China levels by 2028."
- **Unfalsifiable framing:** "China's advantage is a *system* advantage" is true but empty unless it names which parts of the system can be measured and checked.

### Verdict
The **design integration and in-house production** part of the thesis is **corroborated**: it has survived several independent tests (UBS, Nikkei, Rhodium) [2][6][8]. The **"tariffs can't close it"** and **"it's portable"** parts are **not yet severely tested**. They should be held as conjectures, not facts.

---

## 4. From insight to action: a modified DFMEA & PFMEA guideline for EV manufacturers

For engineers and quality leaders, the key question is *how do we capture the cost benefit of integration without importing new failure modes?* The standard reference is the **AIAG & VDA FMEA Handbook (2019)** [20]. It uses a 7-step approach (Planning & Preparation → Structure → Function → Failure → Risk Analysis → Optimisation → Results Documentation) and replaces RPN with **Action Priority (AP)**. Below is how I would **modify** it for highly integrated EV architectures, drawing on the teardown lessons and the bias and falsification thinking above.

### 4.1 Guiding principles

1. **Integration-aware structure analysis.** When eight functions sit in one housing, each failure has a larger *blast radius*. Model the integrated unit as a **system of coupled functions**, not as one component.
2. **"Cost-down" is an explicit failure cause.** Every removed part, thinner wall, cheaper material or merged function gets its own row: *"What did that part do that is now nobody's job?"*
3. **Falsifiable controls (Popper).** Each prevention or detection control must state the **test result that would show it does not work**. A control that cannot fail a test is not a control.
4. **Debiased ratings (Kahneman & Tversky).** Rate Occurrence from **reference-class data** (outside view), not from team intuition. Collect ratings independently *before* group discussion to reduce anchoring.
5. **Link to functional safety and the regulators.** Tie Severity 9–10 items to **ISO 26262** safety goals [21], high-voltage protection to **ISO 6469** [22], battery safety to **UN ECE R100** [23] and China's **GB 38031-2025** "no fire, no explosion" battery requirement [24], and cyber failure modes to **ISO/SAE 21434** [25].

### 4.2 Modified DFMEA (Design FMEA) guidelines

| AIAG-VDA step | Standard practice | **EV-specific modification** |
|---|---|---|
| **1. Planning** | Define scope, team, timing. | Add a **teardown benchmark input**: compare your design with a competitor's integrated design and list every function they merged. Add a **"red team" member** whose job is to argue that the design will fail. |
| **2. Structure** | System → subsystem → component tree. | Model **multi-function units** (X-in-1 e-axle, cell-to-body pack, integrated thermal module) as nodes with **shared resources**: common housing, shared coolant loop, shared PCB, shared ground. Shared resources are where **common-cause failures** occur. |
| **3. Function** | Functions and requirements per element. | For each merged function, record the **lost isolation**: thermal, EMC, galvanic, mechanical. Add requirements for **fault containment** (one function's failure must not propagate to the others). |
| **4. Failure analysis** | Failure effects, modes, causes. | Add standard **EV cause categories**: thermal runaway propagation; HV insulation breakdown; coolant ingress into power electronics; busbar fretting and vibration fatigue; SiC/IGBT thermal cycling; seal ageing in structural packs; software/OTA-induced mis-calibration; cybersecurity compromise of the BMS. Add a **"cost-down delta"** cause for each feature removed versus the previous design or benchmark. |
| **5. Risk analysis** | Severity, Occurrence, Detection → AP. | **Severity:** any credible path to fire, HV exposure or loss of propulsion at speed = 9–10, *regardless of probability*. **Occurrence:** must cite a reference-class source (field data, supplier PPM, physics-of-failure model). Gut-feel ratings are marked "unverified" and raised by one step. **Detection:** credit only tests with a defined **pass/fail criterion that could plausibly fail** (Popper rule). |
| **6. Optimisation** | Actions to reduce AP. | Prefer **design-out** (isolation barriers, fuses, thermal breaks) to detection. For integrated units, include a **service-and-repair failure mode**: a one-piece unit that must be replaced entirely changes warranty cost and the customer's experience. |
| **7. Documentation** | Report, lessons learned. | Record a **"conjecture register"**: assumptions behind ratings (e.g. "seal lasts 10 years at 45 °C") with the **field signal that would refute them** and who monitors it. |

**Example DFMEA line: integrated 8-in-1 e-axle**

| Item / function | Failure mode | Effect | S | Cause | Prevention | Detection (falsifiable) | O | D | AP |
|---|---|---|---|---|---|---|---|---|---|
| Shared coolant jacket cools motor + inverter + OBC | Coolant leaks into inverter compartment | Short circuit → loss of propulsion; possible thermal event | 10 | Gasket compression set after thermal cycling (cost-down: single gasket replaces two) | Dual-barrier seal, drain path away from HV, gasket material validated by compression-set test | 1,500-cycle thermal shock + pressure-decay test; **fail if leak > X mL/min at any check point** | 4 | 3 | **H** |

### 4.3 Modified PFMEA (Process FMEA) guidelines

Integration moves complexity *into the factory*. Fewer parts often means **larger, more critical joins and castings**.

| Process area | Typical EV failure mode | Modified PFMEA requirement |
|---|---|---|
| **Cell incoming and handling** | Cell damage, contamination, ESD | Enforce traceability for 100 % of cells (cell → module → pack → VIN). Rate Occurrence from supplier PPM data, not assumptions. |
| **Laser welding of busbars and tabs** | Lack of fusion, porosity, spatter | **In-line weld monitoring** (photodiode/OCT) with statistically validated thresholds. Detection credit requires proven ability to catch a seeded defect. |
| **Cell-to-pack / cell-to-body adhesive bonding** | Incomplete cure, voids, wrong bead geometry | Vision bead inspection, cure-time interlock, and destructive sampling at a defined frequency. Treat the pack as a **structural part**, so Severity covers crash performance as well. |
| **Large / giga-castings** | Porosity, cracks, dimensional drift | X-ray/CT sampling plan linked to die-life count, die temperature and SPC on shot parameters. Include **repairability** in the effects (crash repair of a single large casting). |
| **Electrolyte fill and formation** | Moisture ingress, under-fill, lithium plating | Dew-point interlocks, weight checks, formation-curve analytics with outlier rejection. |
| **HV connection torque and assembly** | Under/over-torque → arcing/heat | DC tools with torque-angle traces stored per VIN, and error-proofing (poka-yoke) on sequence. |
| **Thermal interface material dispensing** | Insufficient coverage → hotspot | Dispense weight/volume monitoring plus thermal imaging at end of line. |
| **End-of-line (EOL) test** | Escaped insulation fault, BMS mis-flash | Insulation resistance and hi-pot test, BMS software checksum and version check against VIN build record, cybersecurity key provisioning check. |
| **Rework of integrated assemblies** | Hidden damage introduced by rework | Separate PFMEA for **rework and repair**. Integrated units often cannot be partly reworked safely. |

**PFMEA modification checklist**
- [ ] Every Special Characteristic links back to a DFMEA line (keep DFMEA and PFMEA connected both ways).
- [ ] Detection ratings for automated inspection are backed by **seeded-defect studies** (the Popper rule applied to the factory).
- [ ] Occurrence ratings for new processes use **outside-view** data: sister plants, supplier data, published field data.
- [ ] A **pre-mortem** (imagine the launch failed a year from now and explain why) runs before AP sign-off. It is a practical counter to over-confidence and the planning fallacy [13][15][26].
- [ ] Cost-down change requests (ECNs) **automatically reopen** the affected DFMEA and PFMEA rows.

---

## 5. Key takeaways

1. **The teardown thesis is well supported but over-stated.** Integration and vertical integration are real, repeatedly corroborated drivers. Whether the advantage is *portable* abroad and *durable* over time has not yet been tested.
2. **Watch your own biases.** A vivid teardown, a sample of one car and a sticky "25 %" are textbook conditions for anchoring, WYSIATI and narrative fallacy.
3. **Make the claim falsifiable.** Track overseas plant costs, warranty and recall rates, and margins after subsidy changes. These are the severe tests.
4. **Copy integration only with an integration-aware FMEA.** Merging eight functions into one box saves money only if failures in that box stay contained. Modify your DFMEA and PFMEA so that **cost-down is a failure cause, controls are falsifiable, and ratings come from the outside view**.

*If you work in EV engineering, quality or cost analysis, I'd like to hear which of the five hypotheses you think fails first.*

---

## References

1. Phang, J. (2026, 10 Oct). *Nikkei BYD teardown: the Chinese EV cost advantage.* jamesphang.co.uk. https://www.jamesphang.co.uk/blog/2026/10/10/nikkei-byd-teardown-chinese-ev-cost-advantage
2. Nikkei Asia (2024, Oct). *EV teardown showcase reveals secrets to China's low costs.* https://asia.nikkei.com/business/automobiles/electric-vehicles/ev-teardown-showcase-reveals-secrets-to-china-s-low-costs
3. Electrek (2024, 22 Oct). *BYD electric SUV teardown shocks Japan: "How can it be produced at such a low cost?"* https://electrek.co/2024/10/22/byd-ev-teardown-shocks-japan-how-is-it-made-so-cheaply/
4. Motor Illustrated (2024). *Fewer Parts, Lower Costs: Japan's EV Teardown Sheds Light on Chinese Manufacturing.* https://motorillustrated.com/fewer-parts-lower-costs-japans-ev-teardown-sheds-light-on-chinese-manufacturing/142648/
5. Gaming Deputy (2024). *The Japanese dismantled a BYD Seal and released a book priced at 67,000.* https://www.gamingdeputy.com/the-japanese-dismantled-a-byd-seal-and-released-a-book-priced-at-67000/
6. UBS (2023). *Will Chinese electric vehicles (EVs) win globally?* (BYD Seal teardown). https://www.ubs.com/global/en/investment-bank/in-focus/2023/byd-teardown
7. Yicai Global (2023). *China's BYD Seal has 25% cost advantage over European, North American EVs, UBS report shows.* https://yicaiglobal.com/news/chinas-byd-seal-has-25-cost-advantage-over-european-north-american-evs-ubs-report-shows ; see also TechNode (2023, 6 Sept). https://technode.com/2023/09/06/byds-manufacturing-costs-in-eu-could-be-25-lower-than-rivals-ubs/
8. Rhodium Group (2026). *Why Are Chinese EVs So Cheap?* https://rhg.com/research/why-are-chinese-evs-so-cheap/
9. CNBC (2026, 6 Mar). *Western automakers outsourced supply chains for decades — now Chinese rivals have the cost edge.* https://www.cnbc.com/2026/03/06/china-ev-cost-advantage-vertical-integration-byd-tesla-rhodium-report.html
10. Rest of World (2026). *Why are Chinese EVs cheaper than Tesla?* https://restofworld.org/2026/why-are-chinese-evs-cheaper-than-tesla/
11. Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124–1131.
12. Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263–291.
13. Kahneman, D. (2011). *Thinking, Fast and Slow.* Farrar, Straus and Giroux.
14. Tversky, A., & Kahneman, D. (1971). Belief in the law of small numbers. *Psychological Bulletin*, 76(2), 105–110.
15. Kahneman, D., & Lovallo, D. (1993). Timid choices and bold forecasts: A cognitive perspective on risk taking. *Management Science*, 39(1), 17–31.
16. Popper, K. R. (1959). *The Logic of Scientific Discovery.* Hutchinson.
17. Popper, K. R. (1963). *Conjectures and Refutations: The Growth of Scientific Knowledge.* Routledge.
18. El Economista (2025). *Las ganancias de BYD cayeron por primera vez en cuatro años.* https://eleconomista.com.ar/autos/las-ganancias-byd-cayeron-primera-vez-cuatro-anos-despide-empleados-n93692/amp
19. Nikkei Asia (2026). *China's BYD turns to local assembler in Malaysia after shelving plant plan.* https://asia.nikkei.com/business/automobiles/electric-vehicles/china-s-byd-turns-to-local-assembler-in-malaysia-after-shelving-plant-plan
20. AIAG & VDA (2019). *Failure Mode and Effects Analysis — FMEA Handbook* (1st ed.). Automotive Industry Action Group / Verband der Automobilindustrie.
21. ISO 26262:2018. *Road vehicles — Functional safety.*
22. ISO 6469 (Parts 1–4). *Electrically propelled road vehicles — Safety specifications.*
23. UN ECE Regulation No. 100. *Uniform provisions concerning the approval of vehicles with regard to specific requirements for the electric power train.*
24. GB 38031-2025. *Safety requirements for power batteries for electric vehicles* (People's Republic of China).
25. ISO/SAE 21434:2021. *Road vehicles — Cybersecurity engineering.*
26. Klein, G. (2007). Performing a project premortem. *Harvard Business Review*, 85(9), 18–19.
