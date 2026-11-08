# BESS Implementation: Exposure-to-Failure Assessment, India and Global

**Prepared by:** Syselec Technologies, BESS Advisory
**Date:** November 2026
**Basis:**
- IESA *India ESS Market Update, September 2026*
- EPRI BESS Failure Incident Database and the 2026 white paper *Risk Factors and Failure Statistics of Lithium-Ion BESS*
- IEEFA–JMK Research on Indian BESS tariff viability
- Public reporting on major incidents (sources are listed at the end)

> **How to read this document:** "Failure" means any outcome where a BESS does not deliver what was promised. That covers four types:
> - **A. Commercial failure:** the project is cancelled, terminated or never financed
> - **B. Safety failure:** fire, thermal runaway or explosion
> - **C. Performance failure:** availability, efficiency or degradation shortfalls, or warranty disputes
> - **D. Systemic or external failure:** supply chain, policy, grid, climate or cyber events
>
> Risk scores are Syselec's expert judgement on a 1–5 scale for likelihood (L) and impact (I). Exposure = L × I, out of 25.

---

## 1. Executive summary

**Bottom line:** BESS failure exposure globally has shifted from *"will the battery catch fire?"* to *"will the project make money and perform as promised?"* In India this shift is sharper. **The biggest exposure is commercial and execution failure, not safety.**

| | India | Global |
|---|---|---|
| **Overall exposure** | **High (about 16/25)** | **Medium (about 11/25)** |
| Dominant failure type | Commercial (tariff viability, cancellations, financing) | Revenue and market (merchant price saturation), policy and trade |
| Safety failure exposure | Medium, rising with scale. The fleet is young, concentrated in hot climates, and codes are still maturing | Low and falling. Failures per GWh are down 98% since 2018 (EPRI) |
| Performance exposure | Medium–High: heat, dust, inexperienced O&M, untested BESPA guarantees | Medium: degradation and warranty disputes in older fleets |
| Trend | Worsening in the near term because aggressive bids meet rising cell costs | Stable to improving |

**Five findings that matter most**

1. **Safety is improving fast worldwide.** EPRI reports a **98% fall in failures per GWh deployed (2018–2025)**, reaching **0.04 failures/GWh in 2025** (24 incidents across 634 GWh of cumulative deployment). Where a root cause could be assigned, most failures came from **integration, assembly and construction, and balance of system (BoS)**, not from defective cells.
2. **In India, commercial failure is the main risk.**
   - About **19% of all tendered ESS capacity (58.5 of 308 GWh) has been cancelled**. For BESS alone the figure is about **14% (24 of 167 GWh)** (IESA).
   - IEEFA–JMK find that standalone BESS **tariffs fell ~71% while pack prices fell only ~36%**, which points to speculative bidding.
   - Cell prices reportedly rose sharply in 2026. One secondary source reports about +32% from January to July; this needs verification.
3. **India's operating fleet is highly concentrated.** Of the ~13.5 GWh operating, about **89% is merchant** (ACME, Adani, Juniper, Serentica) and **about 95% is in Rajasthan and Gujarat**. That is heavy exposure to one revenue model and to desert heat and dust.
4. **Execution capacity is thin.** Many BOO winners are first-time storage players. Domestic cell capacity is only **~2 GWh**, so most projects depend on imported cells and integrators. IEEFA–JMK expect **9–18-month delays** across the pipeline.
5. **The rules keep changing.** CEA has proposed **grid-forming PCS** and **15% storage on new RE from 2027**. Tariff orders are being challenged: APTEL quashed MERC's order, cancelling MSEDCL's **2 GW / 4 GWh** VGF tender. Projects in development now face redesign or legal risk.

---

## 2. Global evidence base

### 2.1 Safety failures are rare and getting rarer

| Metric (EPRI) | Value |
|---|---|
| Failure rate per deployed GWh, 2018 to 2025 | **−98%** |
| 2025 failure rate | **0.04 failures per GWh deployed** (24 incidents, 634 GWh cumulative) |
| 2024 | 26 incidents, 343 GWh cumulative |
| Aggregate rate, 2018–2025 | 2.087 × 10⁻⁴ incidents per MWh-year |
| Where root causes originate (EPRI–TWAICE–PNNL) | Mostly **integration, assembly and construction**, plus BoS and controls. Cell manufacturing defects are a minority |
| Data caveat | Root cause was public for only 26 of 81 incidents in the earlier study. About 22% of database incidents were confirmed privately. Fleet averages do not predict any single project |

