from diaries.DiarySample import DiarySample
from diaries.OkuDiary import OkuDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    OkuDiary(),
    k23144(),
] 


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
# コミットのための追加