---
title: "When a Cancer Protocol Outruns Its Evidence: Statistical Power, Popper, and Kahneman"
author: Hrushaabh Mishra
blog: hrushaabhmishra blog
date: 2026-10-22
tags: [epistemology, statistics, cancer research, critical thinking, Karl Popper, Kahneman and Tversky, evidence-based medicine]
description: "A case study of a 2024 orthomolecular cancer protocol shows how underpowered studies, case reports and cognitive biases turn into confident treatment advice, and how falsification and base rates can catch the problem."
---

# When a Cancer Protocol Outruns Its Evidence: Statistical Power, Popper, and Kahneman

*By Hrushaabh Mishra*

> **Disclaimer:** This is an essay about scientific reasoning, not medical advice. If you or someone you love is facing cancer, please make treatment decisions with a qualified oncologist.

People often treat "published in a medical journal" as if it meant "proven." It doesn't. A journal article is a claim submitted for scrutiny. How much it is worth depends on two things: whether the studies behind it could actually have detected what they claim (**statistical power**), and whether the claim could ever be shown wrong (**falsifiability**).

This post works through one recent paper as a case study:

> Baghli I, Makis W, Marik PE, et al. *Targeting the Mitochondrial-Stem Cell Connection in Cancer Treatment: A Hybrid Orthomolecular Protocol.* **Journal of Orthomolecular Medicine**, 39(3), 2024. [1]

To be clear from the start, **this paper is not a clinical trial.** It is a narrative review that ends in a treatment protocol: high-dose IV vitamin C, 50,000 IU/day of vitamin D, zinc, ivermectin, mebendazole/fenbendazole, the glutamine antagonist DON, ketogenic diets and water fasting, exercise and hyperbaric oxygen, given for 12 weeks "regardless of cancer type." That is exactly why it is useful as an example. It shows what happens when a protocol is built on a pile of underpowered, preclinical and anecdotal evidence, and then presented as though the pile added up to proof.

I'll use three lenses:

1. **Statistical power:** could the underlying studies detect what they claim?
2. **Karl Popper:** is the theory falsifiable, and has it survived the tests?
3. **Kahneman and Tversky:** which mental shortcuts make weak evidence feel strong?

---

## 1. What the paper claims

The paper builds on a theory the authors call the **Mitochondrial-Stem Cell Connection (MSCC)**. In their words, cancer "arises from impaired oxidative phosphorylation (OxPhos) in one or more stem cells," which become cancer stem cells (CSCs). Its key claims:

- Cancer starts with an OxPhos (mitochondrial respiration) defect in stem cells.
- Tumor cells *need* glucose and glutamine: "no evidence has demonstrated the growth of any tumor cells… with the deprivation of fermentable fuels."
- Metastasis happens when CSCs fuse with macrophages.
- "These principles are applicable to all types of cancer."
- The protocol increases OxPhos, starves tumors of fuel, targets CSCs, is synergistic and safe, and "numerous experiments in cells, animals, and humans support" it.

These are strong, universal claims, so they make a good test case.

---

## 2. Statistical power: the missing number

### What power means

Statistical power is the probability that a study will detect a real effect of a given size. Low power causes two problems that are easy to overlook:

- **Real effects get missed** (false negatives).
- **The "significant" results that do appear are disproportionately false or exaggerated.** Button et al. showed this for neuroscience [8]. Gelman and Carlin call these Type M (magnitude) and Type S (sign) errors [9].

### How many patients a survival claim actually needs

For a survival outcome, the number of **deaths (events)** needed comes from Schoenfeld's formula:

$$
\text{Events} = \frac{4\,(z_{1-\alpha/2} + z_{1-\beta})^2}{(\ln HR)^2}
$$

With the usual α = 0.05 (two-sided) and 80% power (z ≈ 1.96 + 0.84 = 2.80):

| True effect (hazard ratio) | Events (deaths) needed |
|---|---|
| HR 0.70 (30% fewer deaths) | ≈ **247** |
| HR 0.80 (20% fewer deaths) | ≈ **630** |
| HR 0.90 (10% fewer deaths) | ≈ **2,830** |

Compare those figures with the evidence the protocol cites for its human claims:

| Protocol component | Human evidence cited | Effective sample size |
|---|---|---|
| Vitamin D 50,000 IU/day | One pancreatic cancer case report | n = 1 |
| Mebendazole | Two case reports | n = 2 |
| Fenbendazole | Case series | n = 3 |
| Ketogenic metabolic therapy | Glioblastoma case reports | n = 1–2 |
| Ivermectin | Safety/pharmacokinetic studies in healthy volunteers [17] | No efficacy endpoint at all |
| DON | Preclinical studies | 0 patients |
| The full 7-part protocol | **None** | **0 patients** |

