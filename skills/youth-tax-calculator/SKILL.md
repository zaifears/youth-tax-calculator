---
name: youth-tax-calculator
description: Comprehensive Bangladesh individual income tax calculation and filing assistant for the NBR e-Return portal (etaxnbr.gov.bd). Tailored for students, interns, fresh graduates, and young employees entering the tax net under the Income Tax Act 2023. Incorporates the official NBR eReturn System User Manual, zero-difference balance sheet reconciliation (IT-10B / IT-10BB), multi-broker capital loss carry-forward (Section 70), student stipends, Islamic P2P financing (Biniyog.io), mutual funds (EDGE AMC), high bank turnover defense, and audit protection.
---

# Bangladesh Youth Tax Calculator & Filing Expert (`youth-tax-calculator`)
### Authoritative Guide for Students, Interns, Fresh Graduates & First-Time Employees on `etaxnbr.gov.bd`

---

## 1. Identity & System Overview

The **`youth-tax-calculator`** is an expert tax advisory skill engineered for young individuals entering the formal taxation net in Bangladesh under the **Income Tax Act 2023 (ITA 2023)** and the prevailing **Finance Act**.

It synthesizes:
1. **Statutory Tax Laws:** ITA 2023, S.R.O.s, Sixth Schedule (Parts 1 & 2), and annual Finance Act slabs.
2. **Official NBR User Manual:** Exact UI architecture, screen-by-screen navigation, form validations, and system constraints from the National Board of Revenue's official *eReturn System User Manual* (`UserManualEN.pdf`) and *Special Registration Guidelines* (`Special_Registration.pdf`).
3. **Youth Reality Adaptation:** Solutions for academic stipends, competition prize pools, parental support transfers, Islamic P2P investments (Biniyog.io), mutual funds, brokerage accounts, and high bank turnover reconciliation.

---

## 2. Statutory Foundations & Current Rates (AY 2026–2027)

### A. Tax-Free Exemption Ceilings (General & Special)
| Category | Tax-Free Threshold | Statutory Basis |
| :--- | :---: | :--- |
| **General Taxpayers (Male / Young Professionals)** | **BDT 3,50,000 – 4,00,000** | Finance Act Standard |
| **Female Taxpayers & Senior Citizens (Aged 65+)** | **BDT 4,00,000 – 4,50,000** | Finance Act Standard |
| **Persons with Disabilities / Third Gender** | **BDT 4,75,000 – 5,25,000** | Finance Act Standard |
| **Gazetted War-Wounded Freedom Fighters** | **BDT 5,00,000 – 5,50,000** | Finance Act Standard |
| **Parent/Legal Guardian of Disabled Child** | **+ BDT 50,000 per child** | Additional Allowance |

### B. Progressive Tax Slabs & Rates
For taxable income exceeding the tax-free threshold:
| Taxable Income Slab | Tax Rate | Cumulative Max Tax in Slab |
| :--- | :---: | :---: |
| **First Tier (Tax-Free Threshold)** | **0%** | BDT 0 |
| **Next BDT 1,00,000 / 3,00,000** | **5% / 10%** | Slabs per Finance Act |
| **Next BDT 3,00,000 / 4,00,000** | **10% / 15%** | Progressively graduated |
| **Next BDT 4,00,000 / 5,00,000** | **15% / 20%** | Progressively graduated |
| **Next BDT 5,00,000 / 20,00,000** | **20% / 25%** | Progressively graduated |
| **Remaining Balance** | **25% / 30%** | Top marginal slab |

### C. The Minimum Tax Floor Rules (Official Manual Page 67)
* **Dhaka & Chattogram City Corporation areas:** BDT 5,000
* **Other City Corporations:** BDT 4,000
* **Non-City Corporation Municipal / Rural areas:** BDT 3,000
* ⚠️ **CRUCIAL RULE FOR YOUTH & STUDENTS:** Minimum tax **only applies if Total Taxable Income exceeds the tax-free exemption threshold**. If your taxable income is equal to or less than the threshold (e.g., student earning BDT 25,000 salary where taxable part is BDT 16,667 $\le$ 3,50,000), total tax payable is strictly **BDT 0.00**. Minimum tax is **NEVER** charged on income below the tax-free limit!

---

## 3. Statutory Deductions & Exemptions for Youth