**Why the rate fell:** better system design, the arrival of codes and standards (NFPA 855, UL 9540/9540A), and better BMS and operating practice since 2018–2020. EPRI found **no evidence that chemistry alone** decides system-level failure. Design, integration and operations matter more.

### 2.2 Lessons from major incidents

| Incident | What it teaches |
|---|---|
| **South Korea, 2017–2019:** a wave of BESS fires led to a national investigation and halted the market | Poor installation, protection and environmental management at scale can shut down an entire national market |
| **APS McMicken, Arizona, 2019:** explosion that injured firefighters | Gas build-up in enclosed containers. Led to deflagration venting and emergency-response protocols |
| **PG&E Elkhorn, Moss Landing, Sept 2022:** Megapack fire | Root cause was **water ingress from an installation issue**, a construction-quality failure |
| **Vistra Moss Landing, Jan 2025:** major fire at one of the world's largest BESS sites | Official cause still not confirmed (CPUC, Sept 2026). Roughly 1,200 still-charged modules **re-ignited in Sept 2026**. Older indoor, building-style designs, decommissioning risk and community backlash all hit permitting and insurance across the industry |

### 2.3 Commercial and systemic exposure globally

- **Merchant revenue erosion:** ancillary-service and arbitrage prices fall as storage saturates markets (seen in the UK, Texas/ERCOT and Australia). Projects underwritten on early-market prices underperform.
- **Trade and supply-chain policy:** most cells and many containers come from China. Tariffs and foreign-content restrictions (for example in the US) can raise capex and break supply contracts midway through a project.
- **Permitting and community acceptance:** after Moss Landing, local opposition and tighter fire-code reviews slow approvals and raise insurance premiums.
- **Grid connection queues:** long interconnection delays strand capital.
- **Cybersecurity:** connected EMS and SCADA, and remote OEM access, expand the attack surface.

---

## 3. India evidence base

### 3.1 Commercial failure indicators (IESA, Sep 2026)

| Indicator | Value | What it signals |
|---|---|---|
| ESS capacity cancelled | **58.5 GWh of 308 GWh (19%)** | High tender mortality |
| BESS capacity cancelled | **24.0 GWh of 167 GWh (~14%)** | Lower than pumped storage (24%) but material |
| Awarded but no PSA signed or tariff adopted | Large block, mainly FDRE | Capital tied up while offtake is uncertain |
| Contract terminations | G R Infra terminated a 400 MWh NTPC contract | Winners walking away after award |
| Legal reversals | APTEL quashed MERC tariff order, cancelling MSEDCL's 2 GW / 4 GWh tender | Regulatory and legal risk after award |
| 2-hour standalone tariffs | INR **1.48–3.35** lakh/MW/month; IESA asks "how much will survive?" with cell costs rising | Thin or negative margins for some winners |
| Tariff fall vs cost fall (IEEFA–JMK) | Tariffs about −71%, pack prices about −36% | Speculative bidding |
| Lender return expectation (IEEFA–JMK) | 15–20% equity IRR | Many low bids cannot meet it, so financial close fails |
| Expected delays (IEEFA–JMK) | 9–18 months | Pipeline slippage, LD exposure, lost VGF |

### 3.2 Concentration of the operating fleet

Based on IESA's list of 18 operational projects, totalling about 13.5 GWh:

| Concentration | Share | Exposure |
|---|---|---|
| **Merchant standalone** (ACME 4,950, Adani 6,300, Juniper 600, Serentica 200 MWh) | **~89%** | Price risk on power exchanges and ancillary markets |
| **Located in Rajasthan and Gujarat** | **~95%** | Ambient heat often above 45°C, dust, high HVAC load; faster degradation if thermal design is weak |
| **Imported integrators/containers** on the largest sites (e.g. Envision, Hithium) | Majority of MWh | Spares, warranty and service response depend on foreign OEMs |

### 3.3 Structural factors specific to India

