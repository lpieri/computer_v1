# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_class.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cpieri <cpieri@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 20:18:19 by cpieri            #+#    #+#              #
#    Updated: 2019/12/02 10:22:57 by cpieri           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
from utils import *
from color import Color

class Polynomial:

	def __init__(self, equation):
		self.color = Color()
		self.__equation = equation
		self._a = None
		self._b = None
		self._c = None
		self.parse_equation()
		self.solve_equation()

	def solve_equation(self):
		if self.max_power > 2:
			return print (f"{self.color.red}The polynomial degree is stricly greater than 2, I can't solve.{self.color.none}")
		elif self.max_power == 2:
			delta = (self._b * self._b) - (4 * self._a * self._c)
			if delta > 0:
				self.__solve_2_solution(delta)
			elif delta == 0:
				self.__solve_1_solution(delta)
			else:
				self.__solve_no_real_solution(delta)
		elif self.max_power == 1:
			print (f"{self.color.green}The solution is:{self.color.none}")
			sol = -self._c / self._b
			print (f"{self.color.yellow}{sol}{self.color.none}")
		else:
			if self._c == 0:
				print (f"{self.color.green}The solution of the equation are all the real numbers !{self.color.none}")
			else:
				print (f"{self.color.red}There is no solution to the equation !{self.color.none}")

	def parse_equation(self):
		neg = re.findall(r"[X|x]\^-", self.__equation)
		if neg:
			exit_error(f"{self.color.red}The polynomial equation is not valid!{self.color.none}")
		self.core_equation = re.split("(\s)?=(\s)?", self.__equation)[0]
		self.start_egal = re.split("(\s)?=(\s)?", self.__equation)[3]
		pows = self.__parse_select_pows()
		self.__reduct_equation(pows)
		self.__parse_get_degree()

	def __parse_get_degree(self):
		powers = re.findall(r"(\d(\s)?\*(\s)?([X|x]\^([\+|\-])?\d))", self.reduct_equation)
		max_power = 0
		for power in powers:
			power = re.split(r"((\s+)?\*(\s+)?)", power[0])
			value = power[0]
			if int(value):
				power = power[4]
				p = int(power.split('^')[1])
				if (p > max_power):
					max_power = p
			else:
				continue
		self.max_power = max_power
		print (f"{self.color.cyan}Polynomial degree: {self.color.blue}{max_power}{self.color.none}")

	def __parse_select_pows(self):
		powers = re.findall(r"([X|x]\^([\+|\-])?\d)", self.core_equation)
		pows = []
		for power in powers:
			p = re.split(r"(\^)", power[0])
			p = int(p[2])
			pows.append(p)
		return pows

	def __save_int_by_p(self, _value, _power_of,):
		if _power_of == 0:
			self._c = _value
		elif _power_of == 1:
			self._b = _value
		elif _power_of == 2:
			self._a = _value
		else:
			return

	def __reduct_power(self, _power_of, _first):
		space = '' if _first == 0 else ' '
		signe = '' if _first == 0 else '+ '
		regex_power = r"((\s+)?(\+|\-)(\s+)?)?((\d+\.)?\d+)((\s+)?\*(\s+)?)[X|x]\^{power}".format(power=_power_of)
		regex_int = r"((\s+)?(\+|\-)(\s+)?)?((\d+\.)?\d+)"
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
			self.__save_int_by_p(reduct_int, _power_of)
			if reduct_int < 0:
				reduct_int = ft_abs(reduct_int)
				signe = '- '
			elif reduct_int == 0:
				return
			return f"{space}{signe}{reduct_int} * X^{_power_of}"
		if _first == 0:
			if core_power_int >= 0:
				core_power = re.sub(r"(\s)?\+(\s)?", "", core_power)
			else:
				core_power = re.sub(r"(\s)?", "", core_power, count=1)
		return core_power

	def	__reduct_equation(self, powers):
		reduct_equation = ""
		first = 0
		max_p = max(powers)
		for p in powers:
			core_power = self.__reduct_power(p, first)
			if core_power:
				reduct_equation += "{power}".format(power=core_power)
			elif not core_power and self._a == 0 and self._b == 0 and self._c == 0:
				reduct_equation += "0"
			first += 1
		reduct_equation += " = 0"
		self.reduct_equation = reduct_equation
		print (f"{self.color.magenta}Reduced form: {self.color.pink}{reduct_equation}{self.color.none}")

	def __solve_2_solution(self, delta):
		print (f"{self.color.green}Discriminant is strictly positive, the two solutions are:{self.color.none}")
		solution_1 = (-self._b - (delta ** 0.5)) / (2 * self._a)
		solution_2 = (-self._b + (delta ** 0.5)) / (2 * self._a)
		print (f"{self.color.yellow}{round(solution_1, 6)}{self.color.none}")
		print (f"{self.color.yellow}{round(solution_2, 6)}{self.color.none}")

	def __solve_1_solution(self, delta):
		print (f"{self.color.green}The solution is:{self.color.none}")
		solution = -self._b / (2 * self._a)
		print (solution)

	def __solve_no_real_solution(self, delta):
		print (f"{self.color.green}Discriminant is strictly negative, the two solutions are:{self.color.none}")
		solution_1 = (-self._b - (ft_abs(delta)) ** 0.5) / (2 * self._a)
		solution_2 = (-self._b + (ft_abs(delta)) ** 0.5) / (2 * self._a)
		print (f"{self.color.yellow}{round(solution_1, 6)}i{self.color.none}")
		print (f"{self.color.yellow}{round(solution_2, 6)}i{self.color.none}")