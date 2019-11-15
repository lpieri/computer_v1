# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_class.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cpieri <cpieri@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 20:18:19 by cpieri            #+#    #+#              #
#    Updated: 2019/11/15 12:33:20 by cpieri           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
import math
from utils import *

class Polynomial:

	def __init__(self, equation):
		self.__equation = equation
		self._a = 0
		self._b = 0
		self._c = 0
		self.parse_equation()
		self.solve_equation()

	def solve_equation(self):
		if self.max_power > 2:
			return print ("The polynomial degree is stricly greater than 2, I can't solve.")
		delta = (self._b * self._b) - (4 * self._a * self._c)
		print (delta)
		if delta > 0:
			print ("Discriminant is strictly positive, the two solutions are:")
			# self.__calc_2_sol(delta)
		elif delta == 0:
			print ("The solution is:")
			# self.__calc_1_sol(delta)
		else:
			return print ("Discriminant is strictly negative, there is no solution.")

	def parse_equation(self):
		neg = re.findall(r"X\^-", self.__equation)
		if neg:
			exit_error("The polynomial equation is not valid!")
		self.core_equation = self.__equation.split(" = ")[0]
		self.start_egal = self.__equation.split(" = ")[1]
		max_power, pows = self.__find_max_power()
		self.max_power = max_power
		self.__reduct_core(pows)
		print ("Polynomial degree: {p}".format(p=max_power))

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

	def __save_int_by_p(self, _value, _power_of,):
		if _power_of == 0:
			self._c = _value
		elif _power_of == 1:
			self._b = _value
		elif _power_of == 2:
			self._a = _value
		else:
			return

	def __reduct_power(self, _power_of):
		regex_power = r"((\+|\-)\s)?((\d.)?\d+)\s\*\sX\^{power}".format(power=_power_of)
		regex_int = r"((\+|\-)\s)?((\d.)?\d+)"
		core_power = re.search(regex_power, self.core_equation).group()
		core_power_int = re.sub(r"\s+", "", re.match(regex_int, core_power).group())
		core_is_float = re.search(r"(\.)", core_power_int)
		core_power_int = float(core_power_int) if core_is_float else int(core_power_int)
		self.__save_int_by_p(core_power_int, _power_of)
		egal_power = re.search(regex_power, self.start_egal)
		if egal_power:
			egal_power_int = re.sub(r"\s+", "", re.match(regex_int, egal_power.group()).group())
			egal_is_float = re.search(r"(\.)", egal_power_int)
			egal_power_int = float(egal_power_int) if egal_is_float else int(egal_power_int)
			reduct_int = core_power_int - egal_power_int
			return "{int} * X^{power}".format(int=reduct_int, power=_power_of)
		return core_power

	def	__reduct_core(self, powers):
		reduct_equation = ""
		for p in powers:
			core_power = self.__reduct_power(p)
			reduct_equation += " {power}".format(power=core_power)
		reduct_equation += " = 0"
		self.reduct_equation = reduct_equation
		print ("Reduced form:{eq}".format(eq=reduct_equation))