def explain(prediction, permissions, system_calls):

    risk_level = "High" if prediction == "Malware" else "Low"

    explanation = f"""
=====================================
ANDROID MALWARE ANALYSIS REPORT
=====================================

Prediction : {prediction}
Risk Level : {risk_level}

Sensitive Permissions:
{', '.join(permissions)}

Observed System Calls:
{', '.join(system_calls)}

Analysis:
The application requests permissions that may
provide access to sensitive user information.

The observed system-call behaviour suggests
process execution activity that is frequently
encountered in Android malware samples.

Recommendation:
Further static and dynamic analysis is advised.
"""

    return explanation