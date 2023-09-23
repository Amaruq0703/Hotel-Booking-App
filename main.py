import pandas as pd 

# Reading of data

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

    # Method to check card information

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

    # Method to generate confirmation ticket

    def genticket(self):    
        content = f"""\n
        Thank you for your reservation!\n
        Information:\n
        Name: {self.customername}\n
        Hotel: {self.hotel.name}\n
        """
        return content

class Spa(Confi):

    # Method to get spa request

    def spaans(self):
        self.spaans = input('Do you want a spa package? ')

    # Method to print spa confirmation ticket

    def genticket(self):
        if self.spaans == 'yes':
            content = f"""\n
            Thank you for your spa booking!\n
            Spa info:\n
            Name: {self.customername}\n
            Hotel: {self.hotel.name}\n
            """
        else:
            content = 'Ok'
        return content

print(df)
hotelid = input('Enter hotel ID: ')
hotel = Hotel(hotelid)

#  Checking availibility

if hotel.availibility():

    # Getting card info

    cardnum = input('Enter card no. ')
    expiry = input('Enter card expiry: ')
    cvc = input('Enter CVC: ')
    name = input('Enter your name: ')
    creditcard = Pay(cardnum)

    # Checking card info

    if creditcard.payhotel(expiry, name.upper(), cvc):
        hotel.bookhotel()

        # Booking confirmation ticket

        conftick = Confi(customername =name.title(), hotelobj = hotel)
        print(conftick.genticket())

        # Spa confirmation ticket

        spagen = Spa(customername =name.title(), hotelobj = hotel)
        spagen.spaans()
        print(spagen.genticket())
    else:
        print('Problem with payment info')

else: 
    print('Hotel is not available')





