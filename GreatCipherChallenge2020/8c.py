from itertools import product

from utils.cryptography.analyze import quick_analyze
from utils.cryptography.straddle_checkerboard import solve
from utils.factors import find_factors

s = "911277265027555923771329932648265265264824066265025682612911235452550614527555926526482911235452133291127105209914255061452755592612648261240662133299325506145265025682612406626482885023771326525506145264825682911235452550614527726502377132550614526502652652885026482885027555921332772550614529932550614529112354525506145237713271052993271052406627105209914255061452755592650256826129112354525506145288502710528850255061452993265029112354527555927105240839291124066299326502377132550614523771325506145277265029932550614529112354525506145236542650237713237713255061452993277271052488562411183476288502133275559271052568291123545255061452365426502772755592911235452650291123771326482911255061452911235452550614524885626526502772755592911235452650291124885626502911248856235452377132550614527726502993255061452911235452550614523654240839237713236542408392377132377132648299326126502568261275559235452408392568291123545255061452002993240839288502648271052408392755592377132650256826125506145299327555925682650291124885623545235452550614529112710527105241118347623545264827555920991427105299320505326502652755592772710529932612648256823545265025682612652710525682406629112648288502550614529112354525506145288502650256828271052885025506145200271052550614523545255061452755592710524083924066235452911275559271052993255061452755592911255061452612354525506145237713213329112354525506145291124083928850291124083928850291129932550614525506145265025682612755592911271052710526126502772354526482652550614526482568291123545271052408392406623545291126502568261265027555926482568240839200200264827555923545291123545271052408392406623545291123545255061452755592911271052710526129112354525506145236542650237713237713255061452993277271052488562411183476277264829112354525506145213325506145275559271052002002652650288502550614524885626502885025506145277235452648200200265264825682406629112354529932710524083924066235452911235452550614529112408392652406625506145213327727105271052612650256826123771324083929932377132652550614526126502755592648291124885626502885025506145271052568255061452911277271052710525682550614529112772710526502568261291123545299327105240839240662354526502568261291123545299327105240839240662354529112354525506145209914271052993205053265026523771326526502612550614527725506145256829112755592568264824885624111834762550614529932755592568265024885624111834762354525506145265255061452002911264829112612550614526502612650256826127726482911235452648291127555923545255061452650261235452550614527725506145256829112406626502652408392885020505323545264825682406623771326502488562411183476265025682612354526502755592911291123545271052408392755592652650264825682911235452550614523654265023771323771325506145299327727105248856241118347624885627105288502550614529112710528850213326502993288502755592885021332377132550614526502885026482755592354523771327105213327105200299326502377132365427105240839275559261265021332488562650265265271052710523545248856265026526526502133235452550614524885623545271052993291126525506145261264825682354526482755592365427105213329112772650275559237713299326482652652648240662650256826129112354525506145275559265264829112354521332911271052099142550614527555926126482612406621332993255061452650256826124066264828850237713265255061452648256829112354525506145277265023771325506145265026526528850264828850275559213327725506145299325506145291123545255061452377132710529932710524066271052099142550614527555926502568261291123545255061452885027105288502550614529932650291123545275559271052408392911240662993265023771325506145"
print(find_factors(len(s)))
for r in solve(s):
    print(r)
print()
s = s[::-1]
for r in solve(s):
    print(r)
# best = (float('inf'), "", "")
# for i in range(1, 5):
#     for sub in product("012345", repeat=i):
#         s1 = ''.join([str(int(c) + int(sub[idx % i])) for idx,c in enumerate(s)])
#         texts = solve(s)
#         best = min(best, texts[0])
#     print(best)


