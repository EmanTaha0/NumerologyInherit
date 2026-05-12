class Numerology:
    def __init__(self, sNameEMT, sDOBEMT):
        self.sNameEMT = sNameEMT.upper()
        self.sDOBEMT = sDOBEMT

        # Pre-calc values 
        self.__iPersonalityNumber = self.__calcPersonality()
        self.__iSoulNumber = self.__calcSoul()
        self.__iLifePathNumber = self.__calcLifePath()
        self.__iAttitudeNumber = self.__calcAttitude()
        self.__iBirthdayNumber = self.__calcBirthDay()
        self.__iPowerName = self.__reduceNumber(self.__iPersonalityNumber + self.__iSoulNumber)

    
    # Utility Functions
    

    def __convertCharToInteger(self, sCharEMT):
        return ((ord(sCharEMT.upper()) - 65) % 9 + 1) if sCharEMT.isalpha() else 0

    def __reduceNumber(self, iNumberEMT):
        while iNumberEMT > 9:
            iNumberEMT = sum(int(d) for d in str(iNumberEMT))
        return iNumberEMT

    
    # Calculation Functions 

    def __calcPersonality(self):
        iTotalEMT = sum(self.__convertCharToInteger(ch)
                        for ch in self.sNameEMT
                        if ch.isalpha() and ch not in "AEIOU")
        return self.__reduceNumber(iTotalEMT)

    def __calcSoul(self):
        iTotalEMT = sum(self.__convertCharToInteger(ch)
                        for ch in self.sNameEMT
                        if ch in "AEIOU")
        return self.__reduceNumber(iTotalEMT)

    def __calcLifePath(self):
        iTotalEMT = sum(int(ch) for ch in self.sDOBEMT if ch.isdigit())
        return self.__reduceNumber(iTotalEMT)

    def __calcAttitude(self):
        sPartsEMT = self.sDOBEMT.replace("/", "-").split("-")
        iMonthEMT = int(sPartsEMT[0])
        iDayEMT = int(sPartsEMT[1])
        return self.__reduceNumber(iMonthEMT + iDayEMT)

    def __calcBirthDay(self):
        sPartsEMT = self.sDOBEMT.replace("/", "-").split("-")
        return self.__reduceNumber(int(sPartsEMT[1]))

 
    # GETTERS 
    

    @property
    def getPersonality(self):
        return self.__iPersonalityNumber

    @property
    def getSoulNumber(self):
        return self.__iSoulNumber

    @property
    def getLifePath(self):
        return self.__iLifePathNumber

    @property
    def getAttitude(self):
        return self.__iAttitudeNumber

    @property
    def getBirthDay(self):
        return self.__iBirthdayNumber

    @property
    def getPowerName(self):
        return self.__iPowerName
