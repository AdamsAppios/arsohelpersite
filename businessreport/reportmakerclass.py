# problems
from .models import Tmbreport, Labreport, Kalimpreport
from datetime import date, datetime, timedelta


class Refilling():
    dealPrice = 10
    pickPrice = 15
    rndPrice = 150

    def __init__(self, post_variables , group):
        self.post_variables = post_variables
        self.group = group
        if post_variables['dateReport'] == "":
            today = date.today()
            self.dateReport = today.strftime("%Y-%m-%d")
        else:
            self.dateReport = post_variables['dateReport']
        self.yester_date = self.getYesterday(self.dateReport)

    def getYesterday(self, date_string):
        now = date(*map(int, date_string.split('-')))
        yesterday = datetime.strftime(now - timedelta(1), '%Y-%m-%d')
        return yesterday

    def htmlCashTaken(self):
        post_variable = self.post_variables
        if post_variable["cashTkn"] == "0":
            htmlCashTkn = ""
        else:
            htmlCashTkn = " - CT {0}".format(post_variable["cashTkn"])
        return htmlCashTkn

    def htmlTA(self):
        post_variable = self.post_variables
        htmlTA = int(post_variable['ctoCalc']) + \
            int(post_variable["totalExpText"]) + int(post_variable["cashTkn"])
        return htmlTA

    def htmlShortCTO(self):
        post_variable = self.post_variables
        isShortCTO = int(post_variable['ctoRep']) - \
            int(post_variable['ctoCalc'])
        if (isShortCTO < 0):
            htmlShortCTO = "Short {0}".format(isShortCTO)
        elif isShortCTO > 0:
            htmlShortCTO = "Over {0}".format(isShortCTO)
        else:
            htmlShortCTO = ""
        return htmlShortCTO

    def htmlShortSupplies(self, strBeg):
        post_variable = self.post_variables

        if strBeg == "Round":
            reportConsumed = int(post_variable["rndText"])
            begn = int(post_variable["rndBeg"])
            endng = int(post_variable["rndEnd"])
            inSupply = int(post_variable["rndIn"])
        elif strBeg == "CapSeal":
            reportConsumed = int(post_variable['dealText'])+int(
                post_variable["pickText"])+int(post_variable["rndText"])
            begn = int(post_variable["cpSealBeg"])
            endng = int(post_variable["cpSeal"])
            inSupply = int(post_variable["cpSealIn"])
        elif strBeg == "SquareSeal":
            reportConsumed = int(post_variable['squareText'])
            begn = int(post_variable["sqSealBeg"])
            endng = int(post_variable["sqSeal"])
            inSupply = int(post_variable["sqSealIn"])
        else:
            return ""
        differenceSupply = begn - endng
        isShort = reportConsumed - differenceSupply
        htmlShortSupply = "{0} Beg {1}".format(strBeg, begn)
        htmlShortSupply += " - End{0} =".format(endng)
        if isShort < 0:
            htmlShortSupply += "{0} Short {1}".format(
                differenceSupply, isShort)
        elif isShort > 0:
            htmlShortSupply += "{0} Over {1}".format(
                differenceSupply, isShort)
        else:
            htmlShortSupply += "{0}".format(differenceSupply)
        if inSupply > 0:
            htmlShortSupply += " ( In{0} )".format(inSupply)
        return htmlShortSupply

    def htmlShortbadgerMeter(self, modelClass):
        post_variable = self.post_variables
        htmlShortbdgMeter = "Badger Meter {0} ".format(
            int(post_variable["bdgMeter"]))
        try:
            yesterRow = modelClass.objects.get(
                dateReport__exact=self.yester_date)
            if modelClass.__name__ == "Tmbreport":
                gallonsConsumed = int(
                    post_variable['dealText'])+int(post_variable["pickText"])+int(post_variable["rndText"])
            elif modelClass.__name__ == "Labreport":
                gallonsConsumed = int(
                    post_variable['dealText'])+int(post_variable["pickText"])+int(post_variable["rndText"]) + int(post_variable["goodlyText"]) + int(post_variable["squareText"])
            elif modelClass.__name__ == "Kalimpreport":
                gallonsConsumed = float(
                    post_variable['dealText'])+float(post_variable["pickText"])+float(post_variable["rndText"]) + float(post_variable["smallText"])/3 + float(post_variable["squareText"]) + float(post_variable["bakeryGal"])

            isShortBadger = gallonsConsumed - \
                (int(post_variable["bdgMeter"]) - yesterRow.badgermeter)*2
            if (isShortBadger < 0):
                htmlShortbdgMeter += "Short {0}".format(isShortBadger)
            elif isShortBadger > 0 and self.group == "admin": # does not have permission to view adminpy
                htmlShortbdgMeter += "Over {0}".format(isShortBadger)
            else:
                htmlShortbdgMeter += ""
        except (KeyError, modelClass.DoesNotExist):
            htmlShortbdgMeter += ""
        return htmlShortbdgMeter

    def insertSupplyDB(self):
        supplyArr = []
        if int(self.post_variables['rndIn']) > 0:
            supplyArr.append("RndIn={0}".format(self.post_variables['rndIn']))
        if int(self.post_variables['cpSealIn']) > 0:
            supplyArr.append("cpSealIn={0}".format(
                self.post_variables['cpSealIn']))
        if 'sqSealIn' in self.post_variables and int(self.post_variables['sqSealIn']) > 0:
            supplyArr.append("sqSealIn={0}".format(
                self.post_variables['sqSealIn']))
        supplyStr = ",".join(supplyArr)
        # for converting back datas in pandas use supplyArr= supplyStr.split(",") and then supplyArr[i].split("=")
        return supplyStr


