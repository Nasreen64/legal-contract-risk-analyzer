def risk_score(clause):
    clause = clause.lower()
    if "penalty" in clause or "terminate" in clause:
        return "High Risk"
    elif "shall" in clause or "must" in clause:
        return "Medium Risk"
    return "Low Risk"
