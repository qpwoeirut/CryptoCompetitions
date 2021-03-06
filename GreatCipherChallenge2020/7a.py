from utils.cryptography.transposition import decrypt

s = "AVLTWTEOHOFOCELICKTA DRROSIEEDSETDRASITEN DAAIIALSXZTFTEAHPSLB EAMEDTSMDIHSOTNWUNON ETIEIRHVNRTEIQIOCLUE SCEUIWHNRNHTPEAIHODN DNWHHAGHSAMSIHDOTCET HERDIEAEINPSOSGLUFTU INEHESGMSRHTUUIIHCPO RIUFISCDMNOIERGLTOBL EHUOKYELTESCDMASONAV EAREWRVAAEYOBNRFULSJ AANAENSONTEBMSTWYEBE RSENRTIRHIHSSENETOAG TRATEHETHOIPERRSEDEF OIHUHUMOCEREWHYTSMTW EREWCRIDSKEEHHIGVOON GAHACISABOTTVALWOEDD AOCIYNWEVTDESEHHXSLE YLDNLDIBGTIKEIHSEILE MVNEOSEDNUESTTGLAHHH TOFMENRTAROEHTAMOETN DIDECTRIREHIFETENFNO WSENIAJWNMRAHOMDNETE DEEEMILFTRAYOHETBRES TDZTTOEAHHRLBTEEIEOE NMOLOJEFHRONAEIYTLRG IDIHBNIKERASEIOLLTRT HNDTNEDWHLREAEYIESOO NTAWSEHRHHOETOEFPYMC ORRTYUEDHCLGWAODAINM PEHNTLNIXYACSIFCYAEO REEENJWVNDAAITHNSDAI SEOOSANNHETTSELTITRF MPSAHOLINESENDYTAGTP RNHENETEEGVERLHEDFIE RFUNRSSCIUEOHNDLMATE RHLEEAEIDWSBESASEVHS CIETTODDHHNEBEESRYOR SHEIESARTNHDYTOEVLLT IRNTMCOYHIEMBISFAUMS BLAGSIESRENYEODGWNSB YAHIRMRESSRCRTCDYSEA RYSNFCLSDOEEOARLSASM RSWEAHTHLBUBOIERYMZT HHSNESEADNAWNOTTAILM AOELENLDYAWIOTTHVNOD RALTDINACSNDYAWKPARH ONOHRWHUEEHENRFEFDPE RAIOGAISAOPNHRULDTAT HONSOATGAHDHTYENIOTR"

# print(ngrams(s, 1))

order = [0]
for i in range(19):
    order.append(order[-1] + 5)
    if order[-1] >= 20:
        order[-1] -= 19

ans = ""
for block in s.split():
    ans += decrypt(block, order)

print(ans)