A case report has no statistical power. It cannot separate a treatment effect from spontaneous regression, the delayed effect of earlier chemotherapy, misdiagnosis, or ordinary variation in how a disease progresses. The full protocol has never been tested in a single patient as a combined regimen, so its claimed "synergy" is a hypothesis.

### Subgroups and post-hoc analyses

Where the paper does cite real randomized trials, it often picks the subgroup instead of the primary result:

- **VITAL** (25,871 participants) was powered for its **primary** endpoint, and that endpoint was **null**: invasive cancer HR ≈ 0.96 [10]. The paper cites a later **BMI subgroup** analysis instead [11].
- **AMATERASU** (vitamin D in digestive-tract cancers) **missed its primary endpoint** of relapse-free survival [12]. The paper cites a **post-hoc** analysis of p53-immunoreactive patients [13] and describes it as "a recent randomized controlled trial found…"

Subgroups are smaller than the full trial, so they are underpowered by design. When many subgroups are examined, chance alone will make some look "significant." Gelman and Loken call this the **garden of forking paths** [14]. A subgroup result generates a hypothesis. It does not confirm one.

### Ioannidis' arithmetic

John Ioannidis showed that the probability that a "positive" finding is true (its positive predictive value, PPV) depends on the prior odds, the power and the significance threshold [7]:

$$
PPV = \frac{(1-\beta)\,R}{(1-\beta)\,R + \alpha}
$$

Take a realistic prior for a new anticancer agent. Only about 5–7% of oncology drugs that enter clinical testing are ever approved [5], so R ≈ 0.05.

- With 50% power: PPV ≈ **0.34**
- With 20% power: PPV ≈ **0.17**

Even before accounting for bias, most "positive" findings in this setting would be false. The protocol stacks **seven** such components, so the probability that all of them work as claimed is far lower again.

---

## 3. Popper: can this theory be proven wrong?

Karl Popper's demarcation criterion says a scientific theory must **forbid** certain outcomes [2,3]. Finding confirmations is easy. What counts is surviving a *risky* test, one the theory could have failed.

### The universal claims have already been refuted

The paper says its principles apply to **all** cancers. Under Popper's logic, one solid counterexample refutes a universal claim, and several exist:

- **Human tumors do respire.** Isotope-tracing studies in patients during lung cancer surgery showed tumors oxidizing glucose and lactate in their mitochondria [18,19]. Their OxPhos is working.
- **Some cancer stem cells *depend* on OxPhos.** Leukemic stem cells in AML rely on oxidative phosphorylation [20]. Venetoclax + azacitidine kills them partly by *suppressing* OxPhos [21], and in a phase 3 randomized trial it improved median survival from about 9.6 to 14.7 months [22]. MSCC predicts that *enhancing* OxPhos should help. In this setting, a therapy that suppresses it is the standard of care.
- **Tumors cannot form without mitochondrial respiration.** Cancer cells stripped of mitochondrial DNA formed tumors only after acquiring mitochondria from the host [23]. That is the reverse of "OxPhos insufficiency causes cancer."
- **Tumors use more than glucose and glutamine.** Human lung tumors burn lactate [19], which refutes the claim that "no tumor grows" without those fuels.

### The hedged version can't be tested

Where the paper avoids universal claims, it uses words like "may," "could" and "potentially." A theory that only says something *may* happen forbids nothing. The bigger problem is that the paper treats **opposite mechanisms as support for the same theory**:

- The protocol's goal is to *enhance* OxPhos.
- Yet the paper also cites as supporting evidence ivermectin's "mitochondrial dysfunction," metformin (which *inhibits* mitochondrial complex I), and vitamin C acting as a pro-oxidant that *damages* mitochondria.

If restoring mitochondria and damaging them both confirm the theory, no observation could ever count against it. Popper's point was that a theory which explains everything explains nothing [3].

### The Duhem–Quine trap

The protocol combines 7 interventions, offers up to 10 optional add-ons, and allows doses to be adjusted "according to… treatment results." It names no primary endpoint and no failure condition. If a patient does well, the protocol gets the credit. If a patient does poorly, the explanation can always be dose, adherence, stage or a missing add-on. When that many auxiliary assumptions travel with the core hypothesis, the hypothesis can never be isolated and refuted. Imre Lakatos would describe this as a **degenerating research programme**: it absorbs anomalies after the fact instead of predicting new facts [15].

