#!/usr/bin/env python3
"""
================================================================================
BANGLADESH YOUTH TAX CALCULATOR (DETERMINISTIC ENGINE)
Statutory Authority: Income Tax Act 2023 (Act No. XII of 2023 / আয়কর আইন, ২০২৩)
Assessment Year: 2026-2027 (Income Year: 1 July 2025 – 30 June 2026)
================================================================================
Features:
  - Interactive Terminal CLI Wizard for human filers
  - JSON / CLI Flag Interface for AI Agents (Antigravity, Claude, GPT, APIs)
  - Full statutory tax slabs, exemptions, rebates, and ring-fenced capital losses
  - Exact Zero-Difference IT-10B Balance Sheet reconciliation
"""

import sys
import json
import argparse
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional


# ==============================================================================
# 1. DATA STRUCTURES & PROFILE
# ==============================================================================

@dataclass
class BankAccount:
    bank_name: str
    account_no: str
    gross_interest: float = 0.0
    bank_charges: float = 0.0
    tds_deducted: float = 0.0
    closing_balance: float = 0.0

@dataclass
class DividendIncome:
    company_name: str
    gross_dividend: float = 0.0
    tds_deducted: float = 0.0

@dataclass
class BrokerPortfolio:
    broker_name: str
    bo_id: str
    realized_gain: float = 0.0
    realized_loss: float = 0.0  # Positive number
    closing_ledger_cash: float = 0.0

@dataclass
class TaxProfile:
    # Taxpayer Classification
    taxpayer_name: str = "Young Taxpayer"
    taxpayer_category: str = "general"  # general, female, senior_65, disabled, third_gender, freedom_fighter
    has_disabled_dependent: bool = False
    location: str = "dhaka_ctg"  # dhaka_ctg, other_city, non_city
    
    # 1. Employment (Section 32 / Schedule 1)
    gross_salary: float = 0.0  # Internships, trainee wages, basic pay
    
    # 2. Financial Assets (Section 35)
    banks: List[BankAccount] = field(default_factory=list)
    dividends: List[DividendIncome] = field(default_factory=list)
    p2p_crowdfunding_profit: float = 0.0
    p2p_active_principal: float = 0.0  # Asset under IT-10B
    
    # 3. Capital Gains & Secondary Market (Sections 57, 70, 72)
    brokers: List[BrokerPortfolio] = field(default_factory=list)
    
    # 4. Other Sources (Section 38)
    prize_money_net_share: float = 0.0  # Net individual share
    consulting_honorarium: float = 0.0
    
    # 5. Tax-Exempted Income (Sixth Schedule, Part 1)
    university_stipend: float = 0.0     # 100% exempt under Para 8
    foreign_remittance: float = 0.0     # Exempt under Para 24
    
    # 6. Schedule 5 Investments (Sixth Schedule, Part 2)
    mutual_funds_cost: float = 0.0      # Open-end / closed-end funds at cost
    dps_annual_deposit: float = 0.0     # Max eligible: 1,20,000
    listed_stocks_purchased: float = 0.0 # Shares bought & held at year-end
    approved_zakat_donation: float = 0.0
    
    # 7. Form IT-10BB Lifestyle Expenses
    food_household_expenses: float = 0.0
    accommodation_rent: float = 0.0
    transport_expenses: float = 0.0
    utility_internet_mobile: float = 0.0
    education_exam_fees: float = 0.0
    festivals_recreation: float = 0.0
    misc_expenses: float = 0.0
    
    # 8. Form IT-10B Assets & Liabilities
    opening_net_wealth: float = 0.0     # Line 5 of previous return (0 if 1st time)
    cash_in_hand: float = 0.0           # Physical notes as of 30 June
    digital_wallets_balance: float = 0.0 # MFS balances as of 30 June
    gold_bhori: float = 0.0             # Weight in bhori
    gold_declared_value: float = 0.0    # Can be 0 if gifted/inherited (Manual pg 51)
    other_personal_assets: float = 0.0  # Electronics/furniture additions this year
    institutional_liabilities: float = 0.0 # Bank/Student loans
    non_institutional_liabilities: float = 0.0 # Relatives/friends debts
    other_outflow_gifts: float = 0.0    # Donations/gifts given out


# ==============================================================================
# 2. SUBSTANTIVE TAX ENGINE LOGIC
# ==============================================================================

