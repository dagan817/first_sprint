{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMizBlUXMQLtvZgeyzUnSFi",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/dagan817/first_sprint/blob/main/test_calculator_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 374
        },
        "id": "vs3pWwxoH820",
        "outputId": "a5effc6b-c6c1-45b0-c234-120e7d61589d"
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-ef74212557eb>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mcalculator\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mtest_add\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0;32massert\u001b[0m \u001b[0mcalculator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m5\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0;32massert\u001b[0m \u001b[0mcalculator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m5\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m4\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'calculator'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import dovydas_calculator\n",
        "\n",
        "def test_add():\n",
        "    assert dovydas_calculator.add(2, 3) == 5\n",
        "    assert dovydas_calculator.add(-1, 5) == 4\n",
        "    assert dovydas_calculator.add(0, 0) == 0\n",
        "\n",
        "def test_subtract():\n",
        "    assert dovydas_calculator.subtract(5, 2) == 3\n",
        "    assert dovydas_calculator.subtract(10, -3) == 13\n",
        "    assert dovydas_calculator.subtract(0, 0) == 0\n",
        "\n",
        "def test_multiply():\n",
        "    assert dovydas_calculator.multiply(2, 3) == 6\n",
        "    assert dovydas_calculator.multiply(-4, 5) == -20\n",
        "    assert dovydas_calculator.multiply(0, 10) == 0\n",
        "\n",
        "def test_divide():\n",
        "    assert dovydas_calculator.divide(6, 3) == 2\n",
        "    assert dovydas_calculator.divide(10, -2) == -5\n",
        "    assert dovydas_calculator.divide(7, 2) == 3.5\n",
        "    assert dovydas_calculator.divide(5, 0) == \"Error: Division by zero\"\n",
        "\n",
        "def test_nth_root():\n",
        "    assert dovydas_calculator.nth_root(9, 2) == 3\n",
        "    assert dovydas_calculator.nth_root(27, 3) == 3\n",
        "    assert dovydas_calculator.nth_root(16, 4) == 2\n",
        "    assert dovydas_calculator.nth_root(8, 3) == 2"
      ]
    }
  ]
}
