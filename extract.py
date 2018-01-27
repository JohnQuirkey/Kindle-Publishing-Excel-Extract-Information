import csv
import os

path = os.getcwd()
exports = "/kindleExports/"
dir_src = path + exports +'KDPSalesDashboard.csv'


def checkCsvFiles():
    for root,dirs,files in os.walk(dir_src):
        for file in files:
           if file.endswith(".csv"):
               #print(file)
               readFile(file)

def readFiles():
    count = 0
    dareTitle = 'Dare: The New Way to End Anxiety and Stop Panic Attacks Fast (+Bonus Audios)'
    wegTitle = 'Weg Mit Der Panik: Wie Sie sich von Angst und Panik befreien'
    panicoTitle = 'Panico Afuera: Técnica Natural que ayudará a detener rápidamente tus Ataques de Pánico y tu Ansiedad General'

    dare =dareTitle[:55] + (dareTitle[55:] and '..')
    weg = wegTitle[:55] + (wegTitle[55:] and '..')
    panico = panicoTitle[:55] + (panicoTitle[55:] and '..')

    wegNumbers = 0
    dareNumbers = 0
    panicoNumbers = 0

    #Currencies
    USDRoyality = 0
    BRLRoyality = 0
    CADRoyality = 0
    EURRoyality = 0
    GBPRoyality = 0
    INRRoyality = 0
    MXNRoyality = 0
    AUDRoyality = 0


    with open(dir_src, newline='') as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            count = count + 1
            strDate = row[0]
            bookName = row[1]
            bookNumbers = row[9]
            netRoyality = row[13]
            curr = row[14]

            # Sales in Currencies, More Currencies to be added
            if curr == 'USD':
                USDRoyality += float(row[13])
            if curr == 'BRL':
                BRLRoyality += float(row[13])
            if curr == 'CAD':
                CADRoyality += float(row[13])
            if curr == 'EUR':
                EURRoyality += float(row[13])
            if curr == 'GBP':
                GBPRoyality += float(row[13])
            if curr == 'INR':
                INRRoyality += float(row[13])
            if curr == 'MXN':
                MXNRoyality += float(row[13])
            if curr == 'AUD':
                AUDRoyality += float(row[13])


            #Book Numbers

            if bookName == dareTitle:
                dareNumbers += int(row[9])
            if bookName == wegTitle:
                wegNumbers += int(row[9])
            if bookName == panicoTitle:
                panicoNumbers += int(row[9])

        print(' ')
        print(dare + ' sold ' + str(dareNumbers) + ' books')
        print(weg + ' sold ' + str(wegNumbers) + ' books')
        print(panico  + ' sold ' + str(panicoNumbers) + ' books')
        print(' ')
        print('There was ' + str(round(USDRoyality, 2)) + ' in USD') # Change USD to row title
        print('There was ' + str(round(GBPRoyality, 2)) + ' in GBP') # Change USD to row title
        print('There was ' + str(round(EURRoyality, 2)) + ' in EUR') # Change USD to row title
        print('There was ' + str(round(CADRoyality, 2)) + ' in CAD') # Change USD to row title
        print('There was ' + str(round(AUDRoyality, 2)) + ' in AUD') # Change USD to row title
        print('There was ' + str(round(INRRoyality, 2)) + ' in INR') # Change USD to row title
        print('There was ' + str(round(MXNRoyality, 2)) + ' in MXN') # Change USD to row title
        print('There was ' + str(round(BRLRoyality, 2)) + ' in BRL') # Change USD to row title


readFiles()
