from diaries.AbstractDiary import AbstractDiary

class TakaiDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "勉強をしていたら寝落ちしてしまった"

    def get_author(self):
        return "Takai"