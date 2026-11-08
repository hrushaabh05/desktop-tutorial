# Lead Magnet: BESS Entry Readiness Scorecard

**File:** `bess-entry-readiness-scorecard.html`, a single self-contained page that can be hosted on any website or landing-page tool.
**Audience:** The five personas in `../syselec-bess-customer-persona.md`: mid-size and large companies planning to enter BESS as manufacturers, EPC/turnkey contractors, BOO bidders/owners, power-electronics OEMs or O&M service providers.

## How it works

1. The visitor picks their company type, which maps to one of the five personas.
2. They answer 8 questions on mandate, expertise, track record, partners, policy, financial modelling, offtake and timeline.
3. They instantly see a **readiness score out of 100** with a band (Explorer / Builder / Market-ready), a factor-by-factor chart, their **top 3 gaps**, and segment-specific market data and next decisions from the IESA September 2026 update.
4. **Lead capture:** to get the full **BESS Entry Plan**, the **India BESS Entry Playbook 2026** and a free 30-minute **BESS Entry Diagnostic** call, they submit name, work email, company, designation and revenue band. The lead record includes their persona, score, band and every answer, so sales can qualify and personalise the follow-up.

## Before going live

Edit the `CONFIG` block at the top of the `<script>`:
- `FORM_ENDPOINT`: your CRM or form-service URL (HubSpot form, n8n or Zapier webhook, etc.). Leads are POSTed as JSON.
- `CONTACT_EMAIL`: replace the placeholder `bess@syselec.example`. This is the email fallback used when no endpoint is set.

Also:
- Add Syselec's logo and privacy-policy link.
- Prepare the promised assets: the persona-specific PDF report and the *India BESS Entry Playbook 2026*.

## Promotion copy

**LinkedIn post**
> India's installed BESS capacity grew ~17× in nine months, from 0.8 GWh to 13.7 GWh, and 91 GWh of storage was tendered in 2026 alone. Yet ~20% of tendered capacity has been cancelled.
>
> If your company is planning to enter energy storage as a manufacturer, EPC, project owner, OEM or O&M provider, how ready are you really?
>
> Take Syselec's free 5-minute **BESS Entry Readiness Scorecard** and get your score, your best entry point and your top 3 gaps. [link]

**Email subject lines (A/B test):**
- "Is your company ready for India's 308 GWh storage market?"
- "5 minutes to your BESS entry score"
- "Before you bid your first BESS tender, read this"

**Follow-up sequence after a lead submits:**

| Day | Email |
|---|---|
| 0 | Full BESS Entry Plan PDF + Playbook + diagnostic-call booking link |
| 3 | Case-style insight tailored to their persona (e.g. "How to pre-qualify for PSU BESS EPC tenders without references" for the EPC persona) |
| 7 | Policy alert: what the proposed 2027 CEA grid-forming and 15% storage mandates mean for them |
| 14 | Reminder to book the diagnostic call, with the band-specific offer (Explorer: entry strategy sprint; Builder: gap-closure plan; Market-ready: bid/owner's-engineer support) |

**Sales routing tip:** Prioritise leads with revenue above INR 500 crore, a "Builder" or "Market-ready" band, and a timeline under 12 months.
