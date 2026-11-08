# BESS Implementation: Exposure-to-Failure Assessment, India and Global

### Version 2: through the lenses of Kahneman & Tversky (judgement under uncertainty) and Popper (falsifiability)

**Prepared by:** Syselec Technologies, BESS Advisory
**Date:** November 2026
**Evidence base:**
- IESA *India ESS Market Update, September 2026* (data to 1 October 2026)
- EPRI BESS Failure Incident Database and the 2026 white paper *Risk Factors and Failure Statistics of Lithium-Ion BESS*
- IEEFA–JMK Research on Indian BESS tariff viability
- Public reporting on major incidents (sources are listed at the end)

---

## 0. Why this assessment uses two thinking frameworks

Most BESS risk assessments ask *"What could go wrong?"* and then score risks by intuition. That approach has two known weaknesses:

1. **Intuitive judgement is systematically biased.** Daniel Kahneman and Amos Tversky showed that experts, investors and regulators make predictable errors under uncertainty:
   - overconfidence
   - the planning fallacy
   - anchoring
   - the availability heuristic
   - neglecting base rates
   - loss-averse, risk-seeking behaviour after losses

   BESS bidding in India in 2025–26 shows almost every one of them.
2. **Most risk claims cannot be tested.** Karl Popper argued that a claim is useful only if it says what evidence would prove it wrong. "BESS is safe" or "tariffs are viable" are often stated so that no outcome could contradict them. A Popperian assessment states **falsifiable conjectures**, **severe tests** and **refutation criteria**, and then corrects itself when the evidence goes against it.

**How each lens is applied in this document**

| Lens | Tool | Where it appears |
|---|---|---|
| Kahneman & Tversky | **Outside view / reference-class forecasting.** Start from base rates, not the project's own story | Section 2 |
| Kahneman & Tversky | **Bias map.** Which biases affect which actors, and the failures they produce | Section 3 |
| Kahneman & Tversky | **Pre-mortem.** "It is 2029 and it failed. Why?" | Section 4 |
| Kahneman & Tversky | **Calibration and noise reduction.** Probability ranges instead of false precision; structured, independent scoring | Section 5 |
| Popper | **Falsifiable conjectures**, each with a test, a threshold and a deadline | Section 6 |
| Popper | **Asymmetry of evidence.** Many successes cannot prove safety; one failure can disprove it. Absence of evidence is not evidence of absence | Sections 2.3 and 7 |
| Popper | **Against historicism.** Trends such as "cell prices always fall" are not laws | Section 3 |
| Popper | **Piecemeal engineering and error correction.** Staged commitment, kill criteria, learning loops | Section 8 |
| Both | **Self-critique.** Errors this framework exposed in our own first version | Section 1.2 |

---

## 1. Executive summary

### 1.1 Revised verdict

| | India | Global |
|---|---|---|
| **Overall exposure** | **High.** Commercial failure is very likely for part of the pipeline | **Medium** |
| **Commercial failure** (cancelled, never financed, renegotiated) | **Very high.** In mature tender cohorts, *more than half* of tenders ended in cancellation | Medium. Merchant revenue erosion is the main channel |
| **Safety failure** | **Unknown, and should be planned as Medium–High.** India has too few operating years for its clean record to mean anything. At global rates, India should expect several incidents a year by 2028 | **Low and falling** (−98% per GWh since 2018), but **fat-tailed**: one major event can halt a market |
| **Performance failure** | Medium–High (heat, dust, new O&M teams, untested guarantees) | Medium |
| **Most dangerous dynamic** | **Commercial stress turns into safety risk.** Under-priced projects are pushed to cut quality, and quality failures (integration and construction) are the main source of fires worldwide | Regulatory overreaction after a vivid incident |

### 1.2 What the two lenses changed from Version 1 (error correction)