### The risky tests that were omitted

Several large, well-powered trials *could* have supported the protocol's components. They didn't, and the paper doesn't discuss them:

| Test | Result |
|---|---|
| Two Mayo Clinic RCTs of high-dose vitamin C [24,25] | No benefit. (Fair caveat: these used oral dosing, which reaches much lower blood levels [26].) |
| **VITALITY phase 3**: high-dose *IV* vitamin C + chemotherapy, ~440 colorectal cancer patients [27] | **No improvement in progression-free survival overall.** The paper cites this regimen's earlier phase I study, not this phase 3 result. |
| **VITAL**: vitamin D, 25,871 participants [10] | Primary cancer endpoint **null** |
| **MA.32**: metformin, ~3,600 breast cancer patients [28] | **No effect** on invasive disease-free survival |
| Mebendazole phase 2 in GI cancer [29] (the paper cites it only for safety) | **No objective responses** |

These are the risky tests Popper asks for, and the components failed them.

---

## 4. Kahneman and Tversky: why weak evidence feels strong

Kahneman and Tversky catalogued the systematic shortcuts that lead intelligent people to wrong conclusions [4,6,30,31]. Many of them appear in this paper.

**The law of small numbers** [30]. People expect small samples to look like the population. One remarkable patient feels like a pattern. Statistically, n = 1 is close to noise.

**Base-rate neglect** [31]. The paper repeatedly reports in-vitro results such as "vitamin C more effective than cisplatin" and "ivermectin more effective than paclitaxel." Base rates for this kind of evidence are low. Only 6 of 53 landmark preclinical cancer findings could be reproduced [32]. A large replication project found replicated effects about **85% smaller** than the originals [33]. For ivermectin, the in-vitro anticancer concentrations are roughly 20–100 times higher than the peak blood levels reached in human dosing studies [17].

**Availability and survivorship bias.** One cited study analyzed 200 cases of *spontaneous regression* and found that most patients had changed their diet. When you sample only on the outcome, you never see the many people who changed their diet and did not regress.

**The conjunction fallacy** [4]. In the "Linda problem," people judge "a bank teller who is a feminist" more probable than "a bank teller," because the detailed story feels more representative. MSCC is a long causal chain: OxPhos defect → cancer stem cell → fuel dependence → macrophage fusion → metastasis → reversed by seven synergistic agents. Each added link makes the story feel more convincing and makes it **less** probable. Even if every link had a generous 70% chance of being true, six links together would have about a 12% chance (0.7⁶ ≈ 0.12).

**Framing** [6]. The paper reports that Cameron and Pauling's patients had survival "multiplied by 55" (22% vs 0.4% at one year). That ratio rests on a tiny control fraction drawn from *historical* controls, not randomized ones. The paper also says modern therapies add "only 2.4 months" of survival [34]. That figure is the median gain *per drug approval*, not the cumulative progress of oncology. US cancer mortality fell by roughly a third from 1991 to the early 2020s [35].

**The affect heuristic.** Words like "orthomolecular," "natural" and "non-toxic" make risk seem low and benefit seem high at the same time. Yet the protocol's 50,000 IU/day of vitamin D is about 12 times the US upper intake limit. Antioxidants that the paper suggests as optional add-ons have accelerated tumors in animal models [36], and vitamin E *increased* prostate cancer risk in the SELECT trial [37].

**Confirmation bias and WYSIATI** ("What You See Is All There Is") [6]. If a paper shows only supporting studies, the reader builds a confident story from whatever is in front of them and doesn't ask what is missing. The omitted negative trials in Section 3 are what is missing here.

---

## 5. What the paper gets right

Fair criticism should acknowledge the parts that hold up:

- **Metabolic reprogramming is a real hallmark of cancer**, and glutamine blockade is a legitimate area of research. Safer prodrugs of DON are now in early trials.
- **Pharmacologic (IV) vitamin C** has small positive signals in some settings. The criticism that oral dosing can't reach therapeutic blood levels is valid [26].
- **Daily, moderate-dose vitamin D** is associated with a modest reduction in cancer mortality in meta-analyses.
- **Exercise** has the strongest evidence of anything in the protocol. A 2025 randomized trial found structured exercise after colon cancer chemotherapy improved disease-free and overall survival [38].

