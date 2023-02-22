from currencyConversion import ChangeCurrency

def dataEngineering(df1):
    
    obj1 = ChangeCurrency()
    obj1.changeToIndian(df1,'Botswana Pula(P)')

    obj1.changeToIndian(df1,'Brazilian Real(R$)')

    obj1.changeToIndian(df1,'Dollar($)')

    obj1.changeToIndian(df1,'Emirati Diram(AED)')

    obj1.changeToIndian(df1,'Indonesian Rupiah(IDR)')

    obj1.changeToIndian(df1,'NewZealand($)')

    obj1.changeToIndian(df1,'Pounds(專)')

    obj1.changeToIndian(df1,'Qatari Rial(QR)')

    obj1.changeToIndian(df1,'Rand(R)')

    obj1.changeToIndian(df1,'Sri Lankan Rupee(LKR)')

    obj1.changeToIndian(df1,'Turkish Lira(TL)')

    obj1.changeToIndian(df1, 'Indian Rupees(Rs.)')

    return df1

