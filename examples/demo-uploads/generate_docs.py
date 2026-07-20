"""Generate realistic demo estate documents as PDFs."""
from fpdf import FPDF


def make_pdf(filename: str, lines: list[tuple[str, int, bool]]) -> None:
    """lines: list of (text, font_size, is_bold)"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margins(25, 25, 25)
    for text, size, bold in lines:
        pdf.set_font("Helvetica", "B" if bold else "", size)
        if text == "":
            pdf.ln(4)
        else:
            pdf.multi_cell(0, size * 0.5, text)
            pdf.ln(1)
    pdf.output(filename)
    print(f"Created {filename}")


# ── 1. Last Will & Testament ────────────────────────────────────────────────

make_pdf("will_robert_milligan.pdf", [
    ("LAST WILL AND TESTAMENT", 16, True),
    ("OF ROBERT ALAN MILLIGAN", 14, True),
    ("", 0, False),
    ("STATE OF CALIFORNIA", 11, True),
    ("COUNTY OF ALAMEDA", 11, True),
    ("", 0, False),
    ("I, ROBERT ALAN MILLIGAN, a resident of Oakland, County of Alameda, State of California, being of sound and disposing mind and memory, and not acting under duress, menace, fraud, or undue influence of any person, do hereby make, publish, and declare this instrument to be my Last Will and Testament, hereby revoking all former wills and codicils previously made by me.", 10, False),
    ("", 0, False),
    ("ARTICLE I - PERSONAL REPRESENTATIVE", 11, True),
    ("", 0, False),
    ("I hereby appoint my daughter, DANA MARIE MILLIGAN, of Oakland, California, as Executor of this my Last Will and Testament. If DANA MARIE MILLIGAN is unable or unwilling to serve, I appoint my son, JAMES ROBERT MILLIGAN, as successor Executor. I direct that no bond shall be required of any Executor named herein.", 10, False),
    ("", 0, False),
    ("ARTICLE II - PAYMENT OF DEBTS AND EXPENSES", 11, True),
    ("", 0, False),
    ("I direct my Executor to pay all of my just debts, funeral expenses, and the costs of administering my estate as soon after my death as practicable.", 10, False),
    ("", 0, False),
    ("ARTICLE III - SPECIFIC BEQUESTS", 11, True),
    ("", 0, False),
    ("A. I give and bequeath to my daughter DANA MARIE MILLIGAN the real property located at 4821 Telegraph Avenue, Oakland, California 94609, commonly known as my primary residence, together with all improvements thereon and appurtenances thereunto belonging, free and clear of any encumbrances to the extent possible.", 10, False),
    ("", 0, False),
    ("B. I give and bequeath to my son JAMES ROBERT MILLIGAN my 2019 Toyota Camry, VIN 4T1B11HK5KU236784, and all funds held in my Wells Fargo checking account ending in 4471.", 10, False),
    ("", 0, False),
    ("C. I give and bequeath to my granddaughter SOPHIA ELENA MILLIGAN the sum of Fifteen Thousand Dollars ($15,000.00) to be used for educational expenses.", 10, False),
    ("", 0, False),
    ("ARTICLE IV - RESIDUARY ESTATE", 11, True),
    ("", 0, False),
    ("All the rest, residue, and remainder of my estate, both real and personal, of whatever kind and wherever situated, I give, bequeath, and devise to my children DANA MARIE MILLIGAN and JAMES ROBERT MILLIGAN, in equal shares of fifty percent (50%) each. If either child shall predecease me, their share shall pass to their living descendants, per stirpes.", 10, False),
    ("", 0, False),
    ("ARTICLE V - EXECUTOR POWERS", 11, True),
    ("", 0, False),
    ("My Executor shall have all powers granted by the California Probate Code, including without limitation the power to sell, lease, mortgage, or otherwise encumber estate assets; to invest and reinvest estate funds; to employ attorneys, accountants, and other professionals; and to do all acts necessary or appropriate for the proper administration of my estate.", 10, False),
    ("", 0, False),
    ("IN WITNESS WHEREOF, I have hereunto set my hand to this, my Last Will and Testament, on this 14th day of March, 2024.", 10, False),
    ("", 0, False),
    ("", 0, False),
    ("_______________________________", 10, False),
    ("ROBERT ALAN MILLIGAN, Testator", 10, False),
    ("Date of Death: June 3, 2026", 10, False),
    ("", 0, False),
    ("ATTESTATION CLAUSE", 11, True),
    ("", 0, False),
    ("We, the undersigned witnesses, each do hereby declare that the Testator signed this instrument in our presence and declared it to be his Last Will and Testament, and that each of us signed this Will as witness in the presence and at the request of the Testator, and in the presence of each other.", 10, False),
    ("", 0, False),
    ("Witness 1: Margaret Chen, 892 Lakeshore Ave, Oakland CA 94610", 10, False),
    ("Witness 2: David Okonkwo, 117 Grand Ave, Oakland CA 94610", 10, False),
])


# ── 2. Bank Statement ───────────────────────────────────────────────────────

make_pdf("bank_statement_wells_fargo.pdf", [
    ("WELLS FARGO BANK, N.A.", 16, True),
    ("Account Statement", 12, True),
    ("", 0, False),
    ("Statement Period: April 1, 2026 - April 30, 2026", 10, False),
    ("", 0, False),
    ("ACCOUNT HOLDER INFORMATION", 11, True),
    ("Account Holder:   Robert Alan Milligan", 10, False),
    ("Address:          4821 Telegraph Avenue", 10, False),
    ("                  Oakland, CA 94609", 10, False),
    ("", 0, False),
    ("ACCOUNT SUMMARY", 11, True),
    ("Account Type:     Personal Checking", 10, False),
    ("Account Number:   XXXXXX4471", 10, False),
    ("Routing Number:   121042882", 10, False),
    ("", 0, False),
    ("Beginning Balance (April 1, 2026):    $24,318.42", 10, False),
    ("Total Deposits / Credits:              $3,200.00", 10, False),
    ("Total Withdrawals / Debits:           ($1,847.63)", 10, False),
    ("Ending Balance (April 30, 2026):     $25,670.79", 10, False),
    ("", 0, False),
    ("TRANSACTION HISTORY", 11, True),
    ("", 0, False),
    ("04/01  Opening Balance                              $24,318.42", 10, False),
    ("04/03  Direct Deposit - Social Security            +$1,850.00", 10, False),
    ("04/05  PG&E Autopay - Utility                        -$187.44", 10, False),
    ("04/08  ATM Withdrawal - Oakland                      -$200.00", 10, False),
    ("04/10  Direct Deposit - Pension Income             +$1,350.00", 10, False),
    ("04/12  Kaiser Permanente - Medical Premium           -$312.19", 10, False),
    ("04/15  Safeway - Grocery                             -$143.88", 10, False),
    ("04/18  Comcast - Internet/Cable                       -$89.99", 10, False),
    ("04/22  Check #1042 - Property Tax Installment        -$914.13", 10, False),
    ("04/28  ATM Withdrawal - Oakland                      -$200.00", 10, False),
    ("04/30  Closing Balance                              $25,670.79", 10, False),
    ("", 0, False),
    ("IMPORTANT NOTICE", 11, True),
    ("If you have questions about this statement, please contact Wells Fargo Customer Service at 1-800-869-3557 or visit your local branch. For estate and bereavement services, please call 1-800-869-3557 and say 'estate services' to be connected with a specialist.", 10, False),
    ("", 0, False),
    ("Wells Fargo Bank, N.A. Member FDIC.", 9, False),
])


# ── 3. Property Deed ────────────────────────────────────────────────────────

make_pdf("property_deed_telegraph_ave.pdf", [
    ("GRANT DEED", 16, True),
    ("", 0, False),
    ("ALAMEDA COUNTY RECORDER", 12, True),
    ("Document No: 2018-047291", 10, False),
    ("Recorded: September 12, 2018", 10, False),
    ("", 0, False),
    ("APN: 016-124-008-5", 11, True),
    ("", 0, False),
    ("FOR A VALUABLE CONSIDERATION, receipt of which is hereby acknowledged,", 10, False),
    ("", 0, False),
    ("GRANTOR:", 11, True),
    ("Patricia Louise Milligan (deceased) and Robert Alan Milligan, husband and wife as joint tenants", 10, False),
    ("", 0, False),
    ("hereby GRANT to", 10, False),
    ("", 0, False),
    ("GRANTEE:", 11, True),
    ("Robert Alan Milligan, a single man", 10, False),
    ("", 0, False),
    ("the following described real property in the City of Oakland, County of Alameda, State of California:", 10, False),
    ("", 0, False),
    ("LEGAL DESCRIPTION", 11, True),
    ("", 0, False),
    ("Lot 14, Block 22, as designated on the Map of the Piedmont Terrace Tract No. 3, filed in the office of the Recorder of the County of Alameda, State of California, on April 3, 1924, in Book 26 of Maps, at Page 18.", 10, False),
    ("", 0, False),
    ("COMMONLY KNOWN AS:", 11, True),
    ("4821 Telegraph Avenue, Oakland, California 94609", 10, False),
    ("", 0, False),
    ("ASSESSOR'S PARCEL NUMBER: 016-124-008-5", 10, False),
    ("", 0, False),
    ("ESTIMATED FAIR MARKET VALUE AT DATE OF TRANSFER (2018): $785,000.00", 10, False),
    ("ESTIMATED CURRENT MARKET VALUE (2026 per Zillow): $1,240,000.00", 10, False),
    ("", 0, False),
    ("ENCUMBRANCES:", 11, True),
    ("Subject to current taxes and assessments, covenants, conditions, restrictions, reservations, rights, rights of way, and easements of record, if any.", 10, False),
    ("", 0, False),
    ("This deed is being recorded to reflect the transfer of interest following the death of Patricia Louise Milligan on January 17, 2018, pursuant to the right of survivorship.", 10, False),
    ("", 0, False),
    ("", 0, False),
    ("_______________________________", 10, False),
    ("Robert Alan Milligan, Grantor/Grantee", 10, False),
    ("Date: September 10, 2018", 10, False),
    ("", 0, False),
    ("Notarized before me on September 10, 2018", 10, False),
    ("Notary Public: Sandra J. Kim, Commission No. 2187443", 10, False),
    ("County of Alameda, State of California", 10, False),
    ("My Commission Expires: March 15, 2021", 10, False),
])


# ── 4. Creditor Notice / Medical Bill ───────────────────────────────────────

make_pdf("creditor_notice_medical_bill.pdf", [
    ("ALTA BATES SUMMIT MEDICAL CENTER", 16, True),
    ("Patient Financial Services", 12, True),
    ("350 Hawthorne Avenue, Oakland, CA 94609", 10, False),
    ("Phone: (510) 204-4444 | Fax: (510) 204-4001", 10, False),
    ("", 0, False),
    ("STATEMENT OF ACCOUNT", 13, True),
    ("", 0, False),
    ("Patient Name:      Robert Alan Milligan", 10, False),
    ("Date of Birth:     August 22, 1948", 10, False),
    ("Account Number:    AB-2026-00384712", 10, False),
    ("Statement Date:    May 15, 2026", 10, False),
    ("", 0, False),
    ("SERVICE SUMMARY", 11, True),
    ("", 0, False),
    ("Date of Service:   April 28, 2026 - May 2, 2026", 10, False),
    ("Facility:          Alta Bates Summit Medical Center - Oakland Campus", 10, False),
    ("Attending:         Dr. James Thornton, MD - Cardiology", 10, False),
    ("Diagnosis:         Congestive Heart Failure (I50.9)", 10, False),
    ("", 0, False),
    ("ITEMIZED CHARGES", 11, True),
    ("", 0, False),
    ("Room & Board (4 nights ICU)                         $18,400.00", 10, False),
    ("Cardiology Consultation                              $2,200.00", 10, False),
    ("Echocardiogram                                       $1,450.00", 10, False),
    ("Laboratory Services                                    $892.50", 10, False),
    ("Pharmacy                                             $1,237.80", 10, False),
    ("Radiology                                              $640.00", 10, False),
    ("Medical Supplies                                       $318.45", 10, False),
    ("                                          ______________________", 10, False),
    ("Total Charges:                                      $25,138.75", 10, False),
    ("", 0, False),
    ("INSURANCE ADJUSTMENTS", 11, True),
    ("Medicare Part A Payment:                           ($14,200.00)", 10, False),
    ("Medicare Supplemental (AARP):                       ($4,800.00)", 10, False),
    ("                                          ______________________", 10, False),
    ("BALANCE DUE FROM PATIENT / ESTATE:                  $6,138.75", 10, False),
    ("", 0, False),
    ("PAYMENT NOTICE", 11, True),
    ("This account has been referred to our Estate Collections Department as we have been notified of the passing of Robert Alan Milligan on June 3, 2026. We extend our sincere condolences to the family.", 10, False),
    ("", 0, False),
    ("Pursuant to California Probate Code Section 9000 et seq., creditor claims against the estate must be filed within the statutory period. Please contact our Estate Collections Department at (510) 204-4444 ext. 3 to arrange payment or obtain claim filing instructions.", 10, False),
    ("", 0, False),
    ("Creditor:  Alta Bates Summit Medical Center", 10, False),
    ("Amount:    $6,138.75", 10, False),
    ("Type:      Unsecured / Medical", 10, False),
    ("", 0, False),
    ("Please remit payment to: Alta Bates Summit Medical Center, P.O. Box 742116, Los Angeles, CA 90074-2116", 10, False),
])

print("\nAll 4 demo documents created successfully.")