None of these supporting findings depends on the MSCC theory being true. The parts of the protocol with real evidence have trials behind them. The parts that rely most on MSCC have the least human evidence.

The paper also says it plainly in its own discussion: *"comparative studies need to be conducted in both animals and humans to evaluate the effectiveness and safety of this hybrid protocol."* That sentence describes the paper's actual epistemic status: **a hypothesis, not a treatment.**

---

## 6. Why this matters beyond one paper

The stakes are not academic. Patients who used alternative medicine *instead of* conventional cancer treatment had about **2.5 times the risk of death** [16]. A protocol that offers "case studies of cures using monotherapy" can lead people to make exactly that substitution.

When you read any medical claim, published or not, five questions will catch most problems:

1. **What was the primary endpoint, and was the study powered for it?** If the headline comes from a subgroup or a post-hoc analysis, treat it as a hypothesis.
2. **What result would prove this wrong?** If the answer is "nothing," the claim isn't science yet.
3. **What is the base rate?** Most preclinical "cures" never work in people.
4. **What is missing?** Look for the large negative trials the author didn't cite.
5. **How long is the causal chain?** Every added link lowers the probability that the whole story is true.

A good theory sticks its neck out. As Popper put it, the scientific attitude is to seek out the observations that could refute you, not the ones that flatter you [3]. Applied to this paper, the strong claims of the theory have already failed those tests, and the remaining claims are hedged too heavily to be tested.

---

## References