class TaxCalculator:
    
    @staticmethod
    def compute(p: TaxProfile) -> Dict:
        # A. Employment Exemption (Section 32 / 6th Sch Part 1 Para 1)
        statutory_salary_exemption = min(p.gross_salary / 3.0, 450000.0)
        taxable_salary = max(0.0, p.gross_salary - statutory_salary_exemption)
        
        # B. Financial Assets Income & TDS (Section 35)
        total_bank_interest = sum(b.gross_interest for b in p.banks)
        total_bank_charges = sum(b.bank_charges for b in p.banks)
        net_bank_interest = max(0.0, total_bank_interest - total_bank_charges)
        total_bank_tds = sum(b.tds_deducted for b in p.banks)
        
        total_gross_dividend = sum(d.gross_dividend for d in p.dividends)
        total_dividend_tds = sum(d.tds_deducted for d in p.dividends)
        
        taxable_financial_assets = (
            net_bank_interest 
            + total_gross_dividend 
            + p.p2p_crowdfunding_profit
        )
        total_tds = total_bank_tds + total_dividend_tds
        
        # C. Capital Gains & Loss Carry-Forward (Sections 57, 70, 72)
        total_capital_gain = sum(b.realized_gain for b in p.brokers)
        total_capital_loss = sum(b.realized_loss for b in p.brokers)
        net_capital_outcome = total_capital_gain - total_capital_loss
        
        if net_capital_outcome >= 0:
            taxable_capital_gain = net_capital_outcome
            carried_forward_capital_loss = 0.0
        else:
            taxable_capital_gain = 0.0
            # Capital loss is ring-fenced and carried forward 6 years under Section 70
            carried_forward_capital_loss = abs(net_capital_outcome)
            
        # D. Other Sources (Section 38)
        taxable_other_sources = p.prize_money_net_share + p.consulting_honorarium
        
        # E. Total Taxable Income
        total_taxable_income = (
            taxable_salary
            + taxable_financial_assets
            + taxable_capital_gain
            + taxable_other_sources
        )
        
        # F. Fully Exempt Incomes (Sixth Schedule Part 1)
        total_exempt_income = (
            statutory_salary_exemption
            + p.university_stipend
            + p.foreign_remittance
        )
        
        # G. Tax-Free Exemption Ceiling Determination (PwC Bangladesh Tax Summary)
        if p.taxpayer_category in ["female", "senior_65"]:
            ceiling = 450000.0
        elif p.taxpayer_category in ["disabled", "third_gender"]:
            ceiling = 525000.0
        elif p.taxpayer_category == "freedom_fighter":
            ceiling = 550000.0
        else:
            ceiling = 400000.0  # General Resident young male / taxpayer
            
        if p.has_disabled_dependent:
            ceiling += 50000.0
            
        # H. Progressive Tax Slabs Calculation (PwC Bangladesh Tax Summary)
        # Up to ceiling: Nil (0%)
        # Next 300,000 @ 10%
        # Next 400,000 @ 15%
        # Next 500,000 @ 20%
        # Next 2,000,000 @ 25%
        # On the rest of the income @ 30%
        gross_tax_liability = 0.0
        if total_taxable_income > ceiling:
            remaining = total_taxable_income - ceiling
            
            # Slab 1: Next 300,000 @ 10%
            s1 = min(remaining, 300000.0)
            gross_tax_liability += s1 * 0.10
            remaining -= s1
            
            # Slab 2: Next 400,000 @ 15%
            if remaining > 0:
                s2 = min(remaining, 400000.0)
                gross_tax_liability += s2 * 0.15
                remaining -= s2
                
            # Slab 3: Next 500,000 @ 20%
            if remaining > 0:
                s3 = min(remaining, 500000.0)
                gross_tax_liability += s3 * 0.20
                remaining -= s3
                
            # Slab 4: Next 2,000,000 @ 25%
            if remaining > 0:
                s4 = min(remaining, 2000000.0)
                gross_tax_liability += s4 * 0.25
                remaining -= s4
                
            # Slab 5: On the rest of the income @ 30%
            if remaining > 0:
                gross_tax_liability += remaining * 0.30
                
        # I. Schedule 5 Investment Tax Rebate (Sixth Schedule, Part 2)
        eligible_dps = min(p.dps_annual_deposit, 120000.0)
        total_eligible_investments = (
            p.mutual_funds_cost
            + eligible_dps
            + p.listed_stocks_purchased
            + p.approved_zakat_donation
        )
        allowable_rebate = min(
            0.15 * total_eligible_investments,
            0.03 * total_taxable_income,
            1000000.0
        )
        
        # J. Minimum Tax Floor (Section 163 / Manual Page 67)
        if p.location == "dhaka_ctg":
            min_floor = 5000.0
        elif p.location == "other_city":
            min_floor = 4000.0
        else:
            min_floor = 3000.0
            
        # THE GOLDEN MINIMUM TAX RULE:
        # Minimum tax NEVER triggers if total taxable income <= exemption ceiling!
        if total_taxable_income <= ceiling:
            net_tax_payable = 0.0
        else:
            tax_after_rebate = max(0.0, gross_tax_liability - allowable_rebate)
            net_tax_payable = max(min_floor, tax_after_rebate)
            
        # K. TDS Settlement & Refundable Calculation (Section 153 & 160)
        if net_tax_payable == 0.0:
            final_tax_due = 0.0
            source_tax_refundable = total_tds
        elif total_tds >= net_tax_payable:
            final_tax_due = 0.0
            source_tax_refundable = total_tds - net_tax_payable
        else:
            final_tax_due = net_tax_payable - total_tds
            source_tax_refundable = 0.0
            
        # L. Form IT-10BB Total Living Expenses
        total_living_expenses = (
            p.food_household_expenses
            + p.accommodation_rent
            + p.transport_expenses
            + p.utility_internet_mobile
            + p.education_exam_fees
            + p.festivals_recreation
            + p.misc_expenses
        )
        
        # M. Form IT-10B Closing Gross Wealth & Balance Sheet Math
        total_bank_balances = sum(b.closing_balance for b in p.banks)
        total_broker_cash = sum(b.closing_ledger_cash for b in p.brokers)
        
        liquid_cash_assets = (
            p.cash_in_hand
            + total_bank_balances
            + p.digital_wallets_balance
            + total_broker_cash
        )
        
        financial_investments = (
            p.mutual_funds_cost
            + p.listed_stocks_purchased
            + p.p2p_active_principal
        )
        
        closing_gross_wealth = (
            liquid_cash_assets
            + financial_investments
            + p.gold_declared_value
            + p.other_personal_assets
        )
        
        total_liabilities = p.institutional_liabilities + p.non_institutional_liabilities
        closing_net_wealth = closing_gross_wealth - total_liabilities
        
        # N. The Zero-Difference Balance Sheet Equations (Manual Pages 61–62)
        delta_net_wealth = closing_net_wealth - p.opening_net_wealth
        total_fund_outflow = delta_net_wealth + total_living_expenses + p.other_outflow_gifts
        
        # Documented receipts from return
        documented_return_receipts = total_taxable_income + p.university_stipend + p.foreign_remittance
        
        # The Balancing Shortfall under Other Receipts (Parental Support / Gift u/s 56(g))
        required_parental_gift = max(0.0, total_fund_outflow - documented_return_receipts)
        
        total_source_of_fund = documented_return_receipts + required_parental_gift
        difference = total_fund_outflow - total_source_of_fund
        
        return {
            "taxpayer_profile": {
                "name": p.taxpayer_name,
                "category": p.taxpayer_category,
                "location": p.location,
                "exemption_ceiling": round(ceiling)
            },
            "income_summary": {
                "gross_employment_salary": round(p.gross_salary),
                "statutory_salary_exemption_s32": round(statutory_salary_exemption),
                "taxable_salary": round(taxable_salary),
                "taxable_financial_assets_s35": round(taxable_financial_assets),
                "taxable_capital_gains_s57": round(taxable_capital_gain),
                "carried_forward_capital_loss_s70": round(carried_forward_capital_loss),
                "taxable_other_sources_s38": round(taxable_other_sources),
                "total_taxable_income": round(total_taxable_income),
                "total_exempt_income_sch6": round(total_exempt_income)
            },
            "tax_computation": {
                "gross_tax_liability": round(gross_tax_liability),
                "schedule5_tax_rebate": round(allowable_rebate),
                "minimum_tax_floor_applicable": p.location if total_taxable_income > ceiling else "None (Income below ceiling)",
                "net_tax_payable": round(net_tax_payable),
                "total_source_tax_deducted_tds": round(total_tds),
                "final_tax_payable_to_nbr": round(final_tax_due),
                "source_tax_refundable_from_nbr": round(source_tax_refundable)
            },
            "balance_sheet_it10b": {
                "opening_net_wealth": round(p.opening_net_wealth),
                "closing_gross_wealth": round(closing_gross_wealth),
                "total_liabilities": round(total_liabilities),
                "closing_net_wealth": round(closing_net_wealth),
                "change_in_net_wealth_delta_w": round(delta_net_wealth),
                "total_living_expenses_it10bb": round(total_living_expenses),
                "other_outflows_gifts_given": round(p.other_outflow_gifts),
                "total_fund_outflow": round(total_fund_outflow),
                "documented_income_receipts": round(documented_return_receipts),
                "required_parental_gift_support_s56g": round(required_parental_gift),
                "total_sources_of_fund": round(total_source_of_fund),
                "reconciliation_difference": round(difference)  # Must be 0
            }
        }


