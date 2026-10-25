---
title: "Stress-Testing the BYD Teardown Story: Bias, Falsification and a Modified FMEA Playbook for EV Makers"
slug: byd-teardown-cost-advantage-kahneman-popper-fmea
author: Hrushaabh Mishra
date: 2026-10-25
site: hrushaabhmishrablog.com
tags: [BYD, electric vehicles, teardown, cost engineering, Kahneman, Tversky, Karl Popper, DFMEA, PFMEA, manufacturing quality]
meta_description: "Teardowns say BYD wins on cost through integration and in-house production. We test that claim with Kahneman & Tversky, try to falsify it with Popper, and turn the lessons into modified DFMEA/PFMEA guidelines for EV manufacturers."
---

# Stress-Testing the BYD Teardown Story: Bias, Falsification and a Modified FMEA Playbook for EV Makers

*By Hrushaabh Mishra · 25 October 2026 · ~15 min read*

> **TL;DR** — Teardowns of BYD vehicles keep returning the same verdict: Chinese EVs are cheaper mainly because of **part integration, vertical integration and scale**, not mainly because of subsidies or cheap labour. That claim is probably *largely right*, but the way it gets told is open to well-documented thinking errors. Below, I (1) summarise the evidence, (2) run it through Kahneman and Tversky's bias research, (3) restate it as hypotheses that could be proven wrong, in Popper's sense, and say what evidence would refute them, and (4) turn the lessons into a **modified DFMEA and PFMEA guideline** that EV manufacturers can use.

---

## 1. The claim we are testing

This piece was prompted by James Phang's post on the Nikkei BYD teardown and China's EV cost advantage [1]. The teardown story has been building since 2023: Japanese engineers, publishers, investment banks and think tanks have taken BYD cars apart, and they keep reaching a similar conclusion. Explanations still differ. In an earlier post, Phang himself named government support as likely the biggest factor in China's EV affordability, ahead of supply-chain control, scale and design choices [2]. That disagreement is the reason to test the claim and not simply repeat it.

Stated as one thesis:

> **"BYD's cost advantage is *structural*. It comes from fewer, more integrated parts, a high share of components made in-house, and scale. Subsidies and low labour costs explain only a small part of it, so Western and Japanese incumbents cannot close the gap with tariffs alone."**

What the teardown evidence says:

| Source | What it found |
|---|---|
| **Nikkei Asia, EV teardown showcase (Oct 2024)** [3] | Reported that Chinese EV makers keep production costs down "by integrating multiple components into one part and maximizing in-house production, as well as standardizing parts across multiple vehicle models." The event was held in Gifu Prefecture, central Japan, and organised by the regional economy and trade bureau. |
| **Electrek and InsideEVs coverage of the same event** [4][5] | About **70 Japanese auto-parts companies** attended, and more than **90,000 parts from 16 foreign EVs** were on display, including the BYD Atto 3. Attendees asked: *"How can it be produced at such a low cost?"* The Atto 3's "E-Axle" combines **eight components** (including the motor, inverter, transmission, controller, onboard charger, DC-DC converter and battery monitoring system) in one unit. |
| **Motor Illustrated** [6] | A Japanese supplier manager was reportedly surprised by how simple the vehicles were, with significantly fewer parts in some models than in traditional designs. |
| **Nikkei BP, *China BYD "SEAL" Complete Teardown* (Sept 2023)** [7] | A professional teardown report on the BYD Seal, priced at **¥880,000 (book only, tax included)**. That price shows how much Japanese industry values this benchmarking. |
| **UBS Evidence Lab, BYD Seal teardown (Sept 2023)** [8][9][10] | About **75 % of components made in-house**, from batteries to power semiconductors. The Seal is about **15 % cheaper to build than a Shanghai-built Tesla Model 3**. UBS estimated a **~25 % cost advantage** over European-built rivals even if BYD built the car locally in Europe [9]. Other coverage of the same report quoted **~30 %** against Western incumbents [10]. |
| **Rhodium Group, "Why Are Chinese EVs So Cheap?" (Feb 2026)** [11][12][13] | Rhodium found that structural advantages (vertical integration, scale and lower overheads including R&D) drive the gap. Press coverage reports a per-vehicle cost advantage of roughly **$4,700 for BYD versus Tesla**, nearly **80 %** of BYD's core components made in-house, subsidies accounting for **only about 5 %** of that gap, and about **$214/vehicle** from delayed payments to suppliers [12][13]. |

