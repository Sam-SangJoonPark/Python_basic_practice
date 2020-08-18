{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ml_iris_sample.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOkNCp/akErKawult0KHjU6",
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
        "<a href=\"https://colab.research.google.com/github/Sam-SangJoonPark/sangjoonpark/blob/master/ml_iris_sample.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "7RxkVV2WBD1W",
        "colab_type": "text"
      },
      "source": [
        "# 1. 패키지불러오기\n",
        "[링크 텍스트]"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YWy0poos-42n",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "outputId": "28969ad4-c131-4866-e5b1-9cbfa9c3ebba"
      },
      "source": [
        "import sklearn\n",
        "print(sklearn.__version__)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0.22.2.post1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OiPVWhxrA4g-",
        "colab_type": "text"
      },
      "source": [
        "# 1. 개요\n",
        "- (1) iris 붓꽃 분류 모형을 만든다. \n",
        "패키지 불러오기\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b3PBZnGZBPtd",
        "colab_type": "text"
      },
      "source": [
        "#2. 데이터불러오기\n",
        "sklearn 패키지 내장데이터 있음"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3Yn5x6k-BpzN",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "outputId": "49e9c5d7-c0e4-44b5-eabc-267c6bb6bb0b"
      },
      "source": [
        "from sklearn.datasets import load_iris\n",
        "iris = load_iris()     # 이건 bunch 형태의 데이터셋으로 구성됨. \n",
        "# 독립변수로 구성된 데이터\n",
        "iris_data = iris.data\n",
        "\n",
        "\n",
        "# 종속변수\n",
        "iris_label = iris.target\n",
        "print('iris target 값 : ', iris_label[[0,50,100]])\n",
        "\n",
        "print('iris target 명 : ', iris.target_names)\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "iris target 값 :  [0 1 2]\n",
            "iris target 명 :  ['setosa' 'versicolor' 'virginica']\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2LcBPpHzERbj",
        "colab_type": "text"
      },
      "source": [
        "### (2) 데이터 전처리\n",
        " - 상황 : NUmpy 형태, 리스트를\n",
        "  -> excel data 로.\n",
        "  방법 : pandas 를 활용하여 dataframe으로 만들기"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yTv7aqtdBsi2",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7I1UOAvwEi2d",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "name = ['first','second','third','fourth']\n",
        "y = pd.DataFrame(iris_data, columns=name)\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Cozm8A_6E0Uu",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd\n",
        "from sklearn import datasets\n",
        "def sklearn_to_df(sklearn_dataset):\n",
        "    df = pd.DataFrame(sklearn_dataset.data, columns=sklearn_dataset.feature_names)\n",
        "    df['target'] = pd.Series(sklearn_dataset.target)\n",
        "    return df\n",
        "\n",
        "df_iris = sklearn_to_df(load_iris())\n",
        "# https://stackoverflow.com/questions/38105539/how-to-convert-a-scikit-learn-dataset-to-a-pandas-dataset#comment88542773_38105540"
      ],
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YPcPkMpxFIA1",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 419
        },
        "outputId": "eae3ef18-9525-4ce7-e488-b9999515f53d"
      },
      "source": [
        "df_iris"
      ],
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal length (cm)</th>\n",
              "      <th>sepal width (cm)</th>\n",
              "      <th>petal length (cm)</th>\n",
              "      <th>petal width (cm)</th>\n",
              "      <th>target</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>4.7</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.6</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>145</th>\n",
              "      <td>6.7</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.3</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>146</th>\n",
              "      <td>6.3</td>\n",
              "      <td>2.5</td>\n",
              "      <td>5.0</td>\n",
              "      <td>1.9</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>147</th>\n",
              "      <td>6.5</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.2</td>\n",
              "      <td>2.0</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>148</th>\n",
              "      <td>6.2</td>\n",
              "      <td>3.4</td>\n",
              "      <td>5.4</td>\n",
              "      <td>2.3</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>149</th>\n",
              "      <td>5.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>5.1</td>\n",
              "      <td>1.8</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>150 rows × 5 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "     sepal length (cm)  sepal width (cm)  ...  petal width (cm)  target\n",
              "0                  5.1               3.5  ...               0.2       0\n",
              "1                  4.9               3.0  ...               0.2       0\n",
              "2                  4.7               3.2  ...               0.2       0\n",
              "3                  4.6               3.1  ...               0.2       0\n",
              "4                  5.0               3.6  ...               0.2       0\n",
              "..                 ...               ...  ...               ...     ...\n",
              "145                6.7               3.0  ...               2.3       2\n",
              "146                6.3               2.5  ...               1.9       2\n",
              "147                6.5               3.0  ...               2.0       2\n",
              "148                6.2               3.4  ...               2.3       2\n",
              "149                5.9               3.0  ...               1.8       2\n",
              "\n",
              "[150 rows x 5 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nCuIcIlnIE5P",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}