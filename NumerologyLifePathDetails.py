from Numerology import Numerology

class NumerologyLifePathDetails(Numerology):

    def __init__(self, name: str, birthdate: str):
        super().__init__(name, birthdate)

        self.__lifePathDictionary = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and performing",
            4: "The Teacher/Truth Seeker: Honest and meant to mentor others",
            5: "The Adventurer: Loves travel, freedom and meeting people",
            6: "The Inner Child: Caring, nurturing and family-oriented",
            7: "The Naturalist: Loves nature, water and spirituality",
            8: "The Executive: Drawn to money, power and leadership",
            9: "The Humanitarian: Helps others and learns through experience"
        }

        
        self.__lifePathDescription = self.__lifePathDictionary[self.getLifePath]

    
    # Properties 

    @property
    def Name(self):
        return self.sNameEMT

    @property
    def Birthdate(self):
        return self.sDOBEMT

    @property
    def Attitude(self):
        return self.getAttitude

    @property
    def BirthDay(self):
        return self.getBirthDay

    @property
    def LifePath(self):
        return self.getLifePath

    @property
    def Personality(self):
        return self.getPersonality

    @property
    def PowerName(self):
        return self.getPowerName

    @property
    def Soul(self):
        return self.getSoulNumber

    @property
    def LifePathDescription(self):
        return self.__lifePathDescription
