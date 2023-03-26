# initializing ciphertext
cipherText = '''CKCLBAELDK DGJ LFNSMBCA CGQEGCCAI JCUCKFS DGJ LACDBC SAFJMLBI BHDB LHDGQC BHC
OFAKJ DGJ NDVC FMA KEUCI CDIECA BHC LCKK SHFGCI OC JCSCGJ FG BHC LFNSMBCAI MICJ EG
GDBEFGDK ICLMAEBR DGJ BHC CKCLBAELDK IRIBCNI BHDB NDVC FMA LDAI FSCADBC OCAC DKK
LACDBCJ TR CKCLBAELDK DGJ LFNSMBCA CGQEGCCAI DB OSE OC VCCS BHDB SAFQACII
NFUEGQ PFAODAJ OEBH FMA EGGFUDBEUC ACICDALH DGJ FMB-FP-BHC TFY DSSAFDLHCI BHC
JCSDABNCGB FP CKCLBAELDK DGJ LFNSMBCA CGQEGCCAEGQ DB OSE LHDKKCGQCI IBMJCGBI
BF SMIH BHCNICKUCI BF MGJCAIBDGJ IFLECBRI DGJ BCLHGFKFQRI LFNSKCY EIIMCI EG D
TAFDJCA LFGBCYB BHDG OHDBI EG PAFGB FP BHCN OC ODGB FMA IBMJCGBI OHCBHCA BHCR
DAC CDAGEGQ DG MGJCAQADJMDBC NEGFA FA D JFLBFADBC BF BDLVKC IFLECBRI NFIB
SACIIEGQ SAFTKCNI DGJ MGLFUCA GCO ODRI FP IFKUEGQ BHCN OHCBHCA EBI JCUCKFSEGQ
IRIBCNI BHDB LDG KFLDBC PEACPEQHBCAI EG BHC NEJJKC FP D TMAGEGQ TMEKJEGQ FA
LACDBEGQ GCMAFSAFIBHCBELI BHDB KFFV DGJ PMGLBEFG KEVC GDBMADK KENTI FMA
PDLMKBR DGJ IBMJCGBI DAC DB BHC PAFGB CJQC FP ACNDAVDTKC EGGFUDBEFG OHEKC
DJUDGLEGQ BCLHGFKFQECI EI DB FMA LFAC OC DKIF BDVC HMNDG LFGGCLBEFGI UCAR
ICAEFMIKR EG CLC OC SAEJC FMAICKUCI FG BHC PDNEKR-KEVC DBNFISHCAC OC LMKBEUDBC;
PDLMKBR IBMJCGBI DGJ IBDPP CGLFMADQC CDLH FBHCAI CUCAR IMLLCII DGJ DAC BHCAC PFA
BHC LHDKKCGQCI TFBH EG BHC LKDIIAFFN DGJ EG KEPC'''
cipherText2 = cipherText.replace(" ", "")
# length of cipher text
cipher_len = len(cipherText2)
# initializing empty variables
az_freq = {}


# finding the letter frequency for each letters A to Z
def letter_freq(cipher, freq_arr, freq_len):
    # placeholders variables
    perc_str = "%"
    for char in cipher:
        # checks if letter is already in the array
        if char in freq_arr:   
            freq_arr[char] += 1
        else:
            freq_arr[char] = 1
    
    # runs through the array and calculates the percentages
    for char2, amt in freq_arr.items():
        # calculates the percentage and rounds to the nearest whole num
        freq_arr[char2] = str(round(((amt/freq_len)*100) , 2)) + perc_str
    
    print("Letter frequency percentage in the ciphertext is: \n " 
         + str(freq_arr))

    return freq_arr


# test functions
#----------------------------------------------
# lett_perc = letter_freq(cipherText2, az_freq, cipher_len)

# Looking at patterns 1 attempt at a time
attempt1 = cipherText.replace('C','e')
attempt2 = attempt1.replace('B','t')
attempt3 = attempt2.replace('D','a') 
attempt4 = attempt3.replace('A','r') 
attempt5 = attempt4.replace('Q','g')
attempt6 = attempt5.replace('G','n')
attempt7 = attempt6.replace('L','c')
attempt8 = attempt7.replace('E','i')
attempt9 = attempt8.replace('I','s')
attempt10 = attempt9.replace('J','d')
attempt11 = attempt10.replace('K','l')
attempt12 = attempt11.replace('F','o')
attempt13 = attempt12.replace('O','w')
attempt14 = attempt13.replace('T','b')
attempt15 = attempt14.replace('N','m')
attempt16 = attempt15.replace('S','p')
attempt17 = attempt16.replace('M','u')
attempt18 = attempt17.replace('U','v')
attempt19 = attempt18.replace('R','y')
attempt20 = attempt19.replace('P','f')
attempt21 = attempt20.replace('V','k')
attempt22 = attempt21.replace('Y','x')
attempt23 = attempt22.replace('H','h')
print("\n" + attempt23)