The story is consistent across these sources, and it is persuasive. That is the reason to test it carefully.

---

## 2. A Kahneman & Tversky lens: how this story could mislead us

Daniel Kahneman and Amos Tversky showed that intuitive judgement relies on **heuristics** (representativeness, availability, anchoring), mental shortcuts that are usually useful but cause "systematic and predictable errors" [17][18][19]. Teardown narratives are especially exposed to these errors because they are vivid, visual and easy to tell as a story.

### 2.1 "What you see is all there is" (WYSIATI)
A teardown shows you **the bill of materials (BOM)**. It does not show the costs that never reach the parts table: R&D amortisation, warranty reserves, payment terms with suppliers, capital costs, state-backed land and energy prices, or how much capacity a plant actually uses. Kahneman's System 1 builds a confident story from the evidence it has and ignores the evidence it lacks [19]. Rhodium's estimate of the benefit from *supplier payment timing* [12] is exactly this kind of hidden cost: it is real money, and no teardown would ever find it.

> **Debias:** For every teardown claim, ask: *"What part of the total cost per vehicle is invisible on the bench?"*

### 2.2 Representativeness and the law of small numbers
The best-known cost conclusions rest on **one Seal (UBS, Nikkei BP)** or **one Atto 3 among 16 cars on display**. Tversky and Kahneman's "belief in the law of small numbers" [20] describes our tendency to treat a small sample as highly representative of the whole population. One car from one model year cannot tell us how BYD's costs vary across models, plants, years or cost-down cycles.

### 2.3 Anchoring on "25 %"
After UBS published its estimate, "25 %" became the number most articles repeated. Anchoring [17] means later estimates are adjusted from that number and not rebuilt from first principles. Yet even coverage of *the same report* gives a range: 15 % (against a Shanghai-built Model 3) [10], 25 % (against European-built rivals) [9] and 30 % (against Western incumbents) [10]. This **range** is the real finding, and quoting a single point hides it.

### 2.4 Availability and the affect heuristic
Headlines such as *"BYD electric SUV teardown shocks Japan"* [4] make the story easy to recall and emotionally charged. The availability heuristic [17] and the affect heuristic [19] can push decision-makers toward panic responses, such as copying the 8-in-1 e-axle tomorrow, without checking whether that architecture suits their own volumes, supply base and regulators.

### 2.5 Loss aversion and framing
Prospect Theory [18] predicts that people evaluate outcomes against a reference point and become risk-seeking when they are framed as *losing*. For incumbents, that can be good, because it breaks inertia. It can also be bad, because it encourages aggressive cost-down that moves cost into **field failures**. The framing "we are 25 % behind" pushes toward risk-seeking. The framing "we can reach 90 % of their cost with half of the integration risk" pushes toward measured action.

### 2.6 Narrative fallacy and the inside view
"Integration explains everything" is a clean causal story. Kahneman and Lovallo [21] showed that overly optimistic forecasts come from the **inside view**: reasoning from plans and scenarios specific to your own case while neglecting the statistics of the past. The **outside view** asks a different question: *across all the industries where a vertically integrated challenger beat modular incumbents, how long did the advantage last, and what eroded it?*

### 2.7 Survivorship bias
We tear down the *winners*. We rarely tear down the Chinese EV makers that failed despite using the same playbook: integration, in-house parts and subsidies. If many firms copied the model and still failed, then "integration" cannot be a *sufficient* explanation.

**What this means in practice:** none of these biases proves the thesis wrong. They show where it is **over-confident**. The next step is to make it *testable*.

---

## 3. A Popperian lens: trying to falsify the claim

Karl Popper argued that a claim is scientific only if it says what evidence **would prove it wrong**, and that we gain knowledge by subjecting claims to **severe tests** and not by piling up confirmations [22][23]. A teardown supplies confirmations. Popper would ask: *what result would make you give the thesis up?*

The thesis breaks down into five **falsifiable hypotheses**:

| # | Hypothesis | What would **falsify** it | Current status (Oct 2026) |
|---|---|---|---|
| **H1** | Integration and vertical integration are the *main* cost drivers. | A non-Chinese OEM reaches comparable integration and **still** shows a gap of roughly the same size, so something else must explain it. | **Partly survives, partly challenged.** UBS still finds a ~15 % gap even against a Shanghai-built Model 3 [10]. That car uses a Chinese supply base and is itself fairly integrated, so integration alone may not explain all of the gap. Rhodium also points to scale and lower overheads such as R&D [11][12]. |
| **H2** | Subsidies are a *minor* contributor. | Margins or volumes fall sharply when subsidies or tax exemptions are withdrawn, *beyond* what price competition explains. | **Open.** Rhodium puts subsidies at about 5 % of BYD's gap with Tesla [12][13]. Phang's earlier view [2] gives them much more weight. BYD's 2025 net profit fell about 19 %, its first annual decline in four years, which coverage attributes to fierce domestic competition [14]. Price war and policy changes are mixed together in that result, so the test is not clean yet. |
| **H3** | The advantage is *portable*: it survives outside China. | Vehicles assembled outside China cost roughly the same as local incumbents once local labour, energy, rules and supplier ecosystems apply. | **This is the most severe test available, and the evidence is still arriving.** In Malaysia, BYD shelved plans for its own plant and turned to a local contract assembler (Inokom) for completely-knocked-down (CKD) assembly [15][16]. This shows that local rules and partner economics shape the overseas cost model. If the cost gap shrinks sharply abroad, the "structural design" story gives way to an "ecosystem/location" story. |
| **H4** | The cost advantage does **not** come at the expense of durability or safety. | Warranty claims, recalls or field failures per 1,000 vehicles are clearly higher than peers' over a 3–5-year horizon. | **Open, with an early warning sign.** Brazilian coverage of the Japanese teardown reports that attendees judged the Atto 3 battery's water protection insufficient, and that the event organiser said Chinese makers put low production cost ahead of Japanese quality norms [5a]. A teardown shows the part *at time zero*. Only long-run field data (recalls, warranty reserves) can show how it ages. |
| **H5** | Working-capital practices (supplier payment terms) are a *real but small* driver. | Supplier payment practices tighten and BYD's cost per vehicle rises more than about $200–300. | **Testable now.** Rhodium's estimate is about $214/vehicle for BYD [12]. Track BYD's reported payables days against its cost per vehicle. |

### What Popper would warn against
- **Ad hoc rescue:** If H3 fails and someone says "well, the overseas plants are just immature," that is an *auxiliary hypothesis* added only to save the theory. It is allowed only if it makes **new, testable predictions**, for example: "overseas costs will converge to within 10 % of China levels by 2028."
- **Unfalsifiable framing:** "China's advantage is a *system* advantage" is true but empty unless it names which parts of the system can be measured and checked.

### Verdict
The **design integration and in-house production** part of the thesis is **corroborated**: it has survived several independent checks (UBS, the Japanese teardown event, Rhodium) [3][8][11]. The **"tariffs can't close it"** and **"it's portable"** parts are **not yet severely tested**. They should be held as conjectures, not facts.

---

## 4. From insight to action: a modified DFMEA & PFMEA guideline for EV manufacturers

For engineers and quality leaders, the key question is *how do we capture the cost benefit of integration without importing new failure modes?* The standard reference is the **AIAG & VDA FMEA Handbook** (1st edition, 2019) [25]. It uses a 7-step approach (Planning & Preparation → Structure Analysis → Function Analysis → Failure Analysis → Risk Analysis → Optimisation → Results Documentation) and introduces **Action Priority (AP)** in place of the traditional RPN. Below is how I would **modify** it for highly integrated EV architectures, drawing on the teardown lessons and the bias and falsification thinking above.

### 4.1 Guiding principles

1. **Integration-aware structure analysis.** When eight components sit in one housing, each failure has a larger *blast radius*. Model the integrated unit as a **system of coupled functions**, not as one component.
2. **"Cost-down" is an explicit failure cause.** Every removed part, thinner wall, cheaper material or merged function gets its own row: *"What did that part do that is now nobody's job?"*
3. **Falsifiable controls (Popper).** Each prevention or detection control must state the **test result that would show it does not work**. A control that cannot fail a test is not a control.
4. **Debiased ratings (Kahneman & Tversky).** Rate Occurrence from **reference-class data** (outside view), not from team intuition. Collect ratings independently *before* group discussion to reduce anchoring.
5. **Link to functional safety and the regulators.** Tie Severity 9–10 items to **ISO 26262** safety goals [26], high-voltage protection to the **ISO 6469** series [27], battery safety to **UN Regulation No. 100** [28] and China's **GB 38031-2025**, which applies from 1 July 2026 and requires batteries not to catch fire or explode after thermal runaway [29], and cyber failure modes to **ISO/SAE 21434** [30].

