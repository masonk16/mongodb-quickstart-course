class Cage:
    registered_date = None

    name = None
    price = None
    square_metres = None
    is_carpeted = None
    has_toys = None
    allow_dangerous_snakes = None

    bookings = list()

    meta = {
        'db_alias': 'core',
        'collection': 'cages'
    }