| Version 1 claim | Problem exposed | Version 2 correction |
|---|---|---|
| "About 19% of tendered ESS capacity has been cancelled" | **What-you-see-is-all-there-is and right-censoring.** Recent tenders have not had time to fail, so the headline rate averages young and old cohorts and understates the true rate | Cohorts old enough to have resolved show **~54% of tenders cancelled** (27 of 50 tenders from 2018–2023). In the 2023 cohort, **~85% of capacity (34 of 40 GWh)** was cancelled. Use the mature-cohort rate as the outside-view anchor, adjusted for a maturing market |
| "Safety exposure in India: Medium" | **Popper's asymmetry.** India's record of no grid-scale BESS fire comes from only ~5 GWh-years of operation, where the global rate predicts only ~0.2–1.1 incidents. A zero is uninformative | Safety exposure is **unknown, so treat it as Medium–High** until India accumulates enough operating years to test the claim (Conjecture C4) |
| Single-point risk scores, e.g. "16/25" | **Overconfidence and noise.** Point scores imply precision we do not have | **Probability ranges over 2027–2029** with an explicit test that would refute each one (Section 5) |
| Risks listed as independent | **Missing causal structure.** Bias-driven under-pricing increases construction and safety risk | A **causal chain** (Section 3.2) links commercial and technical failure |
| Fire treated as the main global tail risk | **The availability heuristic** affects public reaction too | **Regulatory and social overreaction** to one vivid incident is added as a systemic tail risk (South Korea, 2017–2019 precedent) |

### 1.3 Five headline conclusions

1. **Start from base rates, not narratives.** In India, the reference class "storage tender issued" has historically ended in cancellation more often than in operation. Every new bid should be assumed to face a **25–50% chance of not reaching COD on its original terms** unless shown otherwise.
2. **Indian bidders have anchored on trends, not on costs.** IESA's own headline says standalone tariffs fell "riding on the anticipation that cell costs will keep dropping". Tariffs fell ~71% while pack prices fell only ~36% (IEEFA–JMK). This is extrapolation of a trend as if it were a law, which Popper calls historicism.
3. **Expect gambling for resurrection.** Prospect theory predicts that bidders now "in the loss domain" because cell prices rose (reportedly about +32% from January to July 2026; unverified) will become **risk-seeking**. They will delay, renegotiate and cut costs rather than exit cleanly. That increases quality and safety exposure in 2027–2028.
4. **The safety claim has not yet been tested in India.** At EPRI's 2025 global rate, a fleet of 40–90 GWh in 2027–2028 implies **roughly 2–4 incidents across those two years**. At the 2018–2025 aggregate rate, it implies **~12–22**. Planning for zero is a Popperian error.
5. **Globally, the averages are reassuring but the tail is not.** Failure rates per GWh fell 98%, yet Moss Landing (January 2025, cause still unconfirmed, re-ignition in September 2026) shows that rare events dominate consequences: permitting, insurance and public consent.

---

## 2. The outside view: reference classes and base rates

Kahneman's core advice for forecasting projects is to ignore the inside story ("our project is different") until you have anchored on how similar projects actually turned out.

### 2.1 Reference class 1: Indian storage tenders, by cohort (IESA tracker)

| Tender cohort | Tenders | Cancelled | Operational | Capacity notes | Status |
|---|:-:|:-:|:-:|---|---|
| 2018–2022 | 26 | **14 (54%)** | 8 (31%) | Small, early projects | **Mature.** Outcomes largely known |
| 2023 | 24 | **13 (54%)** | Few | **~34 of 40 GWh cancelled (~85%)** | **Mature** |
| 2024 | 36 | 8 (22%) so far | 1 | 75 GWh; most under construction | Partly resolved |
| 2025 | 69 | 6 (9%) so far | — | 105 GWh; many awarded or open | **Immature, so rate understated** |
| 2026 | 60 | 0 so far | 1 | 80 GWh; mostly open | **Immature, so rate meaningless** |
| **All (2018–2026)** | **215** | **41 (19%)** | **18 (8%)** | **308 GWh; 59 GWh cancelled** | **Mixed ages, so biased low** |

