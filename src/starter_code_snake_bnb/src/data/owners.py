class Owner:
    registered_data = None
    name = None
    email = None

    snake_ids = list()
    cage_ids = list()

    meta = {
        'db_alias': 'core',
        'collection': 'owners'
    }