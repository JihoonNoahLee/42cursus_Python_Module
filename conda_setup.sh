# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    conda_setup.sh                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jihoolee <jihoolee@student.42SEOUL.kr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/16 12:07:49 by jihoolee          #+#    #+#              #
#    Updated: 2023/04/16 12:08:55 by jihoolee         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

MYPATH="/goinfre/$USER/miniconda3"
curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh"
sh Miniconda3-latest-MacOSX-x86_64.sh -b -p $MYPATH

$MYPATH/bin/conda init zsh
$MYPATH/bin/conda config --set auto_activate_base false
source ~/.zshrc

conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy
conda activate 42AI-$USER
