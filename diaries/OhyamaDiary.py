from diaries.AbstractDiary import AbstractDiary
class OhyamaDiary(AbstractDiary):

    def get_date(self):
        return "2021-11-28"
    
    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。"""

    def get_author(self):
        return "Ohyama"