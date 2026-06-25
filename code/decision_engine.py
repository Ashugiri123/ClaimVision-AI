class DecisionEngine:

    def decide(self, gemini_result, history, evidence):

        decision = {}

        if not evidence["evidence_complete"]:

            decision["risk_flags"] = "none"
            decision["issue_type"] = "unknown"
            decision["object_part"] = "unknown"
            decision["severity"] = "unknown"

            decision["evidence_standard_met"] = "false"
            decision["claim_status"] = "not_enough_information"
            decision["claim_status_justification"] = evidence["missing_evidence"]

            return decision

        # -----------------------------
        # Default Values
        # -----------------------------

        decision["risk_flags"] = "none"

        decision["issue_type"] = gemini_result["issue_type"]
        decision["object_part"] = gemini_result["object_part"]
        decision["severity"] = gemini_result["severity"]

        # -----------------------------
        # Invalid Image
        # -----------------------------

        if not gemini_result["valid_image"]:

            decision["evidence_standard_met"] = "false"

            decision["claim_status"] = "not_enough_information"

            decision["claim_status_justification"] = \
                "Uploaded image is invalid or unsuitable for automated inspection."

            return decision

        # -----------------------------
        # No Damage Found
        # -----------------------------

        if not gemini_result["visible_damage"]:

            decision["evidence_standard_met"] = "true"

            decision["claim_status"] = "contradicted"

            decision["claim_status_justification"] = \
                "No visible damage was detected in the submitted image."

            return decision

        # -----------------------------
        # Damage Found
        # -----------------------------

        decision["evidence_standard_met"] = "true"

        decision["claim_status"] = "supported"

        decision["claim_status_justification"] = gemini_result["reason"]

        # -----------------------------
        # User History Check
        # -----------------------------

        if not history.empty:

            row = history.iloc[0]

            if row["history_flags"] != "none":

                decision["risk_flags"] = row["history_flags"]

            if row["past_claim_count"] >= 8:

                decision["risk_flags"] += ";high_claim_frequency"

            if row["last_90_days_claim_count"] >= 4:

                decision["risk_flags"] += ";recent_frequent_claims"

            if row["rejected_claim"] >= 3:

                decision["risk_flags"] += ";high_rejection_history"


        # -----------------------------
        # Final Risk Decision
        # -----------------------------

        if (
            gemini_result["fraud_suspicion"] == "high"
            or decision["risk_flags"] != "none"
        ):

            decision["claim_status"] = "manual_review"

            decision["claim_status_justification"] = (
                "The claim requires manual verification due to customer history "
                "or high fraud suspicion detected by the AI."
            )


        return decision