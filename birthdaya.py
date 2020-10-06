{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled16.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOm2YDBa+1KtqbwxKRFb+3Y",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/singhsani/opencv/blob/master/birthdaya.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9vJ4YHkwbo3n",
        "outputId": "328a9b9e-941c-49f6-b207-e00fdc845145",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 238
        }
      },
      "source": [
        "bday={}\n",
        "while True:\n",
        "  print('Enter the name (blank to quit)')\n",
        "  name=input()\n",
        "  if name=='':\n",
        "    break\n",
        "  if name in bday:\n",
        "    print(bday[name])\n",
        "    print(' ---------------Happy birthday-----------------  ')\n",
        "    print('                ',name,'                         ')\n",
        "  else:\n",
        "    print('enter the birthdate')\n",
        "    date=input()\n",
        "    bday[name]=date;\n",
        "    print('Birthdate is update')\n",
        "print('Congrate , You are out of Program !!!!!!!!!!!!')\n"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter the name (blank to quit)\n",
            "rajni\n",
            "enter the name with birthdate\n",
            "10-may-2000\n",
            "Birthdate is update\n",
            "Enter the name (blank to quit)\n",
            "rajni\n",
            "10-may-2000\n",
            " ---------------Happy birthday-----------------  \n",
            "                            rajni                          \n",
            "Enter the name (blank to quit)\n",
            "\n",
            "Congrate , You are out of Program !!!!!!!!!!!!\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}