
# Interface segregation principle:
# 1. Separate the interface from according to related logic

from zope.interface import implementer, Interface
from abc import ABC, abstractclassmethod

class ICompany(implementer(Interface)):
    @abstractclassmethod
    def importing(self):
        pass

    @abstractclassmethod
    def exporting(self):
        pass

    @abstractclassmethod
    def selling(self):
        pass

    @abstractclassmethod
    def buying(self):
        pass

    @abstractclassmethod
    def managing(self):
        pass

    @abstractclassmethod
    def accounting(self):
        pass

    @abstractclassmethod
    def finance(self):
        pass

    @abstractclassmethod
    def human_resources(self):
        pass

    @abstractclassmethod
    def production(self):
        pass

    @abstractclassmethod
    def sales(self):
        pass

    @abstractclassmethod
    def service(self):
        pass


    @abstractclassmethod
    def manage_staff(self):
        pass


class ICompany_Ex_Im(implementer(ICompany)):
    @abstractclassmethod
    def importing(self):
        pass

    @abstractclassmethod
    def exporting(self):
        pass

class ICompany_Sell_Buy(implementer(ICompany)):
    @abstractclassmethod
    def selling(self):
        pass

    @abstractclassmethod
    def buying(self):
        pass


class ICompany_Selling(implementer(ICompany_Sell_Buy)):
    @abstractclassmethod
    def selling(self):
        pass


class ICompany_Buying(implementer(ICompany_Sell_Buy)):
    @abstractclassmethod
    def buying(self):
        pass


class ICompany_Manage(implementer(ICompany)):
    @abstractclassmethod
    def managing(self):
        pass


class ICompany_Account(implementer(ICompany)):
    @abstractclassmethod
    def accounting(self):
        pass


class ICompany_Finance(implementer(ICompany)):
    @abstractclassmethod
    def finance(self):
        pass


class ICompany_HR(implementer(ICompany)):
    @abstractclassmethod
    def human_resources(self):
        pass


class ICompany_Prod(implementer(ICompany)):
    @abstractclassmethod
    def production(self):
        pass


class ICompany_Sales(implementer(ICompany)):
    @abstractclassmethod
    def sales(self):
        pass


class ICompany_Service(implementer(ICompany)):
    @abstractclassmethod
    def service(self):
        pass


class ICompany_Manage_Staff(implementer(ICompany)):
    @abstractclassmethod
    def manage_staff(self):
        pass
