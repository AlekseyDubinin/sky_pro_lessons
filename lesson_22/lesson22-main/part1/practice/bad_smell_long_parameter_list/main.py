class Unit:
    def __init__(self, field, x_coord, y_coord, is_fly, crawl, speed=1):

        self.speed = speed
        self.crawl = crawl
        self.is_fly = is_fly
        self.y_coord = y_coord
        self.field = field
        self.x_coord = x_coord

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y_coord + speed, x=self.x_coord, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y_coord - speed, x=self.x_coord, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y_coord, x=self.x_coord - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y_coord, x=self.x_coord + speed, unit=self)

    def _get_speed(self):
        if self.is_fly == 'fly':
            return self.speed * 1.2
        elif self.crawl == 'crawl':
            return self.speed * 0.5
        else:
            raise ValueError('Эк тебя раскорячило')
