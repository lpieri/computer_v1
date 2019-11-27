# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    utils.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cpieri <cpieri@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 20:44:50 by cpieri            #+#    #+#              #
#    Updated: 2019/11/27 11:14:44 by cpieri           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def	ft_abs(nb):
	if nb < 0:
		nb = nb * -1
	return nb

def ft_sqrt(nb):
	sqrt = 1
	while sqrt * sqrt < nb:
		sqrt += 1
	return sqrt

def exit_error(error):
	print("{prog} - error: {err}".format(prog=sys.argv[0], err=error))
	sys.exit(-1)