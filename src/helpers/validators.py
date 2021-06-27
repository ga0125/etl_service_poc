# ----------------------------------------------------------------------
# File: src/helpers/validators.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 24 jun 2021
# Brief: Validators methods for ETL services.
# ----------------------------------------------------------------------
import re


class CPFValidator:

    def __init__(self, cpf):
        self.cpf = cpf

    def validate(self):
        if not self.cpf:
            return False

        cpf_checker = self._calculate_digits(self.cpf[:9])
        cpf_checker = self._calculate_digits(cpf_checker)

        if cpf_checker == self.cpf:
            return True
        return False

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self._filter_nan(cpf)

    @staticmethod
    def _filter_nan(cpf):
        return re.sub('[^0-9]', '', cpf)

    @staticmethod
    def _calculate_digits(cpf_slice):
        if not cpf_slice:
            return False

        check_sequency = cpf_slice[0] * len(cpf_slice)
        if check_sequency == cpf_slice:
            return False

        sum: int = 0
        for key, multiplier in enumerate(range(len(cpf_slice)+1, 1, -1)):
            sum += int(cpf_slice[key]) * multiplier

        rest = 11 - (sum % 11)
        rest = rest if rest <= 9 else 0

        return cpf_slice + str(rest)
