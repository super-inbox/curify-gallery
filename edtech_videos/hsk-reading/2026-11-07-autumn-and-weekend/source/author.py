from pathlib import Path
import json
B=Path(__file__).resolve().parent
cards=[]
def add(id,level,zh,en,category,scene,lines,vocab):
 def rows(s):return [dict(zip(['zh','pinyin','en'],x.split('|'))) for x in s.strip().splitlines()]
 c=dict(id=id,level=level,title_zh=zh,title_en=en,category=category,scene=scene,lines=rows(lines),vocab=rows(vocab));assert len(c['lines'])==len(c['vocab'])==8;cards.append(c)
add('hsk2-halloween-party-with-classmates',2,'同学的万圣节聚会','A Halloween Party with Classmates','Festivals','International adult classmates at a friendly Halloween party, handmade black cat ears, pumpkin lanterns and wrapped sweets; cozy, no horror.', '''
万圣节那天，同学请我去聚会。|Wàn shèng Jié nà tiān, tóng xué qǐng wǒ qù jù huì.|On Halloween, a classmate invites me to a party.
我穿了黑衣服，还戴了猫耳朵。|Wǒ chuān le hēi yī fu, hái dài le māo ěr duo.|I wear black clothes and cat ears.
门口有一个可爱的南瓜灯。|Mén kǒu yǒu yí ge kě ài de nán guā dēng.|There is a cute pumpkin lantern by the door.
朋友笑着问我，你是小猫吗？|Péng you xiào zhe wèn wǒ, nǐ shì xiǎo māo ma?|My friend smiles and asks if I am a little cat.
我说，对，我今天是一只黑猫。|Wǒ shuō, duì, wǒ jīn tiān shì yì zhī hēi māo.|I say yes, today I am a black cat.
我们一边聊天，一边吃糖。|Wǒ men yì biān liáo tiān, yì biān chī táng.|We chat and eat sweets.
我学会了几个新的中文词。|Wǒ xué huì le jǐ ge xīn de Zhōng wén cí.|I learn a few new Chinese words.
回家以前，我们一起拍了照片。|Huí jiā yǐ qián, wǒ men yì qǐ pāi le zhào piàn.|Before going home, we take a photo together.
''','''
万圣节|Wàn shèng Jié|Halloween
聚会|jù huì|party
耳朵|ěr duo|ear
南瓜灯|nán guā dēng|pumpkin lantern
黑猫|hēi māo|black cat
聊天|liáo tiān|chat
糖|táng|sweets
照片|zhào piàn|photograph
''')
add('hsk2-a-walk-among-red-autumn-leaves',2,'一起去看红叶','A Walk among Red Leaves','Seasons','Two international adult friends walking in a park of vivid red autumn leaves, resting on a bench, showing family photos by phone.', '''
秋天到了，公园里的叶子红了。|Qiū tiān dào le, gōng yuán lǐ de yè zi hóng le.|Autumn is here, and the leaves in the park have turned red.
星期六，我和朋友一起去看红叶。|Xīng qī liù, wǒ hé péng you yì qǐ qù kàn hóng yè.|On Saturday, my friend and I go to see the red leaves.
路上有红色的叶子，也有黄色的。|Lù shang yǒu hóng sè de yè zi, yě yǒu huáng sè de.|There are red and yellow leaves on the path.
我们慢慢走，听树上的鸟叫。|Wǒ men màn màn zǒu, tīng shù shang de niǎo jiào.|We walk slowly and listen to birds in the trees.
我想拍照，朋友帮我拿着包。|Wǒ xiǎng pāi zhào, péng you bāng wǒ ná zhe bāo.|I want to take photos, so my friend holds my bag.
走累了，我们坐下喝一点水。|Zǒu lèi le, wǒ men zuò xià hē yì diǎn shuǐ.|When we get tired, we sit down and drink some water.
我给家人发了一张红叶的照片。|Wǒ gěi jiā rén fā le yì zhāng hóng yè de zhào piàn.|I send my family a photo of the red leaves.
妈妈说，这里的秋天真漂亮。|Mā ma shuō, zhè lǐ de qiū tiān zhēn piào liang.|My mother says autumn here is beautiful.
''','''
秋天|qiū tiān|autumn
红叶|hóng yè|red leaves
公园|gōng yuán|park
黄色|huáng sè|yellow
鸟|niǎo|bird
拍照|pāi zhào|take a photo
家人|jiā rén|family
漂亮|piào liang|beautiful
''')
add('hsk2-building-a-sandcastle-at-the-beach',2,'海滩上的小城堡','A Sandcastle on the Beach','Travel','Adult international friends on a sunny beach building a small sandcastle above the waterline, playing a ball game and watching sunset.', '''
周末，我和朋友坐车去海边。|Zhōu mò, wǒ hé péng you zuò chē qù hǎi biān.|At the weekend, my friend and I take a ride to the seaside.
我们带了水、帽子和一个小球。|Wǒ men dài le shuǐ, mào zi hé yí ge xiǎo qiú.|We bring water, hats and a small ball.
海水很蓝，沙子暖暖的。|Hǎi shuǐ hěn lán, shā zi nuǎn nuǎn de.|The sea is blue, and the sand is warm.
我说，我们做一个小城堡吧。|Wǒ shuō, wǒ men zuò yí ge xiǎo chéng bǎo ba.|I suggest that we build a little castle.
朋友找来小桶，我把沙子放进去。|Péng you zhǎo lái xiǎo tǒng, wǒ bǎ shā zi fàng jìn qù.|My friend finds a bucket, and I put sand in it.
做好以后，我们在旁边玩球。|Zuò hǎo yǐ hòu, wǒ men zài páng biān wán qiú.|After finishing, we play ball nearby.
太阳快下山了，海面变成金色。|Tài yáng kuài xià shān le, hǎi miàn biàn chéng jīn sè.|As the sun sets, the sea turns golden.
回家时，我们把垃圾都带走了。|Huí jiā shí, wǒ men bǎ lā jī dōu dài zǒu le.|When we leave, we take all our rubbish with us.
''','''
海边|hǎi biān|seaside
帽子|mào zi|hat
沙子|shā zi|sand
城堡|chéng bǎo|castle
小桶|xiǎo tǒng|small bucket
旁边|páng biān|beside
太阳|tài yáng|sun
垃圾|lā jī|rubbish
''')
add('hsk2-a-warm-roasted-sweet-potato',2,'热热的烤红薯','A Warm Roasted Sweet Potato','Everyday life','An international adult student and a friendly street vendor, roasting sweet potatoes on a cool autumn day, sharing a split sweet potato with a classmate.', '''
下课以后，我走路回家。|Xià kè yǐ hòu, wǒ zǒu lù huí jiā.|After class, I walk home.
今天有一点冷，我把手放进口袋。|Jīn tiān yǒu yì diǎn lěng, wǒ bǎ shǒu fàng jìn kǒu dài.|It is a little cold, so I put my hands in my pockets.
路边有人在卖烤红薯。|Lù biān yǒu rén zài mài kǎo hóng shǔ.|Someone is selling roasted sweet potatoes by the road.
我闻到香味，就停了下来。|Wǒ wén dào xiāng wèi, jiù tíng le xià lái.|I smell the lovely aroma and stop.
我问老板，这个多少钱？|Wǒ wèn lǎo bǎn, zhè ge duō shao qián?|I ask the vendor how much this one costs.
买好以后，我先等它凉一点。|Mǎi hǎo yǐ hòu, wǒ xiān děng tā liáng yì diǎn.|After buying it, I wait for it to cool a little.
同学来了，我和她分着吃。|Tóng xué lái le, wǒ hé tā fēn zhe chī.|A classmate arrives, and I share it with her.
红薯很甜，吃完心里暖暖的。|Hóng shǔ hěn tián, chī wán xīn lǐ nuǎn nuǎn de.|The sweet potato is sweet, and I feel warm after eating it.
''','''
烤红薯|kǎo hóng shǔ|roasted sweet potato
口袋|kǒu dài|pocket
路边|lù biān|roadside
香味|xiāng wèi|aroma
老板|lǎo bǎn|vendor
多少钱|duō shao qián|how much
凉|liáng|cool
甜|tián|sweet
''')
add('hsk3-finding-a-book-at-the-weekend-market',3,'周末去逛旧书市集','A Weekend Secondhand Book Market','Everyday life','International adult student browsing an outdoor secondhand book stall, friendly bookseller shows a picture book, sitting in a cafe reading with friend.', '''
周末，朋友带我去逛旧书市集。|Zhōu mò, péng you dài wǒ qù guàng jiù shū shì jí.|At the weekend, a friend takes me to a secondhand book market.
桌上放着各种各样的书。|Zhuō shang fàng zhe gè zhǒng gè yàng de shū.|There are all kinds of books on the tables.
我想找一本容易读的中文书。|Wǒ xiǎng zhǎo yì běn róng yì dú de Zhōng wén shū.|I want to find an easy Chinese book.
老板听了，拿给我一本故事书。|Lǎo bǎn tīng le, ná gěi wǒ yì běn gù shi shū.|The bookseller hears me and hands me a storybook.
里面有很多图，句子也不长。|Lǐ miàn yǒu hěn duō tú, jù zi yě bù cháng.|It has many pictures and short sentences.
我试着读了一页，觉得很有意思。|Wǒ shì zhe dú le yí yè, jué de hěn yǒu yì si.|I try reading a page and find it interesting.
买好书以后，我们找了家咖啡店。|Mǎi hǎo shū yǐ hòu, wǒ men zhǎo le jiā kā fēi diàn.|After buying the book, we find a cafe.
我想每天读一点，慢慢把它读完。|Wǒ xiǎng měi tiān dú yì diǎn, màn màn bǎ tā dú wán.|I want to read a little each day and gradually finish it.
''','''
旧书|jiù shū|secondhand book
市集|shì jí|market
容易|róng yì|easy
故事书|gù shi shū|storybook
句子|jù zi|sentence
一页|yí yè|one page
有意思|yǒu yì si|interesting
咖啡店|kā fēi diàn|cafe
''')
add('hsk2-finding-my-missing-glove',2,'我的手套找到了','Finding My Missing Glove','Everyday life','International adult student realizes one glove is missing, retraces steps to classroom, teacher points to glove under desk, relieved smile.', '''
放学以后，我准备坐车回家。|Fàng xué yǐ hòu, wǒ zhǔn bèi zuò chē huí jiā.|After school, I get ready to take a ride home.
我打开包，发现少了一只手套。|Wǒ dǎ kāi bāo, fā xiàn shǎo le yì zhī shǒu tào.|I open my bag and find that one glove is missing.
另一只还在包里。|Lìng yì zhī hái zài bāo lǐ.|The other glove is still in my bag.
我想了想，又走回教室。|Wǒ xiǎng le xiǎng, yòu zǒu huí jiào shì.|I think for a moment and walk back to the classroom.
老师问我，你在找什么？|Lǎo shī wèn wǒ, nǐ zài zhǎo shén me?|The teacher asks what I am looking for.
我说，一只蓝色的手套。|Wǒ shuō, yì zhī lán sè de shǒu tào.|I say that I am looking for a blue glove.
她指着桌子下面说，在这里。|Tā zhǐ zhe zhuō zi xià miàn shuō, zài zhè lǐ.|She points under the desk and says it is here.
我谢谢老师，把两只手套都戴上。|Wǒ xiè xie lǎo shī, bǎ liǎng zhī shǒu tào dōu dài shang.|I thank the teacher and put on both gloves.
''','''
手套|shǒu tào|glove
准备|zhǔn bèi|prepare
发现|fā xiàn|discover
另一只|lìng yì zhī|the other one
教室|jiào shì|classroom
蓝色|lán sè|blue
下面|xià miàn|underneath
戴上|dài shang|put on
''')
add('hsk3-reading-signs-at-a-museum',3,'在博物馆读中文','Reading Chinese at a Museum','Culture','Two international adult friends in a quiet museum looking at an old teapot, discussing a display label without readable art text, friendly guide explaining.', '''
星期天，我和朋友去博物馆。|Xīng qī tiān, wǒ hé péng you qù bó wù guǎn.|On Sunday, my friend and I go to a museum.
一个旧茶壶引起了我的兴趣。|Yí ge jiù chá hú yǐn qǐ le wǒ de xìng qù.|An old teapot catches my interest.
旁边的牌子上有一段中文介绍。|Páng biān de pái zi shang yǒu yí duàn Zhōng wén jiè shào.|The label beside it has an introduction in Chinese.
我先自己读，再问朋友。|Wǒ xiān zì jǐ dú, zài wèn péng you.|I read it myself first, then ask my friend.
有几个字不认识，不过我能猜到一点。|Yǒu jǐ ge zì bú rèn shi, bú guò wǒ néng cāi dào yì diǎn.|I do not know some characters, but I can guess a little.
工作人员听见了，慢慢给我们解释。|Gōng zuò rén yuán tīng jiàn le, màn màn gěi wǒ men jiě shì.|A staff member hears us and explains slowly.
原来，这把茶壶以前是用来泡茶的。|Yuán lái, zhè bǎ chá hú yǐ qián shì yòng lái pào chá de.|It turns out that this teapot was once used to make tea.
看完展览，我记住了几个新词。|Kàn wán zhǎn lǎn, wǒ jì zhù le jǐ ge xīn cí.|After the exhibition, I remember a few new words.
''','''
博物馆|bó wù guǎn|museum
茶壶|chá hú|teapot
兴趣|xìng qù|interest
牌子|pái zi|sign
介绍|jiè shào|introduction
解释|jiě shì|explain
泡茶|pào chá|make tea
展览|zhǎn lǎn|exhibition
''')
add('hsk3-my-first-chinese-language-corner',3,'第一次参加中文角','My First Chinese Language Corner','Everyday life','Small welcoming circle of international adult students and Chinese volunteers, nervous newcomer becomes comfortable speaking, exchanging contact details at end.', '''
朋友告诉我，学校每周有中文角。|Péng you gào su wǒ, xué xiào měi zhōu yǒu Zhōng wén jiǎo.|A friend tells me the school has a weekly Chinese language corner.
我想去练习，可是有一点紧张。|Wǒ xiǎng qù liàn xí, kě shì yǒu yì diǎn jǐn zhāng.|I want to practise, but I feel a little nervous.
到了那里，大家请我坐在旁边。|Dào le nà lǐ, dà jiā qǐng wǒ zuò zài páng biān.|When I arrive, everyone invites me to sit beside them.
今天的话题是自己喜欢的食物。|Jīn tiān de huà tí shì zì jǐ xǐ huan de shí wù.|Today we talk about our favourite foods.
我说了家乡的一道菜，还画了一张图。|Wǒ shuō le jiā xiāng de yí dào cài, hái huà le yì zhāng tú.|I describe a dish from my hometown and draw a picture.
有人没听懂，我就换个简单的说法。|Yǒu rén méi tīng dǒng, wǒ jiù huàn ge jiǎn dān de shuō fǎ.|When someone does not understand, I try simpler words.
大家认真听，我慢慢不紧张了。|Dà jiā rèn zhēn tīng, wǒ màn màn bù jǐn zhāng le.|Everyone listens carefully, and I slowly feel less nervous.
结束时，我已经想下周再来了。|Jié shù shí, wǒ yǐ jīng xiǎng xià zhōu zài lái le.|By the end, I already want to come back next week.
''','''
中文角|Zhōng wén jiǎo|Chinese corner
练习|liàn xí|practice
紧张|jǐn zhāng|nervous
话题|huà tí|topic
家乡|jiā xiāng|hometown
简单|jiǎn dān|simple
认真|rèn zhēn|careful
结束|jié shù|finish
''')
add('hsk2-making-dumplings-with-friends',2,'一起包饺子','Making Dumplings Together','Everyday life','International adult learner making dumplings with friends in a home kitchen, learning folding from a friend, everyone eats the cooked dumplings at a table.', '''
今天，朋友请我去她家包饺子。|Jīn tiān, péng you qǐng wǒ qù tā jiā bāo jiǎo zi.|Today, a friend invites me to make dumplings at her home.
我们先洗手，再把桌子擦干净。|Wǒ men xiān xǐ shǒu, zài bǎ zhuō zi cā gān jìng.|We wash our hands and wipe the table clean.
桌上有饺子皮，还有肉和菜。|Zhuō shang yǒu jiǎo zi pí, hái yǒu ròu hé cài.|There are dumpling wrappers, meat and vegetables on the table.
她教我少放一点，再把边合上。|Tā jiāo wǒ shǎo fàng yì diǎn, zài bǎ biān hé shang.|She teaches me to use a little filling and close the edges.
我包的第一个饺子有一点大。|Wǒ bāo de dì yī ge jiǎo zi yǒu yì diǎn dà.|The first dumpling I make is a little big.
朋友说，没关系，再试一次。|Péng you shuō, méi guān xi, zài shì yí cì.|My friend says it is fine and tells me to try again.
饺子煮好了，我们一起坐下吃。|Jiǎo zi zhǔ hǎo le, wǒ men yì qǐ zuò xià chī.|When the dumplings are cooked, we sit down to eat.
自己做的饺子，吃起来特别香。|Zì jǐ zuò de jiǎo zi, chī qǐ lái tè bié xiāng.|The dumplings we made ourselves taste especially good.
''','''
饺子|jiǎo zi|dumpling
洗手|xǐ shǒu|wash hands
干净|gān jìng|clean
饺子皮|jiǎo zi pí|dumpling wrapper
肉|ròu|meat
合上|hé shang|close
再试一次|zài shì yí cì|try again
煮|zhǔ|boil
''')
add('hsk2-choosing-postcards-for-friends',2,'给朋友挑明信片','Choosing Postcards for Friends','Travel','Adult international learner in a small postcard shop choosing a city-night postcard and a cat postcard, writing messages at a cafe table.', '''
旅行快结束了，我想买几张明信片。|Lǚ xíng kuài jié shù le, wǒ xiǎng mǎi jǐ zhāng míng xìn piàn.|My trip is nearly over, and I want to buy some postcards.
小店里有很多不同的图案。|Xiǎo diàn lǐ yǒu hěn duō bù tóng de tú àn.|The little shop has many different designs.
我给姐姐挑了一张城市的夜景。|Wǒ gěi jiě jie tiāo le yì zhāng chéng shì de yè jǐng.|I choose a city night view for my older sister.
给朋友的那张，上面有一只猫。|Gěi péng you de nà zhāng, shang miàn yǒu yì zhī māo.|The one for my friend has a cat on it.
老板问我，要不要信封？|Lǎo bǎn wèn wǒ, yào bu yào xìn fēng?|The shopkeeper asks if I would like envelopes.
我说，不用了，谢谢。|Wǒ shuō, bú yòng le, xiè xie.|I say no, thank you.
下午，我坐下来，给每个人写几句话。|Xià wǔ, wǒ zuò xià lái, gěi měi ge rén xiě jǐ jù huà.|In the afternoon, I sit down and write a few words to each person.
我希望他们收到以后会笑。|Wǒ xī wàng tā men shōu dào yǐ hòu huì xiào.|I hope they will smile when they receive them.
''','''
旅行|lǚ xíng|travel
明信片|míng xìn piàn|postcard
图案|tú àn|design
姐姐|jiě jie|older sister
夜景|yè jǐng|night view
信封|xìn fēng|envelope
收到|shōu dào|receive
希望|xī wàng|hope
''')
for folder in ['cards','prompts','narration','video','publish/images','publish/previews','publish/video','qa']:(B/folder).mkdir(parents=True,exist_ok=True)
style='''Create ONE portrait HSK reading poster matching the approved Beijing reference FAITHFULLY. Same cream paper, thin rounded tan border, watercolor cloud badge top left, peach Reading Lesson ribbon, dark brown Chinese title and English subtitle, round header scene, eight generously spaced passage rows on the LEFT (small pinyin above large Chinese), three stacked watercolor story illustrations on the RIGHT, star and heart dividers, gold New Words ribbon and 2x4 numbered pastel vocabulary boxes at the bottom. Same warm watercolor style, typography, spacing and dimensions. This is a new lesson in the SAME template, NOT a redesign. High resolution. Adult foreign learners; warm personal scenes. No extra text in illustrations.\n'''
for c in cards:
 prompt=style+f"Scene: {c['scene']}\nBadge: 适合水平 HSK {c['level']}\nRibbon: 阅读课文 | Reading Lesson\nTitle: {c['title_zh']}\nSubtitle: {c['title_en']}\nEXACT passage, eight rows, pinyin above Chinese. Preserve EVERY character and tone mark; never omit, repeat, reorder or change sentences. Adjust font size slightly if necessary for long rows.\n"
 prompt+='\n'.join(x['pinyin']+'\n'+x['zh'] for x in c['lines'])
 prompt+='\nBottom ribbon: 生词 | New Words\nEight numbered vocabulary boxes, each with THREE text lines: CHINESE, then PINYIN, then ENGLISH MEANING, with a tiny watercolor icon at the side. All eight ENGLISH MEANINGS are REQUIRED. Leave enough room; do not omit any of the three text lines.\n'
 prompt+='\n'.join(f"{i+1}. Chinese: {v['zh']} / pinyin: {v['pinyin']} / English: {v['en']}" for i,v in enumerate(c['vocab']))
 prompt+='\nKeep all eight complete sentences visible. Chinese text is Simplified Chinese. Every vocabulary English meaning MUST be printed below its pinyin, as in the approved reference. No English sentence translations in the passage. No watermark.'
 (B/'prompts'/f'{c["id"]}.txt').write_text(prompt)
 (B/'narration'/f'{c["id"]}.txt').write_text(c['title_zh']+'。\n'+'\n'.join(x['zh'] for x in c['lines'])+'\n')
(B/'batch.json').write_text(json.dumps(cards,ensure_ascii=False,indent=2)+'\n')
print('Authored 10 stories, 80 sentences, 80 vocabulary entries and 10 generation prompts.')
