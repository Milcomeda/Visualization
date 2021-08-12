import pathlib
import pandas

p_tmp = pathlib.Path('C:\\Users\\WAVE\\Desktop\\月度推移').glob('*.xlsm')

for p in p_tmp:
    file_name = p.stem
    read_xlsm = pandas.read_excel(p, sheet_name=2)
    read_xlsm.to_csv('C:\\Users\\WAVE\\Desktop\\月度推移\\' + file_name + '不具合データ.csv', index=None)
    read_xlsm = pandas.read_excel(p, sheet_name=3)
    read_xlsm.to_csv('C:\\Users\\WAVE\\Desktop\\月度推移\\' + file_name + '生産数データ.csv', index=None)
