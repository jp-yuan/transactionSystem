class Transaction:
    def __init__(self,student, amount, branch, service, paymentDate, payInFull = True) -> None:
        self.amount = amount
        self.branch = branch #cup, sm, lc, irvine
        self.service = service #cc program, gpa booster, group class etc.
        self.paymentDate = paymentDate
        self.payInFull = payInFull
        self.student = student

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def branch(self):
        return self._branch

    @branch.setter
    def branch(self, value):
        self._branch = value

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, value):
        self._service = value

    @property
    def paymentDate(self):
        return self._paymentDate

    @paymentDate.setter
    def paymentDate(self, value):
        self._paymentDate = value

    @property
    def payInFull(self):
        return self._payInFull

    @payInFull.setter
    def payInFull(self, value):
        self._payInFull = value

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, value):
        self._student = value