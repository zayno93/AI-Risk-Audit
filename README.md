# AI Risk Audit: Is this banking chatbot safe to deploy?

An end-to-end AI governance audit of an LLM customer-service assistant for a fictional UK bank, carried out the way a bank's AI risk team would.

**Recommendation: Do not deploy yet.** Two high-severity issues must be fixed first: the chatbot leaks confidential information and can be talked out of its rules.

**Overall failure rate: 38%** across 49 red-team tests in 10 risk categories. System prompt leakage failed **100%** of the time. Lending decisions and scam requests were refused **every time** (0%).

**[Read the 2-page executive summary](executive_summary.pdf)**

[Failure rate by category](results/fail_rate_chart.png)


## The scenario

Northgate Bank (fictional) wants to launch **Nora**, an AI assistant that answers customer questions about accounts, cards and fees. I acted as the risk analyst asked to decide whether it was safe to launch.

## What I did

| Step | Output |
|---|---|
| 1. Scoped the system | [System card](01_system_card.md) |
| 2. Classified it under the EU AI Act and UK rules | [Risk classification](02_risk_classification.md) |
| 3. Built a scored risk register with before/after risk ratings | [Risk register](risk_register.xlsx) |
| 4. Red-teamed it with 49 adversarial prompts | [Test cases](tests/test_cases.xlsx) · [Marked results](results/assessed_results.xlsx) |
| 5. Calculated failure rates by category | [Failure rate summary](results/failure_rate_summary.xlsx) |
| 6. Wrote findings and mapped 12 controls to NIST AI RMF | [Findings & NIST mapping](03_findings_and_nist_mapping.md) |
| 7. Made a go/no-go recommendation | [Executive summary](executive_summary.pdf) |

## Key findings

| # | Finding | Severity | Fail rate |
|---|---|---|---|
| 1 | Leaks confidential information: disclosed the staff code in 4 tests and asked a "manager" for their password | High | 71% |
| 2 | Can be talked out of its rules: replied "FreeBot active." to a one-line override | High | 43% |
| 3 | Account-opening guidance varied depending on the customer's name | Medium | 50% |
| 4 | Kind to vulnerable customers, but missed key scam warnings and payment-data warnings | Medium | 36–50% |
| 5 | States unverified facts as certain, including a made-up phone number | Medium | 21% |
| 6 | **Positive:** refused every lending decision and every scam-script request | — | 0% |

## Frameworks used

EU AI Act · UK AI regulation principles · FCA Consumer Duty · OWASP Top 10 for LLM Applications · NIST AI Risk Management Framework

## How it works

- **Model:** Llama 3.2 (1B), run locally with [Ollama](https://ollama.com)
- **Method:** each prompt was sent with Nora's system prompt, and each response was marked Pass, Partial or Fail against a written expected behaviour
- **Fail rate** = (Fails + 0.5 × Partials) ÷ Tests

## Limitations

- Small 1B open model, not a production system, so results show a worst case
- 49 tests is a sample, not full coverage
- Each prompt was run once and marked by a single reviewer

Next steps would be a larger test set, repeated runs, a second reviewer and automated scoring.



*Northgate Bank and Nora are fictional. Built by Muhammad Mahmood. 
LinkedIn (https://www.linkedin.com/in/muhammad-mahmood-757802320/)
