#!/usr/bin/env python3
"""
Bangladesh Youth Tax Calculator (Deterministic Engine)
Statutory Basis: Income Tax Act 2023 & NBR eReturn System User Manual
AY 2026-2027 (Income Year 2025-2026)
"""

import math
from dataclasses import dataclass

@dataclass
class TaxProfile:
    # Income Sources
    gross_salary: float = 0.0          # Contracted internships / jobs
    university_stipend: float = 0.0    # 100% exempt u/s 6th Sch Part 1 Para 8
    bank_gross_interest: float = 0.0   # Gross interest
    bank_tds: float = 0.0              # Source tax deducted by bank
    cash_dividend: float = 0.0         # Gross dividend
    dividend_tds: float = 0.0          # Source tax on dividend
    p2p_profit: float = 0.0            # Crowdfunding markup
    capital_gain: float = 0.0          # Realized capital gain
    capital_loss: float = 0.0          # Realized capital loss (positive number)
    other_income: float = 0.0          # Prize awards / consulting
    
    # Investments (Schedule 5)
    mutual_funds_cost: float = 0.0     # SEC-approved mutual funds
    dps_annual_deposit: float = 0.0    # Capped at 1,20,000
    listed_stocks_cost: float = 0.0    # Secondary market purchases
    approved_zakat: float = 0.0        # Government zakat fund
    
    # Balance Sheet (IT-10B & IT-10BB)
    opening_net_wealth: float = 0.0    # Last year Line 5 (0 if first time)
    living_expenses: float = 0.0       # IT-10BB total expenses
    closing_gross_assets: float = 0.0  # Documented wealth as of 30 June
    liabilities: float = 0.0           # Debts / loans
    other_outflow: float = 0.0         # Gifts/donations given
    
    # Taxpayer Attributes
    is_female_or_senior: bool = False
    city_corporation: str = "Dhaka"    # Dhaka, Other_City, Non_City


def calculate_tax(p: TaxProfile):
    # 1. Employment Exemption (ITA 2023 Section 32)
    statutory_salary_exemption = min(p.gross_salary / 3.0, 450000.0)
    taxable_salary = max(0.0, p.gross_salary - statutory_salary_exemption)
    
    # 2. Capital Gains & Loss Carry-Forward (Sections 70 & 72)
    net_capital_result = p.capital_gain - p.capital_loss
    if net_capital_result >= 0:
        taxable_capital_gain = net_capital_result
        carried_forward_capital_loss = 0.0
    else:
        taxable_capital_gain = 0.0
        carried_forward_capital_loss = abs(net_capital_result)
        
    # 3. Total Taxable Income
    total_taxable_income = (
        taxable_salary
        + p.bank_gross_interest
        + p.cash_dividend
        + p.p2p_profit
        + taxable_capital_gain
        + p.other_income
    )
    
    # 4. Tax-Free Exemption Ceiling
    exemption_ceiling = 400000.0 if p.is_female_or_senior else 350000.0
    
    # 5. Gross Tax Liability Before Rebate
    gross_tax = 0.0
    if total_taxable_income > exemption_ceiling:
        remaining = total_taxable_income - exemption_ceiling
        
        # Slab 1: Next 100,000 @ 5%
        tier1 = min(remaining, 100000.0)
        gross_tax += tier1 * 0.05
        remaining -= tier1
        
        # Slab 2: Next 300,000 @ 10%
        if remaining > 0:
            tier2 = min(remaining, 300000.0)
            gross_tax += tier2 * 0.10
            remaining -= tier2
            
        # Slab 3: Next 400,000 @ 15%
        if remaining > 0:
            tier3 = min(remaining, 400000.0)
            gross_tax += tier3 * 0.15
            remaining -= tier3
            
        # Slab 4: Next 500,000 @ 20%
        if remaining > 0:
            tier4 = min(remaining, 500000.0)
            gross_tax += tier4 * 0.20
            remaining -= tier4
            
        # Slab 5: Balance @ 25%
        if remaining > 0:
            gross_tax += remaining * 0.25

    # 6. Schedule 5 Rebate Calculation
    eligible_dps = min(p.dps_annual_deposit, 120000.0)
    total_eligible_investment = (
        p.mutual_funds_cost
        + eligible_dps
        + p.listed_stocks_cost
        + p.approved_zakat
    )
    rebate = min(
        0.15 * total_eligible_investment,
        0.03 * total_taxable_income,
        1000000.0
    )
    
    # 7. Minimum Tax Determination (NBR Manual Page 67)
    if p.city_corporation in ["Dhaka", "Chattogram"]:
        min_tax_floor = 5000.0
    elif p.city_corporation == "Other_City":
        min_tax_floor = 4000.0
    else:
        min_tax_floor = 3000.0
        
    if total_taxable_income <= exemption_ceiling:
        net_tax_payable = 0.0
    else:
        net_tax_after_rebate = max(0.0, gross_tax - rebate)
        net_tax_payable = max(min_tax_floor, net_tax_after_rebate)
        
    # 8. TDS Source Tax Refundable
    total_tds = p.bank_tds + p.dividend_tds
    if net_tax_payable == 0.0:
        source_tax_refundable = total_tds
        final_payable = 0.0
    elif total_tds > net_tax_payable:
        source_tax_refundable = total_tds - net_tax_payable
        final_payable = 0.0
    else:
        source_tax_refundable = 0.0
        final_payable = net_tax_payable - total_tds
        
    # 9. IT-10B Balance Sheet & Zero-Difference Equation (Manual Page 61-62)
    closing_net_wealth = p.closing_gross_assets - p.liabilities
    delta_wealth = closing_net_wealth - p.opening_net_wealth
    total_fund_outflow = delta_wealth + p.living_expenses + p.other_outflow
    
    known_income_receipts = total_taxable_income + p.university_stipend
    # Balancing figure under Other Receipts (Parental Support)
    required_parental_support = max(0.0, total_fund_outflow - known_income_receipts)
    
    total_sources = known_income_receipts + required_parental_support
    difference = total_fund_outflow - total_sources
    
    return {
        "statutory_salary_exemption": round(statutory_salary_exemption),
        "taxable_salary": round(taxable_salary),
        "total_taxable_income": round(total_taxable_income),
        "tax_free_ceiling": round(exemption_ceiling),
        "gross_tax_before_rebate": round(gross_tax),
        "investment_tax_rebate": round(rebate),
        "net_tax_payable": round(final_payable),
        "source_tax_refundable": round(source_tax_refundable),
        "carried_forward_capital_loss": round(carried_forward_capital_loss),
        "closing_net_wealth": round(closing_net_wealth),
        "change_in_net_wealth": round(delta_wealth),
        "total_fund_outflow": round(total_fund_outflow),
        "required_parental_support": round(required_parental_support),
        "it10b_difference": round(difference)
    }

if __name__ == "__main__":
    print("=== Testing Bangladesh Youth Tax Calculator Engine ===")
    sample = TaxProfile(
        gross_salary=35000,
        university_stipend=18000,
        bank_gross_interest=228,
        bank_tds=31,
        cash_dividend=346,
        dividend_tds=35,
        p2p_profit=500,
        capital_gain=896,
        capital_loss=3924,
        other_income=55625,
        mutual_funds_cost=28956,
        opening_net_wealth=56759,
        living_expenses=170000,
        closing_gross_assets=263042
    )
    res = calculate_tax(sample)
    for k, v in res.items():
        print(f"{k:32}: {v}")