class TalambanRef(Refilling):
    dealPrice = 8
    pickPrice = 12

    def __init__(self, post_variables, group):
        super().__init__(post_variables, group)

    def modifyDB(self):
        try:
            tmbRow = Tmbreport.objects.get(dateReport__exact=self.dateReport)
        except (KeyError, Tmbreport.DoesNotExist):
            print("creating new object")
            tmbNew = Tmbreport(
                dateReport=self.dateReport,
                dealer=self.post_variables['dealText'],
                pickup=self.post_variables['pickText'],
                rndgal=self.post_variables['rndText'],
                supplyIns=self.insertSupplyDB(),
                rndEnd=int(self.post_variables['rndEnd']) +
                int(self.post_variables['rndIn']),
                badgermeter=self.post_variables['bdgMeter'],
                capsealEnd=int(
                    self.post_variables['cpSeal']) + int(self.post_variables['cpSealIn']),
                expensesText=self.post_variables['expensesText'],
                cashturnoverCalc=self.post_variables['ctoCalc'],
                cashturnoverRep=self.post_variables['ctoRep'],
                cashtaken=self.post_variables['cashTkn'],
                dutyText=self.post_variables["duties"]
            )
            tmbNew.save()
        else:
            print("updating date")
            tmbRow.dateReport = self.dateReport
            tmbRow.dealer = self.post_variables['dealText']
            tmbRow.pickup = self.post_variables['pickText']
            tmbRow.rndgal = self.post_variables['rndText']
            tmbRow.supplyIns = self.insertSupplyDB()
            tmbRow.rndEnd = int(
                self.post_variables['rndEnd']) + int(self.post_variables['rndIn'])
            tmbRow.badgermeter = self.post_variables['bdgMeter']
            tmbRow.capsealEnd = int(
                self.post_variables['cpSeal']) + int(self.post_variables['cpSealIn'])
            tmbRow.cashturnoverCalc = self.post_variables['ctoCalc']
            tmbRow.cashturnoverRep = self.post_variables['ctoRep']
            tmbRow.cashtaken = self.post_variables['cashTkn']
            tmbRow.expensesText = self.post_variables['expensesText']
            tmbRow.dutyText = self.post_variables["duties"]
            tmbRow.save()

    def postToContext(self):
        context = {}
        for key, value in self.post_variables.items():
            context[key] = value
        # add new dictionary keys
        context["dayOfWeek"] = datetime.strptime(
            self.dateReport, '%Y-%m-%d').strftime('%A')
        if context["totalExpText"] == "":
            context["totalExpText"] = "0"
        context["htmlShortSl"] = self.htmlShortSupplies("CapSeal")
        context["htmlShortRnd"] = self.htmlShortSupplies("Round")
        context["htmlCashTkn"] = self.htmlCashTaken()
        context["htmlShortCTO"] = self.htmlShortCTO()
        context["htmlShortbdgMeter"] = self.htmlShortbadgerMeter(Tmbreport)
        context["htmlDisplaySales"] = self.htmlDisplaySales()
        context["TA"] = self.htmlTA()
        return context

    def htmlDisplaySales(self):
        post_variable = self.post_variables
        arr = []
        arr.append(int(post_variable["dealText"]) * self.dealPrice)
        arr.append(int(post_variable["pickText"]) * self.pickPrice)
        if post_variable["rndText"] != "0":
            arr.append(int(post_variable["rndText"]) * self.rndPrice)
        arr = [str(i) for i in arr]
        arr = "/".join(arr)
        return arr

    def ajax_yesterday(self):
        try:
            tmbRow = Tmbreport.objects.get(dateReport__exact=self.yester_date)
        except (KeyError, Tmbreport.DoesNotExist):
            return {}
        else:
            data = {
                "dateReport": tmbRow.dateReport,
                "rndEnd": tmbRow.rndEnd,
                "badgermeter": tmbRow.badgermeter,
                "capSealEnd": tmbRow.capsealEnd
            }
            return data


