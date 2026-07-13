# Oradano明朝GSRRフォント Ver. 0.2018.0101 について

2018年01月01日  
内田明  
<uchida at happy dot email dot ne dot jp>


## Oradano明朝フォント／Oradano明朝GSRRフォントとは何か

Oradano明朝フォント／Oradano明朝GSRRフォントとは、活字の格好よさの源
泉を考える材料として内田が製作中のフォントです。このフォントで日本語
電子テキストを表示・印刷させると、和レトロ、活版印刷風になります。
Greek（ギリシア文字）、Symbol（記号）、Roman（ラテン文字）、そして
Russian（キリル文字）を刷新したVer. 0.2016.0611から、このフォントの
ことをOradano明朝GSRRフォントと呼称しています。

Oradano明朝GSRRフォントが実装する漢字数は、「U+7A50（穐）」を除くJIS
第一水準漢字に相当する字種と、[青空文庫](http://www.aozora.gr.jp)登録
作品で使用される漢字の上位3000字をカバーしている他、その範囲外に幾らか
趣味的な漢字を含むものになっています。

このフォントが実装している仮名および仮名に準ずる記号の多くは、東京築
地活版製造所が明治30年-31年に販売しあるいは印刷していた五号活字(“築
地体前期五号仮名”の最終型)に基づき、内田がアウトライン化したものです。

いわゆる前期五号と後期五号の特徴を併せ持っており、明治10年代から大正
昭和戦前期にかけて、築地活版系が印刷した書籍や秀英舎系が印刷した書籍
の雰囲気をよく伝え得るであろうスタイルとなっています。

合略仮名「トキ」および「トモ」については、“後期五号”期にあたる明治
36年に刊行された東京築地活版製造所『活版見本』に掲載されているものを
採用し、UnicodeのPrivate Use Area（私用領域）を活用して収録しておりま
す（「トキ」はPUAのU+F8A0、「トモ」はPUAのU+F8B0と、CJK漢字拡張C領域
で登録されてしまったU+2A708）。

仮名および仮名に準ずる記号以外のアルファベットを含む非漢字は、Oradano
明朝フォント制作当初に内田が新規にデザインしたものでしたが、Oradano明
朝GSRRフォントVer. 0.2016.0611以降、多くの字形が次の資料に依拠するもの
となっています。

-ギリシア大文字：印刷局活版部[『活字紋様見本』](http://dl.ndl.go.jp/info:ndljp/pid/853858/73)
-ギリシア小文字：林鶴一[『新撰平面三角法教科書』](http://dl.ndl.go.jp/info:ndljp/pid/828770/82)
-ラテン文字およびアラビア数字：東京築地活版製造所[『活版見本』](http://dl.ndl.go.jp/info:ndljp/pid/854017/27)
-ラテン小文字のうち「qx」：三好学[『日本植物景観』](http://dl.ndl.go.jp/info:ndljp/pid/936654/7)
-ラテン小文字のうち「ß」：G. K. Frommann・J. A. Pangkofer編[『Die Deutschen mundarten』1856年版](https://babel.hathitrust.org/cgi/pt?q1=%C3%9F;id=njp.32101068568839;view=image;seq=415;start=1;sz=10;page=root;num=401)
-アクセント付きラテン文字：東京築地活版製造所[『活版見本』](http://dl.ndl.go.jp/info:ndljp/pid/854017/69)
-アクセント付きラテン文字のうち「Åå」：[『Sveriges och Norges stats-kalendar』1868年版](https://babel.hathitrust.org/cgi/pt?id=umn.31951001295866m;view=1up;seq=417)
-ラテン文字リガチャのうち「Ææ」：Anthony Trollope[『The Commentaries Of Caesar』](https://archive.org/stream/in.ernet.dli.2015.170366/2015.170366.The-Commentaries-Of-Caesar#page/n7/mode/2up)
-ラテン文字リガチャのうち「Œœ」：Paterne Berrichon編[『Œuvres de Arthur Rimbaud』](https://archive.org/stream/uvresdearthurrim00rimb#page/69/mode/1up)
-キリル文字（「ІіѲѳѢѣѴѵ」含む）：大川信次郎[『露語独修文法詳解』](http://dl.ndl.go.jp/info:ndljp/pid/862132/6)
-キリル文字のうち「лруф」：西海枝静[『初学独修露語研究』](http://dl.ndl.go.jp/info:ndljp/pid/943069/11)
-「＆」：William Skeen[『Early Typography』](https://archive.org/stream/earlytypography00skee#page/103/mode/1up)
-「！＄，．-：；？＠～￡＋－＝±×÷√∠∫⊥§¶*†‡」：交進社印刷所[『印刷の栞』](http://dl.ndl.go.jp/info:ndljp/pid/1261243/33)
-「（）｛｝「」『』【】〔〕○◎●」：大阪出版社[『最新活版印刷業案内』](http://dl.ndl.go.jp/info:ndljp/pid/1017790/22)
-「―«»」：Paterne Berrichon編[『Œuvres de Arthur Rimbaud』](https://archive.org/stream/uvresdearthurrim00rimb#page/n14/mode/1up)-「♯♭♮♩♪♫♬」：近森出来治[『楽典初梯』](http://dl.ndl.go.jp/info:ndljp/pid/854810/14)
-「⁉⁈⁇‼〽￥〃≠≒∴♂♀〒卍﹆﹅◦•▷▶◁◀△▲▽▼☆★◆□■⦿◉→←↑↓◐◑◒◓❖％‰⅓⅔¼½¾」：字母宗[『字母と活字　五号漢字九千体見本』](https://note.mu/uakira2/n/ncfdc795434a7)
-「／＼♨＊」：森川龍文堂[『龍文堂活字清鑒』](https://note.mu/uakira2/n/ncfdc795434a7)
-「☞」：青山進行堂[『富多無可思』](https://note.mu/uakira2/n/na224013f91ba)
-「、。※〈〉《》‘’〝〟♤♠♢♦♢♥♧♣☖☗↗↘↖↙⇄⇦⇦⇧⇩⤴⤵」：日本活字工業[『NTF活字書体』](https://note.mu/uakira2/n/nd0a83b356ad7)
-「☼☽☾☿♃♄♅♆♈♉♊♋♍♍♎♏♐♑♒♓☉☊☋☍🌚🌛🌝🌜」：American Type Founders Co.[『Handy specimen book』](https://archive.org/stream/cu31924014559730#page/n62/mode/1up)
-「〓」（記号ではなく実際に印刷された活字の後姿）：放浪山人[『探偵奇談新ジゴマ』](http://dl.ndl.go.jp/info:ndljp/pid/907501/82)

このフォントが実装している漢字の多くは、東京築地活版製造所が印刷した
深井鑑一郎[『標注 漢文入門』](http://dl.ndl.go.jp/info:ndljp/pid/868843)
及び漢字統一協会[『同文新字典』](http://dl.ndl.go.jp/info:ndljp/pid/863407)
の築地三号活字に由来します。
また「泌」は、東京築地活版製造所が印刷した
飯高芳康・青木純造[『医家綱鑑』](http://dl.ndl.go.jp/info:ndljp/pid/832992/140)
の古い築地三号活字に由来し、「窯」は東京築地活版製造所が印刷した
栗原鑑司[『石炭乾餾工業』](http://dl.ndl.go.jp/info:ndljp/pid/1131597/142)
に由来します。
「鮟鱇」も同じく細川潤次郎[『吾園随筆賸編　巻四』](http://dl.ndl.go.jp/info:ndljp/pid/985321/31)
に由来します。

このフォントが実装している漢字のうち、「壱弐泊峰峯肪匁蘆芦霰矧珂括享
脅娯煮釋譯据偵囁鞣禰鯰葵臆屑窟錆辿樽廿裡嚀埃屹犇縊縋薔跟軫辷顫掴殲塹
嗄紘栃畠蛛睆侘俎俤俥寵忉橙沓粂縹譫迚鴫鹼麾麿凧凩嗾埴埼憧憬撿擽柢燠瓩
瓱胛鎬閾噺怺恫挽灌瞞萎偲呶喀抒捗捩杣椴楠楢癈葦餠椛昴彿氐洌洹渙溯簀繻
髏咤曄燁瓔瞿菟觜杻嘸攘礒蕁蕈蠕顥佼孵嶮寥毘紬鵞僑冨凪梱鋲怜蔚薛塙摸瑳
袁鄒鈑鍔」は、
郁文舎印刷所が印刷した芳賀剛太郎[『誤似明弁 新案漢字典』](http://dl.ndl.go.jp/info:ndljp/pid/863027)
の築地三号活字に由来します。
このうち「壱弐」は同書のために特製された活字だった可能性があります。

このフォントが実装している漢字または漢字に準ずる記号のうち、次に掲げ
るものは東京築地活版製造所以外の印刷所が印刷した併記資料の築地三号活
字に由来します。

-「々」：井上哲次郎[『巽軒講話集 初編』](http://dl.ndl.go.jp/info:ndljp/pid/898305/198)
-「塀」：細越夏村[『迷へる巡礼の詩集』](http://dl.ndl.go.jp/info:ndljp/pid/876470/55)
-「耗」：添田寿一[『実用一家経済法』](http://dl.ndl.go.jp/info:ndljp/pid/949775/73)
-「枠」：写真術研究会[『実地応用素人写真術』](http://dl.ndl.go.jp/info:ndljp/pid/854001/9)
-「搾」：後藤喜間太[『工場巡り 日本の模範工業』](http://dl.ndl.go.jp/info:ndljp/pid/955203/161)
-「閑」：高津鍬三郎[『新編本邦小史 上巻』](http://dl.ndl.go.jp/info:ndljp/pid/1082828/24)
-「紺」：武田寿[『絵ものがたり 浄瑠璃の女』](http://dl.ndl.go.jp/info:ndljp/pid/906967/118)
-「礎」：杉山富槌[『心理的教授原則』](http://dl.ndl.go.jp/info:ndljp/pid/808928/25)
-「拓」：福禄寿翁[『成功自在 運命の開拓』](http://dl.ndl.go.jp/info:ndljp/pid/754677/16)
-「喰」：井上正賀[『神経衰弱栄養療法』](http://dl.ndl.go.jp/info:ndljp/pid/934058/101)
-「筈」：大熊資徳[『鯣』](http://dl.ndl.go.jp/info:ndljp/pid/908858/33)
-「冴」：沢ゆき子[『詩集 孤独の愛 』](http://dl.ndl.go.jp/info:ndljp/pid/909814/83)
-「唄」：沢ゆき子[『詩集 孤独の愛 』](http://dl.ndl.go.jp/info:ndljp/pid/909814/105)
-「驤」：石井平太[『大西郷の心の奥底』](http://dl.ndl.go.jp/info:ndljp/pid/951648/175)
-「呪」：伊藤環翠[『精神宗用義夫の奉公 岐阜放光 三年間ノ実験談』](http://dl.ndl.go.jp/info:ndljp/pid/899315/55)
-「詛」：片山孤村[『現代の独逸文化及文芸』](http://dl.ndl.go.jp/info:ndljp/pid/970299/73)
-「顎」：樋口紋太[『新時代之婦人生活手引』](http://dl.ndl.go.jp/info:ndljp/pid/961482/157)
-「癪」：竹内師水[『十二宮子供の躾方 淘宮上より観たる処世の解決』](http://dl.ndl.go.jp/info:ndljp/pid/920402/188)
-「濶」：宮地猛男[『訪問記』](http://dl.ndl.go.jp/info:ndljp/pid/898364/132)
-「鬘」：鈴木秋風[『新式赤毛布』](http://dl.ndl.go.jp/info:ndljp/pid/898515/81)
-「餉」：生駒彦三郎[『蚕飼ひの栞』](http://dl.ndl.go.jp/info:ndljp/pid/840487/31)
-「跛」：大橋新太郎[『幼年玉手函 第五編』](http://dl.ndl.go.jp/info:ndljp/pid/1168229/9)
-「截」：長田秀雄[『歓楽の鬼』](http://dl.ndl.go.jp/info:ndljp/pid/921829/77)
-「躙」：満木峰丸[『満洲之地理歴史』](http://dl.ndl.go.jp/info:ndljp/pid/767152/39)
-「喋」：尾崎行雄[『学堂回顧録』](http://dl.ndl.go.jp/info:ndljp/pid/953811/18)
-「玲」：岡本かの子[『浴身』](http://dl.ndl.go.jp/info:ndljp/pid/983510/59)
-「褪」：井川寛一郎[『インキ製造法』](http://dl.ndl.go.jp/info:ndljp/pid/847478/79)
-「蕊」：平川全篤[『実験薬用サフラン栽培法』](http://dl.ndl.go.jp/info:ndljp/pid/908679/17)
-「唸」：中央気象台[『気象雑纂 第1巻』](http://dl.ndl.go.jp/info:ndljp/pid/984839/6)
-「惣」：遠藤総越・加藤桃蹊[『芳譚』](http://dl.ndl.go.jp/info:ndljp/pid/778691/117)
-「瑠」：武田寿[『絵ものがたり 浄瑠璃の女』](http://dl.ndl.go.jp/info:ndljp/pid/906967/5)
-「噌」：桜井ちか子[『実用和洋惣菜料理』](http://dl.ndl.go.jp/info:ndljp/pid/946167/41)
-「伎」：松林伯知[『太閤栄華物語 夏之巻』](http://dl.ndl.go.jp/info:ndljp/pid/890439/76)
-「挿」：修文館[『女子家事訓』](http://dl.ndl.go.jp/info:ndljp/pid/848392/24)
-「堰」：長峰安三郎他[『式辞演説大全』](http://dl.ndl.go.jp/info:ndljp/pid/865628/72)
-「芯」：陸軍造兵廠[『考案記録. 第14回』](http://dl.ndl.go.jp/info:ndljp/pid/1241611/49)
-「腺」：坪井次郎[『坪井生理衛生教科書』](http://dl.ndl.go.jp/info:ndljp/pid/931424/40)
-「摯」：白面人[『働き盛りの男』](http://dl.ndl.go.jp/info:ndljp/pid/983272/168)
-「椎」：丘浅治郎[『簡易動物学講義』](http://dl.ndl.go.jp/info:ndljp/pid/832665/48)
-「氾」：干河岸貫一[『修養史譚』](http://dl.ndl.go.jp/info:ndljp/pid/756728/89)
-「挫」：坪谷善四郎[『通俗明治歴史』](http://dl.ndl.go.jp/info:ndljp/pid/773463/109)
-「疏」：日本書籍[『国語綴方教法及教授案　高等小學科第四學年　前期』](http://dl.ndl.go.jp/info:ndljp/pid/812112/60)
-「嶋」：山脇義男・嶋田浦[『実用和服裁縫問答書　上巻』](http://dl.ndl.go.jp/info:ndljp/pid/902350/98)
-「鳶」：國語科研究會[『高等小學言文一致文』](http://dl.ndl.go.jp/info:ndljp/pid/1083833/15)
-「夥」：乾坤独歩[『キウリアス・アイランド　冒険小説』](http://dl.ndl.go.jp/info:ndljp/pid/885983/64)
-「髷」：松崎天民[『漂泊の男流転の女』](http://dl.ndl.go.jp/info:ndljp/pid/908948/85)
-「沁」：大島正健[『漢音呉音の研究』](http://dl.ndl.go.jp/info:ndljp/pid/1126573/64)
-「鱈」：加治亮介[『大久保彦左衛門』](http://dl.ndl.go.jp/info:ndljp/pid/1718126/29)
-「鬚」：幸田露伴[『潮待ち草』](http://dl.ndl.go.jp/info:ndljp/pid/889068/47)
-「燵」：田村西男[『新落語』](http://dl.ndl.go.jp/info:ndljp/pid/891381/30)
-「埒」：五峰仙史[『滑稽老書生』](http://dl.ndl.go.jp/info:ndljp/pid/886397/39)
-「顰」：松崎天民[『淪落の女』](http://dl.ndl.go.jp/info:ndljp/pid/912220/90)
-「攫」：森晋太郎編訳[『セシル・ローヅ帝王流豪富譚』](http://dl.ndl.go.jp/info:ndljp/pid/782499/38)
-「噬」：下田歌子[『少女文庫　第二編』](http://dl.ndl.go.jp/info:ndljp/pid/1169239/36)
-「圀」：安永三四郎[『花紅柳緑』](http://dl.ndl.go.jp/info:ndljp/pid/754977/14)
-「壜」：弄珠子ビリケン[『和洋手品種あかし』](http://dl.ndl.go.jp/info:ndljp/pid/915482/100)
-「娑」：多田鼎[『仏伝涅槃篇』](http://dl.ndl.go.jp/info:ndljp/pid/817355/151)
-「懣」：白柳秀湖[『親分子分　英雄篇』](http://dl.ndl.go.jp/info:ndljp/pid/777518/86)
-「甃」：磯ケ谷紫江[『浅草の歌』](http://dl.ndl.go.jp/info:ndljp/pid/905360/21)
-「篏」：写真術研究会[『実地応用素人写真術』](http://dl.ndl.go.jp/info:ndljp/pid/854001/15)
-「罎」：原精一郎[『毒の話』](http://dl.ndl.go.jp/info:ndljp/pid/837123/164)
-「飜」：木下正中[『産婆學講義　下巻』](http://dl.ndl.go.jp/info:ndljp/pid/1082295/124)
-「搦」：渡辺霞亭[『豊臣秀吉　藤吉郎の巻　後編』](http://dl.ndl.go.jp/info:ndljp/pid/887526/112)
-「蚪」：野々垣淳一[『実験食用蛙飼養法』](http://dl.ndl.go.jp/info:ndljp/pid/1019470/24)
-「褄」：前田とみ子・宮川すい子[『家庭裁縫新書』](http://dl.ndl.go.jp/info:ndljp/pid/848583/21)
-「躓」：トルストイ[『性慾論』](http://dl.ndl.go.jp/info:ndljp/pid/897014/63)
-「鮨」：堀内新泉[『立志小説　人の妻』](http://dl.ndl.go.jp/info:ndljp/pid/945452/176)
-「鵙」：樋口二葉[『動物お伽噺』](http://dl.ndl.go.jp/info:ndljp/pid/1919391/185)
-「罠」：平塚篤[『破天荒大怪賊　ジゴマ少年』](http://dl.ndl.go.jp/info:ndljp/pid/1716437/37)
-「骶」：榊順次郎[『産婆学』](http://dl.ndl.go.jp/info:ndljp/pid/1082296/158)
-「鱲」：生間正起[『日本家事調理法』](http://dl.ndl.go.jp/info:ndljp/pid/849125/75)
-「齕」：桂湖村他[『史記国字解　第一』](http://dl.ndl.go.jp/info:ndljp/pid/959952/133)
-「藐」：光悦会[『光悦　天』](http://dl.ndl.go.jp/info:ndljp/pid/1183305/51)
-「罣」：大谷光瑞[『般若波羅密多心経講話』](http://dl.ndl.go.jp/info:ndljp/pid/1021610/45)
-「栞」：横浜新報社著作部[『横浜繁昌記』](http://dl.ndl.go.jp/info:ndljp/pid/764453/245)
-「萠」：白柳秀湖[『大日本閨門史』](http://dl.ndl.go.jp/info:ndljp/pid/980907/261)
-「蚓」：茅原廉太郎[『世界文明推移史論』](http://dl.ndl.go.jp/info:ndljp/pid/768401/106)
-「鵺」：松家旅館[『京の伝説と戯曲を語る』](http://dl.ndl.go.jp/info:ndljp/pid/1102923/28)
-「㡡」：久保田万太郎[『青鷺』](http://dl.ndl.go.jp/info:ndljp/pid/963073/4)
-「堺」：大西五一郎・宮本通義[『堺市繁栄政策』](http://dl.ndl.go.jp/info:ndljp/pid/784605/6)
-「場」：瀬田弥太郎[『抒情小曲集 哀吟余情』](http://dl.ndl.go.jp/info:ndljp/pid/914575/37)
-「樗」：藪宕山[『一基の塔』](http://dl.ndl.go.jp/info:ndljp/pid/921781/14)
-「吽」：富岡俊次郎[『南無阿吽阿』](http://dl.ndl.go.jp/info:ndljp/pid/1091590/5)
-「悧」：大木遠吉[『我が抱負』](http://dl.ndl.go.jp/info:ndljp/pid/898672/126)
-「悸」：岡田道一[『少女の衛生』](http://dl.ndl.go.jp/info:ndljp/pid/935702/46)
-「扼」：野崎小蟹[『水兵と其母』](http://dl.ndl.go.jp/info:ndljp/pid/1720673/56)
-「瓏」：鈴木為次郎[『新式囲碁死活研究 下巻』](http://dl.ndl.go.jp/info:ndljp/pid/927128/34)
-「舐」：大窪弥次六[『わんぱく中学生』](http://dl.ndl.go.jp/info:ndljp/pid/915702/39)
-「唵」：岩間月舟[『一休珍話』](http://dl.ndl.go.jp/info:ndljp/pid/915592/72)
-「澍」：鈴木為次郎[『本化妙観配十二支御聖訓之栞』](http://dl.ndl.go.jp/info:ndljp/pid/823951/160)
-「伜」：赤壁紅堂[『中京実業家出世物語』](http://dl.ndl.go.jp/info:ndljp/pid/1020503/80)
-「俣」：逓信省編[『水力調査書　第四巻　九州』](http://dl.ndl.go.jp/info:ndljp/pid/966492/117)
-「宍」：玉田玉秀斎[『大力無双宍戸源八郎正国』](http://dl.ndl.go.jp/info:ndljp/pid/890273/111)
-「廼」：東久世通禧編[『竹廼舎歌集』](http://dl.ndl.go.jp/info:ndljp/pid/1900324/7)
-「橇」：井口紫濤[『探険奇談氷原旅行』](http://dl.ndl.go.jp/info:ndljp/pid/888003/80)
-「檮」：佐伯有義[『古事記講義』](http://dl.ndl.go.jp/info:ndljp/pid/1020209/104)
-「浬」：小泉憲貞[『境港沿革史』](http://dl.ndl.go.jp/info:ndljp/pid/950827/26)
-「粍」：陸軍造兵廠[『考案記録　第16回』](http://dl.ndl.go.jp/info:ndljp/pid/1241625/52)
-「糎」：陸軍造兵廠[『考案記録　第16回』](http://dl.ndl.go.jp/info:ndljp/pid/1241625/87)
-「簸」：町田桜園編[『学校史劇　第二編（神代の巻二）』](http://dl.ndl.go.jp/info:ndljp/pid/1456728/6)
-「纒」：巌谷小波・金子紫草[『少年世界読本　第三巻』](http://dl.ndl.go.jp/info:ndljp/pid/1169635/64)
-「罫」：台東隠士[『株式期米相場の活顧問　上巻』](http://dl.ndl.go.jp/info:ndljp/pid/913827/17)
-「驢」：園部紫嬌[『講話資料新お伽百話』](http://dl.ndl.go.jp/info:ndljp/pid/1919774/25)
-「埜」：印旛郡編[『千葉県印旛郡誌』](http://dl.ndl.go.jp/info:ndljp/pid/950705/349)
-「狛」：淀川左岸水害予防組合編[『淀川左岸水害予防組合誌　後編附表』](http://dl.ndl.go.jp/info:ndljp/pid/1448867/6)
-「珪」：那須章弥編[『セメント節約剤　珪藻土講話』](http://dl.ndl.go.jp/info:ndljp/pid/969770/6)
-「痙」：弘田長[『小児看護の栞』](http://dl.ndl.go.jp/info:ndljp/pid/934434/72)
-「苅」：横瀬夜雨[『花守日記』](http://dl.ndl.go.jp/info:ndljp/pid/889219/36)
-「馮」：河瀬蘇北[『現代之人物観無遠慮に申上候』](http://dl.ndl.go.jp/info:ndljp/pid/959082/206)
-「咋」：石川県羽咋郡[『羽咋郡誌』](http://dl.ndl.go.jp/info:ndljp/pid/764730/6)
-「桝」：小野強編[『閻魔言』](http://dl.ndl.go.jp/info:ndljp/pid/898421/59)
-「瀞」：山形県経済部編[『出羽百姓一揆録』](http://dl.ndl.go.jp/info:ndljp/pid/1234949/18)
-「癌」：田中裕吉[『病理纂録』](http://dl.ndl.go.jp/info:ndljp/pid/834107/34)
-「瀦」：日本国勢調査記念出版協会[『日本国勢調査記念録　福岡県』](http://dl.ndl.go.jp/info:ndljp/pid/907045/16)
-「熔」：東京地学協会[『伊豆大島火山』](http://dl.ndl.go.jp/info:ndljp/pid/831433/21)
-「琳」：藤岡作太郎[『近世絵画史』](http://dl.ndl.go.jp/info:ndljp/pid/936288/58)
-「瘠」：吉川南湖[『青年修養　教への泉』](http://dl.ndl.go.jp/info:ndljp/pid/915317/43)
-「碕」：高碕達之助[『缶詰及製缶業から工作機械製造業に』](http://dl.ndl.go.jp/info:ndljp/pid/1091606/1)
-「鈷」：権田雷斧[『真言密教法具便覧　乾』](http://dl.ndl.go.jp/info:ndljp/pid/926974/31)
-「鑓」：文部省調査[『全国優良小学校実況』](http://dl.ndl.go.jp/info:ndljp/pid/808955/201)
-「躊躇」：トルストイ 著・大住舜 抄訳[『性慾論』](http://dl.ndl.go.jp/info:ndljp/pid/897014/98)
-「曼荼」：佐伯法雲[『南無大師』](http://dl.ndl.go.jp/info:ndljp/pid/822232/78)
-「珈琲」：山田稲子・真能まさき[『実践家政法』](http://dl.ndl.go.jp/info:ndljp/pid/848379/20)
-「茱萸」：清水好太郎[『詩集　はらいぞう』](http://dl.ndl.go.jp/info:ndljp/pid/919384/33)
-「檸檬」：遠藤治一[『周密栽培果樹要覧』](http://dl.ndl.go.jp/info:ndljp/pid/944965/32)
-「蟷螂」：山田潤二[『伯林脱出記』](http://dl.ndl.go.jp/info:ndljp/pid/953118/59)

また次に掲げるものは、東京築地活版製造所以外の印刷所が印刷した併記資
料の、おそらく築地二号と思われる活字に由来します。

-「皙」：渡部万蔵[『世界大勢論』](http://dl.ndl.go.jp/info:ndljp/pid/783404/15)

また次の掲げるものは、東京築地活版製造所が印刷した併記資料の四号活字
に由来します。

-「𢌞」：ワールブルヒ[『実験物理学』](http://dl.ndl.go.jp/info:ndljp/pid/830128/267)
-「埵」：駒ケ嶺愚童[『最新案内十和田の錦』](http://dl.ndl.go.jp/info:ndljp/pid/949905/27)
-「揷」：佐藤仁之助[『新撰仮字遣』](http://dl.ndl.go.jp/info:ndljp/pid/862376/53)
-「坩堝」：近藤会次郎[『近世工業化学書』](http://dl.ndl.go.jp/info:ndljp/pid/847516/18)

また次に掲げるものは、東京築地活版製造所以外の印刷所が印刷した併記資
料の、おそらく築地四号と思われる活字に由来します。

-「呟」：中村京[『寂しい跫音』](http://dl.ndl.go.jp/info:ndljp/pid/921928/57)
-「枡」：山枡儀重[『欧米革新教育の実際』](http://dl.ndl.go.jp/info:ndljp/pid/980041/15)
-「匆」：鎌内庄太郎[『実業教育　商業作文資料　上』](http://dl.ndl.go.jp/info:ndljp/pid/866000/48)
-「溲」：南梁居士[『偉人豪傑言行録』](http://dl.ndl.go.jp/info:ndljp/pid/777424/100)
-「臙」：糟谷美一[『昆虫の生涯』](http://dl.ndl.go.jp/info:ndljp/pid/832683/193)
-「屓」：井上江花[『江花叢書　第一巻』](http://dl.ndl.go.jp/info:ndljp/pid/922037/31)
-「鶸」：山村暮鳥[『童謡童話集　万物の世界』](http://dl.ndl.go.jp/info:ndljp/pid/970196/18)
-「婀」：持原皿山[『軍人の恋』](http://dl.ndl.go.jp/info:ndljp/pid/886183/13)
-「蠍」：中川柳涯編[『ポケット伊蘇普物語』](http://dl.ndl.go.jp/info:ndljp/pid/896654/114)
-「骰」：穂積陳重[『法窓夜話』](http://dl.ndl.go.jp/info:ndljp/pid/936012/53)
-「蚖」：勝井桜涯[『嗚呼蒲生氏 上巻』](http://dl.ndl.go.jp/info:ndljp/pid/945061/14)
-「嬬」：斎藤渓舟[『女官物語』](http://dl.ndl.go.jp/info:ndljp/pid/946223/33)
-「彬」：坪井忍[『国の光』](http://dl.ndl.go.jp/info:ndljp/pid/755211/12)
-「詑」：植松美佐男[『家庭少女小説　勿忘草』](http://dl.ndl.go.jp/info:ndljp/pid/908441/74)
-「姶」：地質調査所編[『工業原料用鉱物調査報告　第16号』](http://dl.ndl.go.jp/info:ndljp/pid/929985/26)
-「噤」：久木田七郎[『鍼灸手引草』](http://dl.ndl.go.jp/info:ndljp/pid/907861/36)
-「楕」：飯嶋賢之輔編[『三工宝典』](http://dl.ndl.go.jp/info:ndljp/pid/961964/12)
-「硲」：硲慈弘[『天台宗聖典』](http://dl.ndl.go.jp/info:ndljp/pid/1054679/411)
-「薗」：台湾総督官房調査課[『南支那及南洋調査　第187輯』](http://dl.ndl.go.jp/info:ndljp/pid/1148609/15)


## Oradano明朝フォント／Oradano明朝GSRRフォントの利用

このフォントは、印刷・表示、電子文書への埋め込み等の目的で、誰もが自
由に無償で用いることができます。
このフォントの配布・再配布は、自由に無償で行うことができます。
このフォントを、より大きな規模のソフトウエアパッケージの一部として販
売するなどしても構いません。
このフォントを用いて新たなフォントの開発を行うことも可能です。


## Oradano明朝フォント／Oradano明朝GSRRフォントの免責事項

Oradano明朝フォント／Oradano明朝GSRRフォントは、「あるがまま」で提供
される物であり、製作者および再配布者は、公的・私的な規格や言語慣習へ
の適合性、何らかの用途への有用性などの、品質に関する保証を一切行いま
せん。
このフォントの利用に起因する損害に対し、その責任はすべて利用者が負う
ものとします。損害の起こる可能性が知られていた場合でも、製作者および
再配布者は、法的・道義的な責任を負うことはありません。
製作者および再配布者は、このフォントに不具合が発見されたときに、それ
を修正・告知する義務を負いません。