| Income Type | Statutory Citation | Tax Treatment | e-Return Portal Input Method |
| :--- | :--- | :--- | :--- |
| **Employment / Internship Salary** | Section 32; Sixth Schedule | Lower of **1/3rd gross salary** or **BDT 4,50,000** is exempt | Enter gross Basic Salary in Schedule 1; system auto-computes 1/3rd deduction |
| **University Stipend / Scholarship** | Sixth Schedule, Part 1, Para 8 | **100% Tax-Exempt** | Select `Tax Exempted Income: Yes` on Screen 1; disclose under Para `Any Other Exemption` |
| **Parental Gift / Family Support** | Section 56(g) | **100% Non-Taxable** | Enter in IT-10B under `Source of Fund` $\rightarrow$ `Other Receipts` (Manual Page 60) |
| **Bank Profit / Savings Interest** | Section 35 | Taxable; claim bank TDS credit | Disclose under `Financial Assets` $\rightarrow$ `Interest/Profit (Bank/FI)`; enter TDS |
| **Cash Dividends** | Section 35 | Taxable; claim 10%/15% TDS | Disclose under `Financial Assets` $\rightarrow$ `Dividend (Any kind)`; claim TDS |
| **Islamic P2P Markup (Biniyog.io)** | Section 35 / 38 | Taxable profit only | Disclose under `Interest From Any Other Securities/Financial Assets` |
| **Stock Capital Gains / Losses** | Sections 57, 70, 72 | Gains taxed/exempt; Losses carried forward | Disclose under `Capital Gains` $\rightarrow$ `Transfer of share of listed Company` |
| **Hackathon / Case Competition** | Section 38 | Taxable (user's net share only) | Disclose under `Other Sources` $\rightarrow$ `Any Other Income` |

---

## 4. Investment Tax Rebate Formula (Schedule 5)

Under the Sixth Schedule (Part 2), tax rebates on eligible investments are calculated as:

$$\text{Rebate} = \min \begin{cases} 
15\% \text{ (or prevailing rate)} \times \text{Eligible Investment} \\ 
3\% \times \text{Total Taxable Income} \\ 
\text{BDT } 10,00,000 \text{ (Absolute Statutory Cap)} 
\end{cases}$$

### Eligible Youth Investment Categories:
1. **Open-End / Closed-End Mutual Funds:** SEC-approved funds (e.g., EDGE Al-Amin Shariah Consumer Fund, Shanta, LankaBangla). Enter at purchase cost.
2. **Deposit Pension Scheme (DPS):** Allowable actual deposits up to **BDT 1,20,000** per year.
3. **Listed Stocks & Securities:** Purchases in secondary market (shares held at year-end).
4. **Life / Health Insurance Premiums:** Up to 10% of the insurance policy sum assured.
5. **Government Zakat Fund / Approved Philanthropic Contributions:** 100% eligible.

> [!NOTE]
> Tax rebate directly reduces tax liability. However, a rebate **cannot create a negative tax liability or generate a tax refund by itself**. Refunds only arise from excess TDS (Tax Deducted at Source) or AIT (Advance Income Tax) paid.

---

## 5. Official NBR e-Return UI/UX & Technical Constraints
*(Derived from the NBR eReturn System User Manual)*

### A. Technical Pre-requisites
* **Portal URL:** `https://etaxnbr.gov.bd`
* **Supported Devices:** Laptop or Desktop computer with minimum 1366×768 screen resolution. (NBR officially advises against using mobile smartphones due to modal overlay clipping and dropdown misfiring).
* **Browser Compatibility:** Google Chrome, Microsoft Edge, Mozilla Firefox.
* **NID-Verified Mobile Number:** The registration SIM **must be biometrically registered against the taxpayer's own NID**. If registered under a parent's NID, registration will fail.

### B. Special Registration for Overseas Bangladeshis / NRBs (Manual Appendix)
Expatriate Bangladeshis or students abroad without a BD biometric SIM can register by emailing `ereturn@etaxnbr.gov.bd` with:
1. Current country of residence and foreign mailing address.
2. Active overseas cell phone number.
3. High-resolution scan of Bangladeshi NID / Smart Card.
4. Copy of Bangladeshi passport (bio pages) and valid visa page.
5. Passport-sized photograph.
*NBR verifies the email and issues a secure registration link valid for 7 days.*

### C. Critical UI Quirks & Portal Behavior
1. **Single Page Application (SPA) Trap:** The portal runs on Angular. Do NOT use the browser's Back/Forward buttons or refresh the page (`F5`) without saving, as unsaved form state will be purged. Always click **Save & Continue** or **Save as Draft**.
2. **The "Green Tick" (✓) Requirement:** In dropdown forms—especially under **Capital Gains** (`Transfer of share of listed Company`) and **Financial Assets**—selecting an item from the dropdown displays a small **green checkmark icon (✓)** next to it. You **MUST click the green tick** to mount and render the form input fields!
3. **The "Tax Exempted Income" Navigation Lock:** If you have tax-free income (e.g., university stipend, remittances), you **must select `Yes`** for *"Any income which is fully exempted from tax?"* on Screen 1. If left as `No`, the entire `Tax Exempted Income` left-hand tab remains invisible and inaccessible.
4. **Whole Integer Enforcement:** The system strictly rejects decimals or paisa. All currency figures must be rounded to the nearest integer.
5. **No Negative Total Income:** Total income across all heads cannot be less than zero. Realized capital losses cannot create negative total income; they must be carried forward under Section 70.

---

## 6. Screen-by-Screen Filing Workflow on `etaxnbr.gov.bd`

### Screen 1: Assessment Information
* **Return Scheme:** `Self` (Section 180 / Universal Self).
* **Assessment Year:** Select current AY (e.g., `2026-2027`).
* **Income Year:** Pre-filled (e.g., `01/07/2025 to 30/06/2026`).
* **Resident Status:** `Resident` (Standard for citizens living in BD $\ge$ 182 days).
* **Any income which is fully exempted from tax?** Select **`Yes`** *(Essential to disclose student stipends)*.
* **Heads of Income:** Select **`Yes`**, then tick relevant heads:
  * ☑ `Income from Employment` (if contracted intern / salaried)
  * ☑ `Income from Financial Assets` (bank interest, dividends, P2P profit)
  * ☑ `Capital Gains` (stock trading realized gain/loss)
  * ☑ `Income from Other Sources` (case competitions, consulting, freelance)
* Click **Save & Continue**.

### Screen 2: Additional Information & IT-10B Criteria
* **Location of Main Source of Income:** Select your City Corporation (e.g., `Dhaka South City Corporation`).
* **Any Claim for Tax Rebate for Investment?** Select **`Yes`**.
* **Mandatory IT-10B Asset Statement Prompts:**
  * *Total Gross Wealth exceeds BDT 50,00,000?* Change default "Yes" to **`No`**.
  * *Own Motor Car?* `No` | *Offshore Property?* `No` | *Company Director?* `No` | *House Property/Apartment in City Corp?* `No`.
  * **Portal Prompt:** *"IT10B is not mandatory for you. Still want to submit?"* $\rightarrow$ Select **`Yes`**.
    *(Filing IT-10B voluntarily creates an unbroken legal paper trail, shields you against future bank turnover audits, and whitens accumulated capital)*.
* Click **Save & Continue**.

### Screen 3: Income Details

#### 1. Income from Employment (Schedule 1)
* Select `Private/Other than Government Pay Scale`.
* Enter Employer Name (e.g., `IFA Consultancy`, `bKash Limited`).
* Enter `Basic Salary`. For interns without salary breakdown, enter total stipend received under Basic Salary.
* Allowances default to `0`.
* The portal automatically deducts $\min(\frac{1}{3} \text{ Salary}, \text{BDT } 4,50,000)$ as tax-exempt!
* Click `+ Add Employment` to add multiple internships/jobs during the income year.

#### 2. Income from Financial Assets (Section 35)
* **Bank / FI Interest:** Select `Interest/Profit (Bank/FI)`. Enter Bank Name, Account Number, Gross Interest Credited, Bank Charges/Fees (`0`), and TDS Deducted.
* **Dividends:** Select `Dividend (Any kind)`. Enter Company/Fund Name, BO Account Number, Gross Dividend, and TDS Deducted.
* **Islamic P2P Crowdfunding:** Select `Interest From Any Other Securities/Financial Assets`. Enter platform name (e.g., `biniyog.io / Pure Fintech Ltd`), description, and net profit markup.

#### 3. Capital Gains (Sections 57, 70, 72)
* Select `Transfer of share of listed Company (Individual)`.
* 💡 **Click the Green Checkmark (✓)** to render the inputs.
* Enter BO ID (16 digits), Broker Name, Client Code, and Date.
* Enter Gross Realized Gain or Loss. **Negative numbers (e.g., `-3924`) are accepted!**
* If you trade across multiple brokers, click `+ Add Another Category` to list each broker's net realized figure.
* Net capital losses cannot be offset against salary or bank interest; the portal backend auto-routes unabsorbed losses to `Loss Not Set Off - Section 70`.

#### 4. Income from Other Sources (Section 38)
* Select `Any Other Income`.
* **Competition / Hackathon Prize Money:** When prize money clears into a team leader's account, declare **only your individual proportionate share** (e.g., 1/4th of BDT 1,10,000 = BDT 27,500).
* Retain bank statements demonstrating the immediate outward disbursement of the remaining shares to your teammates.

#### 5. Tax Exempted Income
* Select `Other Exemption under 6th Schedule Part 1`.
* In the Paragraph dropdown, select `Any Other Exemption Under 6th Schedule Part 1`.
* Enter Description: `Student Stipend to Meet Cost of Education`.
* Enter Source/Particulars: `[University Name] Student Scholarship & Stipend` (e.g. BUP).
* Enter Amount: (e.g., `18,000`).

*Click **Save & Continue**.*

### Screen 4: Tax Rebate (Schedule 5)
* Tick ☑ **`Unit Certificate/Mutual Fund/ETF/Joint Investment Scheme`**.
* Enter Open-End Mutual Fund Name (e.g., `EDGE Al-Amin Shariah Consumer Fund`), BO Account Number, and purchase cost.
* ⚠️ **Do NOT double-count:** If open-end mutual fund units are held inside a brokerage BO account, declare them ONLY under Mutual Funds, NOT again under `Listed Stocks or Shares`.
* If you maintain a DPS, tick `Deposit Pension Scheme (DPS)` and enter bank name, account number, and yearly deposits (up to BDT 1,20,000).
* Click **Save & Continue**.

### Screen 5: Expenditure Statement (Form IT-10BB)
For youth and students with total income $\le$ BDT 5,00,000 without cars or city corporation real estate, IT-10BB is optional, but filing a realistic statement is best practice.

**Realistic & Defensible Youth Expenditure Breakdown:**
| Category | Realistic Annual Range | Sample Entry | Rationale / Comments |
| :--- | :---: | :---: | :--- |
| **Personal & Food Expenses** | BDT 40,000 – 80,000 | `60000` | Living with family; personal meal expenses |
| **Accommodation Expenses** | BDT 0 | `0` | Residing in family home (Comment: `Living with Family`) |
| **Transport Expenses** | BDT 15,000 – 30,000 | `20000` | Metro Rail, public transit, bus, ride-sharing |
| **Utility Expenses** | BDT 6,000 – 15,000 | `10000` | Mobile recharge, home internet share |
| **Education Expenses** | Exact fees paid | `55000` | University semester tuition + professional exams (BUP / ICAB) |
| **Festivals & Recreation** | BDT 10,000 – 30,000 | `20000` | Eid gifts, personal books, clothing |
| **Misc. & Outflow** | BDT 5,00,0 – 10,000 | `5000` | Incidentals and stationery |
| **Total Living Expenditure** | **BDT 1,30,000 – 2,20,000** | **BDT 1,70,000** | Balanced against total receipts |

*Click **Save & Continue**.*

### Screen 6: Assets & Liabilities (Form IT-10B)

#### 1. Assets
* **Financial Assets:**
  * Listed Shares / Mutual Funds: Enter acquisition cost (e.g., `28956`).
  * Other Financial Assets: Enter P2P principal (e.g., Biniyog.io active campaigns: `199178`).
* **Cash & Fund Outside Business:**
  * Enter aggregate liquid balance as of **30 June** across:
    - Cash in hand
    - Bank accounts (closing ledger balances from bank tax certificates)
    - Mobile Financial Services (bKash, Nagad, Rocket closing balances)
    - Uninvested brokerage BO ledger cash
* **Gold & Personal Jewellery (Manual Page 51):**
  - Inherited or gifted gold: State quantity in Bhori/Grams. Under NBR official rules, *value may be declared as `0` if acquisition cost is unknown*.
* **Personal Electronics (Laptops/Phones):**
  - Used personal electronics bought in preceding years under BDT 50,000 need NOT be added as new assets in the current year, preventing artificial cash outflow distortions.

#### 2. Liabilities
* Institutional (Student loans, bank liabilities) or Non-institutional (borrowed from relatives).

#### 3. Other Outflow
* Form IT-10BB living expenses auto-populate here.
* Gifts or financial contributions given to others (if any).

#### 4. Net Wealth of Previous Income Year (Manual Page 60–61)
* **First-Time Filers:** Enter `0` (or initial opening net wealth if documented).
* **Repeat Filers:** Enter the **exact closing Net Wealth from Line 5 of previous year's Form IT-10B**.

#### 5. Source of Fund (Manual Page 59–60)
* **Income Shown in Return:** Auto-calculated from Taxable Income + Tax-Exempt Stipends.
* **Other Receipts:**
  * If capital losses were carried forward under Section 70, the portal auto-lists: `Loss Not Set Off - Section 70: -[Amount]`.
  * **Parental Gift / Family Support (Manual Page 60):** Click `+ Add` under Other Receipts. Title: `Gift and Living Support from Parents`. Enter the exact balancing figure so that:

$$\text{Difference} = \text{Total Fund Outflow} - \text{Total Source of Fund} \equiv \mathbf{0.00}$$

> [!IMPORTANT]
> **NBR ZERO-DIFFERENCE RULE (Manual Page 61–62):**
> The portal strictly evaluates that `Difference == 0`. If the difference is not zero, the portal flags an imbalance error. Always balance `Other Receipts` to reach exact zero.

*Click **Save & Continue**.*

### Screen 7: Tax & Payment
1. **Tax Computation Review:**
   * Tax on Regular Income: Calculated based on slabs.
   * Less Tax Rebate (Schedule 5): Subtracted.
   * Net Tax Payable: If income $\le$ threshold, displays **`0.00`**.
2. **Tax Deducted at Source (TDS) & Advance Tax:**
   * Bank TDS and Dividend TDS appear as tax credits.
   * If Net Tax is `0.00` and TDS was deducted, the portal registers the TDS under **`Source Tax Refundable`** (e.g., `BDT 31 Refundable`).
3. **Payment Methods (if tax is due):**
   * Instant e-Payment gateway supports **bKash, Nagad, Rocket, Upay**, Debit Cards, Credit Cards, and Internet Banking.
   * Generates automated e-Challan / A-Challan with immediate clearing.

### Screen 8: Return View, OTP Verification & Document Retrieval
1. Click **Proceed to online return** to preview the full 14-page Form IT-11GA draft.
2. Verify all figures, schedules, and attachments.
3. Check the declaration box: *"I declare that the information provided is correct and complete."*
4. Click **Submit Return**. A 6-digit OTP is sent via SMS to your NID-verified phone number.
5. Enter the OTP and confirm submission.
6. **IMMEDIATE POST-SUBMISSION ACTIONS (Manual Chapter 8):**
   * Download and save the **PSR (Proof of Submission of Return)** / Acknowledgement Slip. *(Mandatory under Section 264 for opening bank accounts, getting credit cards, trade licenses, etc.)*.
   * Download the official **Tax Certificate** (featuring NBR QR code verification).
   * Download and archive the complete **Submitted Return (Form IT-11GA)**.

---

## 7. The Section 70 PDF Discrepancy Explained (Audit Defense)

When filing with a net capital loss carried forward under Section 70:
* **In the Online Portal:** The database calculates `Total Outflow == Total Source of Fund`, displaying **`Difference: 0`**, which satisfies the validation check and permits submission.
* **In the Generated 14-Page PDF Draft:** The backend report generator deducts the negative carried-forward loss from Receipts in the summary block. As a result:
  $$\text{Line 7 (Gross Wealth)} + \text{Carried Loss} = \text{Line 10 (Total Assets)}$$
  *(e.g., BDT 2,60,014 + BDT 3,028 = BDT 2,63,042).*
* **DCT Audit Defense:** This is a documented, standard system-generated artifact of the Synesis IT e-Return reporting engine. It is 100% corroborated and justified by the system-generated *Section 70 Loss Carry Forward Statement* appended on Page 12 of the return. It does NOT constitute an evasion, discrepancy, or taxpayer accounting error.

---

## 8. Youth Audit Defense Dossier (6-Year Retention Checklist)

Under Sections 182 and 183 of ITA 2023, the Deputy Commissioner of Taxes (DCT) may call for records within 6 years. Maintain a dedicated digital/physical binder containing:

1. **Bank Statements:** Full 12-month statements for all active bank accounts (July 1 – June 30), highlighting competition disbursements and incoming family support.
2. **Bank Tax Certificates:** Annual certificates showing 30 June balance, interest credited, and TDS deducted.
3. **Brokerage Statements:** Signed portfolio valuations and tax certificates from all active brokerage houses (NBL, IDLC, etc.) as of 30 June.
4. **Mutual Fund Tax Certificates:** Official dividend and investment tax certificates from asset management companies (e.g. EDGE AMC).
5. **Fintech / P2P Tax Statements:** Signed annual statements from crowdfunding platforms (Biniyog.io / Pure Fintech Ltd).
6. **Academic Verification:** University Student ID, fee clearance receipts, and stipend payment advice (e.g. BUP Trust Bank records).
7. **Professional Exam Receipts:** Invoices and payment proofs for ICAB / ACCA / professional certifications.
8. **Signed Parental Gift Declaration:** A signed confirmation from father/mother stating that they provided living and educational support to their son/daughter during the income year under Section 56(g).
9. **Final PSR & Return Acknowledgement:** Downloaded from `etaxnbr.gov.bd`.