class LabangonRef(Refilling):
    smallPrice = 8
    squarePrice = 15

    def __init__(self, post_variables, group):
        super().__init__(post_variables, group)

    def modifyDB(self):
        try:
            labRow = Labreport.objects.get(dateReport__exact=self.dateReport)
        except (KeyError, Labreport.DoesNotExist):
            print("creating new object")
            labNew = Labreport(
                dateReport=self.dateReport,
                dealer=self.post_variables['dealText'],
                pickup=self.post_variables['pickText'],
                less=self.post_variables['less'],
                rndgal=self.post_variables['rndText'],
                smallText=self.post_variables['smallText'],
                goodly=self.post_variables['goodlyText'],
                square=self.post_variables['squareText'],
                supplyIns=self.insertSupplyDB(),
                rndEnd=int(self.post_variables['rndEnd']) +
                int(self.post_variables['rndIn']),
                badgermeter=self.post_variables['bdgMeter'],
                capsealEnd=int(
                    self.post_variables['cpSeal']) + int(self.post_variables['cpSealIn']),
                squareSlEnd=int(
                    self.post_variables['sqSeal']) + int(self.post_variables['sqSealIn']),
                expensesText=self.post_variables['expensesText'],
                cashturnoverCalc=self.post_variables['ctoCalc'],
                cashturnoverRep=self.post_variables['ctoRep'],
                cashtaken=self.post_variables['cashTkn'],
                dutyText=self.post_variables["duties"]
            )
            labNew.save()
        else:
            print("updating date")
            labRow.dateReport = self.dateReport
            labRow.dealer = self.post_variables['dealText']
            labRow.less = self.post_variables['less']
            labRow.pickup = self.post_variables['pickText']
            labRow.rndgal = self.post_variables['rndText']
            labRow.smallText = int(self.post_variables['smallText'])
            labRow.goodly = self.post_variables['goodlyText']
            labRow.square = self.post_variables['squareText']
            labRow.supplyIns = self.insertSupplyDB()
            labRow.rndEnd = int(
                self.post_variables['rndEnd']) + int(self.post_variables['rndIn'])
            labRow.badgermeter = self.post_variables['bdgMeter']
            labRow.capsealEnd = int(
                self.post_variables['cpSeal']) + int(self.post_variables['cpSealIn'])
            labRow.squareSlEnd = int(
                self.post_variables['sqSeal']) + int(self.post_variables['sqSealIn'])
            labRow.cashturnoverCalc = self.post_variables['ctoCalc']
            labRow.cashturnoverRep = self.post_variables['ctoRep']
            labRow.cashtaken = self.post_variables['cashTkn']
            labRow.expensesText = self.post_variables['expensesText']
            labRow.dutyText = self.post_variables["duties"]
            labRow.save()

    def postToContext(self):
        context = {}
        for key, value in self.post_variables.items():
            context[key] = value
        # add new dictionary keys
        context["dayOfWeek"] = datetime.strptime(
            self.dateReport, '%Y-%m-%d').strftime('%A')
        if context["totalExpText"] == "":
            context["totalExpText"] = "0"
        context["dealLess"] = int(
            self.post_variables['dealText']) - int(self.post_variables['less'])
        context["htmlShortSl"] = self.htmlShortSupplies("CapSeal")
        context["htmlShortRnd"] = self.htmlShortSupplies("Round")
        context["htmlShortSq"] = self.htmlShortSupplies("SquareSeal")
        context["htmlCashTkn"] = self.htmlCashTaken()
        context["htmlShortCTO"] = self.htmlShortCTO()
        context["htmlDisplaySales"] = self.htmlDisplaySales()
        context["htmlShortbdgMeter"] = self.htmlShortbadgerMeter(Labreport)
        context["htmlSquare"] = self.htmlSquare()
        context["htmlSmall"] = self.htmlSmall()
        context["htmlGoodly"] = self.htmlGoodly()
        context["TA"] = self.htmlTA()
        return context

    def htmlGoodly(self):
        post_variable = self.post_variables
        if post_variable["goodlyText"] == "0" or post_variable["goodlyText"] == "":
            return ""
        else:
            return " Goodly{0}".format(post_variable["goodlyText"])

    def htmlSquare(self):
        post_variable = self.post_variables
        if post_variable["squareText"] == "0" or post_variable["squareText"] == "":
            return ""
        else:
            return " ☐{0}".format(post_variable["squareText"])

    def htmlSmall(self):
        post_variable = self.post_variables
        if post_variable["smallText"] == "0" or post_variable["smallText"] == "":
            return ""
        else:
            return " Sg{0}".format(post_variable["smallText"])

    def htmlDisplaySales(self):
        post_variable = self.post_variables
        arr = []
        arr.append((int(post_variable["dealText"]) -
                    int(post_variable["less"])) * self.dealPrice)
        arr.append(int(post_variable["pickText"]) * self.pickPrice)
        if post_variable["smallText"] != "0":
            arr.append(int(post_variable["smallText"]) * self.smallPrice)
        if post_variable["squareText"] != "0":
            arr.append(int(post_variable["squareText"]) * self.squarePrice)
        if post_variable["rndText"] != "0":
            arr.append(int(post_variable["rndText"]) * self.rndPrice)
        arr = [str(i) for i in arr]
        arr = "/".join(arr)
        return arr

    def ajax_yesterday(self):
        try:
            labRow = Labreport.objects.get(dateReport__exact=self.yester_date)
        except (KeyError, Labreport.DoesNotExist):
            return {}
        else:
            data = {
                "dateReport": labRow.dateReport,
                "rndEnd": labRow.rndEnd,
                "badgermeter": labRow.badgermeter,
                "capSealEnd": labRow.capsealEnd,
                "sqSealEnd": labRow.squareSlEnd
            }
            return data


