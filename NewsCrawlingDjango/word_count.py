import pandas as pd
from konlpy.tag import Hannanum
import re

word = {'코로나','거리두기','BTS','연예인','군인','지인','위인','노숙인','문재인','김종인','이재오','라미란','설리','구하라','전북','전남','이란','경상남도','경상북도','전라남도','전라북도','충청남도','충청북도','제주특별자치도','간호학과', '건축학과', '건축공학과', '게임학과', '경영정보학과', '경영학과', '경제학과', '경찰학과', '관광학과', '교육학과', '국어교육과', '국어국문학과', '군사학과', '기계공학과', '기독교학과', '노어노문학과', '농업자원경제학과', '독어독문학과', '동물자원학과', '문예창작학과', '문헌정보학과', '문화재보존학과', '물리치료학과', '물리학과', '법학과', '북한학과', '불교학과', '불어불문학과', '사학과', '사회학과', '사회복지학과', '산업공학과', '생명과학과', '세무학과', '서어서문학과', '섬유공학과', '소방학과', '수산생명의학과', '수의학과', '수학과', '심리학과', '식품영양학과', '신학과', '약학과', '언어학과', '에너지공학과', '연극학과', '영상학과', '영어영문학과', '유아교육과', '윤리교육과', '의학과', '일반사회교육과', '일어일문학과', '임상병리학과', '자유전공학부', '재료공학과', '전자공학과', '정치외교학과', '조경학과', '중어중문학과', '지리학과', '지리교육과', '지적학과', '철학과', '치의학과', '치위생학과', '커뮤니케이션학과', '컴퓨터공학과', '특성화학과', '특수교육과', '한문학과', '한의학과', '항공운항학과', '화학공학과', '화학과'}
data = pd.read_csv('/output.csv',encoding = 'utf-8')
hannanum = Hannanum()
t_noun= []
t_nouns, t_count= [],[]
Title = []

def filter(nouns):
  strs = list(nouns.split())
  warn = set(strs)&word
  if warn:
    for x in warn:
      strs.remove(x)
    string = ' '.join(strs)
    nns = hannanum.nouns(string)
    for x in warn:
      nns.append(x)
    return (nns)
  else:
    return (hannanum.nouns(i))


def t_counts(mylist):
  new_list = []
  count = []
  for v in mylist:
    if v not in new_list:
      new_list.append(v)
      count.append(1)
    else:
      count[new_list.index(v)] = count[new_list.index(v)]+1
  t_nouns.append(new_list)
  t_count.append(count)


for i,row in data.iterrows():
  Title.append(re.sub(r'\[.*?\]|\(종합\)|"|,|…|”|“|·',' ',(re.sub("'",' ',str(row['Title'])))))

for i in Title:
  t_noun.append(filter(i))

for i in t_noun:
  t_counts(i)



df = pd.DataFrame({'title' : data['Title'],'t_element': t_nouns,'t_count':t_count})
df.to_csv('dataframe.csv')