**Outside-view reading**
- **Naive base rate:** 19% cancelled. **Mature-cohort base rate:** about 54% of tenders.
- The market has matured since 2023, with VGF, standard BESPAs and experienced bidders, so the 2024–2026 cohorts should do better than 54%. The *inside-view* adjustment should still be modest, because the 2025–26 cohorts carry a new stress (bids below cost) that earlier cohorts did not.
- **Our calibrated anchor:** **25–40% of 2024–2026 tendered capacity will be cancelled, re-tendered or materially renegotiated by end-2029.** This is tested in Conjecture C1.
- Caveat: early cohorts include pumped storage, FDRE and technology-agnostic tenders that differ from standalone BESS. BESS-only cancellation to date is ~14% of capacity (24 of 167 GWh), but it is right-censored in the same way.

### 2.2 Reference class 2: global safety incident rates (EPRI)

| Metric | Value |
|---|---|
| Failure rate per GWh deployed, 2018 to 2025 | **−98%** |
| 2025 rate | **0.04 incidents per GWh** (24 incidents, 634 GWh cumulative) |
| 2018–2025 aggregate rate | **2.087 × 10⁻⁴ incidents per MWh-year** (≈ 0.21 per GWh-year) |
| Origin of root causes (where known) | Mostly **integration, assembly and construction**, plus balance of system and controls; not cell defects |
| Reporting caveat | ~22% of incidents in the database were confirmed only privately. Root cause was public for just 26 of 81 incidents in the earlier study |

### 2.3 Applying the base rate to India: what the zero means

India's operating fleet grew from 0.8 GWh (December 2025) to 13.7 GWh (September 2026). Adding up the monthly installed capacity from IESA gives **about 5 GWh-years of cumulative operation**.

| Rate assumed | Incidents expected over India's history to date | Probability of seeing zero |
|---|:-:|:-:|
| EPRI 2025 rate (0.04 per GWh-year) | ~0.2 | ~80% |
| EPRI 2018–2025 aggregate (0.21 per GWh-year) | ~1.1 | ~33% |

**Popperian conclusion:** India's clean record **cannot distinguish** "Indian projects are as safe as best global practice" from "Indian projects are as risky as the early global fleet". The claim has simply not yet been tested.

**Forward view for 2027–2028.** If India's operating fleet grows to 40–90 GWh, it will accumulate about **57–105 GWh-years**:

| Rate assumed | Expected incidents, 2027–2028 |
|---|:-:|
| Mature global rate (0.04) | **~2–4** |
| Aggregate global rate (0.21) | **~12–22** |

India's profile points toward the upper half of that range rather than the mature rate: new integrators, first-time EPCs, desert heat, and cost pressure from low bids. **Stakeholders should plan emergency response, insurance and communications for several incidents a year, not for zero.**

### 2.4 Reference class 3: modular infrastructure delivery

Bent Flyvbjerg's research on large projects, which applies Kahneman's outside view, finds that **modular, repeatable projects** (solar, wind, transmission) have much smaller cost and schedule overruns than bespoke megaprojects. BESS is highly modular, which is good news. It suggests India's main exposure is **not construction overrun as such** but **commercial terms set before construction**. This matches IEEFA–JMK's expectation of 9–18-month delays, which are driven mainly by financing and PSA problems rather than build complexity.

---

## 3. Bias map: how predictable judgement errors create failure

### 3.1 Who is biased, how, and what it produces

