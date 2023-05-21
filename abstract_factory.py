from abc import ABC, abstractmethod


class AbstractMovie(ABC):
    @abstractmethod
    def get_title(self):
        '''название'''

    @abstractmethod
    def get_duration(self):
        '''длительность'''


class ActionMovie(AbstractMovie):
    def get_title(self):
        return "Action Movie"

    def get_duration(self):
        return 120

class ComedyMovie(AbstractMovie):
    def get_title(self):
        return "Comedy Movie"

    def get_duration(self):
        return 90


class AbstractMovieFactory(ABC):
    @abstractmethod
    def create_movie(self):
        '''создание фильма'''


class ActionMovieFactory(AbstractMovieFactory):
    def create_movie(self):
        return ActionMovie()

      
class ComedyMovieFactory(AbstractMovieFactory):
    def create_movie(self):
        return ComedyMovie()


def client_code(factory):
    movie = factory.create_movie()
    print("Название:", movie.get_title())
    print("Длительность:", movie.get_duration())

    
if __name__ == '__main__':
    action_factory = ActionMovieFactory()
    comedy_factory = ComedyMovieFactory()
    
    client_code(action_factory)
    client_code(comedy_factory)
