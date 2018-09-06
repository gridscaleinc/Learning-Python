import xlrd
import xlsxwriter
from collections import Counter
from itertools import chain
from janome.tokenizer import Tokenizer

## Excelファイル読み込み
# 例）C:\Users\〜\Documents\〜
# ファイル名の前に'r'を入れてください。理由：rを使うとraw文字列として扱われ、エスケープシーケンスとして処理されなくなります。（わからなければスルーしてください）
book = xlrd.open_workbook(r"エクセルファイルのパスを入れてください")

# エクセルシートの1枚目を変数に格納
sheet_1 = book.sheet_by_index(0)
# 1列目のみ読み取るのでcol(columnの略)に0を格納（0が1番目を表す為）
col = 0
data = []
each_data = []
# 1列目に記載されているすべてのセルを1行目から順に読み取ります
t = Tokenizer()
for row in range(sheet_1.nrows):
    val = sheet_1.cell(row, col).value
    tokens = t.tokenize(val)
    for token in tokens:
        partOfSpeech = token.part_of_speech.split(',')[0]
        # 今回抽出するのは名詞だけとします。（もちろん他の品詞を追加、変更、除外可能です。）
        if partOfSpeech == u'名詞':
            each_data.append(token.surface) # token.surfaceは表層形(語彙)です。詳しくはこちら...http://ailaby.com/janome/
        # すべての形態素を含ませたいのであればif構文を外し、each_data.append(token.surface)のみ記載してください。
    data.append(each_data)
    each_data = []

## 文章を形態素毎に分割したデータをいれるエクセルファイル作成（今回は名詞のみ）
# 例）C:\Users\〜\Documents\〜
# パスの前のrは省略しないでください
data_book = xlsxwriter.Workbook(r"作成するエクセルファイルのパス")
# シート作成・変数定義
data_sheet = data_book.add_worksheet('data')
for row in range(len(data)):
    for i in range(len(data[row])):
        data_sheet.write(row, i, data[row][i])
# エクセルを保存
data_book.close()

#すべての語彙を同じ配列に格納
chain_data = list(chain.from_iterable(data))
c = Counter(chain_data)

result_ranking = c.most_common(100) # 出現頻度100位までを変数に格納
# 語彙出現ランキングを記述するエクセルを作成（パスは上記参考に適当にいれてください）
result_book = xlsxwriter.Workbook(r"エクセルファイルのパスをいれてください")
# resultという名前のシートを作ります
result_sheet = result_book.add_worksheet('result')
for row in range(len(result_ranking)):
    for i in range(len(result_ranking[row])):
        result_sheet.write(row, i, result_ranking[row][i])
# エクセルを保存
result_book.close()