# ==============================================================================
# 3. TERMINAL FORMATTING & DISPLAY HELPERS
# ==============================================================================

def print_audit_report(res: Dict):
    p = res["taxpayer_profile"]
    inc = res["income_summary"]
    tax = res["tax_computation"]
    bs = res["balance_sheet_it10b"]
    
    print("\n" + "=" * 78)
    print(f"  BANGLADESH YOUTH TAX RETURN AUDIT DOSSIER - AY 2026-2027")
    print("  Governing Law: Income Tax Act 2023 & NBR e-Return Portal")
    print("=" * 78)
    print(f"Taxpayer Name     : {p['name']}")
    print(f"Category / Ceiling: {p['category'].upper()} (Ceiling: BDT {p['exemption_ceiling']:,})")
    print(f"Filing Scheme     : Universal Self (Section 180 / Online)")
    print("-" * 78)
    
    print("\n[PART 1: HEADS OF INCOME & STATUTORY EXEMPTIONS]")
    print(f"  * Employment Gross Salary (Sec 32)      : BDT {inc['gross_employment_salary']:>10,}")
    print(f"    - Less: 1/3rd Statutory Exemption     : BDT {-inc['statutory_salary_exemption_s32']:>10,}")
    print(f"    = Net Taxable Salary                  : BDT {inc['taxable_salary']:>10,}")
    print(f"  * Financial Assets (Bank/Div/P2P) (s.35): BDT {inc['taxable_financial_assets_s35']:>10,}")
    print(f"  * Capital Gains (Sec 57)                : BDT {inc['taxable_capital_gains_s57']:>10,}")
    if inc['carried_forward_capital_loss_s70'] > 0:
        print(f"    * Unabsorbed Loss Carried Forward (s.70): BDT {inc['carried_forward_capital_loss_s70']:>8,} (For 6 Years)")
    print(f"  * Other Sources (Awards/Prizes) (s.38)  : BDT {inc['taxable_other_sources_s38']:>10,}")
    print(f"  --------------------------------------------------------")
    print(f"  TOTAL TAXABLE INCOME (Net Tax Base)     : BDT {inc['total_taxable_income']:>10,}")
    print(f"  Total Exempted Inflow (Stipends/Sch 6)  : BDT {inc['total_exempt_income_sch6']:>10,}")

    print("\n[PART 2: TAX COMPUTATION & TDS CREDITS]")
    print(f"  * Gross Tax on Slabs                    : BDT {tax['gross_tax_liability']:>10,}")
    print(f"  * Less: Schedule 5 Investment Rebate    : BDT {-tax['schedule5_tax_rebate']:>10,}")
    print(f"  * Minimum Tax Floor Status              : {tax['minimum_tax_floor_applicable']}")
    print(f"  --------------------------------------------------------")
    print(f"  NET TAX PAYABLE TO NBR                  : BDT {tax['final_tax_payable_to_nbr']:>10,}")
    if tax['source_tax_refundable_from_nbr'] > 0:
        print(f"  >>> SOURCE TAX REFUNDABLE (TDS CREDIT)  : BDT {tax['source_tax_refundable_from_nbr']:>10,} (Govt Owes You)")

    print("\n[PART 3: FORM IT-10B BALANCE SHEET RECONCILIATION]")
    print(f"  * Opening Net Wealth (Prior Year Line 5): BDT {bs['opening_net_wealth']:>10,}")
    print(f"  * Closing Gross Documented Assets (30 J): BDT {bs['closing_gross_wealth']:>10,}")
    print(f"  * Total Liabilities / Debts             : BDT {bs['total_liabilities']:>10,}")
    print(f"  * Closing Net Wealth                    : BDT {bs['closing_net_wealth']:>10,}")
    print(f"  * Change in Net Wealth (Delta-W)             : BDT {bs['change_in_net_wealth_delta_w']:>10,}")
    print(f"  * Add: Living Expenses (Form IT-10BB)   : BDT {bs['total_living_expenses_it10bb']:>10,}")
    print(f"  * Add: Other Outflows (Gifts given)     : BDT {bs['other_outflows_gifts_given']:>10,}")
    print(f"  --------------------------------------------------------")
    print(f"  TOTAL FUND OUTFLOW                      : BDT {bs['total_fund_outflow']:>10,}")
    print(f"  Documented Income Inflows (Taxable+Ex)  : BDT {bs['documented_income_receipts']:>10,}")
    print(f"  REQUIRED PARENTAL GIFT (Line 1(c) s.56g): BDT {bs['required_parental_gift_support_s56g']:>10,}")
    print(f"  TOTAL SOURCE OF FUNDS                   : BDT {bs['total_sources_of_fund']:>10,}")
    print("  " + "-" * 56)
    diff = bs['reconciliation_difference']
    diff_status = "PASSED (0.00)" if diff == 0 else f"FAILED MISMATCH ({diff})"
    print(f"  PORTAL SUMMARY DIFFERENCE               : {diff_status:>18}")
    print("=" * 78 + "\n")


