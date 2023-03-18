{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNlJid34qXr5cceQAagoY6Z",
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
        "<a href=\"https://colab.research.google.com/github/Sahilkumar19/calculus-part-2/blob/main/damping.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#input = A,B,C,x0,v0\n",
        "#output\n",
        "      #kind of damping\n",
        "      #plot of both independent salution\n",
        "      #plot of the final salution"
      ],
      "metadata": {
        "id": "8zMZAeJWs14t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import math"
      ],
      "metadata": {
        "id": "i_0WqH9OqwSr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a=int(input('enter a num:'))\n",
        "b=int(input('enter a num:'))\n",
        "c=int(input('enter a num:'))\n",
        "x0=int(input('enter value at t=0:'))\n",
        "v0=int(input('enter value of derivative of x at t=0:'))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o7Kmjcbbn9zn",
        "outputId": "21e6cb79-a478-4e18-f4db-02acf052faf1"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "enter a num:4\n",
            "enter a num:6\n",
            "enter a num:2\n",
            "enter value at t=0:4\n",
            "enter value of derivative of x at t=0:1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tlist = [i/100 for i in range(1001)]     #list of inputs or we can say the values of x"
      ],
      "metadata": {
        "id": "UyVXO-80oBVQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "d=(b**2-4*a*c)                     # discriminant of the quadratic equation and in this shell we are using conditional statements \n",
        "                                    #to check nature of damping by checking the value of d whether its +ve , 0 ,or -v\n",
        "if d>0:\n",
        "  value = 'over damped'\n",
        "elif d == 0:\n",
        "  value = 'critically damped'\n",
        "else:\n",
        "  value = 'under damped' "
      ],
      "metadata": {
        "id": "V-rNSQfgoE9L"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "lmda1=(-b-(b**2-4*a*c)**0.5)/(2*a)         # root of the quadratic equation \n",
        "lmda2=(-b+(b**2-4*a*c)**0.5)/(2*a)         # root of the quadratic equation\n",
        "if lmda1!=lmda2:\n",
        "  d1=(v0-lmda2*x0)/(lmda1-lmda2)         # coefficient for lmda1\n",
        "  d2=(v0-lmda1*x0)/(lmda2-lmda1)         # coefficient for lmda2\n",
        "else:\n",
        "  d1=x0\n",
        "  d2=v0-lmda2*x0\n",
        "alpha=-b/(2*a)                             \n",
        "beta=(abs(b**2/(4*a**2)-c/a))**0.5"
      ],
      "metadata": {
        "id": "jv2gNN2aoGXz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if value == 'over damped':  #in this shell we are collecting the values of solution corresponding to each value of t in a list first we are comparing each value to check what kind \n",
        "  print('over damped')      # of damping it is and then for that type of damping we have written the formula for corresponding damping and then we have passed each value of t by iterating\n",
        "  xlist = []                #them by for loop and for each t we are getting a x and that x we are appending in the xlist which is the accumulataor\n",
        "  for t in tlist:\n",
        "    x=d1*math.exp(lmda1*t)+d2*math.exp(lmda2*t)\n",
        "    xlist.append(x)\n",
        "elif value == 'critically damped':\n",
        "  print('critically damped')\n",
        "  xlist = []\n",
        "  for t in tlist:\n",
        "    x=(x0+(v0-lmda1*x0)*t)*math.exp(lmda1*t)  \n",
        "    xlist.append(x)\n",
        "else:\n",
        "  xlist = []\n",
        "  print('under damped')\n",
        "  for t in tlist:\n",
        "    x=math.exp(alpha*t)*(x0*math.cos(beta*t)+(v0+alpha*x0)*math.sin(beta*t)/beta)\n",
        "    xlist.append(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6DxXi9ZJoJju",
        "outputId": "bbb48f87-9403-4a21-bb44-e62ff6554b17"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "over damped\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "GRAPH OF OVERDAMPED"
      ],
      "metadata": {
        "id": "jfq853B5skvY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.plot(tlist, xlist)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "uswwNKEHoSS3",
        "outputId": "407ec487-02c6-4a19-b32f-539b3dc73de6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f4e4d052460>]"
            ]
          },
          "metadata": {},
          "execution_count": 24
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAWoAAAD4CAYAAADFAawfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/NK7nSAAAACXBIWXMAAAsTAAALEwEAmpwYAAAeZElEQVR4nO3dd3yV5f3/8dfnnOyEJGQwQwiEsEHAiBNRXFRcxVq31q/+tGoVW2ud1VZtq62t41tr3dpiHV9FRVS0KlVBBdmEJcgegUDIgOzk+v2RQFERApyT+4z38/E4j5x5530/xDc317nu+zLnHCIiErp8XgcQEZG9U1GLiIQ4FbWISIhTUYuIhDgVtYhIiIsJxkazsrJcXl5eMDYtIhKRZs2atcU5l72n14JS1Hl5ecycOTMYmxYRiUhmtvr7XtPQh4hIiFNRi4iEOBW1iEiIU1GLiIQ4FbWISIhTUYuIhDgVtYhIiAvKPOpgcc6xaGMFCzdUsKm8hhi/j46p8QzqmkavDimYmdcRRUQCLiyKuqa+kfFfrObZaatYX1a9x/fkZiRx9rAcLj2qO+lJcW2cUEQkeEK+qGetLmXcS3NZt62aI3tmMu7EAobnZdA5PYGmJli7rYpZq7fx9vyNPPjBVzzxyddcNTKfq0b2JD7G73V8EZGDZsFY4aWwsNAF4hTyF6av5s43F9IlPYH7xw7mqF5Ze33/4o0VPPzBMiYvLCY/O5kHzx3C4Jz0g84hIhJsZjbLOVe4p9dC9svEJz9Zwe2vFzGydzZvXz9inyUN0K9zKn+/+FCe/clhVNc18qPHPmf8F6vRcmMiEs5CsqjfnLue372zmDGDOvP4xYeSmhC7X58/vm8H3r5+BEfmZ3LHG0Xc9noRDY1NQUorIhJcrS5qM/Ob2RwzmxTMQPPWlnHTq/MZ3iODB88dQqz/wP4uaZ8cx7M/OYyrj8vnxRlruOaF2dTUNwY4rYhI8O1PC44DFgcrCEBVXQPjXppDdko8f7/oUOJiDu6A3+czbh7dl7tO78/7izZx+fNfqqxFJOy0qgnNLAcYAzwVzDC/f2cxq0ureOCcQ8hIDtwUu8uO7sGfzzmEz77eytXjZ1HXoGEQEQkfrT1kfQj4FfC9DWdmV5rZTDObWVJSst9ByqrqmFy0icuP7sGR+Zn7/fl9OfvQHH531iCmLC3huhdna8xaRMLGPovazE4DNjvnZu3tfc65J5xzhc65wuzsPa4ms1fpSXG8d8MIfnlKn/3+bGtdcHgud57Wn/cWbuLuSYs0G0REwkJrTng5GjjDzE4FEoBUMxvvnLso0GEyU+IDvcnv+J9jelBcUcMTn6wgLzOZ/zmmR9B/p4jIwdjnEbVz7lbnXI5zLg84D/goGCXdlm4Z3ZfRAzpxz9uLeH9hsddxRET2KiTnUQebz2fNZy12TeOGl+eyfHOl15FERL7XfhW1c+4/zrnTghWmLSXG+Xn84kKS4vxc9c9ZbK9t8DqSiMgeReUR9U6d0hJ45PyhrNyyg5tfna8vF0UkJEV1UQMclZ/FzaP78vaCjTw9daXXcUREviPqixrgymN7MnpAJ+57dwnz1pZ5HUdE5BtU1ICZcf/Zg+mYmsC4l+ZovFpEQoqKukVaUiwPnjuENaVV/GbiQq/jiIjsoqLezfAeGfzs+F68OmsdE+dt8DqOiAigov6O608oYFhuOrdPWMC6bVVexxERUVF/W4zfx8PnDaXJOW5+TVP2RMR7Kuo96JaRxG1j+jFt+VZemL7G6zgiEuVU1N/jguG5jCjI4vfvLGbNVg2BiIh3VNTfY+eUPb8ZN706j6YmDYGIiDdU1HvRJT2RX5/Wn+krS/nH56u8jiMiUUpFvQ/nFOZwXJ9s7pu8hNVbd3gdR0SikIp6H8yM+8YOJtbn47bXF2gWiIi0ORV1K3RKS+BXP+jLtOVbeXXWOq/jiEiUUVG30oXDcyns3p7fvbOYLdtrvY4jIlFERd1KPp/xh7GD2FHbwN1vLfI6johEERX1fijo2I5rjuvFxHkbmLJ0s9dxRCRKqKj30zXH59OrQwp3vF7EDl0OVUTagIp6P8XH+Llv7CDWl1Xz5/e/8jqOiEQBFfUBKMzL4KIjcnnus5VaEUZEgk5FfYB+NbovWSnx3P7GAhp1ermIBJGK+gClJsTy69P6U7S+gvFfrPY6johEMBX1QThtcGdGFGTxwHtL2VxR43UcEYlQKuqDYGbcfeZAahubuPftxV7HEZEIpaI+SD2ykrl6ZD4T521g6rItXscRkQikog6Aq4/LJy8ziTvfLKK2odHrOCISYVTUAZAQ6+fuMweyYssOHv94hddxRCTCqKgD5Nje2YwZ1Jm/Tlmu61aLSECpqAPo16f1J9Zn3PnmQl23WkQCRkUdQJ3SEvjFyX34+KsS3i0q9jqOiEQIFXWAXXpkd/p3TuXutxaxXRdtEpEAUFEHWIzfx70/HMimyhoe+rcu2iQiB09FHQTDcttz3mG5PPvZKhZtqPA6joiEORV1kNw8ug9pibHc8cYCmnTRJhE5CCrqIElPiuPWH/Rl9poyXpm51us4IhLGVNRB9KNDcxiel8F9k5dQuqPO6zgiEqZU1EFkZtxz1kC21zRw37u6aJOIHBgVdZD16dSOy4/pwSsz1zFzVanXcUQkDO2zqM0swcxmmNk8M1toZr9ti2CR5PoTCuiSlsDtrxdR39jkdRwRCTOtOaKuBUY55w4BhgCjzeyIoKaKMMnxMdx1xgCWbqrkuWmrvI4jImFmn0Xtmm1veRjbctN8s/10cv+OjOrbgQc/+IoNZdVexxGRMNKqMWoz85vZXGAz8G/n3PQ9vOdKM5tpZjNLSkoCHDP8mRm/PWMATc5xz6RFXscRkTDSqqJ2zjU654YAOcBwMxu4h/c84ZwrdM4VZmdnBzhmZOiWkcR1owp4t6iYKUs3ex1HRMLEfs36cM6VAVOA0UFJEwWuGNGDntnJ3PXmQmrqtRqMiOxba2Z9ZJtZesv9ROAkYEmQc0Ws+Bg/9545kDWlVfxtynKv44hIGGjNEXVnYIqZzQe+pHmMelJwY0W2o3plcdaQLvz94xWsKNm+7w+ISFRrzayP+c65oc65wc65gc65u9siWKS7bUw/4mN9/PrNIq0GIyJ7pTMTPdKhXQI3ndKHacu38tb8jV7HEZEQpqL20IWHd2dQ1zTumbSIipp6r+OISIhSUXvI7zN+98OBbNley1/e12owIrJnKmqPDc5J56LDu/OPz1dRtL7c6zgiEoJU1CHgl6f0ISM5jttfX0CjVoMRkW9RUYeAtMRYbh/Tj3nrynlxxhqv44hIiFFRh4izhnTlyJ6Z/HHyEkoqa72OIyIhREUdIppXgxlAdX0jf3hHq8GIyH+pqENIrw7tuPLYnkyYs55py7d4HUdEQoSKOsRcN6qAvMwkbnt9AdV1umiTiKioQ05CrJ/fjx3E6q1VPPSh5laLiIo6JB2Vn8W5hd146tOVmlstIirqUHXbqf1onxTHLRPm06AFcUWimoo6RKUlxfLbMwZQtL6CZ7UgrkhUU1GHsFMHdeLEfh3587+XsmZrlddxRMQjKuoQtnNudYzPx+1vLNB1q0WilIo6xHVOS+Tm0X34dNkWXp+z3us4IuIBFXUYuPDw7hzavT33TFrE1u06vVwk2qiow4DPZ9w3dhDbaxv47VuLvI4jIm1MRR0mCjq247pRBUyct4H3FhZ7HUdE2pCKOoxcfVw+A7qkcvvrRWzbUed1HBFpIyrqMBLr9/HAOYdQXl3Hb95a6HUcEWkjKuow069zKteNKuDNuRoCEYkWKuowpCEQkeiiog5Duw+B3DVRQyAikU5FHaZ2DoFMnLeByUUaAhGJZCrqMLZzCOSONzQEIhLJVNRhbPchkDs1BCISsVTUYa5f51TGnVDAW/M28OZcXQtEJBKpqCPAT0fmMyw3nTveKGJDWbXXcUQkwFTUESDG7+PBc4fQ1OS48ZV5NDXpcqgikURFHSG6ZyZz5+n9+XzFVp6ZttLrOCISQCrqCPLjwm6c3L8jf5y8lCXFFV7HEZEAUVFHEDPjD2MHkZoYyw0vzaW2odHrSCISACrqCJOZEs8ffzSIJcWV/Pn9r7yOIyIBoKKOQKP6duTCw3N58tMVTFu+xes4InKQVNQR6o4x/cnPTuGGl+eyRct3iYQ1FXWESozz89cLhlJRXc8vNGVPJKypqCNY306p3Hl6fz75qoQnP13hdRwROUAq6gh3wfBcTh3UiT+9t5TZa7Z5HUdEDsA+i9rMupnZFDNbZGYLzWxcWwSTwGiesjeYTmkJXP/iHMqr672OJCL7qTVH1A3Ajc65/sARwLVm1j+4sSSQ0hJj+d/zh1JcXsOtE+bjnMarRcLJPovaObfROTe75X4lsBjoGuxgElhDc9tz0yl9eGdBMS9MX+N1HBHZD/s1Rm1mecBQYPoeXrvSzGaa2cySkpIAxZNA+n8jejKydzZ3v7WI+evKvI4jIq3U6qI2sxTgNeAG59x3LiThnHvCOVfonCvMzs4OZEYJEJ/PeOjcIWS3i+fq8bO1KoxImGhVUZtZLM0l/YJzbkJwI0kwtU+O428XDqOkspYbXp5Lo+ZXi4S81sz6MOBpYLFz7i/BjyTBdki3dO46oz8ff1XCIx8u8zqOiOxDa46ojwYuBkaZ2dyW26lBziVBdsHwXM4elsMjHy1jytLNXscRkb1ozayPqc45c84Nds4Nabm90xbhJHjMjHvPGkifju244aW5rC2t8jqSiHwPnZkYxRLj/Pz9okNpco6rX5hFdZ2uXy0SilTUUS4vK5mHzh3Cwg0V/Oo1nQwjEopU1MIJ/Tpy0yl9eGveBv72n6+9jiMi3xLjdQAJDVePzGdpcSV/em8pBR1SOHlAJ68jiUgLHVEL0Pzl4v1nD2ZwTho/f3kuS4srvY4kIi1U1LJLQqyfJy4uJCk+hiv+8SWlOnNRJCSoqOUbOqUl8MTFh7KpopZrXphFXUOT15FEop6KWr5jaG577hs7iC9WlHLrhAWaCSLiMX2ZKHs0dlgOq7dW8fCHy+iWkcgNJ/b2OpJI1FJRy/e64cQC1m2r5qEPlpHTPokfHZrjdSSRqKSilu/VvIzXIIorqrnltfl0SUvgqF5ZXscSiToao5a9iovx8dhFh5KfncJV42fx1SZN2xNpaypq2afUhFievewwEmP9XPbslxSX13gdSSSqqKilVbqkJ/LMTw6jvLqeS56ZTlmV5liLtBUVtbTawK5pPHlJIau2VvGTZ79kR22D15FEooKKWvbLkfmZ/PX8ocxfV8ZPx8+itkGXRhUJNhW17LeTB3Ti/rMH8+myLfxc6y6KBJ2m58kBOaewG+XV9dz79mJSExbwh7GDaF5eU0QCTUUtB+yKET3ZVlXHo1O+Jjk+hjvG9FNZiwSBiloOyi9P7sOO2kaenrqSGJ9xyw/6qqxFAkxFLQfFzLjr9P40NDXx+Ccr8PuMm07po7IWCSAVtRw0M+PuMwbS2AR/+8/XxPiMX5zcx+tYIhFDRS0B4fMZvztrIE1Njkc+Wo7f52PciQVexxKJCCpqCRifr/kiTo3O8eAHX9HY1MTPT+qtYRCRg6SiloDy+ZrXXvQZPPLRcnbUNWo2iMhBUlFLwPl9xn1jB5MUF8PTU1dSVdfIvWcNxO9TWYscCBW1BIXP1zwbJDnez6NTvqa6roEHzjmEGL9OhhXZXypqCRoz46ZT+pIUF8Of3ltKVV0jj5w/lIRYv9fRRMKKDm8k6K49vhd3nd6f9xdt4tJnZlBeXe91JJGwoqKWNnHZ0T14+LwhzF6zjR///XM2lld7HUkkbKiopc2cOaQrz102nPVl1Yz922da1kuklVTU0qaO7pXFy1cdQUOT40ePfcaMlaVeRxIJeSpqaXMDuqQx4eqjyGoXz0VPT2fivA1eRxIJaSpq8US3jCRe++lRDMlJ5/oX5/CX95fSpAUIRPZIRS2eaZ8cx/grDufHhTk88tFyrv3XbKrqtA6jyLepqMVTcTE+7j97MHeM6cfkhcX8+HHNCBH5NhW1eM7MuGJET56+tJBVW6o446/TmL1mm9exREKGilpCxqi+HZlwzVEkxPo49/HP+efnq3BO49YiKmoJKb07tmPSz0YwoiCbX7+5kF+8Mk/j1hL19lnUZvaMmW02s6K2CCSSlhTLU5cUcuNJvXlj7np++OhnrCjZ7nUsEc+05oj6OWB0kHOIfIPPZ1x3QgHPXzaczZU1nPHXabyzYKPXsUQ8sc+ids59Auj0MfHEsb2zmXT9CPI7pHDNC7O5dcJ8DYVI1AnYGLWZXWlmM81sZklJSaA2K0LX9ET+76ojuWpkT16csZbT/3cqCzeUex1LpM0ErKidc0845wqdc4XZ2dmB2qwI0Dzf+tYf9GP85YdTWdPADx/9jKenrtSsEIkKmvUhYeWYgizeHTeCY3tncc+kRVz67Jc6QUYinopawk5mSjxPXlLI3WcOYMbKrZz84Ce8Omudjq4lYrVmet6LwOdAHzNbZ2aXBz+WyN6ZGZccmcfkccfSt1M7fvl/87ji+ZlsqqjxOppIwFkwjkIKCwvdzJkzA75dkT1pbHI899kq/jh5CQmxfn5zRn/OGtIVM616LuHDzGY55wr39JqGPiTs+X3G5cf04N1xI+jVIYWfvzyPS56ZwaotO7yOJhIQKmqJGD2zU3jlqiO5+8wBzF1TxskPfcIjHy6jtqHR62giB0VFLRHF72seu/7gxpGc1L8jf/n3V5z68Kd8sWKr19FEDpiKWiJSx9QEHr1gGM9ddhh1jU2c98QX3PDSHE3lk7CkopaIdlyfDrx/w0h+dnwv3ikqZtQDH/PwB8uortNwiIQPFbVEvMQ4P788pQ8f/mIko/p24MEPvuKEP/+HN+eu19xrCQsqaoka3TKSePTCYbx85RG0T45j3EtzOfuxz5iu8WsJcSpqiTqH98xk4s+O4f6zB7G+rJpzn/iCS5+ZQdF6XehJQpNOeJGoVl3XyPOfr+Kx/3xNeXU9YwZ35saTetMzO8XraBJl9nbCi4paBCivrufJT1bw9NSV1DU2cfawrlxzXC/yspK9jiZRQkUt0kollbU8OmU5/5qxhobGJs44pAvXHt+Lgo7tvI4mEU5FLbKfNlfU8NTUlYz/YjXV9Y2MHtCJa4/vxcCuaV5HkwilohY5QKU76nh22kqem7aKytoGju2dzeXH9ODYgixd9EkCSkUtcpAqaur55+eref6zVWyurKWgQwqXH9ODs4Z2JSHW73U8iQAqapEAqWtoYtL8DTz16UoWbawgIzmOiw7P5aIjutMhNcHreBLGVNQiAeac44sVpTw9dSUfLtmE34wT+3XkwiNyOTo/C59PwyKyf/ZW1DFtHUYkEpgZR+ZncmR+Jiu37ODFGWv4v5lrmbywmNyMJM4fnss5hTlkpcR7HVUigI6oRQKkpr6R9xYW88L0NcxYWUqs3zipf0fGDs1hZJ9sYv06EVi+n4Y+RNrY8s2V/Gv6Wt6Yu57SHXVkJsdx+iFdOHtYDgO7pmrGiHyHilrEI/WNTXy8tIQJc9bxwaLN1DU2UdAhhR8O68ppg7qQm5nkdUQJESpqkRBQXlXPpAUbeH32emau3gbAwK6pnDqoM2MGdaZ7pk5Xj2YqapEQs7a0ineLNvL2gmLmrS0DoH/nVMYM7szogZ3I10Whoo6KWiSErdtWxeSiYt5esJE5a8oA6JGVzKi+HTihbwcO65GhLyKjgIpaJExsKKvmw8Wb+GDxZj7/eit1jU20i4/h2D7ZnNC3AyN7Z5OpKX8RSUUtEoZ21DYwbfkWPly8mY+WbqakshaAAV1SOaZXFkf3yuKwvAwS43QKeyRQUYuEuaYmx4L15Xy6rISpy7cwa/U26hsdcX4fhXntObqluAd2SSVGwyRhSUUtEmGq6hqYsbKUacu3MHX5VhZvrAAgKc7P0Nx0DsvL4LC8DIZ0Syc5XicghwOdQi4SYZLiYjiuTweO69MBgC3ba/lixVZmrtrGjJWlPPzhMpwDv88Y2CWVwrwMDstrz+CcdDqnJeiEmzCjI2qRCFRRU8/s1duai3tVKXPXllHX0ARAdrt4DslJY3BOOod0S2dw1zTaJ8d5nFh0RC0SZVITYr9xxF3b0MiiDRXMX1fOvLVlzFtXxgeLN+96f25GEoNz0ujfJZV+nVLp1zmVjqnxOvIOESpqkSgQH+NnaG57hua23/VcRU09RevKmbeunPnrypizpoxJ8zfuer19Uix9O6XSt3M7+nVuLvCCjilaKMEDKmqRKJWaEMtRvbI4qlfWrufKq+tZWlzJ4o0VLCmuYNHGSl6csYaa+uZhE59Bt4wk8rNTyM9OJj87hV4dUsjPTtHwSRCpqEVkl7TEWIb3yGB4j4xdzzU2OVZv3cGS4kqWFFfydcl2vt68nanLt+wa9wbISI7bVd55WcnkZiQ13zKTSE2I9WJ3IoaKWkT2yu8zeman0DM7hVMHdd71fGOTY/226ubi3nnbvIP3F22idEfdN7bRPimW3IwkumUk0T2zpcAzkumankintATiYjT3e29U1CJyQPw+Izez+Yj5+L4dvvFaRU09a0urWLO1ijWl/70tWF/O5KJiGpq+OdssKyWeLukJdE5LoHNaYsv9//7s0C4+qk/kUVGLSMClJsQyoEsaA7qkfee1hsYmNpbXsHprFRvKqtlQXs3Gsho2lFfzdckOpi7bwo66xm98xu8zMpPj6JAaT3ZKPNntWm4p8XRITdh1P7tdfESe4BN5eyQiIS3G76NbyzDInjjnqKhpYONuBb6xrIaSylpKtteyubKGRRsr2LK9jsam754HkhTnJ7tdPBnJcWQkxdE+OY72SbG0/8bjODKSY2mfFEd6Uhz+EF+MWEUtIiHFzEhLjCUtsXl64PdpanJsq6qjZHttc4lX1rK58r/3t1XVUVxRw+KNFWyrqqe6vnGP2zFr/hdARnIcqYmxpCbEkJoQS2rizp+xtPvWc+12u58U5w/6fHMVtYiEJZ/PyEyJJzMlnr6d9v3+6rpGtlXVUbqjjrKqekqr6ti2o/nxzucrahqorKlnQ1k1FTUNVFTXU7vbzJY98fuMdgkxpMTH0CUtkVd+emSA9vC/WlXUZjYaeBjwA0855+4LeBIRkSBKjPOTGJdIl/TE/fpcbUMjlS2lvbPIK6obqKip/8b97bUNxAXpC899FrWZ+YFHgZOAdcCXZjbRObcoKIlEREJIfIyf+BQ/WR4u2NCa+h8OLHfOrXDO1QEvAWcGN5aIiOzUmqLuCqzd7fG6lue+wcyuNLOZZjazpKQkUPlERKJewAZUnHNPOOcKnXOF2dnZgdqsiEjUa01Rrwe67fY4p+U5ERFpA60p6i+BAjPrYWZxwHnAxODGEhGRnfY568M512BmPwPeo3l63jPOuYVBTyYiIkAr51E7594B3glyFhER2YPovRyViEiYCMritmZWAqw+wI9nAVsCGCccaJ8jX7TtL2if91d359wep8wFpagPhpnN/L6VeCOV9jnyRdv+gvY5kDT0ISIS4lTUIiIhLhSL+gmvA3hA+xz5om1/QfscMCE3Ri0iIt8UikfUIiKyGxW1iEiIC5miNrPRZrbUzJab2S1e5wk2M+tmZlPMbJGZLTSzcV5naitm5jezOWY2yessbcHM0s3sVTNbYmaLzSzwazWFGDP7ecuf6yIze9HMErzOFGhm9oyZbTazot2eyzCzf5vZspaf7QPxu0KiqHdbReYHQH/gfDPr722qoGsAbnTO9QeOAK6Ngn3eaRyw2OsQbehhYLJzri9wCBG+72bWFbgeKHTODaT5GkHneZsqKJ4DRn/ruVuAD51zBcCHLY8PWkgUNVG4ioxzbqNzbnbL/Uqa/+f9zoIMkcbMcoAxwFNeZ2kLZpYGHAs8DeCcq3POlXkaqm3EAIlmFgMkARs8zhNwzrlPgNJvPX0m8HzL/eeBswLxu0KlqFu1ikykMrM8YCgw3eMobeEh4FfA3pd2jhw9gBLg2ZbhnqfMLNnrUMHknFsPPACsATYC5c65971N1WY6Ouc2ttwvBjoGYqOhUtRRy8xSgNeAG5xzFV7nCSYzOw3Y7Jyb5XWWNhQDDAMec84NBXYQoH8Oh6qWcdkzaf5LqguQbGYXeZuq7bnmuc8Bmf8cKkUdlavImFkszSX9gnNugtd52sDRwBlmtorm4a1RZjbe20hBtw5Y55zb+a+lV2ku7kh2IrDSOVfinKsHJgBHeZyprWwys84ALT83B2KjoVLUUbeKjJkZzeOWi51zf/E6T1twzt3qnMtxzuXR/N/4I+dcRB9pOeeKgbVm1qflqROARR5GagtrgCPMLKnlz/kJRPgXqLuZCFzacv9S4M1AbLRVCwcEW5SuInM0cDGwwMzmtjx3W8siDRJZrgNeaDkIWQFc5nGeoHLOTTezV4HZNM9umkMEnk5uZi8CxwFZZrYOuAu4D3jFzC6n+VLPPw7I79Ip5CIioS1Uhj5EROR7qKhFREKcilpEJMSpqEVEQpyKWkQkxKmoRURCnIpaRCTE/X/2v3bT/HagSwAAAABJRU5ErkJggg==\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "GRAPH OF CRITICALLY DAMPED"
      ],
      "metadata": {
        "id": "wjwAeEJgry7u"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.plot(tlist, xlist)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "cZ67_fPNoV9Z",
        "outputId": "07ed9047-616b-4c1f-e88e-2d32d4c9e4d3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f4e5dba4c70>]"
            ]
          },
          "metadata": {},
          "execution_count": 13
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "GRAPH OF UNDERDAMPED"
      ],
      "metadata": {
        "id": "pZrAYn6Bsbdz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "plt.plot(tlist, xlist)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "D55RaZnqoWyD",
        "outputId": "db4c313b-1be7-4cf2-dd7d-73bc81ea2fb1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[<matplotlib.lines.Line2D at 0x7f4e4d0da100>]"
            ]
          },
          "metadata": {},
          "execution_count": 19
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}