1. Baghli I, Makis W, Marik PE, et al. Targeting the Mitochondrial-Stem Cell Connection in Cancer Treatment: A Hybrid Orthomolecular Protocol. *J Orthomol Med.* 2024;39(3).
2. Popper KR. *The Logic of Scientific Discovery.* London: Hutchinson; 1959.
3. Popper KR. *Conjectures and Refutations: The Growth of Scientific Knowledge.* London: Routledge; 1963.
4. Tversky A, Kahneman D. Extensional versus intuitive reasoning: the conjunction fallacy in probability judgment. *Psychol Rev.* 1983;90(4):293–315.
5. Hay M, Thomas DW, Craighead JL, Economides C, Rosenthal J. Clinical development success rates for investigational drugs. *Nat Biotechnol.* 2014;32(1):40–51.
6. Kahneman D. *Thinking, Fast and Slow.* New York: Farrar, Straus and Giroux; 2011.
7. Ioannidis JPA. Why most published research findings are false. *PLoS Med.* 2005;2(8):e124.
8. Button KS, Ioannidis JPA, Mokrysz C, et al. Power failure: why small sample size undermines the reliability of neuroscience. *Nat Rev Neurosci.* 2013;14(5):365–376.
9. Gelman A, Carlin J. Beyond power calculations: assessing Type S (sign) and Type M (magnitude) errors. *Perspect Psychol Sci.* 2014;9(6):641–651.
10. Manson JE, Cook NR, Lee IM, et al. Vitamin D supplements and prevention of cancer and cardiovascular disease. *N Engl J Med.* 2019;380(1):33–44.
11. Chandler PD, Chen WY, Ajala ON, et al. Effect of vitamin D3 supplements on development of advanced cancer: a secondary analysis of the VITAL randomized clinical trial. *JAMA Netw Open.* 2020;3(11):e2025850.
12. Urashima M, Ohdaira H, Akutsu T, et al. Effect of vitamin D supplementation on relapse-free survival among patients with digestive tract cancers: the AMATERASU randomized clinical trial. *JAMA.* 2019;321(14):1361–1369.
13. Kanno K, Akutsu T, Ohdaira H, Suzuki Y, Urashima M. Effect of vitamin D supplements on relapse or death in a p53-immunoreactive subgroup with digestive tract cancer: post hoc analysis of the AMATERASU randomized clinical trial. *JAMA Netw Open.* 2023;6(8):e2328886.
14. Gelman A, Loken E. The statistical crisis in science. *Am Sci.* 2014;102(6):460–465.
15. Lakatos I. *The Methodology of Scientific Research Programmes.* Cambridge: Cambridge University Press; 1978.
16. Johnson SB, Park HS, Gross CP, Yu JB. Use of alternative medicine for cancer and its impact on survival. *J Natl Cancer Inst.* 2018;110(1):121–124.
17. Guzzo CA, Furtek CI, Porras AG, et al. Safety, tolerability, and pharmacokinetics of escalating high doses of ivermectin in healthy adult subjects. *J Clin Pharmacol.* 2002;42(10):1122–1133.
18. Hensley CT, Faubert B, Yuan Q, et al. Metabolic heterogeneity in human lung tumors. *Cell.* 2016;164(4):681–694.
19. Faubert B, Li KY, Cai L, et al. Lactate metabolism in human lung tumors. *Cell.* 2017;171(2):358–371.
20. Lagadinou ED, Sach A, Callahan K, et al. BCL-2 inhibition targets oxidative phosphorylation and selectively eradicates quiescent human leukemia stem cells. *Cell Stem Cell.* 2013;12(3):329–341.
21. Pollyea DA, Stevens BM, Jones CL, et al. Venetoclax with azacitidine disrupts energy metabolism and targets leukemia stem cells in patients with acute myeloid leukemia. *Nat Med.* 2018;24(12):1859–1866.
22. DiNardo CD, Jonas BA, Pullarkat V, et al. Azacitidine and venetoclax in previously untreated acute myeloid leukemia. *N Engl J Med.* 2020;383(7):617–629.
23. Tan AS, Baty JW, Dong LF, et al. Mitochondrial genome acquisition restores respiratory function and tumorigenic potential of cancer cells without mitochondrial DNA. *Cell Metab.* 2015;21(1):81–94.
24. Creagan ET, Moertel CG, O'Fallon JR, et al. Failure of high-dose vitamin C (ascorbic acid) therapy to benefit patients with advanced cancer: a controlled trial. *N Engl J Med.* 1979;301(13):687–690.
25. Moertel CG, Fleming TR, Creagan ET, et al. High-dose vitamin C versus placebo in the treatment of patients with advanced cancer who have had no prior chemotherapy: a randomized double-blind comparison. *N Engl J Med.* 1985;312(3):137–141.
26. Padayatty SJ, Sun H, Wang Y, et al. Vitamin C pharmacokinetics: implications for oral and intravenous use. *Ann Intern Med.* 2004;140(7):533–537.
27. Wang F, He MM, Xiao J, et al. A randomized, open-label, multicenter, phase 3 study of high-dose vitamin C plus FOLFOX ± bevacizumab versus FOLFOX ± bevacizumab in unresectable untreated metastatic colorectal cancer (VITALITY study). *Clin Cancer Res.* 2022;28(19):4232–4239.
28. Goodwin PJ, Chen BE, Gelmon KA, et al. Effect of metformin vs placebo on invasive disease-free survival in patients with breast cancer: the MA.32 randomized clinical trial. *JAMA.* 2022;327(20):1963–1973.
29. Mansoori S, Fryknäs M, Alvfors C, et al. A phase 2a clinical study on the safety and efficacy of individualized dosed mebendazole in patients with advanced gastrointestinal cancer. *Sci Rep.* 2021;11:8981.
30. Tversky A, Kahneman D. Belief in the law of small numbers. *Psychol Bull.* 1971;76(2):105–110.
31. Tversky A, Kahneman D. Judgment under uncertainty: heuristics and biases. *Science.* 1974;185(4157):1124–1131.
32. Begley CG, Ellis LM. Raise standards for preclinical cancer research. *Nature.* 2012;483(7391):531–533.
33. Errington TM, Mathur M, Soderberg CK, et al. Investigating the replicability of preclinical cancer biology. *eLife.* 2021;10:e71601.
34. Ladanie A, Schmitt AM, Speich B, et al. Clinical trial evidence supporting US Food and Drug Administration approval of novel cancer therapies between 2000 and 2016. *JAMA Netw Open.* 2020;3(11):e2024406.
35. Siegel RL, Giaquinto AN, Jemal A. Cancer statistics, 2024. *CA Cancer J Clin.* 2024;74(1):12–49.
36. Sayin VI, Ibrahim MX, Larsson E, et al. Antioxidants accelerate lung cancer progression in mice. *Sci Transl Med.* 2014;6(221):221ra15.
37. Klein EA, Thompson IM Jr, Tangen CM, et al. Vitamin E and the risk of prostate cancer: the Selenium and Vitamin E Cancer Prevention Trial (SELECT). *JAMA.* 2011;306(14):1549–1556.
38. Courneya KS, Vardy JL, O'Callaghan CJ, et al. Structured exercise after adjuvant chemotherapy for colon cancer. *N Engl J Med.* 2025.

---

*If you found this useful, share it with someone who forwards "miracle cure" studies. The aim isn't cynicism about science. It's asking every claim, including the ones we like, how it could turn out to be wrong.*
