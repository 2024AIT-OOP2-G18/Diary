from diaries.DiarySample import DiarySample
from diaries.k23144 import k23144

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    k23144(),
] 

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
# コミットのための追加