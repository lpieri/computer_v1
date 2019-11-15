# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynomial_class.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cpieri <cpieri@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 20:18:19 by cpieri            #+#    #+#              #
#    Updated: 2019/09/17 21:03:55 by cpieri           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
from utils import *

class Polynomial:

	def __init__(self, equation):
		self.equation = equation
		self.parse_equation()

	def parse_equation(self):
		neg = re.findall("X\^-", self.equation)
		if neg:
			exit_error("The polynomial equation is not valid!")
		self.start_egal = self.equation.split(" = ")[1]
		self.core_equation = self.equation.split(" = ")[0]
		print (self.core_equation, self.start_egal)