- **Supply dependency:** about 2 GWh of domestic cell capacity against a 14 GWh fleet and a 122 GWh pipeline. Exposed to cell-price swings, currency movements and trade policy.
- **New entrants:** many BOO winners and EPCs have no BESS track record. This is the exact zone (integration, assembly, construction) where EPRI finds most failures begin.
- **Codes and emergency response still maturing:** fire-safety approvals, spacing rules and local fire-brigade readiness lag behind deployment speed.
- **Offtaker credit:** state DISCOM payment discipline varies, a risk for 12-year BOO contracts.
- **Moving technical requirements:** the proposed 2027 grid-forming mandate, CTUIL augmentation guidance, KSERC's 85% efficiency benchmark and new land norms (1.2 acres/100 MWh) can strand or force redesigns of projects already in development.
- **Skills gap:** few trained BESS O&M technicians, thermal specialists and commissioning engineers.

---

## 4. Risk register: India vs Global

L = likelihood, I = impact, E = exposure (L×I). Trend arrows show the near-term direction for India: ↑ worsening, → stable, ↓ improving.

| # | Risk | Type | India L | India I | **India E** | Global E | Trend (India) | Key mitigation |
|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | Unviable bid tariff, so the project cannot reach financial close | A | 4 | 5 | **20** | 9 | ↑ | Lender-grade model with cell-price and degradation stress tests; bid discipline |
| 2 | Tender cancellation, PSA not signed or tariff not adopted | A | 4 | 4 | **16** | 6 | → | Target offtakers with signed PSAs and healthy DISCOMs; legal review of tender terms |
| 3 | Cell and container price or supply shock | D | 4 | 4 | **16** | 12 | ↑ | Index-linked or fixed-price supply contracts; dual sourcing; hedging; domestic suppliers |
| 4 | Construction delay leading to LDs and VGF loss | A | 4 | 4 | **16** | 9 | ↑ | Owner's engineer; schedule-backed EPC; early grid-connectivity work |
| 5 | Integration, assembly or construction defect (the main global root cause of fires) | B | 3 | 5 | **15** | 10 | ↑ | Design reviews, FAT/SAT, QA/QC at site, independent commissioning |
| 6 | Thermal stress and dust causing accelerated degradation | C | 4 | 3 | **12** | 6 | → | HVAC/liquid cooling sized for 50°C, filtration, augmentation planning |
| 7 | Availability or efficiency below BESPA guarantees | C | 3 | 4 | **12** | 8 | ↑ | Performance-linked O&M, spares strategy, EMS analytics |
| 8 | Merchant revenue erosion as more storage enters | A | 3 | 4 | **12** | 16 | ↑ | Hybrid revenue stacking; partial contracting; conservative price decks |
| 9 | Regulatory change (grid-forming, codes, land, efficiency) | D | 4 | 3 | **12** | 8 | ↑ | Regulatory watch; future-proof PCS specifications; change-in-law clauses |
| 10 | Fire or thermal runaway event | B | 2 | 5 | **10** | 10 | → | NFPA 855 / UL 9540A-compliant design, gas detection and venting, fire-brigade drills |
| 11 | OEM warranty disputes and slow foreign OEM support | C | 3 | 3 | **9** | 9 | → | Back-to-back warranties, local spares, independent capacity testing |
| 12 | Offtaker payment default or delay | A | 3 | 3 | **9** | 4 | → | Payment-security mechanisms, LC/escrow, state selection |
| 13 | Skills shortage in O&M and commissioning | C | 4 | 2 | **8** | 4 | → | Training academies, OEM certification, outsourced specialist O&M |
| 14 | Grid connectivity or evacuation delay | D | 3 | 3 | **9** | 12 | → | Early CTU/STU applications; use of existing RE connectivity (CTUIL augmentation) |
| 15 | Cyber-attack on EMS or SCADA | D | 2 | 4 | **8** | 8 | ↑ | IEC 62443 practices, network segregation, controlled OEM remote access |
| 16 | Community opposition, permitting or insurance tightening after incidents | D | 2 | 3 | **6** | 12 | ↑ | Transparent safety cases, setback distances, emergency-response plans |
| 17 | End-of-life, decommissioning and recycling liabilities | D | 2 | 3 | **6** | 6 | ↑ | Battery Waste Management Rules compliance; recycling contracts from day one |

**Exposure bands:** 15–25 Critical · 10–14 High · 5–9 Moderate · below 5 Low

### Heat-map summary