# ==============================================================================
# 4. INTERACTIVE CLI WIZARD
# ==============================================================================

def run_interactive_wizard() -> TaxProfile:
    def ask_float(prompt: str, default: float = 0.0) -> float:
        val = input(f"{prompt} [{default}]: ").strip()
        if not val:
            return default
        try:
            return float(val)
        except ValueError:
            print("Invalid input, defaulting to 0.")
            return default

    def ask_str(prompt: str, default: str) -> str:
        val = input(f"{prompt} [{default}]: ").strip()
        return val if val else default

    print("\n" + "=" * 65)
    print("   BANGLADESH YOUTH TAX CALCULATOR - INTERACTIVE WIZARD")
    print("   Tailored for Students, Interns & Young Employees")
    print("=" * 65)

    p = TaxProfile()
    p.taxpayer_name = ask_str("Enter your name", "Young Taxpayer")
    
    cat = ask_str("Category (general / female / senior_65 / disabled / third_gender / freedom_fighter)", "general").lower()
    p.taxpayer_category = cat if cat in ["general", "female", "senior_65", "disabled", "third_gender", "freedom_fighter"] else "general"
    
    loc = ask_str("Location (dhaka_ctg / other_city / non_city)", "dhaka_ctg").lower()
    p.location = loc if loc in ["dhaka_ctg", "other_city", "non_city"] else "dhaka_ctg"
    
    print("\n--- 1. INCOME SOURCES ---")
    p.gross_salary = ask_float("Gross Employment / Internship Salary")
    p.university_stipend = ask_float("University Stipend / Scholarship (100% Tax-Exempt)")
    p.prize_money_net_share = ask_float("Competition / Award Net Share (Your 1/4th or individual share)")
    p.consulting_honorarium = ask_float("Freelance / Consulting Honorarium")
    
    print("\n--- 2. FINANCIAL ASSETS & SAVINGS ---")
    gross_int = ask_float("Total Bank Interest Credited across all accounts")
    int_tds = ask_float("Total Bank Source Tax (TDS) Deducted")
    bank_bal = ask_float("Total Bank Closing Balance as of 30 June")
    if gross_int > 0 or bank_bal > 0:
        p.banks.append(BankAccount("Primary Bank", "12345", gross_int, 0.0, int_tds, bank_bal))
        
    p.p2p_crowdfunding_profit = ask_float("P2P / Micro-Crowdfunding Profit Markup")
    p.p2p_active_principal = ask_float("P2P Active Invested Principal (as of 30 June)")
    
    print("\n--- 3. CAPITAL GAINS / SECONDARY MARKET STOCKS ---")
    gain = ask_float("Total Realized Capital Gains from BO accounts")
    loss = ask_float("Total Realized Capital Losses from BO accounts")
    broker_cash = ask_float("Uninvested Cash in BO Ledger as of 30 June")
    if gain > 0 or loss > 0 or broker_cash > 0:
        p.brokers.append(BrokerPortfolio("Primary Brokerage", "1200000000000000", gain, loss, broker_cash))
        
    print("\n--- 4. TAX REBATE INVESTMENTS (SCHEDULE 5) ---")
    p.mutual_funds_cost = ask_float("Mutual Funds Purchase Cost (EDGE AMC, etc.)")
    p.dps_annual_deposit = ask_float("DPS Total Deposit this Income Year (Max 1.2 Lakh)")
    p.listed_stocks_purchased = ask_float("Stock Market Purchases Held at Year End")
    
    print("\n--- 5. LIVING EXPENSES (FORM IT-10BB) ---")
    p.food_household_expenses = ask_float("Food & Household Expenses (Annual)", 60000.0)
    p.transport_expenses = ask_float("Transport / Metro / Ride-sharing (Annual)", 20000.0)
    p.utility_internet_mobile = ask_float("Internet & Mobile Recharge (Annual)", 10000.0)
    p.education_exam_fees = ask_float("Tuition Fees & Professional Exams (Annual)", 55000.0)
    p.festivals_recreation = ask_float("Festivals & Personal Recreation (Annual)", 20000.0)
    p.misc_expenses = ask_float("Misc Incidentals", 5000.0)
    
    print("\n--- 6. ASSETS & WEALTH CONTINUITY (FORM IT-10B) ---")
    p.opening_net_wealth = ask_float("Opening Net Wealth from Last Year's Line 5 (0 if first time)")
    p.cash_in_hand = ask_float("Physical Cash in Hand as of 30 June", 10000.0)
    p.digital_wallets_balance = ask_float("Digital Wallets (bKash/Nagad) Balance as of 30 June", 5000.0)
    
    return p


