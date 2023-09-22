import pandas as pd 

df = pd.read_csv('hotels.csv', dtype ={'id':str})

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
    def payhotel(self):
        pass

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

print(df)
hotelid = input('Enter hotel ID: ')
hotel = Hotel(hotelid)

if hotel.availibility():
    hotel.bookhotel()
    name = input('Enter your name: ')
    conftick = Confi(customername =name, hotelobj = hotel)
    print(conftick.genticket())

else: 
    print('Hotel is not available')





