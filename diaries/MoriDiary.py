from diaries.AbstractDiary import AbstractDiary

class MoriDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "風邪を引いた。喉が痛い。"

    def get_author(self):
        return "Mori"
