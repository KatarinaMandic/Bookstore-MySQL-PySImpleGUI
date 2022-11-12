class Author:

    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.born = data['born']
        self.died = data['died']
        self.biography = data['biography']
        self.photo = data['photo']

    def __str__(self) -> str:
        author_data =  f'{self.first_name} {self.last_name} ('
        if self.born != None:
            author_data+= f'{self.born.year}'
        author_data += '-'
        if self.died != None:
            author_data+= f'{self.died.year}'
        author_data +=')'
        return author_data