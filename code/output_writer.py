from pathlib import Path


class OutputWriter:

    def write_report(
        self,
        decision,
        gemini_result,
        history,
        requirements,
        conversation,
    ):

        report = f"""# Insurance Claim Evaluation Report

## Final Decision

Claim Status: {decision["claim_status"]}

Evidence Standard Met: {decision["evidence_standard_met"]}

Reason:
{decision["claim_status_justification"]}

---

## Gemini Analysis

Valid Image: {gemini_result["valid_image"]}

Issue Type: {gemini_result["issue_type"]}

Object Part: {gemini_result["object_part"]}

Severity: {gemini_result["severity"]}

Visible Damage: {gemini_result["visible_damage"]}

Reason:
{gemini_result["reason"]}

---

## Evidence Requirements

"""

        for _, row in requirements.iterrows():
            report += f"- {row['minimum_image_evidence']}\n"

        report += "\n---\n\n"

        report += "## User History\n\n"

        if len(history) > 0:
            report += history.to_string(index=False)
        else:
            report += "No previous history."

        report += "\n\n---\n\n"

        report += "## Customer Conversation\n\n"

        report += conversation

        output_file = (
            Path(__file__).parent
            / "evaluation"
            / "evaluation_report.md"
        )

        output_file.parent.mkdir(exist_ok=True)

        output_file.write_text(
            report,
            encoding="utf-8"
        )

        return output_file