#ttessenceswhersspettrendlenanandledinnenceblenotteryawingaswhenandletteryaprettesmaittgewingaswhenondlenodinneprettrewinganceblenodinnendlellcersspenawingandlebletteryawingassencersspewingancenanallcendlellceswhepressewingattrewingatteryawingarsspesmattresmadinnesmaittgewingaswhenceblenotteryawingallcesmallcewingattrencetteryaswhesmadilrtettedinnettrencersspewingarsspewingassencettrewingatteryawingarnyencersspersspewingattressesmadllbedturdsnellcepreswhesmabletteryawingarnyencesseswhetteryancettersspendlettewingatteryawingadllbenancesseswhetteryancettedllbencettedllberyarsspewingassencettrewingatteryawingarnyedilrtersspernyedilrtersspersspendlettrenonceblenoswheryadilrtebletteryawingaiiettredilrtellcendlesmadilrteswhersspenceblenowingattreswheblencettedllberyaryawingattesmasmadturdsneryandleswheittgesmattreickencenaswhessesmattrenondlebleryanceblenonasmabledinnettendlellcewingatteryawingallcenceblelesmallcewingaiiesmawingaryawingaswhesmadilrtedinneryatteswhesmattrewingaswhettewinganoryawingarsspepretteryawingattedilrtellcettedilrtellcettettrewingawinganceblenoswhettesmasmanoncesseryandlenawingandlebletteryasmadilrtedinneryattenceblenonceswhendlebledilrteiieiiendleswheryatteryasmadilrtedinneryatteryawingaswhettesmasmanotteryawingarnyencersspersspewingattressesmadllbedturdsnessendletteryawingaprewingaswhesmaiieiienancellcewingadllbencellcewingasseryandleiieiienandlebledinnetteryattresmadilrtedinneryatteryawingattedilrtenadinnewingapressesmasmanonceblenorsspedilrtettrersspenawinganonceswhendlettedllbencellcewingasmablewingattessesmasmablewingattessesmanceblenotteryattresmadilrtedinneryanceblenotteryattresmadilrtedinneryatteryawingaittgesmattreickencenarsspenancenowingassewingabletteswheblendledllbedturdsnewingattreswheblencedllbedturdsneryawinganawingaiiettendlettenowingancenonceblenossendletteryandletteswheryawingancenoryawingassewingablettedinnencenadilrtellceickeryandlebledinnersspencedllbedturdsnenceblenoryanceswhettetteryasmadilrteswhenancendlebletteryawingarnyencersspersspewingattressesmadllbedturdsnedllbesmallcewingattesmallceprencettrellceswhellceprersspewingancellcendleswheryarsspesmapresmaiiettrencersspernyesmadilrteswhenoncepredllbencenanasmasmaryadllbencenanancepreryawingadllberyasmattrettenawinganondlebleryandleswhernyesmaprettessenceswhersspettrendlenanandledinnenceblenotteryawingaswhenandletteryaprettesmaittgewingaswhenondlenodinneprettrewinganceblenodinnendlellcersspenawingandlebletteryawingassencersspewingancenanallcendlellceswhepressewingattrewingatteryawingarsspesmattresmadinnesmaittgewingaswhenceblenotteryawingallcesmallcewingattrencetteryaswhesmadilrtettedinnettrencersspewingw

s = "TWASBRILLIGANDTHESLITHYTOVESDIDGYREANDGIMBLEINTHEWABEALLMIMSYWERETHEBOROGOVESANDTHEMOMERATHSOUTGRABEBEWARETHEJABBERWOCKMYSONTHEJAWSTHATBITETHECLAWSTHATCATCHBEWARETHEJUBJUBBIRDANDSHUNTHEFRUMIOUSBANDERSNATCHHETOOKHISVORPALSWORDINHANDLONGTIMETHEMANXOMEFOEHESOUGHTSORESTEDHEBYTHETUMTUMTREEANDSTOODAWHILEINTHOUGHTANDASINUFFISHTHOUGHTHESTOODTHEJABBERWOCKWITHEYESOFFLAMECAMEWHIFFLINGTHROUGHTHETULGEYWOODANDBURBLEDASITCAMEONETWOONETWOANDTHROUGHANDTHROUGHTHEVORPALBLADEWENTSNICKERSNACKHELEFTITDEADANDWITHITSHEADHEWENTGALUMPHINGBACKANDHASTTHOUSLAINTHEJABBERWOCKCOMETOMYARMSMYBEAMISHBOYOFRABJOUSDAYCALLOOHCALLAYHECHORTLEDINHISJOYTWASBRILLIGANDTHESLITHYTOVESDIDGYREANDGIMBLEINTHEWABEALLMIMSYWERETHEBOROGOVESANDTHEMOMERATHSOUTGRABE"
s = [c.upper() for c in s if c.isalpha()]
s = ''.join(s)
s = s.replace('X', 'Z')
print(s)
print(len(s))