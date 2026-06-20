from data_loader import DataLoader


class HistoryChecker:

    def __init__(self):
        loader = DataLoader()
        self.history = loader.load_user_history()

    def get_user_history(self, user_id):
        rows = self.history[self.history["user_id"] == user_id]
        return rows