# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cpieri <cpieri@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/17 20:04:23 by cpieri            #+#    #+#              #
#    Updated: 2019/09/17 20:58:45 by cpieri           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from polynomial_class import Polynomial
from utils import *

if __name__ == "__main__":
	if (len(sys.argv) != 2):
		exit_error("You didn't enter just one polynomial equation as a parameter!")
	else:
		Polynomial(sys.argv[1])