def match_donation_to_recipient(donation, recipients):
    """
    Very simple matching logic for now:
    - Choose the recipient nearest in location
    (Later we will improve using real distance algorithms)
    """
    if not recipients:
        return None
    
    # For now: just return the first recipient
    return recipients[0]
