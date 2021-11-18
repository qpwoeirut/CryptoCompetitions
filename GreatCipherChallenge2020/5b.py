from string import ascii_lowercase

from utils.cryptography.analyze import ngrams, repeats, replace_by_dict

s = "YLSYL LN OBOLHPB OQSOB YLN QHEFLSB YL LSZJWJ LH NJS ABOXHQYJYLS LXFBZLJS, NJS ABFPLS ELHLFJNLS IJH YBPJYB, ZJXNJPQHJOLHPL, JN BFYLHJOQLHPB MXFQYQAB YL NBS QHSPFXOLHPBS HBFOJPQDBS HLALSJFQBS ZJFJ JABOZJSJF NJ FLJNQYJY NLEJN G ZBNQPQAJ LSZJWBNJ JN FQPOB YLN AJOÑQB IQSPBFQAB YL QHSPQPXAQBHJNQUJAQBH YL NJ QYLJ YL LXFBZJ. LH LN OJFAB YL LSL ZFBALSB YL YLSJFFBNNB EFJYXJN G AFLAQLHPL ABHSBNQYJAQBH YL NJ XHQYJY LXFBZLJ -LVQAJUOLHPL JABEQYB LH NJ DLFPQLHPL YLN YLFLAIB QHPLFHB LSZJWBN ZBF NJ OBYLFHJ ZLFSZLAPQDJ JZBFPJYJ ZBF LN JFPQAXNB HBDLHPJ G PFLS YL NJ ABHSPQPXAQBH LSZJWBNJ- LN ABHEFLSB YL NBS YQZXPJYBS G LN SLHJYB JZFBÑJFBH, LH DÍSZLFJS YL NJ FLXHQBH YL OJJSPFQAIN, SLHYJS FLSBNXAQBHLS LH NJS KXL, XHJ DLU OJS, SL JNLHPJÑJ VQFOLOLHPL NJ ZLFSLDLFJHAQJ LH LSL ZFBALSB IQSPBFQAB. YL LHPFL NBS JOZNQBS ABHPLHQYBS YL YQAIJS FLSBNXAQBHLS, LS BZBFPXHB YLSPJAJF JIBFJ LN YLAQYQYB JZBGB YL NJS ABFPLS ELHLFJNLS LH VJDBF YL NJ QHSPQPXAQBHJNQUJAQBH YL XHJ QHAQZQLHPL AQXYJYJHVJ ABOXHQPJFQJ. LH LVLAPB, LN JFPQAXNB E, A YLN PFJPJYB YL NJ XHQBH LXFBZLJ ZFBZBHL XHJ HXLDJ FLYJAAQBH ZJFJ LN JFPQAXNB BAIB Ñ, JZJFPJYB XHB, YLN PFJPJYB ABHSPQPXPQDB YL NJ ABOXHQYJY LXFBZLJ. LH LN SL LSPJÑNLAL KXL PBYB AQXYJYJHB YL NJ XHQBH KXL FLSQYJ LH XH LSPJYB OQLOÑFB YLN KXL HB SLJ HJAQBHJN PLHYFJ YLFLAIB J SLF LNLAPBF G LNLEQÑNL LH NJS LNLAAQBHLS OXHQAQZJNLS YLN LSPJYB OQLOÑFB LH KXL FLSQYJ; G LNNB, LH NJS OQSOJS ABHYQAQBHLS KXL NBS HJAQBHJNLS YL YQAIB LSPJYB."

# for i in range(1, 4):
#     print(ngrams(s, i))
#
# print(repeats(s, 2))

table = {
    'A': 'c',
    'B': 'o',
    'D': 'v',
    'E': 'g',
    'F': 'r',
    'G': 'y',
    'H': 'n',
    'I': 'h',
    'J': 'a',
    'K': 'q',
    'L': 'e',
    'M': 'j',
    'N': 'l',
    'Ñ': 'b',
    'O': 'm',
    'P': 't',
    'Q': 'i',
    'S': 's',
    'U': 'z',
    'V': 'f',
    'W': 'ñ',
    'X': 'u',
    'Y': 'd',
    'Z': 'p'
}

print(len(table))

print(s)
s = s.replace('Í', 'i')
print(replace_by_dict(s, table).upper())