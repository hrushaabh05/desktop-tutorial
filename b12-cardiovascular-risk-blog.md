# Does Low B12 Really Raise Your Heart Risk? Putting a Popular Claim on Trial

*A test using Popper's falsification and Kahneman and Tversky's work on cognitive bias*

---

## The claim

You've probably seen it on a supplement label or a wellness blog: **"Low vitamin B12 increases your risk of heart disease."**

The story is tidy. B12, along with folate and B6, helps the body clear an amino acid called **homocysteine**. Low B12 means higher homocysteine. High homocysteine damages blood vessel walls, which leads to atherosclerosis and then to heart attacks and strokes. So topping up your B12 should protect your heart.

It sounds right. That is exactly why it needs testing.

In this post I don't try to prove the claim. I try to break it. Karl Popper argued [15] that the way to learn whether an idea is true is to expose it to tests it could fail. Daniel Kahneman and Amos Tversky showed [13] that our intuitions about what "sounds right" go wrong in predictable ways. Together they give a useful method: **find the biases that make the claim feel convincing, then look for the evidence that could disprove it.**

---

## Part 1: Why the claim feels true (the Kahneman–Tversky audit)

Before looking at any data, it helps to ask why we find this claim believable in the first place.

### 1. The representativeness trap: a good story feels like good evidence

The B12 → homocysteine → damaged arteries → heart attack chain *looks like* how disease should work. Kahneman and Tversky showed that we judge probability by how well something fits a mental prototype, not by how often it is actually true [13]. A detailed mechanism feels more likely precisely because it is detailed.

### 2. The conjunction fallacy: more steps should mean less confidence

The famous "Linda problem" showed that people rate "A and B" as more likely than "A" alone when the combined story is more vivid. That is mathematically impossible [14].

The B12 claim is a conjunction of several links:

| Link | Must be true |
|---|---|
| 1 | Low B12 meaningfully raises homocysteine in typical people |
| 2 | Homocysteine *causes* vascular damage (rather than just marking it) |
| 3 | That damage is large enough to change event rates |
| 4 | Raising B12 reverses the process |

Even if each link were 70% likely, the whole chain would be about **0.7⁴ ≈ 24%** likely. Each extra step in the story makes it *feel* more convincing while making it *less* probable.

### 3. Availability: the vivid origin story

The hypothesis began in 1969, when pathologist Kilmer McCully described children with **homocystinuria**, a rare genetic disorder that causes extremely high homocysteine. They had severe, early atherosclerosis [16]. Those cases are dramatic and easy to remember. But homocysteine levels in homocystinuria are often 10 or more times normal, while the "mildly high" levels seen in the general population are just a few µmol/L above average. Reasoning from an extreme, memorable case to everyday variation is the availability heuristic at work.

### 4. Base-rate neglect: surrogate markers fail often

The claim quietly assumes that lowering a biomarker lowers disease. The base rate for that assumption is poor. Raising HDL with CETP inhibitors, suppressing arrhythmias with antiarrhythmic drugs (the CAST trial [17]), and taking antioxidant vitamins (beta-carotene, vitamin E) all improved a marker or fit a plausible mechanism, and all failed to help or caused harm in trials. Any surrogate-based claim should start with a sceptical prior.

### 5. Confounding, and "What You See Is All There Is"

People with low B12 tend to be older, to have kidney disease (which raises homocysteine on its own), to have poorer diets, to smoke more, and to take drugs like metformin or acid suppressants. Kahneman's **WYSIATI** describes how we build a confident story from the data in front of us without asking what is missing. An observed association between low B12 and heart disease says nothing, by itself, about cause.

**Verdict of the bias audit:** Our confidence in the claim comes mostly from how coherent the story is, not from evidence. Now we test it.

---

## Part 2: Making the claim falsifiable (the Popperian setup)

For Popper, a claim is scientific only if we can say in advance **what result would prove it wrong.** So let's commit to predictions before looking:

> **H (causal claim):** Low B12 causally increases cardiovascular risk, largely by raising homocysteine.

If H is true, we should observe:

- **P1:** Higher homocysteine is associated with more cardiovascular events in cohort studies.
- **P2:** Randomised trials that lower homocysteine with B vitamins (including B12) reduce cardiovascular events.
- **P3:** People who are *genetically* prone to higher homocysteine (an unconfounded "natural experiment") have more heart disease.
- **P4:** B-vitamin treatment should not *cause* harm to the cardiovascular system.

P1 is a weak test, since confounding can produce it even if H is false. **P2 and P3 are the severe tests**: they could clearly fail if H is wrong. Popper would say they are the ones that matter.

---

## Part 3: The evidence

### P1 — Observational association: ✅ Passed (but this is the easy test)

The **Homocysteine Studies Collaboration** (JAMA, 2002), a meta-analysis of prospective studies, found that a 25% lower homocysteine level (about 3 µmol/L) was associated with roughly **11% lower ischaemic heart disease risk** and **19% lower stroke risk** [1].