| Exposure | India | Global |
|---|---|---|
| **Critical (15–25)** | Unviable tariffs (1), cancellations and PSA delays (2), supply shocks (3), construction delay (4), integration defects (5) | Merchant revenue erosion (8) |
| **High (10–14)** | Heat and degradation (6), guarantee shortfall (7), merchant erosion (8), regulatory change (9), fire (10) | Supply shocks (3), integration defects (5), fire (10), grid connection (14), permitting and insurance (16) |
| **Moderate (5–9)** | Warranty (11), payment (12), skills (13), grid (14), cyber (15), community (16), end-of-life (17) | Most others |

---

## 5. Where failure concentrates across the project lifecycle

| Stage | India exposure | Global exposure | Typical failure |
|---|:-:|:-:|---|
| 1. Bid and tariff discovery | **Very high** | Medium | Bid below cost, so the project is later abandoned |
| 2. PSA, financing and financial close | **Very high** | Medium | No signed PSA, or lenders reject the model |
| 3. Procurement and supply chain | High | High | Price shock, delivery delay, quality variance |
| 4. Construction and integration | **High** | High | Defects (water ingress, wiring, protection), schedule slip |
| 5. Testing, commissioning and handover | High | Medium | Inadequate FAT/SAT, grid-code non-compliance |
| 6. Operation (years 1–3, warranty period) | Medium–High | Medium | Availability or efficiency shortfall; early thermal events |
| 7. Mid-life (years 4–12) | Medium (no track record yet) | Medium | Degradation, augmentation, warranty expiry |
| 8. End-of-life | Low now, rising | Medium | Decommissioning hazards (see the Moss Landing re-ignition) |

**Insight:** Globally, the risk curve peaks in **construction, integration and early operation**. In India the curve is **front-loaded**: most projects that fail do so **before they are built**, at the bid, PSA and financing stages. As the 122 GWh pipeline turns into steel over 2027–2029, India's exposure will shift toward the global pattern of construction and operational failure. That is when safety and performance risks will rise.

---

## 6. Exposure by type of market entrant

| Entrant (Syselec persona) | Highest exposure | Failure scenario to avoid |
|---|---|---|
| **Manufacturer** (cells, packs, containers) | Price war with Chinese suppliers; underused capacity if tenders are cancelled; certification gaps | Building a plant for demand that slips by 18 months |
| **EPC / turnkey contractor** | LDs, integration defects, back-to-back warranty gaps | Absorbing OEM failures under its own performance guarantees |
| **BOO bidder / owner** | Unviable tariff, financing, PSA, offtaker credit | Winning a bid that can't reach financial close |
| **PCS / EMS OEM** | Regulatory redesign (grid-forming), type-testing delays | Products non-compliant with the 2027 rules |
| **O&M provider** | Guarantee-linked liability, skills, thermal management | Paying penalties for availability shortfalls caused by design flaws |

---

## 7. Early-warning indicators to monitor

1. **Bid-to-cost gap:** the L1 tariff compared with Syselec's bottom-up cost benchmark and the CTUIL benchmark of INR 0.8 Cr/MWh. A gap above 15% is a red flag.
2. **Time from LoA to PSA:** more than 6 months signals offtake risk.
3. **LFP cell price index:** month-on-month moves above 10% call for re-checking project viability.
4. **Cancellation and re-tender rate:** tracked monthly through the IESA tender tracker.
5. **Fleet availability and round-trip efficiency** for commissioned projects against BESPA guarantees.
6. **Container internal temperature** and HVAC duty cycle at desert sites in peak summer.
7. **Thermal-event near-misses:** off-gas alarms, BMS isolations, cell-imbalance trends.
8. **Regulatory calendar:** final CEA grid-forming rules, state storage mandates, APTEL and CERC rulings.

---

## 8. Mitigation playbook

