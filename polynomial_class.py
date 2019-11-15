# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_class.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cpieri <cpieri@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 20:18:19 by cpieri            #+#    #+#              #
#    Updated: 2019/11/15 11:45:51 by cpieri           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
from utils import *

class Polynomial:

	def __init__(self, equation):
		self.__equation = equation
		self.parse_equation()

	def __find_max_power(self):
		powers = re.findall(r"(X\^\d)", self.core_equation)
		max_power = 0
		pows = []
		for power in powers:
			p = int(power.split('^')[1])
			pows.append(p)
			if p > max_power:
				max_power = p
		return max_power, pows

	def parse_equation(self):
		neg = re.findall(r"X\^-", self.__equation)
		if neg:
			exit_error("The polynomial equation is not valid!")
		self.core_equation = self.__equation.split(" = ")[0]
		self.start_egal = self.__equation.split(" = ")[1]
		max_power, pows = self.__find_max_power()
		# print (max_power, pows)
		self.reduct_core(pows)

	def __reduct_power(self, _power_of):
		regex_power = r"((\+|\-)\s)?((\d.)?\d+)\s\*\sX\^{power}".format(power=_power_of)
		regex_int = r"((\+|\-)\s)?((\d.)?\d+)"
		core_power = re.search(regex_power, self.core_equation).group()
		core_power_int = re.sub(r"\s+", "", re.match(regex_int, core_power).group())
		core_is_float = re.search(r"(\.)", core_power_int)
		core_power_int = float(core_power_int) if core_is_float else int(core_power_int)
		egal_power = re.search(regex_power, self.start_egal)
		if egal_power:
			egal_power_int = re.sub(r"\s+", "", re.match(regex_int, egal_power.group()).group())
			egal_is_float = re.search(r"(\.)", egal_power_int)
			egal_power_int = float(egal_power_int) if egal_is_float else int(egal_power_int)
			reduct_int = core_power_int - egal_power_int
			return "{int} * X^{power}".format(int=reduct_int, power=_power_of)
		return core_power

	def	reduct_core(self, powers):
		reduct_equation = ""
		for p in powers:
			core_power = self.__reduct_power(p)
			reduct_equation += " {power}".format(power=core_power)
		reduct_equation += " = 0"
		self.reduct_equation = reduct_equation
		print ("Reduced form:{eq}".format(eq=reduct_equation))