So the association is real. But as we saw, confounding and reverse causation (vascular and kidney disease can raise homocysteine) are serious problems. Passing P1 corroborates very little.

### P2 — Randomised controlled trials: ❌ Failed

This is where the hypothesis meets a severe test. Starting in the late 1990s, large trials gave people folic acid, **B12**, and often B6. Homocysteine dropped by about 20–30%, just as intended. Cardiovascular events did not.

| Trial | Population | B vitamins | Result on major CV events |
|---|---|---|---|
| **VISP** (JAMA 2004) [2] | ~3,700 stroke patients | High- vs low-dose folate/B6/B12 | No difference |
| **NORVIT** (NEJM 2006) [3] | ~3,750 post-heart-attack | Folate + B12 ± B6 | No benefit; combined arm trended toward **harm** (RR ≈ 1.22) |
| **HOPE-2** (NEJM 2006) [4] | ~5,500 with vascular disease or diabetes | Folate + B6 + B12 (1 mg) | RR 0.95 (no significant effect); stroke modestly lower |
| **WAFACS** (JAMA 2008) [5] | ~5,400 high-risk women | Folate + B6 + B12 | No effect |
| **SEARCH** (JAMA 2010) [6] | ~12,000 heart-attack survivors | Folate 2 mg + B12 1 mg | RR 1.04 (no effect) |
| **VITATOPS** (Lancet Neurol 2010) [7] | ~8,200 stroke/TIA patients | Folate + B6 + B12 | RR 0.91 (borderline, not significant) |

Pooled analyses confirm the pattern:

- **Clarke et al. (Arch Intern Med, 2010):** 8 trials and about 37,000 participants. Homocysteine fell by about 25%, and the risk ratio for major vascular events was **1.01 (95% CI 0.97–1.05)**, essentially zero effect [9].
- **Cochrane review (Martí-Carvajal et al., 2017):** no effect on heart attack (RR ≈ 1.02) and a small possible reduction in stroke (RR ≈ 0.90) [12]. The stroke signal comes mostly from folic acid in populations without food fortification (for example, the Chinese **CSPPT** trial, which used folic acid *without* B12 [11]).

The prediction was clear: lower homocysteine, fewer events. The intervention reliably lowered homocysteine, and **the predicted outcome did not appear.** In Popperian terms, the mechanistic hypothesis has been **refuted by a severe test**.

### P3 — Mendelian randomisation (nature's trial): ❌ Failed

People with the **MTHFR 677TT** genotype have lifelong homocysteine levels that are about 20–25% higher. Because genes are assigned at conception, this variant works like a natural randomised trial, free of most lifestyle confounding.

Early published studies seemed to show a link with heart disease. But a large analysis by **Clarke et al. (PLoS Medicine, 2012)**, which included about 48,000 cases and 68,000 controls from *previously unpublished* datasets, found **no association** (OR ≈ 1.02) [10]. The apparent effect in earlier studies was largely explained by **publication bias**. Mendelian randomisation studies of genetically predicted B12 levels have likewise found no convincing causal link with coronary artery disease.

Here a Kahneman–Tversky lesson meets a Popperian one: the "confirming" literature was itself a biased sample, the published studies being the ones that told the good story.

### P4 — No harm: ⚠️ Failed in at least one setting

In the **DIVINe trial** (JAMA, 2010), people with diabetic kidney disease received high-dose folate, B6, and B12 (as cyanocobalamin). They had **faster kidney function decline** and roughly **double the rate of vascular events** (HR ≈ 2.0) compared with placebo [8]. One plausible explanation is that cyanocobalamin is poorly handled in kidney disease. Either way, a simple "more B vitamins means healthier arteries" model did not predict this.

---

## Part 4: The rescue attempts (and why Popper would be wary)

When a favoured hypothesis fails, defenders often add **auxiliary hypotheses** to save it. Popper called these *ad hoc* moves [15], and Imre Lakatos described a research programme that keeps patching itself instead of making new successful predictions as *degenerating* [18]. The common defences are:

1. **"The trials were too short."** Several ran for 5–7 years, and SEARCH ran for about 7. The expected effect from the cohort data should have been visible.
2. **"Folate fortification masked the effect."** This might explain some stroke data. But many trials (NORVIT, HOPE-2, SEARCH in the UK) were run in largely unfortified populations, and they still found no heart benefit.
3. **"The patients already had disease, so it was too late."** WAFACS and parts of HOPE-2 included primary-prevention participants, with the same null result.
4. **"Homocysteine isn't the mechanism; B12 works some other way."** That is possible, but it is a *new* hypothesis without independent support. It replaces the original causal story rather than rescuing it.

Each defence can be argued, but none made a new prediction that was later confirmed. That is the signature of a degenerating programme.

---

## Part 5: What survives?

Applying the claim honestly, here is where it stands:

| Version of the claim | Status |
|---|---|
| *"Low B12 is associated with higher cardiovascular risk."* | **Corroborated, but weak.** Explained largely by confounding and reverse causation. |
| *"Low B12 causes heart disease via homocysteine, and supplements prevent it."* | **Falsified** by large RCTs and Mendelian randomisation. |
| *"B vitamins (mainly folic acid) may modestly reduce stroke in folate-poor populations."* | **Plausible, limited.** Driven by folate, not B12. |
| *"Correcting genuine, clinically significant B12 deficiency improves cardiovascular outcomes."* | **Untested.** Most trials enrolled people with normal B12. This is the one remaining open question. |

Note what happened to the claim. To survive, it had to shrink to a narrow, specific form: *frank deficiency* rather than *low-normal levels*, and *possibly* rather than *proven*. In Popper's terms, the surviving claim has much less empirical content. It says far less about the world, which is why it is harder to refute.

---

## So, should you care about your B12?

**Yes, but not for your heart.**

Genuine B12 deficiency is serious and worth treating. It can cause anaemia, irreversible nerve damage, cognitive problems, and fatigue. People at higher risk include older adults, vegans and vegetarians, people with pernicious anaemia or gut surgery, and long-term users of metformin or acid-suppressing drugs. If you are in one of these groups, ask your doctor about testing.

But taking B12 supplements to **prevent heart attacks** is not supported by the best available evidence. If heart health is your goal, the interventions with strong trial evidence are well known: blood pressure control, lowering LDL cholesterol, not smoking, physical activity, and managing diabetes.

---

## The bigger lesson

The B12–heart story is a case study in how a reasonable idea can mislead for decades:

- A **vivid origin** (availability)
- A **coherent mechanism** (representativeness, conjunction fallacy)
- A **confounded association** (WYSIATI)
- A **publication-biased literature** (confirmation bias at scale)

What eventually settled the question was not a better story but a **test the hypothesis could fail**. It failed.

> *"The game of science is, in principle, without end. He who decides one day that scientific statements do not call for any further test... retires from the game."*
> — Karl Popper, *The Logic of Scientific Discovery* [15]

The habit is worth practising on the next health claim that seems obviously true: ask what result would prove it wrong, and then check whether anyone has looked.

---

### References

*Numbers in square brackets in the text refer to the list below.*

1. Homocysteine Studies Collaboration. Homocysteine and risk of ischemic heart disease and stroke: a meta-analysis. *JAMA*. 2002;288:2015–2022.
2. Toole JF et al. (VISP). *JAMA*. 2004;291:565–575.
3. Bønaa KH et al. (NORVIT). *N Engl J Med*. 2006;354:1578–1588.
4. Lonn E et al. (HOPE-2). *N Engl J Med*. 2006;354:1567–1577.
5. Albert CM et al. (WAFACS). *JAMA*. 2008;299:2027–2036.
6. SEARCH Collaborative Group. *JAMA*. 2010;303:2486–2494.
7. VITATOPS Trial Study Group. *Lancet Neurol*. 2010;9:855–865.
8. House AA et al. (DIVINe). *JAMA*. 2010;303:1603–1609.
9. Clarke R et al. Effects of lowering homocysteine levels with B vitamins on cardiovascular disease, cancer, and cause-specific mortality. *Arch Intern Med*. 2010;170:1622–1631.
10. Clarke R et al. Homocysteine and coronary heart disease: meta-analysis of MTHFR case-control studies, avoiding publication bias. *PLoS Med*. 2012;9:e1001177.
11. Huo Y et al. (CSPPT). *JAMA*. 2015;313:1325–1335.
12. Martí-Carvajal AJ et al. Homocysteine-lowering interventions for preventing cardiovascular events. *Cochrane Database Syst Rev*. 2017;8:CD006612.
13. Tversky A, Kahneman D. Judgment under uncertainty: heuristics and biases. *Science*. 1974;185:1124–1131.
14. Tversky A, Kahneman D. Extensional versus intuitive reasoning: the conjunction fallacy. *Psychol Rev*. 1983;90:293–315.
15. Popper K. *The Logic of Scientific Discovery*. London: Hutchinson; 1959. / *Conjectures and Refutations*. London: Routledge; 1963.
16. McCully KS. Vascular pathology of homocysteinemia: implications for the pathogenesis of arteriosclerosis. *Am J Pathol*. 1969;56:111–128.
17. Echt DS et al. (CAST). Mortality and morbidity in patients receiving encainide, flecainide, or placebo. *N Engl J Med*. 1991;324:781–788.
18. Lakatos I. Falsification and the methodology of scientific research programmes. In: Lakatos I, Musgrave A, eds. *Criticism and the Growth of Knowledge*. Cambridge University Press; 1970:91–196.

*This article is for educational purposes and isn't medical advice. Talk to your doctor before starting or stopping supplements.*
