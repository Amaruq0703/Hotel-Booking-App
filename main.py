import pandas as pd 

df = pd.read_csv('hotels.csv', dtype ={'id':str})
carddf = pd.read_csv('cards.csv', dtype = str).to_dict(orient='records')
class User:
    def getuser(self):
        pass

class Hotel:
    def __init__(self, hotelid):
        self.hotelid = hotelid
        self.name = df.loc[df['id']== hotelid, 'name'].squeeze()
    def seehotel(self):
        pass
    def bookhotel(self):
        #Booking hotel by changing availibility to no

        df.loc[df['id'] == self.hotelid, 'available'] = 'no'
        df.to_csv('hotels.csv', index =False)
        
    def availibility(self):
        # Checking if hotel is availible

        availibility =  df.loc[df['id'] == self.hotelid, 'available'].squeeze()
        if availibility == 'yes':
            return True
        else:
            return False

class Pay:
    def __init__(self, number):
        self.number = number
    def payhotel(self, expir, name, cvc):
        cardinfo = {'number': self.number, 'expiration': expir, 
                    'cvc': cvc, 'holder': name}
        if cardinfo in carddf:
            return True
        else:
            return False

class Confi:
    def __init__(self, customername, hotelobj):
        self.customername = customername
        self.hotel = hotelobj
    def genticket(self):    
        content = f"""
        Thank you for your reservation!
        Information:
        Name: {self.customername}
        Hotel: {self.hotel.name}
        """
        return content

class Spa(Confi):

    def spaans(self):
        self.spaans = input('Do you want a spa package? ')

    def genticket(self):
        if self.spaans == 'yes':
            content = f"""
            Thank you for your spa booking!
            Spa info:
            Name: {self.customername}
            Hotel: {self.hotel.name}
            """
        else:
            content = 'Ok'
        return content

print(df)
hotelid = input('Enter hotel ID: ')
hotel = Hotel(hotelid)

if hotel.availibility():
    cardnum = input('Enter card no. ')
    expiry = input('Enter card expiry: ')
    cvc = input('Enter CVC: ')
    name = input('Enter your name: ')
    creditcard = Pay(cardnum)
    if creditcard.payhotel(expiry, name.upper(), cvc):
        hotel.bookhotel()
        conftick = Confi(customername =name.title(), hotelobj = hotel)
        print(conftick.genticket())
        spagen = Spa(customername =name.title(), hotelobj = hotel)
        spagen.spaans()
        print(spagen.genticket())
    else:
        print('Problem with payment info')

else: 
    print('Hotel is not available')





