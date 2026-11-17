import json,re,unicodedata
from pathlib import Path
from pypinyin import pinyin,Style
ROOT=Path(__file__).resolve().parent
cards=json.loads((ROOT/'batch.json').read_text())
errors=[]; tones=[]
def base(s):return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if not unicodedata.combining(c)).replace('ü','u')
for c in cards:
 for n,row in enumerate(c['lines']+c['vocab']):
  hz=re.findall(r'[\u4e00-\u9fff]',row['zh']); py=re.findall(r'[a-zA-ZüÜāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ]+',row['pinyin'].lower())
  if len(hz)!=len(py):errors.append([c['id'],n,'alignment',len(hz),len(py)]);continue
  for i,(h,p) in enumerate(zip(hz,py)):
   choices=pinyin(h,style=Style.TONE,heteronym=True)[0]
   if base(p) not in [base(x) for x in choices]:errors.append([c['id'],n,h,p,choices])
   if p.lower() not in choices:tones.append([c['id'],n,h,p])
report=dict(cards=len(cards),sentences=80,glossary_entries=80,alignment_or_reading_errors=errors,tone_exceptions_to_review=tones,level_note='HSK2–3 practice targets; proper names and thematic extension vocabulary are glossed. Not an official vocabulary-only syllabus.')
(ROOT/'text-qa.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
assert not errors