### 4.2 Modified DFMEA (Design FMEA) guidelines

| AIAG-VDA step | Standard practice | **EV-specific modification** |
|---|---|---|
| **1. Planning** | Define scope, team, timing. | Add a **teardown benchmark input**: compare your design with a competitor's integrated design and list every function they merged. Add a **"red team" member** whose job is to argue that the design will fail. |
| **2. Structure** | System → subsystem → component tree. | Model **multi-function units** (X-in-1 e-axle, cell-to-body pack, integrated thermal module) as nodes with **shared resources**: common housing, shared coolant loop, shared PCB, shared ground. Shared resources are where **common-cause failures** occur. |
| **3. Function** | Functions and requirements per element. | For each merged function, record the **lost isolation**: thermal, EMC, galvanic, mechanical. Add requirements for **fault containment** (one function's failure must not propagate to the others). |
| **4. Failure analysis** | Failure effects, modes, causes. | Add standard **EV cause categories**: thermal runaway propagation; HV insulation breakdown; water or coolant ingress into power electronics and packs; busbar fretting and vibration fatigue; power-semiconductor thermal cycling; seal ageing in structural packs; software/OTA-induced mis-calibration; cybersecurity compromise of the BMS. Add a **"cost-down delta"** cause for each feature removed versus the previous design or benchmark. |
| **5. Risk analysis** | Severity, Occurrence, Detection → AP. | **Severity:** any credible path to fire, HV exposure or loss of propulsion at speed = 9–10, *regardless of probability*. **Occurrence:** must cite a reference-class source (field data, supplier PPM, physics-of-failure model). Gut-feel ratings are marked "unverified" and raised by one step. **Detection:** credit only tests with a defined **pass/fail criterion that could plausibly fail** (Popper rule). |
| **6. Optimisation** | Actions to reduce AP. | Prefer **design-out** (isolation barriers, fuses, thermal breaks) to detection. For integrated units, include a **service-and-repair failure mode**: a one-piece unit that must be replaced entirely changes warranty cost and the customer's experience. |
| **7. Documentation** | Report, lessons learned. | Record a **"conjecture register"**: assumptions behind ratings (e.g. "seal lasts 10 years at 45 °C") with the **field signal that would refute them** and who monitors it. |

**Example DFMEA line: integrated 8-in-1 e-axle** *(illustrative ratings)*

| Item / function | Failure mode | Effect | S | Cause | Prevention | Detection (falsifiable) | O | D | AP |
|---|---|---|---|---|---|---|---|---|---|
| Shared coolant jacket cools motor + inverter + OBC | Coolant leaks into inverter compartment | Short circuit → loss of propulsion; possible thermal event | 10 | Gasket compression set after thermal cycling (cost-down: single gasket replaces two) | Dual-barrier seal, drain path away from HV, gasket material validated by compression-set test | Thermal-shock cycling + pressure-decay test; **fail if leak rate exceeds the specified limit at any check point** | 4 | 3 | **H** |

### 4.3 Modified PFMEA (Process FMEA) guidelines

Integration moves complexity *into the factory*. Fewer parts often means **larger, more critical joins and castings**.

| Process area | Typical EV failure mode | Modified PFMEA requirement |
|---|---|---|
| **Cell incoming and handling** | Cell damage, contamination, ESD | Enforce traceability for 100 % of cells (cell → module → pack → VIN). Rate Occurrence from supplier PPM data, not assumptions. |
| **Laser welding of busbars and tabs** | Lack of fusion, porosity, spatter | **In-line weld monitoring** with statistically validated thresholds. Detection credit requires proven ability to catch a seeded defect. |
| **Cell-to-pack / cell-to-body adhesive bonding and sealing** | Incomplete cure, voids, wrong bead geometry, water-ingress paths | Vision bead inspection, cure-time interlock, pack-level leak test, and destructive sampling at a defined frequency. Treat the pack as a **structural part**, so Severity covers crash performance as well. |
| **Large / giga-castings** | Porosity, cracks, dimensional drift | X-ray/CT sampling plan linked to die-life count, die temperature and SPC on shot parameters. Include **repairability** in the effects (crash repair of a single large casting). |
| **Electrolyte fill and formation** | Moisture ingress, under-fill, lithium plating | Dew-point interlocks, weight checks, formation-curve analytics with outlier rejection. |
| **HV connection torque and assembly** | Under/over-torque → arcing/heat | DC tools with torque-angle traces stored per VIN, and error-proofing (poka-yoke) on sequence. |
| **Thermal interface material dispensing** | Insufficient coverage → hotspot | Dispense weight/volume monitoring plus thermal imaging at end of line. |
| **End-of-line (EOL) test** | Escaped insulation fault, BMS mis-flash | Insulation-resistance and hi-pot test, BMS software checksum and version check against VIN build record, cybersecurity key provisioning check. |
| **Rework of integrated assemblies** | Hidden damage introduced by rework | Separate PFMEA for **rework and repair**. Integrated units often cannot be partly reworked safely. |

**PFMEA modification checklist**
- [ ] Every Special Characteristic links back to a DFMEA line (keep DFMEA and PFMEA connected both ways).
- [ ] Detection ratings for automated inspection are backed by **seeded-defect studies** (the Popper rule applied to the factory).
- [ ] Occurrence ratings for new processes use **outside-view** data: sister plants, supplier data, published field data.
- [ ] A **pre-mortem** (imagine the launch has already failed and explain why) runs before AP sign-off. It is a practical counter to over-confidence and the planning fallacy [19][21][24].
- [ ] Cost-down change requests (ECNs) **automatically reopen** the affected DFMEA and PFMEA rows.

---

## 5. Key takeaways

1. **The teardown thesis is well supported but over-stated.** Integration and vertical integration are real, repeatedly corroborated drivers. Whether the advantage is *portable* abroad and *durable* over time has not yet been tested.
2. **Watch your own biases.** A vivid teardown, a sample of one car and a sticky "25 %" are textbook conditions for anchoring, WYSIATI and narrative fallacy.
3. **Make the claim falsifiable.** Track overseas assembly costs, warranty and recall rates, and margins after policy changes. These are the severe tests.
4. **Copy integration only with an integration-aware FMEA.** Merging eight components into one box saves money only if failures in that box stay contained. Modify your DFMEA and PFMEA so that **cost-down is a failure cause, controls are falsifiable, and ratings come from the outside view**.

*If you work in EV engineering, quality or cost analysis, I'd like to hear which of the five hypotheses you think fails first.*

---

## References

**Source post and teardown evidence**

1. Phang, J. (2026, 10 October). *Nikkei BYD teardown: Chinese EV cost advantage.* jamesphang.co.uk. https://www.jamesphang.co.uk/blog/2026/10/10/nikkei-byd-teardown-chinese-ev-cost-advantage
2. Phang, J. (2025, 11 May). *The Global Race for EV Dominance: How China is Driving Affordability.* jamesphang.co.uk. https://www.jamesphang.co.uk/blog/2025/5/11/the-global-race-for-ev-dominance-how-china-is-driving-affordability
3. Nikkei Asia (2024, October). *EV teardown showcase reveals secrets to China's low costs.* https://asia.nikkei.com/business/automobiles/electric-vehicles/ev-teardown-showcase-reveals-secrets-to-china-s-low-costs
4. Electrek (2024, 22 October). *BYD electric SUV teardown shocks Japan: "How can it be produced at such a low cost?"* https://electrek.co/2024/10/22/byd-ev-teardown-shocks-japan-how-is-it-made-so-cheaply/
5. InsideEVs (2024). *BYD EV Teardown In Japan Reveals The Secret To Its Affordability.* https://insideevs.com/news/738606/byd-ev-teardown-impresses-japan/
   5a. AutoPapo (2024). *Japoneses desmontam carros elétricos chineses para descobrirem o motivo de serem tão baratos* [in Portuguese]. https://autopapo.com.br/noticia/carros-eletricos-chineses-desmontados-japao/
6. Motor Illustrated (2024). *Fewer Parts, Lower Costs: Japan's EV Teardown Sheds Light on Chinese Manufacturing.* https://motorillustrated.com/fewer-parts-lower-costs-japans-ev-teardown-sheds-light-on-chinese-manufacturing/142648/
7. Nikkei BP (2023, September). *中国BYD「SEAL（海豹）」徹底分解［全体編］* [China BYD "SEAL" complete teardown — overall edition]. ISBN 978-4-296-20229-4. https://project.nikkeibp.co.jp/mirai/byd_seal/all/ ; shop listing: https://shop.nikkeibp.co.jp/front/commodity/0000/288240/

**Cost analyses**

8. UBS (2023). *Will Chinese electric vehicles (EVs) win globally?* (BYD Seal teardown). https://www.ubs.com/global/en/investment-bank/in-focus/2023/byd-teardown
9. TechNode (2023, 6 September). *BYD production costs in EU could be 25% lower than rivals: UBS.* https://technode.com/2023/09/06/byds-manufacturing-costs-in-eu-could-be-25-lower-than-rivals-ubs/
10. Winton, N. (2023, 5 September). *BYD Introduces Seal In Munich, Said To Have A 15% Price Edge Over Tesla.* Forbes. https://www.forbes.com/sites/neilwinton/2023/09/05/byd-introduces-seal-in-munich-said-to-have-a-15-price-edge-over-tesla/
11. Rhodium Group (2026, February). *Why Are Chinese EVs So Cheap?* https://rhg.com/research/why-are-chinese-evs-so-cheap/
12. CNBC (2026, 6 March). *Here's the real reason why Chinese EVs are undercutting Western rivals.* https://www.cnbc.com/2026/03/06/china-ev-cost-advantage-vertical-integration-byd-tesla-rhodium-report.html
13. Rest of World (2026). *Why Chinese EVs are cheaper than Tesla and it's not subsidies.* https://restofworld.org/2026/why-are-chinese-evs-cheaper-than-tesla/

**BYD performance and overseas operations**

14. El Economista (2026, 30 March). *Las ganancias de BYD cayeron por primera vez en cuatro años* [in Spanish]. https://eleconomista.com.ar/autos/las-ganancias-byd-cayeron-primera-vez-cuatro-anos-despide-empleados-n93692
15. Nikkei Asia (2026). *China's BYD turns to local assembler in Malaysia after shelving plant plan.* https://asia.nikkei.com/business/automobiles/electric-vehicles/china-s-byd-turns-to-local-assembler-in-malaysia-after-shelving-plant-plan
16. CnEVPost (2026, 16 October). *BYD picks CKD assembly partner in Malaysia.* https://cnevpost.com/2026/10/16/byd-picks-ckd-assembly-partner-malaysia/

**Behavioural science and philosophy of science**

17. Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124–1131. https://pubmed.ncbi.nlm.nih.gov/17835457/
18. Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263–291.
19. Kahneman, D. (2011). *Thinking, Fast and Slow.* New York: Farrar, Straus and Giroux. ISBN 978-0-374-27563-1.
20. Tversky, A., & Kahneman, D. (1971). Belief in the law of small numbers. *Psychological Bulletin*, 76(2), 105–110.
21. Kahneman, D., & Lovallo, D. (1993). Timid choices and bold forecasts: A cognitive perspective on risk taking. *Management Science*, 39(1), 17–31. https://doi.org/10.1287/mnsc.39.1.17
22. Popper, K. R. (1959). *The Logic of Scientific Discovery.* London: Hutchinson. (English edition of *Logik der Forschung*, 1934.)
23. Popper, K. R. (1963). *Conjectures and Refutations: The Growth of Scientific Knowledge.* London: Routledge & Kegan Paul.
24. Klein, G. (2007). Performing a project premortem. *Harvard Business Review*, 85(9), 18–19. https://hbr.org/2007/09/performing-a-project-premortem

**Engineering standards**

25. AIAG & VDA (2019). *FMEA Handbook* (1st ed.). Automotive Industry Action Group / Verband der Automobilindustrie.
26. ISO 26262:2018 (2nd ed.). *Road vehicles — Functional safety.* https://www.iso.org/standard/68383.html
27. ISO 6469 series (Parts 1–4). *Electrically propelled road vehicles — Safety specifications.* International Organization for Standardization.
28. UNECE Regulation No. 100. *Uniform provisions concerning the approval of vehicles with regard to specific requirements for the electric power train.* Overview of Revision 3: TÜV SÜD, *New mandatory safety testing requirements for electric vehicle batteries under R100.* https://www.tuvsud.com/en-gb/resource-centre/white-papers/new-mandatory-safety-testing-requirements-for-electric-vehicle-batteries-under-r100
29. GB 38031-2025. *Safety requirements for power batteries used in electric vehicles* (PRC national standard, applies from 1 July 2026). See CnEVPost (2026, 30 June), *China's toughest battery safety rules take effect in July.* https://cnevpost.com/2026/06/30/china-toughest-battery-safety-rules-take-effect-july
30. ISO/SAE 21434:2021 (1st ed., August 2021). *Road vehicles — Cybersecurity engineering.* https://saemobilus.sae.org/standards/isosae21434-road-vehicles-cybersecurity-engineering