class KalimpyoRef(Refilling):
    smallPrice = 8
    squarePrice = 15
    bakeryPrice = 15
    smallSqPrice = 10

    def __init__(self, post_variables, group):
        super().__init__(post_variables, group)

    def modifyDB(self):
        try:
            kalRow = Kalimpreport.objects.get(
                dateReport__exact=self.dateReport)
        except (KeyError, Kalimpreport.DoesNotExist):
            print("creating new object")
            kalNew = Kalimpreport(
                dateReport=self.dateReport,
                dealer=self.post_variables['dealText'],
                pickup=self.post_variables['pickText'],
                less=self.post_variables['less'],
                rndgal=self.post_variables['rndText'],
                smallText=self.post_variables['smallText'],
                smallSquare=self.post_variables['smallSquare'],
                bakeryGal=self.post_variables["bakeryGal"],
                square=self.post_variables['squareText'],
                supplyIns=self.insertSupplyDB(),
                rndEnd=int(
                    self.post_variables['rndEnd']) + int(self.post_variables['rndIn']),
                badgermeter=self.post_variables['bdgMeter'],
                capsealEnd=int(
                    self.post_variables['cpSeal']) + int(self.post_variables['cpSealIn']),
                squareSlEnd=int(
                    self.post_variables['sqSeal']) + int(self.post_variables['sqSealIn']),
                expensesText=self.post_variables['expensesText'],
                cashturnoverCalc=self.post_variables['ctoCalc'],
                cashturnoverRep=self.post_variables['ctoRep'],
                cashtaken=self.post_variables['cashTkn'],
                dutyText=self.post_variables["duties"]
            )
            kalNew.save()
        else:
            print("updating date")
            kalRow.dateReport = self.dateReport
            kalRow.dealer = self.post_variables['dealText']
            kalRow.less = self.post_variables['less']
            kalRow.pickup = self.post_variables['pickText']
            kalRow.rndgal = self.post_variables['rndText']
            kalRow.smallText = int(self.post_variables['smallText'])
            kalRow.square = self.post_variables['squareText']
            kalRow.smallSquare = self.post_variables['smallSquare']
            kalRow.bakeryGal = self.post_variables["bakeryGal"]
            kalRow.supplyIns = self.insertSupplyDB()
            kalRow.rndEnd = int(
                self.post_variables['rndEnd']) + int(self.post_variables['rndIn'])
            kalRow.badgermeter = self.post_variables['bdgMeter']
            kalRow.capsealEnd = int(
                self.post_variables['cpSeal']) + int(self.post_variables['cpSealIn'])
            kalRow.squareSlEnd = int(
                self.post_variables['sqSeal']) + int(self.post_variables['sqSealIn'])
            kalRow.cashturnoverCalc = self.post_variables['ctoCalc']
            kalRow.cashturnoverRep = self.post_variables['ctoRep']
            kalRow.cashtaken = self.post_variables['cashTkn']
            kalRow.expensesText = self.post_variables['expensesText']
            kalRow.dutyText = self.post_variables["duties"]
            kalRow.save()

    def ajax_yesterday(self):
        try:
            kalRow = Kalimpreport.objects.get(
                dateReport__exact=self.yester_date)
        except (KeyError, Kalimpreport.DoesNotExist):
            return {}
        else:
            data = {
                "dateReport": kalRow.dateReport,
                "rndEnd": kalRow.rndEnd,
                "badgermeter": kalRow.badgermeter,
                "capSealEnd": kalRow.capsealEnd,
                "sqSealEnd": kalRow.squareSlEnd
            }
            return data

    def htmlDisplaySales(self):
        post_variable = self.post_variables
        arr = []
        arr.append((int(post_variable["dealText"]) -
                    int(post_variable["less"])) * self.dealPrice)
        arr.append(int(post_variable["pickText"]) * self.pickPrice)
        if post_variable["smallText"] != "0":
            arr.append(int(post_variable["smallText"]) * self.smallPrice)
        if post_variable["squareText"] != "0":
            arr.append(int(post_variable["squareText"]) * self.squarePrice)
        if post_variable["smallSquare"] != "0":
            arr.append(int(post_variable["smallSquare"]) * self.smallSqPrice)
        if post_variable["bakeryGal"] != "0":
            arr.append(int(post_variable["bakeryGal"]) * self.bakeryPrice)
        if post_variable["rndText"] != "0":
            arr.append(int(post_variable["rndText"]) * self.rndPrice)
        arr = [str(i) for i in arr]
        arr = "/".join(arr)
        return arr

    def htmlSquare(self):
        post_variable = self.post_variables
        if post_variable["squareText"] == "0" or post_variable["squareText"] == "":
            return ""
        else:
            return " ☐{0}".format(post_variable["squareText"])

    def htmlSmall(self):
        post_variable = self.post_variables
        if post_variable["smallText"] == "0" or post_variable["smallText"] == "":
            return ""
        else:
            return " Sg{0}".format(post_variable["smallText"])

    def htmlSmallSquare(self):
        post_variable = self.post_variables
        if post_variable["smallSquare"] == "0" or post_variable["smallSquare"] == "":
            return ""
        else:
            return " Small☐{0}".format(post_variable["smallSquare"])

    def htmlBakeryGal(self):
        post_variable = self.post_variables
        if post_variable["bakeryGal"] == "0" or post_variable["bakeryGal"] == "":
            return ""
        else:
            return " Bkry{0}".format(post_variable["bakeryGal"])

    def postToContext(self):
        context = {}
        for key, value in self.post_variables.items():
            context[key] = value
        # add new dictionary keys
        context["dayOfWeek"] = datetime.strptime(
            self.dateReport, '%Y-%m-%d').strftime('%A')
        if context["totalExpText"] == "":
            context["totalExpText"] = "0"
        context["dealLess"] = int(
            self.post_variables['dealText']) - int(self.post_variables['less'])
        context["htmlShortSl"] = self.htmlShortSupplies("CapSeal")
        context["htmlShortRnd"] = self.htmlShortSupplies("Round")
        context["htmlShortSq"] = self.htmlShortSupplies("SquareSeal")
        context["htmlCashTkn"] = self.htmlCashTaken()
        context["htmlShortCTO"] = self.htmlShortCTO()
        context["htmlDisplaySales"] = self.htmlDisplaySales()
        context["htmlShortbdgMeter"] = self.htmlShortbadgerMeter(Kalimpreport)
        context["htmlSquare"] = self.htmlSquare()
        context["htmlSmallSq"] = self.htmlSmallSquare()
        context["htmlSmall"] = self.htmlSmall()
        context["htmlBkry"] = self.htmlBakeryGal()
        context["TA"] = self.htmlTA()
        return context
