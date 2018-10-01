'''
004 Homework sample
出力日:　2018-09-06
----------------------------
本人    ドム    45才
長女    チェルシー    12才
愛犬    ドフィー    2才
'''

iFamily = ['本人','ドム' ,'45才']
iFamily.append('長女')
iFamily.append('チェルシー')
iFamily.append('12才')
iFamily += ['愛犬','ドフィー','2才']

for Famileyinfo in iFamily:
    print(Famileyinfo)

# Print exercises
from datetime import date
print()
print ("出力日:",end="  ")
print (date.today())
print ("----------------------------")
print ("本人" + "   " + "ドム" + "   "  + "45才")
print ("長女" + "   " + "チェルシー" + "   "  + "12才")
print ("愛犬" + "   " + "ドフィー" + "   "  + "2才")








''' Memo
１．Print句相関
      （１）.Python3の場合、Printが「Print文」から「Print関数」へと変わり、
      それにあわせて、末尾に追加される文字を　end optionで指定できるようになりました。

      （２）. from 。。。import。。。。の形で一文を宣言すると、print文を上書きする形で　Python３のPrint関数を
      使うことができるようになります。

２．Listの使い方
'''