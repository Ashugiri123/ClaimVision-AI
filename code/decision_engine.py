class DecisionEngine:

    def decide(self, gemini_result, history):

        decision = {}

        if not gemini_result["valid_image"]:
            decision["evidence_standard_met"] = "false"
            decision["claim_status"] = "not_enough_information"

        elif gemini_result["visible_damage"]:
            decision["evidence_standard_met"] = "true"
            decision["claim_status"] = "supported"

        else:
            decision["evidence_standard_met"] = "true"
            decision["claim_status"] = "contradicted"

        decision["issue_type"] = gemini_result["issue_type"]
        decision["object_part"] = gemini_result["object_part"]
        decision["severity"] = gemini_result["severity"]

        decision["claim_status_justification"] = gemini_result["reason"]

        return decision