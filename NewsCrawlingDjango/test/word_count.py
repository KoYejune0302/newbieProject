
from konlpy.tag import Hannanum

hannanum = Hannanum()
t_nouns = hannanum.nouns('공부 하기싫다')
print(t_nouns)