# ==============================================================================
# 5. CLI ARGUMENT PARSER & ENTRYPOINT
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Bangladesh Youth Tax Calculator (Income Tax Act 2023 & NBR e-Return)"
    )
    parser.add_argument("--json", type=str, help="JSON string representing TaxProfile")
    parser.add_argument("--file", type=str, help="Path to JSON file representing TaxProfile")
    parser.add_argument("--output-json", action="store_true", help="Print result strictly as raw JSON (for AI agents)")
    
    # CLI shortcut flags for quick agent execution
    parser.add_argument("--salary", type=float, default=None, help="Gross salary")
    parser.add_argument("--stipend", type=float, default=0.0, help="University stipend")
    parser.add_argument("--interest", type=float, default=0.0, help="Bank interest")
    parser.add_argument("--bank-tds", type=float, default=0.0, help="Bank TDS")
    parser.add_argument("--bank-balance", type=float, default=0.0, help="Bank closing balance")
    parser.add_argument("--capital-gain", type=float, default=0.0, help="Realized capital gain")
    parser.add_argument("--capital-loss", type=float, default=0.0, help="Realized capital loss")
    parser.add_argument("--mutual-funds", type=float, default=0.0, help="Mutual funds cost")
    parser.add_argument("--expenses", type=float, default=0.0, help="Total living expenses")
    parser.add_argument("--opening-wealth", type=float, default=0.0, help="Opening net wealth")
    parser.add_argument("--closing-assets", type=float, default=0.0, help="Closing gross assets")
    
    args = parser.parse_args()
    
    # Mode 1: JSON via argument or file
    if args.json:
        raw = args.json.strip()
        if (raw.startswith("'") and raw.endswith("'")) or (raw.startswith('"') and raw.endswith('"')):
            raw = raw[1:-1]
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            data = json.loads(raw.replace('\\"', '"'))
        profile = TaxProfile(**data)
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            data = json.load(f)
        profile = TaxProfile(**data)
        
    # Mode 2: CLI Flags provided
    elif args.salary is not None:
        profile = TaxProfile(
            gross_salary=args.salary,
            university_stipend=args.stipend,
            mutual_funds_cost=args.mutual_funds,
            opening_net_wealth=args.opening_wealth,
            food_household_expenses=args.expenses
        )
        if args.interest > 0 or args.bank_balance > 0 or args.bank_tds > 0:
            profile.banks.append(BankAccount("Primary Bank", "0001", args.interest, 0.0, args.bank_tds, args.bank_balance))
        if args.capital_gain > 0 or args.capital_loss > 0:
            profile.brokers.append(BrokerPortfolio("Primary Broker", "0001", args.capital_gain, args.capital_loss, 0.0))
            
    # Mode 3: Interactive Terminal Wizard
    else:
        profile = run_interactive_wizard()
        
    # Compute
    results = TaxCalculator.compute(profile)
    
    if args.output_json:
        print(json.dumps(results, indent=2))
    else:
        print_audit_report(results)


if __name__ == "__main__":
    main()