| Lever | Actions |
|---|---|
| **Bid discipline** | Stress-test bids on cell price (±30%), degradation, augmentation cost, availability and DISCOM payment delay. Walk away from bids below the benchmark |
| **Contract architecture** | Back-to-back warranties and LDs with OEMs and EPCs; change-in-law and price-variation clauses; payment security from offtakers |
| **Engineering quality** | Independent design review, FAT/SAT protocols, site QA/QC, grid-code compliance studies, owner's engineer through commissioning. This targets the integration and construction zone where EPRI finds most failures begin |
| **Safety by design** | UL 9540A test data, NFPA 855 spacing, gas detection and deflagration venting, emergency-response plans with local fire services, and safe decommissioning procedures |
| **Climate-ready design** | Thermal management sized for ambient temperatures of 50°C or more, dust filtration, and derating and augmentation built into the energy model |
| **Supply-chain resilience** | Dual sourcing, domestic-content roadmap, inspections at the factory and on arrival, and a spares strategy |
| **Operational excellence** | Performance-linked O&M, EMS analytics for state-of-health and availability, trained technicians, cybersecurity controls |
| **Portfolio balance** | Avoid concentration in one state, one revenue model or one OEM. Mix contracted and merchant revenue |

---

## 9. Conclusion

- **Globally,** BESS has become a **technically mature, increasingly safe** asset class. The remaining exposure lies in **market revenue, trade policy and community acceptance**, plus the quality of integration and construction.
- **In India,** the opportunity is very large (308 GWh tendered and a 17-fold jump in installed capacity in nine months). But the **probability of commercial failure is high**: aggressive tariffs, rising cell costs, PSA delays, legal challenges and inexperienced entrants.
- As the pipeline is built, **construction quality and operations in harsh climates** will become the next major exposure.

**For companies entering the market, the critical success factors are:**
1. Bid with discipline
2. Build with quality-assured integration
3. Design for Indian heat and grid codes
4. Operate with performance-linked accountability

Syselec's advisory services (bid modelling, owner's engineering, design and commissioning assurance, and O&M and warranty frameworks) are aimed at exactly these exposures.

---

## Sources

- India Energy Storage Alliance (IESA), *ESS Market Update, September 2026*. Tender data compiled by Debmalya Sen, updated to 1 October 2026
- EPRI, [*Risk Factors and Failure Statistics of Lithium-Ion BESS* (white paper, 2026)](https://restservice.epri.com/publicdownload/000000003002034920/0/Product) and [BESS Failure Incident Database](https://storagewiki.epri.com/index.php/BESS_Failure_Incident_Database)
- ESS News, [Global battery storage failure rate down 98% since 2018](https://www.ess-news.com/2026/10/15/global-battery-storage-failure-rate-down-98-since-2018/)
- Utility Dive, [Battery system failures fell 98% in 7 years, but older systems need special attention](https://www.utilitydive.com/news/battery-system-failures-fell-98-in-7-years-but-older-systems-need-special/832882/)
- Energy-Storage.news, [Battery storage failure incident rate dropped 97% between 2018 and 2023](https://www.energy-storage.news/battery-storage-failure-incident-rate-dropped-97-between-2018-and-2023/)
- CalMatters, [Moss Landing battery fire reignites fears (Sept 2026)](https://calmatters.org/environment/2026/09/moss-landing-battery-fire-reignites-fears/)
- PG&E, [Findings of September 2022 Moss Landing Megapack incident](https://www.pge.com/en/newsroom/currents/safety/pg-e-shares-findings-of-september-2022-moss-landing-megapack-inc.html)
- POWER Magazine, [Building a safer storage industry after the Moss Landing fire](https://www.powermag.com/building-a-safer-storage-industry-after-the-moss-landing-fire)
- IEEFA–JMK Research, [Viability of standalone battery energy storage tariffs discovered in 2025](https://ieefa.org/resources/viability-standalone-battery-energy-storage-tariffs-discovered-2025) and [India's energy storage push: tariff viability and financing hurdles loom](https://ieefa.org/articles/indias-energy-storage-push-gathers-momentum-tariff-viability-and-financing-hurdles-loom)
- Mercom India, [Execution risks loom for Indian battery storage developers as tariffs drop sharply](https://mercomindia.com/execution-risks-loom-for-indian-battery-storage-developers-as-tariffs-drop-sharply)
- SolarQuarter, [APTEL quashes MERC's BESS tariff order, cancels MSEDCL's 2,000 MW / 4,000 MWh tender](https://solarquarter.com/2026/06/06/aptel-quashes-mercs-bess-tariff-order-cancels-msedcls-2000-mw-4000-mwh-battery-storage-tender/amp/)
- Ventura Securities research note on 2026 cell-price movement (secondary source, not independently verified)

*Risk scores are Syselec's expert judgement for planning purposes and do not predict outcomes for individual projects.*
