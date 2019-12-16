# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_class.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cpieri <cpieri@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 20:18:19 by cpieri            #+#    #+#              #
#    Updated: 2019/12/16 17:14:38 by cpieri           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
from utils import ft_sqrt, ft_abs, exit_error, get_int
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
		self._a = 0 if self._a == None else self._a
		self._b = 0 if self._b == None else self._b
		self._c = 0 if self._c == None else self._c
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
			sol = -float(self._c) / self._b
			print (f"{self.color.yellow}{sol}{self.color.none}")
		else:
			if not self._c:
				print (f"{self.color.green}The solution of the equation are all the real numbers !{self.color.none}")
			else:
				print (f"{self.color.red}There is no solution to the equation !{self.color.none}")

	def __solve_2_solution(self, delta):
		print (f"{self.color.green}Discriminant is strictly positive, the two solutions are:{self.color.none}")
		print (f"{self.color.green}Discriminant value is: {self.color.yellow}{delta}{self.color.none}")
		solution_1 = (-float(self._b) - ft_sqrt(delta)) / (2 * self._a)
		solution_2 = (-float(self._b) + ft_sqrt(delta)) / (2 * self._a)
		print (f"{self.color.yellow}{round(solution_1, 6)}{self.color.none}")
		print (f"{self.color.yellow}{round(solution_2, 6)}{self.color.none}")

	def __solve_1_solution(self, delta):
		print (f"{self.color.green}Discrimant is stricly egal to 0, the solution is:{self.color.none}")
		print (f"{self.color.green}Discriminant value is: {self.color.yellow}{delta}{self.color.none}")
		solution = -float(self._b) / (2 * self._a)
		print (f"{self.color.yellow}{solution}{self.color.none}")

	def __solve_no_real_solution(self, delta):
		print (f"{self.color.green}Discriminant is strictly negative, the two solutions are:{self.color.none}")
		print (f"{self.color.green}Discriminant value is: {self.color.yellow}{delta}{self.color.none}")
		a = (2 * self._a)
		i = round((ft_sqrt(ft_abs(delta))) / a, 6)
		b = -float(self._b) / a
		solution_1 = f"{b} - {i}i"
		solution_2 = f"{b} + {i}i"
		print (f"{self.color.yellow}{solution_1}{self.color.none}")
		print (f"{self.color.yellow}{solution_2}{self.color.none}")

	def parse_equation(self):
		neg = re.findall(r"[X|x]\^\-", self.__equation)
		fpow = re.findall(r"[X|x]\^(\d+\.\d+)", self.__equation)
		check_validity = self.__check_validity()
		if neg or fpow or check_validity:
			exit_error(f"{self.color.red}The polynomial equation is not valid!{self.color.none}")
		self.core_equation = re.split(r"(\s)?=(\s)?", self.__equation)[0]
		self.start_egal = re.split(r"(\s)?=(\s)?", self.__equation)[3]
		if self.core_equation and self.start_egal:
			pows = self.__parse_select_pows()
			self.__reduct_equation(pows)
			self.__parse_get_degree()
		else:
			exit_error(f"{self.color.red}The polynomial equation is not valid!{self.color.none}")

	def __check_validity(self):
		regex = r"((\s+)?(\+|\-)(\s+)?)?((\d+\.)?\d+)((\s+)?\*(\s+)?)[X|x]\^(\d+)"
		sub_all_power = re.sub(regex, "", self.__equation)
		sub_equal = re.sub(r"(\s)?=(\s)?", "", sub_all_power)
		error = sub_equal
		if error and error != '0':
			return True
		return False

	def __parse_get_degree(self):
		powers = re.findall(r"((\d+)(\s)?\*(\s)?([X|x]\^([\+|\-])?\d+))", self.reduct_equation)
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

	def __parse_select_pows(self, eq=None):
		if eq == None:
			eq = self.__equation
		powers = re.findall(r"([X|x]\^([\+|\-])?\d+)", eq)
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
		regex_power = r"(((\s+)?(\+|\-)(\s+)?)?((\d+\.)?\d+)((\s+)?\*(\s+)?)[X|x]\^{power}\b)".format(power=_power_of)
		core_power = re.search(regex_power, self.core_equation)
		egal_power = re.search(regex_power, self.start_egal)
		if core_power:
			core_power = core_power.group()
			self.core_equation = self.core_equation[len(core_power)::]
			core_power_int = get_int(core_power)
			self.__save_int_by_p(core_power_int, _power_of)
			if egal_power:
				egal_power = egal_power.group()
				egal_power_int = get_int(egal_power)
				reduct_int = core_power_int - egal_power_int
				self.start_egal = re.sub(regex_power.format(power=_power_of), "", self.start_egal, 1)
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
		elif not core_power and egal_power:
			egal_power = egal_power.group()
			egal_power_int = get_int(egal_power)
			egal_power_int *= -1
			self.__save_int_by_p(egal_power_int, _power_of)
			if egal_power_int < 0:
				egal_power_int = ft_abs(egal_power_int)
				signe = '- '
			return f"{space}{signe}{egal_power_int} * X^{_power_of}"


	def	__re_reduct_core(self):
		pows = self.__parse_select_pows(self.reduct_equation)
		first = 0
		for p in pows:
			space = '' if first == 0 else ' '
			signe = '' if first == 0 else '+ '
			regex_power = r"(((\s+)?(\+|\-)(\s+)?)?((\d+\.)?\d+)((\s+)?\*(\s+)?)[X|x]\^{power}\b)".format(power=p)
			core_power = re.findall(regex_power, self.reduct_equation)
			new_power_int = 0
			if len(core_power) > 1:
				for nb in core_power:
					nb_val = nb[5]
					core_is_float = re.search(r"(\.)", nb_val)
					nb_val = float(nb_val) if core_is_float else int(nb_val)
					signe = nb[3]
					if signe == '-':
						nb_val = -nb_val
					new_power_int += nb_val
				self.__save_int_by_p(new_power_int, p)
				if (signe == '+' or new_power_int > 0) and first == 0:
					new_reduct_power = f"{space}{new_power_int} * X^{p}"
				else:
					if new_power_int < 0:
						new_power_int = new_power_int * -1
					new_reduct_power = f"{space}{signe} {new_power_int} * X^{p}"
				self.reduct_equation = re.sub(regex_power, '', self.reduct_equation, len(core_power) - 1)
				self.reduct_equation = re.sub(regex_power, new_reduct_power, self.reduct_equation, 1)
			pows.remove(p)
			first += 1

	def	__reduct_equation(self, powers):
		reduct_equation = ""
		first = 0
		for p in powers:
			core_power = self.__reduct_power(p, first)
			if core_power:
				reduct_equation += "{power}".format(power=core_power)
			first += 1
		if not self._a and not self._b and not self._c:
			reduct_equation += "0"
		reduct_equation += " = 0"
		self.reduct_equation = reduct_equation
		self.__re_reduct_core()
		print (f"{self.color.magenta}Reduced form: {self.color.pink}{self.reduct_equation}{self.color.none}")