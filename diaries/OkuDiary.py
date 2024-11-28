from diaries.AbstractDiary import AbstractDiary

class OkuDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return "ラジオ体操に参加した"

    def get_author(self):
        return "Oku"
