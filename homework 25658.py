class Hotel:
    def __init__(self,name,place,room_mid,mid_room_price,rooms_lux,lux_room_price):
        self.name = name
        self.place = place
        self.room_mid = room_mid
        self.mid_room_price = mid_room_price
        self.rooms_lux = rooms_lux
        self.lux_room_price = lux_room_price
    def presentation(self):
        print(f'hello in { self.name }hotel ')
        print(f'in {self.place}')
        print(f' mid rooms {self.room_mid} and ther price{self.mid_room_price}')
        print(f'lux rooms {self.lux} and ther price {self.lux_room_price}')

    def booking(self,room_type):
        if self.room_mid == 'free':
            print('mid room is free want it ? yes no')
            if room_type == 'yes':
                self.room_mid[room] == 'busy'
                print(f'all right it will cost {self.mid_room_price}')
            else:
                print('ok')
        elif  self.rooms_lux == 'free':
            print('we have lux room want it')
            if room_type == 'yes':
                self.rooms_lux == 'busy'
                print(f'all right it will cost {self.lux_room_price}')
            else:
                print('then bay')
        elif not self.rooms_lux == 'free' or self.room_mid =='free':
            print('all rooms are busy sorry')

hotel1 = Hotel(
    name="Lerane",
    place="Geghard",
    rooms_mid={"room1": "free", "room2": "free"},
    mid_room_price=15000,
    rooms_lux={"room1": "free", "room2": "busy"},
    lux_room_price=25000
)
hotel1.presentation()
hotel1.booking("mid")
