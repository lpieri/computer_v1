# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cpieri <cpieri@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 20:44:50 by cpieri            #+#    #+#              #
#    Updated: 2019/12/09 11:46:00 by cpieri           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re
from color import Color

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
	if nb == 0 or nb == 1:
		return nb
	calc = nb
	diff = calc
	calc = 0.5 * (calc + nb / calc)
	while calc != diff:
		diff = calc
		calc = 0.5 * (calc + nb / calc)
	return calc

def exit_error(error):
	print("{prog} - error: {err}".format(prog=sys.argv[0], err=error))
	sys.exit(-1)