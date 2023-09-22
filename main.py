import pandas as pd 

df = pd.read_csv('hotels.csv', dtype ={'id':str})

class User:
    def getuser(self):
        pass

class Hotel:
    def __init__(self, hotelid):
        self.hotelid = hotelid
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
    def payhotel(self):
        pass

class Confi:
    def __init__(self, customername, hotelobj):
        pass
    def genticket(self):    
        pass

hotelid = input('Enter hotel ID:')
hotel = Hotel(hotelid)

if hotel.availibility():
    hotel.bookhotel()
    name = input('Enter your name: ')
    conftick = Confi(name, hotel)
    print(conftick.genticket())

else: 
    print('Hotel is not available')