| Actor | Bias (Kahneman & Tversky) | How it shows up in BESS (evidence) | Failure it produces | Debiasing remedy |
|---|---|---|---|---|
| **Bidders / developers** | **Anchoring** | Each auction's L1 tariff becomes the anchor for the next. Standalone 2-hour tariffs slid to INR 1.48–2.4 lakh/MW/month across 2025–26 tenders (IESA) | Bids anchored to rivals' prices, not to own cost | Build bids bottom-up from cost before seeing market L1s, then compare |
| | **Representativeness / trend extrapolation** (Popper: historicism) | "Cell costs will keep dropping" (IESA headline). Tariffs fell 71% vs packs 36% (IEEFA–JMK) | Under-priced 12-year contracts that turn loss-making when cells rise | Treat cost trends as conjectures; stress-test with **+30% cell price** and flat prices |
| | **Overconfidence and the planning fallacy** | Commissioning timelines assume best case; IEEFA–JMK expect 9–18-month delays | LDs, VGF timing loss, missed CODs | Reference-class schedule: add P50 slippage of 9 months to every plan |
| | **Winner's curse** (Thaler, building on K&T) | Many first-time winners; lenders expect 15–20% IRR that low bids cannot deliver | Failure to reach financial close; contract termination (G R Infra, 400 MWh NTPC) | Bid at the price where *you* still clear the lender's IRR, not where you win |
| | **Loss aversion and risk-seeking after losses** (prospect theory) | After cell prices rose, winners are "in losses" relative to their bid reference point | Delay, renegotiation, value engineering, **quality cutting** instead of a clean exit | Pre-agreed **kill criteria** set before award; independent owner's engineer |
| | **Sunk-cost escalation** | Bank guarantees and bid security already committed | Continuing doomed projects | Decide on forward-looking value only; quantify the cost of exiting |
| **Lenders and investors** | **What-you-see-is-all-there-is** | Credit models built on the project's own model with no base-rate overlay | Mispriced risk; sudden withdrawal later | Require reference-class adjustments and independent technical due diligence |
| **OEMs and integrators** | **Optimism bias** | Warranty curves assume ideal thermal conditions | Degradation disputes at 45–50°C sites | Site-specific degradation tests; warranties that account for temperature |
| **Regulators and procurers** | **Certainty effect** | Preference for fixed tariffs, set by L1 discovery regardless of viability | Awarding to non-viable bids; later cancellations | Benchmark-based rejection of abnormally low bids (CTUIL's INR 0.8 Cr/MWh is a start) |
| | **Availability cascade** (Kuran & Sunstein, discussed by Kahneman) | South Korea 2017–2019: a run of fires led to market-wide shutdown and investigation | **Moratorium** after one vivid Indian incident, hurting good projects too | Prepare incident-response protocols and transparent reporting *before* the first event |
| **Public and local authorities** | **Availability heuristic and probability weighting** | Moss Landing coverage strongly shapes perceived risk, despite the 0.04/GWh base rate | Permit refusals, setback demands, higher insurance premiums | Communicate base rates; show credible safety cases (UL 9540A, NFPA 855) |
| **Indian developers on safety** | **Availability (absence)** | "No major BESS fire has happened in India" | Under-investment in detection, venting and firefighting readiness | Use global base rates (Section 2.3), not local memory |
| **Consultants (including Syselec)** | **Overconfidence and confirmation bias** | Version 1 gave single-point scores and used the 19% cancellation figure | False precision | Ranges, independent scoring, published refutation criteria (Section 6) |

### 3.2 The causal chain: how bias in bidding becomes a fire risk

```
Trend extrapolation and anchoring  →  bids below true cost (2025–26)
        ↓
Cell prices rise (2026)  →  winners move into the loss domain (prospect theory)
        ↓
Risk-seeking response: delay, renegotiate, value-engineer instead of exiting
        ↓
Cheaper integrators, compressed commissioning, thinner QA/QC, weaker thermal design
        ↓
Integration, assembly and construction defects  =  EPRI's main root-cause zone
        ↓
Higher incident and performance-failure rates in 2027–2029 operation
        ↓
One vivid incident  →  availability cascade  →  regulatory pause  →  systemic commercial failure
```

**Implication:** commercial risk and safety risk in India are **correlated, not independent**. Portfolios and insurers that model them separately will underestimate tail exposure.

---

## 4. Pre-mortem: "It is December 2029. India's BESS build-out disappointed. What happened?"

This is a Kahneman-endorsed technique (developed by Gary Klein). We assume failure and explain it, which counters the overconfidence of forward planning. Probabilities are calibrated subjective estimates for 2027–2029.

| # | Failure story | Mechanism | Probability (2027–29) | Leading indicator to watch |
|---|---|---|:-:|---|
| PM1 | **Winner's-curse wave.** A large share of 2025–26 low-tariff awards never reach financial close | Anchoring plus trend extrapolation, then rising cell prices | **40–60%** that ≥25% of that capacity is cancelled or renegotiated | Time from LoA to PSA above 6 months; re-tender notices |
| PM2 | **Quality fade.** Stressed projects cut QA and thermal design and suffer early failures | Loss-domain risk-seeking (Section 3.2) | **30–45%** | FAT/SAT waivers, integrator switches, compressed commissioning |
| PM3 | **One fire, national pause.** A vivid incident triggers a moratorium or a sweeping review | Availability cascade (South Korea precedent) | **10–20%** of a pause of 6 months or more | First incident; media intensity; ministerial statements |
| PM4 | **Desert degradation.** Rajasthan and Gujarat assets (~95% of the operating fleet) fade faster than warranted | Optimism bias in warranty and thermal design | **25–40%** | Year-1 and year-2 capacity tests; HVAC duty cycles |
| PM5 | **Merchant spread collapse.** The ~89% merchant fleet sees arbitrage revenue shrink | Fallacy of composition: each project assumes others won't enter | **35–55%** that 2028 revenue per MW is ≥20% below 2026 | IEX evening-to-solar price spreads; ancillary-market prices |
| PM6 | **Policy whiplash.** Legal reversals and new technical rules strand projects | Planning fallacy about regulation | **30–50%** that a further major tender or order is quashed or reworked | APTEL and CERC rulings; final CEA grid-forming rules |
| PM7 | **Supply shock.** Cell export controls or a price spike from China | Neglect of concentrated supply (~2 GWh domestic cells) | **15–30%** | Lithium carbonate prices; trade-policy announcements |

The probabilities overlap and are not mutually exclusive. Several could happen together, and PM1, PM2 and PM3 are causally linked.

---

## 5. Calibrated risk register (ranges with refutation tests)

**Probability** is the chance the risk materialises at material scale for the Indian market over 2027–2029. **Impact** is on the 1–5 scale used in Version 1. The **falsifier** is the observation that would show our estimate was too pessimistic. Ranges, rather than points, follow the guidance on noise in *Noise* (Kahneman, Sibony & Sunstein, 2021). Scores should be re-estimated independently by at least three assessors, then aggregated.

| # | Risk | Type | India probability | Impact | Global probability | Falsifier (we are too pessimistic if…) |
|---|---|---|:-:|:-:|:-:|---|
| 1 | Under-priced bids fail to reach financial close | Commercial | **40–60%** | 5 | 15–25% | <15% of 2025–26 awarded capacity is cancelled or renegotiated by end-2028 |
| 2 | PSA or tariff-adoption delay, or legal reversal | Commercial | **40–60%** | 4 | 10–20% | Median time from LoA to PSA <4 months for 2026 awards |
| 3 | Cell or container price or supply shock | Systemic | 30–45% | 4 | 25–40% | LFP cell prices stable within ±10% through 2028 |
| 4 | Construction delay over 9 months (LDs, VGF loss) | Commercial | **50–70%** | 4 | 20–35% | Median COD slippage on 2025–26 awards <3 months |
| 5 | Integration or construction defect causing an incident | Safety | 30–45% | 5 | 15–25% | Incident rate ≤ 0.04 per GWh-year over ≥60 GWh-years (Conjecture C4) |
| 6 | Accelerated degradation at hot sites | Performance | 25–40% | 3 | 10–20% | ≥70% of desert sites within warranty curve at year-2 tests |
| 7 | Availability or efficiency below BESPA guarantees | Performance | 30–45% | 4 | 15–25% | Fleet-average availability ≥95% and RTE ≥85% in 2027–28 |
| 8 | Merchant revenue erosion of 20% or more | Commercial | 35–55% | 4 | 50–70% | Indian merchant revenue per MW in 2028 ≥ 2026 level |
| 9 | Disruptive regulatory change (grid-forming retrofit, codes) | Systemic | 30–50% | 3 | 20–35% | Final CEA rules apply prospectively, with no retrofit obligation |
| 10 | Major fire triggering a sector-wide pause | Systemic | 10–20% | 5 | 5–10% | Any incident handled without a pause in tendering |
| 11 | OEM warranty disputes | Performance | 25–40% | 3 | 20–30% | No public warranty or arbitration disputes by 2029 |
| 12 | Offtaker payment delays over 60 days | Commercial | 20–35% | 3 | 5–10% | Late-payment-surcharge data shows timely payment for BESS contracts |
| 13 | Cyber incident on EMS or SCADA | Systemic | 5–15% | 4 | 5–15% | No reported incident, with mandatory reporting in place |
| 14 | Decommissioning or re-ignition hazards (end of life) | Safety | 5–10% | 3 | 10–20% | Safe-discharge protocols adopted in all O&M contracts |

---

## 6. Popperian conjectures: falsifiable claims with deadlines

Each conjecture is stated boldly enough to be refuted. Syselec will review these publicly against the data and **revise the assessment where any is refuted**. Being refuted is a success of the method, not a failure.

| ID | Conjecture | Test / data source | Refuted if… | Review date |
|---|---|---|---|---|
| **C1** | 25–40% of 2024–2026 tendered ESS capacity will be cancelled, re-tendered or materially renegotiated | IESA tender tracker; nodal-agency notices | <15% or >55% by the review date | Dec 2029 (interim Dec 2027) |
| **C2** | ≥25% of 2-hour standalone BESS capacity awarded below INR 2.2 lakh/MW/month in 2025–26 will be delayed more than 12 months, renegotiated or cancelled | Award list (IESA); COD records | <10% | Dec 2028 |
| **C3** | Through 2028, more Indian BESS capacity will be lost to commercial failure than to safety or performance shutdowns | Cancelled GWh vs GWh offline for more than 3 months | GWh lost to technical failure exceeds GWh cancelled | Dec 2028 |
| **C4** | Indian grid-scale BESS will not perform better than the global 2025 incident rate (0.04 per GWh-year) | Incident reports vs cumulative GWh-years | **Zero** reported incidents after ≥60 GWh-years *with mandatory reporting in place* (probability of that by chance at the global rate is ~9%) | Dec 2028 |
| **C5** | Median COD slippage for 2025–26 BESS awards will be ≥9 months | Scheduled vs actual COD | Median <3 months | Dec 2028 |
| **C6** | ≥30% of Rajasthan and Gujarat BESS sites will show year-2 capacity below the OEM warranty curve | Annual capacity tests (owners, lenders) | <10% of sites below the curve | Dec 2028 |
| **C7** | Indian merchant BESS revenue per MW in 2028 will be ≥20% below 2026 | IEX price spreads; owner disclosures | Revenue per MW flat or higher | Mar 2029 |
| **C8** | The global incident rate will not rise again: 2026–27 rates stay ≤0.04 per GWh | EPRI database updates | Any year above 0.06 per GWh | EPRI 2027/2028 updates |

**A condition for testability.** C4 and C6 can be tested only if **incident and performance data are reported**. Without mandatory incident reporting and capacity-test disclosure in India, the safety claim stays unfalsifiable, and in Popper's terms is not knowledge. **Recommendation: industry bodies (IESA, CEA) should establish a national BESS incident and performance register.**

---

## 7. Tail risks the averages hide

Popper's asymmetry and Kahneman's work on rare events both warn against judging rare, high-impact outcomes by fleet averages.

| Tail event | Why averages mislead | Exposure |
|---|---|---|
| **A sector-wide moratorium after one incident** | The rate of 0.04 per GWh says nothing about political reaction. South Korea shows one vivid cluster can halt a national market | India: high consequence, because the market is young and visible |
| **Correlated failure in one design** | ~95% of India's fleet is in two hot states, and large sites share a few OEMs. A design flaw could affect many sites at once | India: high concentration |
| **A large site that fails and keeps failing** | Moss Landing: unclear cause, then re-ignition of ~1,200 charged modules 20 months later | Global and India (GWh-scale merchant sites) |
| **Supply-chain discontinuity** | Diversification assumptions fail when one country supplies most cells | Global and India |
| **Cyber attack on a fleet** | Not in historical incident data at all, which shows "no data" is not "no risk" | Global, rising |

---

## 8. Decision protocol for companies entering BESS

This combines Kahneman's decision hygiene with Popper's piecemeal engineering: commit in stages, and correct errors at each one.

### 8.1 Debiasing checklist for any bid, investment or plant decision

Adapted from Kahneman, Lovallo & Sibony, *Before You Make That Big Decision* (HBR, 2011).

1. **Outside view:** Have we anchored on the reference-class base rates in Section 2 before looking at our own project?
2. **Anchoring:** Was our tariff or price built bottom-up **before** we looked at the latest L1 results?
3. **Trend extrapolation:** What happens to IRR if cell prices are **flat or +30%** instead of falling?
4. **Planning fallacy:** Does the schedule include reference-class slippage of 9 months at P50?
5. **Winner's curse:** At our bid, do we still clear the lender's 15–20% IRR under P90 assumptions?
6. **Pre-mortem:** Has the team written down the three most likely reasons this project fails?
7. **Independent views:** Were risk scores produced independently by at least three people before discussion, to reduce noise and groupthink?
8. **Loss domain:** If conditions worsen after award, what are our **pre-committed exit triggers**?
9. **Severe test (Popper):** Have we tried hard to **break** our financial model, not just confirm it? What single assumption, if wrong, kills the project?
10. **Safety base rate:** Are emergency response, insurance and communications planned for the **global incident rate**, not for India's history of zero?

### 8.2 Kill criteria to agree before committing (examples)

- L1 tariff falls below bottom-up cost plus the lender's required margin → **do not bid**
- No signed PSA within 6 months of LoA → **re-evaluate**, and exit if bank-guarantee exposure is below exit cost
- Delivered cell price rises more than 20% above the bid assumption with no price-variation clause → **stop procurement and renegotiate**
- FAT/SAT failures or integrator substitution → **hold commissioning** until an independent review is complete
- Year-1 capacity test below the warranty curve → **trigger warranty claim and thermal audit**

### 8.3 Piecemeal engineering: staged entry

- **Manufacturers:** start with pack and container assembly at 1–2 GWh. Expand to cells only after offtake and cost conjectures survive 12–18 months of market testing.
- **EPCs:** build references on small EPC tenders (1–30 MWh) before taking large LD-heavy turnkey contracts.
- **Bidders:** limit any single tender to a share of the balance sheet that a full write-off would not threaten.
- **O&M providers:** pilot performance-linked contracts at 2–3 sites and publish learnings before scaling guarantees.

---

## 9. What would change our overall verdict?

In Popper's spirit, these are the observations that would make us **downgrade India's exposure from High to Medium**:

1. Cancellation and renegotiation of 2024–2026 cohorts stays **below 15%** through 2028 (C1 refuted).
2. Median COD slippage for 2025–26 awards is **under 3 months** (C5 refuted).
3. With mandatory incident reporting in place, India accumulates **60+ GWh-years with no incidents** (C4 refuted), showing quality better than the global average.
4. Year-2 capacity tests at desert sites are **within warranty** at more than 70% of sites (C6 refuted).

And these would make us **upgrade global exposure from Medium to High**:

1. EPRI's incident rate rises **above 0.06 per GWh** in any year (C8 refuted).
2. A second Moss Landing-scale event leads to **moratoria in two or more major markets**.

---

## 10. Conclusion

- **Globally:** BESS has largely solved the problem of *average* safety. The remaining exposure lies in **revenue erosion, trade and supply policy, and rare high-consequence events** that shape regulation and public consent.
- **In India:** the dominant exposure is **commercial failure created by predictable judgement errors**: anchoring on falling L1 tariffs, extrapolating cell-price trends, and the winner's curse. Prospect theory predicts that stressed winners will not exit cleanly. They will **trade quality for survival**. That links commercial failure to the integration and construction defects that cause most BESS incidents worldwide.
- **The safety question in India is still open.** India's clean record is statistically uninformative. On global base rates, the industry should expect several incidents a year as the fleet passes 40–90 GWh, and should build reporting, emergency response and communications now. That reduces the chance that one event triggers an availability cascade.

**For market entrants, the winning posture is:**
1. Use base rates, not narratives
2. Price bottom-up, not by anchoring on rivals
3. Pre-commit kill criteria
4. Try to refute your own business case before the market does
5. Scale in stages, with error correction at each step

These are the disciplines Syselec's advisory work (bid modelling, owner's engineering, commissioning assurance and O&M frameworks) is built to enforce.

