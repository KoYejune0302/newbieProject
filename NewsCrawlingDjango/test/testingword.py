import matplotlib.pyplot as plt
import pandas as pd
from functools import reduce
import operator
import matplotlib
from IPython.display import set_matplotlib_formats
from wordcloud import WordCloud

#csv파일 불러오기
def load_word_df(path):
    df = pd.read_csv(path, encoding="utf8")
    df = df.dropna()
    df = df.reset_index()
    return df

#문자와 빈도수 추출
def extract_words(df):
    # dataframe 값 갖고오기
    s_count = df["s_count"]
    s_element = df["s_element"]
    # 리스트 생성 함수

    # 함수 적용
    sele = listroy(s_element)
    scou = listroy(s_count)

    return sele, scou

#추출된 문자열을 리스트로 변경
#이때 생성되는 2차원리스트를 1차원 리스트로 변경
def listroy(mylist):
    temp0=[]
    for i in range(len(mylist)):
        temp1 = mylist[i]
        temp2 = temp1[1:len(temp1) - 1]
        temp1 = temp2.split(', ')
        temp0.append(temp1)
    #2차원 리스트 -> 1차원 리스트
    temp1=list(reduce(operator.add, temp0))
    return temp1

#리스트를 딕셔너리로 {문자:문자의 빈도수}
def to_dict(sele, scou):
    scou1 = []
    # int 변환
    for i in range(len(scou)):
        a = int(scou[i])
        scou1.append(a)

    return dict(zip(sele, scou1))

#워드클라우드 디자인 설정
def draw_word_cloud(words):
    # 폰트 설정
    matplotlib.rc('font', family='Malgun Gothic')
    # 글자 선명도 개선
    set_matplotlib_formats('retina')
    # 워드 클라우드 설정(폰트,배경색,폰트색,폭,높이).words의 빈도수의 따라
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf",
                          background_color='white',
                          colormap="Accent_r",
                          width=1500,
                          height=1000).generate_from_frequencies(words)
    # 워드 클라우드 창 실행
    plt.imshow(wordcloud)
    plt.axis("off")
    return plt

#워드클라우드 실행
def show_word_cloud(path):
    df = load_word_df(path)
    sele, scou = extract_words(df)
    words = to_dict(sele, scou)
    plt = draw_word_cloud(words)
    plt.show()

#파일 주소
show_word_cloud("C:/Users/dlsrn/PycharmProjects/wordcloud/dataframe.csv")
