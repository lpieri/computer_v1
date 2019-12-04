# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cpieri <cpieri@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 20:44:50 by cpieri            #+#    #+#              #
#    Updated: 2019/12/04 13:48:19 by cpieri           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re
from color import *

def	ft_abs(nb):
	if nb < 0:
		nb = nb * -1
	return nb

def	get_int(power):
	regex_int = r"((\s+)?(\+|\-)(\s+)?)?((\d+\.)?\d+)"
	nb_of_power = re.sub(r"\s+", "", re.match(regex_int, power).group())
	check_is_float = re.search(r"(\.)", nb_of_power)
	nb_of_power = float(nb_of_power) if check_is_float else int(nb_of_power)
	return nb_of_power

def ft_sqrt(nb):
	sqrt = 1
	while sqrt * sqrt < nb:
		sqrt += 1
	return sqrt

def exit_error(error):
	print("{prog} - error: {err}".format(prog=sys.argv[0], err=error))
	sys.exit(-1)