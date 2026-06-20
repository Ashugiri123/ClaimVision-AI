import re


class ClaimParser:

    @staticmethod
    def clean_conversation(conversation):
        """
        Remove speaker labels and clean the conversation.
        """

        conversation = re.sub(r"Customer:", "", conversation)
        conversation = re.sub(r"Support:", "", conversation)
        conversation = re.sub(r"Agent:", "", conversation)
        conversation = conversation.replace("|", " ")
        conversation = " ".join(conversation.split())

        return conversation