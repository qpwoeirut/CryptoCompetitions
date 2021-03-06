from utils.cryptography.analyze import quick_analyze
from gunnCryptoClub.polyalphabetic.vigenereCipher import decrypt


s = "DKAPHSGCGIKFRBZOJDLSLYINBKOIFGAYCDDNSWNSLFOYSLPVWVIEXKHFCAQDUKLSOUCRPBLWIUEODINTQLWIVHSQIXLJNJSEKNDBKOMEUSNPSAONHINPBDZVKHMJRDZEEWKULSWIEKJGYCSWXTGGDBCAFVTLMIBSBSFTTJQOPRBCIEOHAEUPCLMOALZHMGKCYZECGMCHJDIFYDYZSSTZHRLYNOWXQJZUBMJQFNQYZOIHWUYAYWOOTMJDTYEJKEHQYIHIHAVHUBWDCXCCMFNDZWRBBCKOCNGWZTKNBDSXPYDBKOMEAMQGCJCSQUAADZHHQJNVPXLSFKDIWRPSLKNYIDDZEZQPSFUUSLVYHVCIEPSJIAJXJSEKIHOUPXVKGHBVTCGXSZYHMZLBAJVJYPLDXYHLWLIDOXNVFIZTEQRUBBEZVPFYVMDUZDAKINOYHKVJXAQSIVDWICKXLDZTTKNBSNTAJVPEQPUXTYZVPVWVYUVMKNNRPOSLBEJVGMMWCCEJVFOKCRLMAQIFGXAXNHKCKSHELRKLMXBEGBVJXAQJHRKPCDSSALWMKAXGYLLWNFFHAWZWCHKSAALHFZURQSSVQPXVBHARGRMWATRWIWKZQWPMQCAURHKYIEMHOXDUJQJEZJSOSEGKPYYPIKHUHUCJSWDSJAXYVGFUASVUJHZGRIBVTGJDSJKRXTMDTJPZJDIIXRBMMUOMQIZONBPLXKITBVWJZGCZMOHTSQIYVXXEGBVRPZYYINXPYMOIIFJZVQNVWHBUVOQSWOVLYHLOALLKFZDJCYHZGNVQTARCRRBMMWESUIMYXGWHKIVOQRWVBBLAEVPTAVYNHCCLHAVCFPEQRKKWGWIHEAWNYVWVJSEGYPTIKJKACBWIHESQXCLAOOSEGJUUUNSEEWMIWSTZHHUBWDCXJQPTRYZSEHRFQYTTZDYSBBSNZQOTEVDJIICSMBOITZDYSVVOYSQJZEBENJCXUIXSCIFFFSLCGZGRIZNNIPMWYQUVRIHWWBUTRMPGXFOPFSWQGXPXWKCAFGWAUXPQFLQYCLUYSLLGHAOXDLKJIVDXEQVOJVFUSLRMEIQBVSGVTUUBKTCQJZPGXAVPXQBMFTPDLJJINDEDODZBAIWRUUYWWBXNHHFILCRLMZCFFFQJHRECCVTTAJ"

quick_analyze(s)
print(decrypt("qwertyuiopasdfghjklzxcvbn", s))