---

## Sources

**Data and market evidence**
- India Energy Storage Alliance (IESA), *ESS Market Update, September 2026*. Tender data compiled by Debmalya Sen, updated to 1 October 2026. Cohort figures are read from the IESA tender-status chart.
- EPRI, [*Risk Factors and Failure Statistics of Lithium-Ion BESS* (2026)](https://restservice.epri.com/publicdownload/000000003002034920/0/Product) and the [BESS Failure Incident Database](https://storagewiki.epri.com/index.php/BESS_Failure_Incident_Database)
- ESS News, [Global battery storage failure rate down 98% since 2018](https://www.ess-news.com/2026/10/15/global-battery-storage-failure-rate-down-98-since-2018/)
- Utility Dive, [Battery system failures fell 98% in 7 years](https://www.utilitydive.com/news/battery-system-failures-fell-98-in-7-years-but-older-systems-need-special/832882/)
- Energy-Storage.news, [Battery storage failure incident rate dropped 97% between 2018 and 2023](https://www.energy-storage.news/battery-storage-failure-incident-rate-dropped-97-between-2018-and-2023/)
- CalMatters, [Moss Landing battery fire reignites fears (Sept 2026)](https://calmatters.org/environment/2026/09/moss-landing-battery-fire-reignites-fears/)
- PG&E, [Findings of the September 2022 Moss Landing Megapack incident](https://www.pge.com/en/newsroom/currents/safety/pg-e-shares-findings-of-september-2022-moss-landing-megapack-inc.html)
- POWER Magazine, [Building a safer storage industry after the Moss Landing fire](https://www.powermag.com/building-a-safer-storage-industry-after-the-moss-landing-fire)
- IEEFA–JMK Research, [Viability of standalone battery energy storage tariffs discovered in 2025](https://ieefa.org/resources/viability-standalone-battery-energy-storage-tariffs-discovered-2025) and [Tariff viability and financing hurdles loom](https://ieefa.org/articles/indias-energy-storage-push-gathers-momentum-tariff-viability-and-financing-hurdles-loom)
- Mercom India, [Execution risks loom for Indian battery storage developers](https://mercomindia.com/execution-risks-loom-for-indian-battery-storage-developers-as-tariffs-drop-sharply)
- SolarQuarter, [APTEL quashes MERC's BESS tariff order, cancels MSEDCL's 2,000 MW / 4,000 MWh tender](https://solarquarter.com/2026/06/06/aptel-quashes-mercs-bess-tariff-order-cancels-msedcls-2000-mw-4000-mwh-battery-storage-tender/amp/)
- Ventura Securities research note on 2026 cell-price movement (secondary source, not independently verified)

**Thinking frameworks**
- Tversky, A. & Kahneman, D. (1974). *Judgment under Uncertainty: Heuristics and Biases.* Science.
- Kahneman, D. & Tversky, A. (1979). *Prospect Theory: An Analysis of Decision under Risk.* Econometrica.
- Kahneman, D. & Lovallo, D. (1993). *Timid Choices and Bold Forecasts.* Management Science. (The outside view.)
- Kahneman, D. (2011). *Thinking, Fast and Slow.*
- Kahneman, D., Lovallo, D. & Sibony, O. (2011). *Before You Make That Big Decision.* Harvard Business Review.
- Kahneman, D., Sibony, O. & Sunstein, C. (2021). *Noise: A Flaw in Human Judgment.*
- Klein, G. (2007). *Performing a Project Premortem.* Harvard Business Review.
- Kuran, T. & Sunstein, C. (1999). *Availability Cascades and Risk Regulation.* Stanford Law Review.
- Flyvbjerg, B. & Gardner, D. (2023). *How Big Things Get Done.*
- Popper, K. (1959). *The Logic of Scientific Discovery.*
- Popper, K. (1957). *The Poverty of Historicism.*
- Popper, K. (1963). *Conjectures and Refutations.*

*All probabilities are Syselec's calibrated subjective estimates for planning purposes. They are stated as ranges and tied to refutation criteria so they can be tested and corrected. They do not predict outcomes for individual projects.*
