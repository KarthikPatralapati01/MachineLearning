{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "93IUOYd6587Z"
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline\n",
    "from google.colab import files\n",
    "import io"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "sfntUICQ_bL3",
    "outputId": "e06a4e86-0c92-4eea-cc25-bd5735978118"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mounted at /content/drive\n"
     ]
    }
   ],
   "source": [
    "from google.colab import drive\n",
    "drive.mount('/content/drive')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "id": "CjUfVng26GDt"
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Path to your CSV file in Google Drive\n",
    "file_path = '/content/synthetic_network_traffic.csv'\n",
    "\n",
    "# Read the CSV file using Pandas\n",
    "df = pd.read_csv(file_path)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 206
    },
    "id": "IFWDeTiJ6GHm",
    "outputId": "3a8ad4f2-d134-4e6b-d413-50d8368a5a3e"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "  <div id=\"df-eeb80968-1773-4003-9d6c-0f220d8cab6e\" class=\"colab-df-container\">\n",
       "    <div>\n",
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
       "      <th>SourceIP</th>\n",
       "      <th>DestinationIP</th>\n",
       "      <th>SourcePort</th>\n",
       "      <th>DestinationPort</th>\n",
       "      <th>Protocol</th>\n",
       "      <th>BytesSent</th>\n",
       "      <th>BytesReceived</th>\n",
       "      <th>PacketsSent</th>\n",
       "      <th>PacketsReceived</th>\n",
       "      <th>Duration</th>\n",
       "      <th>IsAnomaly</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.496714</td>\n",
       "      <td>-0.138264</td>\n",
       "      <td>0.647689</td>\n",
       "      <td>1.523030</td>\n",
       "      <td>-0.234153</td>\n",
       "      <td>-0.234137</td>\n",
       "      <td>1.579213</td>\n",
       "      <td>0.767435</td>\n",
       "      <td>-0.469474</td>\n",
       "      <td>0.542560</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>-0.463418</td>\n",
       "      <td>-0.465730</td>\n",
       "      <td>0.241962</td>\n",
       "      <td>-1.913280</td>\n",
       "      <td>-1.724918</td>\n",
       "      <td>-0.562288</td>\n",
       "      <td>-1.012831</td>\n",
       "      <td>0.314247</td>\n",
       "      <td>-0.908024</td>\n",
       "      <td>-1.412304</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1.465649</td>\n",
       "      <td>-0.225776</td>\n",
       "      <td>0.067528</td>\n",
       "      <td>-1.424748</td>\n",
       "      <td>-0.544383</td>\n",
       "      <td>0.110923</td>\n",
       "      <td>-1.150994</td>\n",
       "      <td>0.375698</td>\n",
       "      <td>-0.600639</td>\n",
       "      <td>-0.291694</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-0.601707</td>\n",
       "      <td>1.852278</td>\n",
       "      <td>-0.013497</td>\n",
       "      <td>-1.057711</td>\n",
       "      <td>0.822545</td>\n",
       "      <td>-1.220844</td>\n",
       "      <td>0.208864</td>\n",
       "      <td>-1.959670</td>\n",
       "      <td>-1.328186</td>\n",
       "      <td>0.196861</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.738467</td>\n",
       "      <td>0.171368</td>\n",
       "      <td>-0.115648</td>\n",
       "      <td>-0.301104</td>\n",
       "      <td>-1.478522</td>\n",
       "      <td>-0.719844</td>\n",
       "      <td>-0.460639</td>\n",
       "      <td>1.057122</td>\n",
       "      <td>0.343618</td>\n",
       "      <td>-1.763040</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>\n",
       "    <div class=\"colab-df-buttons\">\n",
       "\n",
       "  <div class=\"colab-df-container\">\n",
       "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-eeb80968-1773-4003-9d6c-0f220d8cab6e')\"\n",
       "            title=\"Convert this dataframe to an interactive table.\"\n",
       "            style=\"display:none;\">\n",
       "\n",
       "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
       "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
       "  </svg>\n",
       "    </button>\n",
       "\n",
       "  <style>\n",
       "    .colab-df-container {\n",
       "      display:flex;\n",
       "      gap: 12px;\n",
       "    }\n",
       "\n",
       "    .colab-df-convert {\n",
       "      background-color: #E8F0FE;\n",
       "      border: none;\n",
       "      border-radius: 50%;\n",
       "      cursor: pointer;\n",
       "      display: none;\n",
       "      fill: #1967D2;\n",
       "      height: 32px;\n",
       "      padding: 0 0 0 0;\n",
       "      width: 32px;\n",
       "    }\n",
       "\n",
       "    .colab-df-convert:hover {\n",
       "      background-color: #E2EBFA;\n",
       "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
       "      fill: #174EA6;\n",
       "    }\n",
       "\n",
       "    .colab-df-buttons div {\n",
       "      margin-bottom: 4px;\n",
       "    }\n",
       "\n",
       "    [theme=dark] .colab-df-convert {\n",
       "      background-color: #3B4455;\n",
       "      fill: #D2E3FC;\n",
       "    }\n",
       "\n",
       "    [theme=dark] .colab-df-convert:hover {\n",
       "      background-color: #434B5C;\n",
       "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
       "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
       "      fill: #FFFFFF;\n",
       "    }\n",
       "  </style>\n",
       "\n",
       "    <script>\n",
       "      const buttonEl =\n",
       "        document.querySelector('#df-eeb80968-1773-4003-9d6c-0f220d8cab6e button.colab-df-convert');\n",
       "      buttonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "\n",
       "      async function convertToInteractive(key) {\n",
       "        const element = document.querySelector('#df-eeb80968-1773-4003-9d6c-0f220d8cab6e');\n",
       "        const dataTable =\n",
       "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
       "                                                    [key], {});\n",
       "        if (!dataTable) return;\n",
       "\n",
       "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
       "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
       "          + ' to learn more about interactive tables.';\n",
       "        element.innerHTML = '';\n",
       "        dataTable['output_type'] = 'display_data';\n",
       "        await google.colab.output.renderOutput(dataTable, element);\n",
       "        const docLink = document.createElement('div');\n",
       "        docLink.innerHTML = docLinkHtml;\n",
       "        element.appendChild(docLink);\n",
       "      }\n",
       "    </script>\n",
       "  </div>\n",
       "\n",
       "\n",
       "<div id=\"df-ba1e938e-cd22-40da-9d56-4c452a356a52\">\n",
       "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-ba1e938e-cd22-40da-9d56-4c452a356a52')\"\n",
       "            title=\"Suggest charts\"\n",
       "            style=\"display:none;\">\n",
       "\n",
       "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
       "     width=\"24px\">\n",
       "    <g>\n",
       "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
       "    </g>\n",
       "</svg>\n",
       "  </button>\n",
       "\n",
       "<style>\n",
       "  .colab-df-quickchart {\n",
       "      --bg-color: #E8F0FE;\n",
       "      --fill-color: #1967D2;\n",
       "      --hover-bg-color: #E2EBFA;\n",
       "      --hover-fill-color: #174EA6;\n",
       "      --disabled-fill-color: #AAA;\n",
       "      --disabled-bg-color: #DDD;\n",
       "  }\n",
       "\n",
       "  [theme=dark] .colab-df-quickchart {\n",
       "      --bg-color: #3B4455;\n",
       "      --fill-color: #D2E3FC;\n",
       "      --hover-bg-color: #434B5C;\n",
       "      --hover-fill-color: #FFFFFF;\n",
       "      --disabled-bg-color: #3B4455;\n",
       "      --disabled-fill-color: #666;\n",
       "  }\n",
       "\n",
       "  .colab-df-quickchart {\n",
       "    background-color: var(--bg-color);\n",
       "    border: none;\n",
       "    border-radius: 50%;\n",
       "    cursor: pointer;\n",
       "    display: none;\n",
       "    fill: var(--fill-color);\n",
       "    height: 32px;\n",
       "    padding: 0;\n",
       "    width: 32px;\n",
       "  }\n",
       "\n",
       "  .colab-df-quickchart:hover {\n",
       "    background-color: var(--hover-bg-color);\n",
       "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
       "    fill: var(--button-hover-fill-color);\n",
       "  }\n",
       "\n",
       "  .colab-df-quickchart-complete:disabled,\n",
       "  .colab-df-quickchart-complete:disabled:hover {\n",
       "    background-color: var(--disabled-bg-color);\n",
       "    fill: var(--disabled-fill-color);\n",
       "    box-shadow: none;\n",
       "  }\n",
       "\n",
       "  .colab-df-spinner {\n",
       "    border: 2px solid var(--fill-color);\n",
       "    border-color: transparent;\n",
       "    border-bottom-color: var(--fill-color);\n",
       "    animation:\n",
       "      spin 1s steps(1) infinite;\n",
       "  }\n",
       "\n",
       "  @keyframes spin {\n",
       "    0% {\n",
       "      border-color: transparent;\n",
       "      border-bottom-color: var(--fill-color);\n",
       "      border-left-color: var(--fill-color);\n",
       "    }\n",
       "    20% {\n",
       "      border-color: transparent;\n",
       "      border-left-color: var(--fill-color);\n",
       "      border-top-color: var(--fill-color);\n",
       "    }\n",
       "    30% {\n",
       "      border-color: transparent;\n",
       "      border-left-color: var(--fill-color);\n",
       "      border-top-color: var(--fill-color);\n",
       "      border-right-color: var(--fill-color);\n",
       "    }\n",
       "    40% {\n",
       "      border-color: transparent;\n",
       "      border-right-color: var(--fill-color);\n",
       "      border-top-color: var(--fill-color);\n",
       "    }\n",
       "    60% {\n",
       "      border-color: transparent;\n",
       "      border-right-color: var(--fill-color);\n",
       "    }\n",
       "    80% {\n",
       "      border-color: transparent;\n",
       "      border-right-color: var(--fill-color);\n",
       "      border-bottom-color: var(--fill-color);\n",
       "    }\n",
       "    90% {\n",
       "      border-color: transparent;\n",
       "      border-bottom-color: var(--fill-color);\n",
       "    }\n",
       "  }\n",
       "</style>\n",
       "\n",
       "  <script>\n",
       "    async function quickchart(key) {\n",
       "      const quickchartButtonEl =\n",
       "        document.querySelector('#' + key + ' button');\n",
       "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
       "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
       "      try {\n",
       "        const charts = await google.colab.kernel.invokeFunction(\n",
       "            'suggestCharts', [key], {});\n",
       "      } catch (error) {\n",
       "        console.error('Error during call to suggestCharts:', error);\n",
       "      }\n",
       "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
       "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
       "    }\n",
       "    (() => {\n",
       "      let quickchartButtonEl =\n",
       "        document.querySelector('#df-ba1e938e-cd22-40da-9d56-4c452a356a52 button');\n",
       "      quickchartButtonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "    })();\n",
       "  </script>\n",
       "</div>\n",
       "\n",
       "    </div>\n",
       "  </div>\n"
      ],
      "text/plain": [
       "   SourceIP  DestinationIP  SourcePort  DestinationPort  Protocol  BytesSent  \\\n",
       "0  0.496714      -0.138264    0.647689         1.523030 -0.234153  -0.234137   \n",
       "1 -0.463418      -0.465730    0.241962        -1.913280 -1.724918  -0.562288   \n",
       "2  1.465649      -0.225776    0.067528        -1.424748 -0.544383   0.110923   \n",
       "3 -0.601707       1.852278   -0.013497        -1.057711  0.822545  -1.220844   \n",
       "4  0.738467       0.171368   -0.115648        -0.301104 -1.478522  -0.719844   \n",
       "\n",
       "   BytesReceived  PacketsSent  PacketsReceived  Duration  IsAnomaly  \n",
       "0       1.579213     0.767435        -0.469474  0.542560      False  \n",
       "1      -1.012831     0.314247        -0.908024 -1.412304      False  \n",
       "2      -1.150994     0.375698        -0.600639 -0.291694      False  \n",
       "3       0.208864    -1.959670        -1.328186  0.196861      False  \n",
       "4      -0.460639     1.057122         0.343618 -1.763040      False  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "EhalPUEY6GK4",
    "outputId": "edf04ca5-2a3a-41ea-d43a-2873107ec5a2"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SourceIP           0\n",
       "DestinationIP      1\n",
       "SourcePort         1\n",
       "DestinationPort    1\n",
       "Protocol           1\n",
       "BytesSent          1\n",
       "BytesReceived      1\n",
       "PacketsSent        1\n",
       "PacketsReceived    1\n",
       "Duration           1\n",
       "IsAnomaly          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "id": "EOv5zcN4A8XL"
   },
   "outputs": [],
   "source": [
    "df.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "xRflsCw191mb"
   },
   "source": [
    "**Changing the datatypes of a column from int to boolean**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "lvZLXV6K6GOq",
    "outputId": "9585fd77-3d4d-4232-eff5-5131c5939f7e"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SourceIP           float64\n",
       "DestinationIP      float64\n",
       "SourcePort         float64\n",
       "DestinationPort    float64\n",
       "Protocol           float64\n",
       "BytesSent          float64\n",
       "BytesReceived      float64\n",
       "PacketsSent        float64\n",
       "PacketsReceived    float64\n",
       "Duration           float64\n",
       "IsAnomaly             bool\n",
       "dtype: object"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "id": "JNS0OMP46GSE"
   },
   "outputs": [],
   "source": [
    "from pandas.core.arrays import boolean\n",
    "df['IsAnomaly']=df['IsAnomaly'].astype(bool)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "s8FDUyOq6GVs",
    "outputId": "0a4aab97-95d3-453b-d33a-9a8c8b756e06"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SourceIP           float64\n",
       "DestinationIP      float64\n",
       "SourcePort         float64\n",
       "DestinationPort    float64\n",
       "Protocol           float64\n",
       "BytesSent          float64\n",
       "BytesReceived      float64\n",
       "PacketsSent        float64\n",
       "PacketsReceived    float64\n",
       "Duration           float64\n",
       "IsAnomaly             bool\n",
       "dtype: object"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "qEuDQy4j6GZh",
    "outputId": "78400f21-134a-4a4b-a630-e72342f89a10"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SourceIP           0\n",
       "DestinationIP      0\n",
       "SourcePort         0\n",
       "DestinationPort    0\n",
       "Protocol           0\n",
       "BytesSent          0\n",
       "BytesReceived      0\n",
       "PacketsSent        0\n",
       "PacketsReceived    0\n",
       "Duration           0\n",
       "IsAnomaly          0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "bR_0531f_XNs"
   },
   "source": [
    "The dataset consists of the following columns:\n",
    "\n",
    "SourceIP: Source IP address of network traffic.\n",
    "\n",
    "Destination IP: Destination IP address of network traffic.\n",
    "\n",
    "SourcePort: Source port number.\n",
    "\n",
    "DestinationPort: Destination port number.\n",
    "\n",
    "Protocol: Network protocol used.\n",
    "\n",
    "BytesSent: Number of bytes sent in the network communication.\n",
    "\n",
    "BytesReceived: Number of bytes received in the network communication.\n",
    "\n",
    "PacketsSent: Number of packets sent.\n",
    "\n",
    "PacketsReceived: Number of packets received.\n",
    "\n",
    "Duration: Duration of the network communication.\n",
    "\n",
    "Additionally, there is a binary target variable:\n",
    "IsAnomaly: 0 for regular network traffic, 1 for anomalous network traffic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 300
    },
    "id": "xIZyv0VS6Gdg",
    "outputId": "ec67a2b0-c19b-4942-dca7-67d0d96e84ef"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "  <div id=\"df-a1683e3c-847a-47f9-8e53-7c35baaa8965\" class=\"colab-df-container\">\n",
       "    <div>\n",
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
       "      <th>SourceIP</th>\n",
       "      <th>DestinationIP</th>\n",
       "      <th>SourcePort</th>\n",
       "      <th>DestinationPort</th>\n",
       "      <th>Protocol</th>\n",
       "      <th>BytesSent</th>\n",
       "      <th>BytesReceived</th>\n",
       "      <th>PacketsSent</th>\n",
       "      <th>PacketsReceived</th>\n",
       "      <th>Duration</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>84600.000000</td>\n",
       "      <td>84600.000000</td>\n",
       "      <td>84600.000000</td>\n",
       "      <td>84600.000000</td>\n",
       "      <td>84600.000000</td>\n",
       "      <td>84600.000000</td>\n",
       "      <td>84600.000000</td>\n",
       "      <td>84600.000000</td>\n",
       "      <td>84600.000000</td>\n",
       "      <td>84600.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>-0.001361</td>\n",
       "      <td>0.004459</td>\n",
       "      <td>-0.004863</td>\n",
       "      <td>-0.007567</td>\n",
       "      <td>0.004002</td>\n",
       "      <td>-0.001145</td>\n",
       "      <td>-0.002120</td>\n",
       "      <td>-0.000419</td>\n",
       "      <td>0.001752</td>\n",
       "      <td>0.000294</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.001086</td>\n",
       "      <td>1.003272</td>\n",
       "      <td>1.002116</td>\n",
       "      <td>1.002699</td>\n",
       "      <td>0.996825</td>\n",
       "      <td>0.999653</td>\n",
       "      <td>0.999598</td>\n",
       "      <td>0.997631</td>\n",
       "      <td>1.000847</td>\n",
       "      <td>0.999112</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-4.295391</td>\n",
       "      <td>-4.465604</td>\n",
       "      <td>-4.829436</td>\n",
       "      <td>-4.413886</td>\n",
       "      <td>-3.997015</td>\n",
       "      <td>-4.164295</td>\n",
       "      <td>-4.462969</td>\n",
       "      <td>-4.319465</td>\n",
       "      <td>-3.984321</td>\n",
       "      <td>-4.157734</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>-0.676920</td>\n",
       "      <td>-0.670082</td>\n",
       "      <td>-0.684160</td>\n",
       "      <td>-0.683350</td>\n",
       "      <td>-0.664569</td>\n",
       "      <td>-0.674570</td>\n",
       "      <td>-0.678847</td>\n",
       "      <td>-0.677309</td>\n",
       "      <td>-0.673542</td>\n",
       "      <td>-0.680239</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>-0.002316</td>\n",
       "      <td>0.002619</td>\n",
       "      <td>-0.005130</td>\n",
       "      <td>-0.003860</td>\n",
       "      <td>0.004968</td>\n",
       "      <td>-0.004721</td>\n",
       "      <td>0.001693</td>\n",
       "      <td>0.002775</td>\n",
       "      <td>0.001601</td>\n",
       "      <td>0.001043</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.670061</td>\n",
       "      <td>0.682693</td>\n",
       "      <td>0.671370</td>\n",
       "      <td>0.664164</td>\n",
       "      <td>0.677522</td>\n",
       "      <td>0.672753</td>\n",
       "      <td>0.677339</td>\n",
       "      <td>0.675245</td>\n",
       "      <td>0.677838</td>\n",
       "      <td>0.673449</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>3.859376</td>\n",
       "      <td>4.611257</td>\n",
       "      <td>4.004674</td>\n",
       "      <td>4.479084</td>\n",
       "      <td>4.526784</td>\n",
       "      <td>4.065773</td>\n",
       "      <td>4.153257</td>\n",
       "      <td>4.678949</td>\n",
       "      <td>3.989945</td>\n",
       "      <td>4.289893</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>\n",
       "    <div class=\"colab-df-buttons\">\n",
       "\n",
       "  <div class=\"colab-df-container\">\n",
       "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a1683e3c-847a-47f9-8e53-7c35baaa8965')\"\n",
       "            title=\"Convert this dataframe to an interactive table.\"\n",
       "            style=\"display:none;\">\n",
       "\n",
       "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
       "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
       "  </svg>\n",
       "    </button>\n",
       "\n",
       "  <style>\n",
       "    .colab-df-container {\n",
       "      display:flex;\n",
       "      gap: 12px;\n",
       "    }\n",
       "\n",
       "    .colab-df-convert {\n",
       "      background-color: #E8F0FE;\n",
       "      border: none;\n",
       "      border-radius: 50%;\n",
       "      cursor: pointer;\n",
       "      display: none;\n",
       "      fill: #1967D2;\n",
       "      height: 32px;\n",
       "      padding: 0 0 0 0;\n",
       "      width: 32px;\n",
       "    }\n",
       "\n",
       "    .colab-df-convert:hover {\n",
       "      background-color: #E2EBFA;\n",
       "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
       "      fill: #174EA6;\n",
       "    }\n",
       "\n",
       "    .colab-df-buttons div {\n",
       "      margin-bottom: 4px;\n",
       "    }\n",
       "\n",
       "    [theme=dark] .colab-df-convert {\n",
       "      background-color: #3B4455;\n",
       "      fill: #D2E3FC;\n",
       "    }\n",
       "\n",
       "    [theme=dark] .colab-df-convert:hover {\n",
       "      background-color: #434B5C;\n",
       "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
       "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
       "      fill: #FFFFFF;\n",
       "    }\n",
       "  </style>\n",
       "\n",
       "    <script>\n",
       "      const buttonEl =\n",
       "        document.querySelector('#df-a1683e3c-847a-47f9-8e53-7c35baaa8965 button.colab-df-convert');\n",
       "      buttonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "\n",
       "      async function convertToInteractive(key) {\n",
       "        const element = document.querySelector('#df-a1683e3c-847a-47f9-8e53-7c35baaa8965');\n",
       "        const dataTable =\n",
       "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
       "                                                    [key], {});\n",
       "        if (!dataTable) return;\n",
       "\n",
       "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
       "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
       "          + ' to learn more about interactive tables.';\n",
       "        element.innerHTML = '';\n",
       "        dataTable['output_type'] = 'display_data';\n",
       "        await google.colab.output.renderOutput(dataTable, element);\n",
       "        const docLink = document.createElement('div');\n",
       "        docLink.innerHTML = docLinkHtml;\n",
       "        element.appendChild(docLink);\n",
       "      }\n",
       "    </script>\n",
       "  </div>\n",
       "\n",
       "\n",
       "<div id=\"df-ce4721e0-24ef-4705-950f-59409312a510\">\n",
       "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-ce4721e0-24ef-4705-950f-59409312a510')\"\n",
       "            title=\"Suggest charts\"\n",
       "            style=\"display:none;\">\n",
       "\n",
       "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
       "     width=\"24px\">\n",
       "    <g>\n",
       "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
       "    </g>\n",
       "</svg>\n",
       "  </button>\n",
       "\n",
       "<style>\n",
       "  .colab-df-quickchart {\n",
       "      --bg-color: #E8F0FE;\n",
       "      --fill-color: #1967D2;\n",
       "      --hover-bg-color: #E2EBFA;\n",
       "      --hover-fill-color: #174EA6;\n",
       "      --disabled-fill-color: #AAA;\n",
       "      --disabled-bg-color: #DDD;\n",
       "  }\n",
       "\n",
       "  [theme=dark] .colab-df-quickchart {\n",
       "      --bg-color: #3B4455;\n",
       "      --fill-color: #D2E3FC;\n",
       "      --hover-bg-color: #434B5C;\n",
       "      --hover-fill-color: #FFFFFF;\n",
       "      --disabled-bg-color: #3B4455;\n",
       "      --disabled-fill-color: #666;\n",
       "  }\n",
       "\n",
       "  .colab-df-quickchart {\n",
       "    background-color: var(--bg-color);\n",
       "    border: none;\n",
       "    border-radius: 50%;\n",
       "    cursor: pointer;\n",
       "    display: none;\n",
       "    fill: var(--fill-color);\n",
       "    height: 32px;\n",
       "    padding: 0;\n",
       "    width: 32px;\n",
       "  }\n",
       "\n",
       "  .colab-df-quickchart:hover {\n",
       "    background-color: var(--hover-bg-color);\n",
       "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
       "    fill: var(--button-hover-fill-color);\n",
       "  }\n",
       "\n",
       "  .colab-df-quickchart-complete:disabled,\n",
       "  .colab-df-quickchart-complete:disabled:hover {\n",
       "    background-color: var(--disabled-bg-color);\n",
       "    fill: var(--disabled-fill-color);\n",
       "    box-shadow: none;\n",
       "  }\n",
       "\n",
       "  .colab-df-spinner {\n",
       "    border: 2px solid var(--fill-color);\n",
       "    border-color: transparent;\n",
       "    border-bottom-color: var(--fill-color);\n",
       "    animation:\n",
       "      spin 1s steps(1) infinite;\n",
       "  }\n",
       "\n",
       "  @keyframes spin {\n",
       "    0% {\n",
       "      border-color: transparent;\n",
       "      border-bottom-color: var(--fill-color);\n",
       "      border-left-color: var(--fill-color);\n",
       "    }\n",
       "    20% {\n",
       "      border-color: transparent;\n",
       "      border-left-color: var(--fill-color);\n",
       "      border-top-color: var(--fill-color);\n",
       "    }\n",
       "    30% {\n",
       "      border-color: transparent;\n",
       "      border-left-color: var(--fill-color);\n",
       "      border-top-color: var(--fill-color);\n",
       "      border-right-color: var(--fill-color);\n",
       "    }\n",
       "    40% {\n",
       "      border-color: transparent;\n",
       "      border-right-color: var(--fill-color);\n",
       "      border-top-color: var(--fill-color);\n",
       "    }\n",
       "    60% {\n",
       "      border-color: transparent;\n",
       "      border-right-color: var(--fill-color);\n",
       "    }\n",
       "    80% {\n",
       "      border-color: transparent;\n",
       "      border-right-color: var(--fill-color);\n",
       "      border-bottom-color: var(--fill-color);\n",
       "    }\n",
       "    90% {\n",
       "      border-color: transparent;\n",
       "      border-bottom-color: var(--fill-color);\n",
       "    }\n",
       "  }\n",
       "</style>\n",
       "\n",
       "  <script>\n",
       "    async function quickchart(key) {\n",
       "      const quickchartButtonEl =\n",
       "        document.querySelector('#' + key + ' button');\n",
       "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
       "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
       "      try {\n",
       "        const charts = await google.colab.kernel.invokeFunction(\n",
       "            'suggestCharts', [key], {});\n",
       "      } catch (error) {\n",
       "        console.error('Error during call to suggestCharts:', error);\n",
       "      }\n",
       "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
       "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
       "    }\n",
       "    (() => {\n",
       "      let quickchartButtonEl =\n",
       "        document.querySelector('#df-ce4721e0-24ef-4705-950f-59409312a510 button');\n",
       "      quickchartButtonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "    })();\n",
       "  </script>\n",
       "</div>\n",
       "\n",
       "    </div>\n",
       "  </div>\n"
      ],
      "text/plain": [
       "           SourceIP  DestinationIP    SourcePort  DestinationPort  \\\n",
       "count  84600.000000   84600.000000  84600.000000     84600.000000   \n",
       "mean      -0.001361       0.004459     -0.004863        -0.007567   \n",
       "std        1.001086       1.003272      1.002116         1.002699   \n",
       "min       -4.295391      -4.465604     -4.829436        -4.413886   \n",
       "25%       -0.676920      -0.670082     -0.684160        -0.683350   \n",
       "50%       -0.002316       0.002619     -0.005130        -0.003860   \n",
       "75%        0.670061       0.682693      0.671370         0.664164   \n",
       "max        3.859376       4.611257      4.004674         4.479084   \n",
       "\n",
       "           Protocol     BytesSent  BytesReceived   PacketsSent  \\\n",
       "count  84600.000000  84600.000000   84600.000000  84600.000000   \n",
       "mean       0.004002     -0.001145      -0.002120     -0.000419   \n",
       "std        0.996825      0.999653       0.999598      0.997631   \n",
       "min       -3.997015     -4.164295      -4.462969     -4.319465   \n",
       "25%       -0.664569     -0.674570      -0.678847     -0.677309   \n",
       "50%        0.004968     -0.004721       0.001693      0.002775   \n",
       "75%        0.677522      0.672753       0.677339      0.675245   \n",
       "max        4.526784      4.065773       4.153257      4.678949   \n",
       "\n",
       "       PacketsReceived      Duration  \n",
       "count     84600.000000  84600.000000  \n",
       "mean          0.001752      0.000294  \n",
       "std           1.000847      0.999112  \n",
       "min          -3.984321     -4.157734  \n",
       "25%          -0.673542     -0.680239  \n",
       "50%           0.001601      0.001043  \n",
       "75%           0.677838      0.673449  \n",
       "max           3.989945      4.289893  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 423
    },
    "id": "Ttlw76LD6Ghr",
    "outputId": "4d41be9f-8dec-4531-b328-96fe1c933510"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proportion of Minority Class: 0.52%\n"
     ]
    }
   ],
   "source": [
    "class_division = [\n",
    "    df[df['IsAnomaly'] == 0].shape[0],\n",
    "    df[df['IsAnomaly'] == 1].shape[0]\n",
    "]\n",
    "my_labels = ['Majority Class','Minority Class']\n",
    "plt.pie(class_division, labels = my_labels,autopct='%1.2f%%')\n",
    "plt.show()\n",
    "print(\"Proportion of Minority Class: \" + str(round(df[df['IsAnomaly'] == 1 ].shape[0]/df.shape[0] * 100, 2)) + \"%\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "id": "h8IEDufV6GlM"
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import GradientBoostingClassifier, AdaBoostClassifier\n",
    "from sklearn.model_selection import GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "id": "9gNNX5dQ6GpC"
   },
   "outputs": [],
   "source": [
    "features = df.drop('IsAnomaly', axis=1)\n",
    "labels = df['IsAnomaly']\n",
    "\n",
    "# Split data into train (60%), validation (20%), and test (20%)\n",
    "X_train, X_temp, y_train, y_temp = train_test_split(features, labels, test_size=0.4, random_state=42, stratify=labels)\n",
    "X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "A75jz_evCP6f",
    "outputId": "7b662072-70e5-4582-a7a2-14125f1a7e28"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6\n",
      "0.2\n",
      "0.2\n"
     ]
    }
   ],
   "source": [
    "for dataset in [y_train, y_val, y_test]:\n",
    "    print(round(len(dataset) / len(labels), 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "rlGisVHz6Gs8",
    "outputId": "18a0b255-d966-4b5c-dcfb-33259e3a0753"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proportion of Minority Class in train set: 0.52%\n",
      "Proportion of Minority Class in test set: 0.53%\n",
      "Proportion of Minority Class in validation set: 0.53%\n"
     ]
    }
   ],
   "source": [
    "print(\"Proportion of Minority Class in train set: \" + str(round(y_train.sum() / len(y_train) * 100, 2)) + \"%\")\n",
    "print(\"Proportion of Minority Class in test set: \" + str(round(y_test.sum() / len(y_test) * 100, 2)) + \"%\")\n",
    "print(\"Proportion of Minority Class in validation set: \" + str(round(y_val.sum() / len(y_val) * 100, 2)) + \"%\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ln5MnPns6Gw3",
    "outputId": "22168d55-5ba4-4554-8e83-3901be25d26c"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The X_train shape:  (50760, 10)\n",
      "The X_test shape:  (16920, 10)\n",
      "The X_val shape:  (16920, 10)\n"
     ]
    }
   ],
   "source": [
    "print(\"The X_train shape: \", X_train.shape)\n",
    "print(\"The X_test shape: \", X_test.shape)\n",
    "print(\"The X_val shape: \", X_val.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "id": "JZozfz5HCXfr"
   },
   "outputs": [],
   "source": [
    "from imblearn.over_sampling import ADASYN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 452
    },
    "id": "yZqL94uSCYet",
    "outputId": "7362ab78-ba2c-4d62-8b46-10286b864695"
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAgMAAAGiCAYAAAB6c8WBAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABK80lEQVR4nO3dd3hUVeI+8HdmMiWVVAghIaElhA4RRHqJIkSKWBGFUEQFLIiube2yq6uifEUUVg3sKoJI2x+g9KKAkNACoYSSBNJDep92f38gozEBEkjuuTPzfp4nj2bmzp13Qso75557rkqSJAlERETktNSiAxAREZFYLANEREROjmWAiIjIybEMEBEROTmWASIiIifHMkBEROTkWAaIiIicHMsAERGRk2MZICIicnIsA0QKFhYWhtjYWNExruvs2bO466670KxZM6hUKqxbt65R9hsbG4uwsLBG2RcRXR/LANmNpUuXQqVS2T4MBgPCw8Mxe/Zs5OTkiI530/bt24e33noLRUVFoqPclMmTJ+P48eOYN28e/vvf/+K222677vYlJSV4++230b17d3h4eMDV1RVdunTBSy+9hMzMTJlSE9GfuYgOQNRQ77zzDtq0aYOqqir8+uuv+OKLL7Bp0yacOHECbm5uouM12L59+/D2228jNjYW3t7eNe47c+YM1GrldvbKykrs378fr732GmbPnn3D7S9cuIDo6GhcvHgRDzzwAGbMmAGdTofExER8/fXXWLt2LZKTk2VITkR/xjJAdmfkyJG2d5/Tp0+Hn58f5s+fj/Xr12PChAl1Pqa8vBzu7u5yxryh+mTS6/Uypbk5eXl5AFCrxNTFbDZj/PjxyMnJwa5duzBgwIAa98+bNw8ffPBBU8QkohtQ7lsOonoaNmwYACAlJQXAlWPNHh4eOH/+PEaNGgVPT09MnDgRwJU/wHPnzkVISAj0ej0iIiLw0Ucf4a8X71SpVJg9eza+++47REREwGAwICoqCnv27Kn1/EeOHMHIkSPh5eUFDw8PDB8+HL/99luNba4e4ti9ezdmzpyJ5s2bIzg4GG+99RZefPFFAECbNm1sh0BSU1MB1D1n4MKFC3jggQfg6+sLNzc39O3bFxs3bqyxza5du6BSqfDDDz9g3rx5CA4OhsFgwPDhw3Hu3Ll6fV1v9LreeusthIaGAgBefPFFqFSq6x7jX716NY4dO4bXXnutVhEAAC8vL8ybN++6mT766CP069cPfn5+cHV1RVRUFH788cda223duhUDBgyAt7c3PDw8EBERgVdffbXGNp999hk6d+4MNzc3+Pj44LbbbsPy5ctrbJORkYGpU6eiRYsW0Ov16Ny5M7755ptaz1effREpGUcGyO6dP38eAODn52e7zWw2Y8SIERgwYAA++ugjuLm5QZIkjBkzBjt37sS0adPQo0cPbN68GS+++CIyMjLwySef1Njv7t27sXLlSjzzzDPQ6/VYtGgR7r77bhw8eBBdunQBACQlJWHgwIHw8vLC3/72N2i1WixevBhDhgzB7t27cfvtt9fY58yZMxEQEIA33ngD5eXlGDlyJJKTk/H999/jk08+gb+/PwAgICCgzteak5ODfv36oaKiAs888wz8/PywbNkyjBkzBj/++CPuvffeGtu///77UKvVeOGFF1BcXIx//etfmDhxIg4cOHDdr2l9Xtf48ePh7e2NOXPmYMKECRg1ahQ8PDyuuc///e9/AIDHHnvsus99PQsWLMCYMWMwceJEGI1GrFixAg888AA2bNiAmJgYW/Z77rkH3bp1wzvvvAO9Xo9z585h7969tv38+9//xjPPPIP7778fzz77LKqqqpCYmIgDBw7gkUceAXDla923b19bMQwICMBPP/2EadOmoaSkBM8991y990WkeBKRnYiLi5MASNu2bZPy8vKkS5cuSStWrJD8/PwkV1dXKT09XZIkSZo8ebIEQHr55ZdrPH7dunUSAOm9996rcfv9998vqVQq6dy5c7bbAEgApISEBNttaWlpksFgkO69917bbePGjZN0Op10/vx5222ZmZmSp6enNGjQoFrZBwwYIJnN5hrP/+GHH0oApJSUlFqvOTQ0VJo8ebLt8+eee04CIP3yyy+220pLS6U2bdpIYWFhksVikSRJknbu3CkBkCIjI6Xq6mrbtgsWLJAASMePH6/9Bf6T+r6ulJQUCYD04YcfXnd/kiRJPXv2lJo1a3bD7a6aPHmyFBoaWuO2ioqKGp8bjUapS5cu0rBhw2y3ffLJJxIAKS8v75r7Hjt2rNS5c+frPv+0adOkli1bSpcvX65x+8MPPyw1a9bMlqU++yJSOh4mILsTHR2NgIAAhISE4OGHH4aHhwfWrl2LVq1a1djuqaeeqvH5pk2boNFo8Mwzz9S4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n3/+eUyfPh3R0dF4//33cf78+ZvOQXQrWAaI6LqmTp2KpUuXYtmyZZg6dWq9H/fX4W6VSnXNSwpfS12rMNaHTqfDpEmTEBcXB6PRiOXLl183e3h4OIA/rvFQXytWrMALL7yAadOmYcuWLTh69CimTJlim+wIXDk8sX//fvTr1w8rV65EeHg4fvvtNwDAW2+9haSkJMTExGDHjh3o1KmTrcAQyYllgIiu6+6774bRaITJZKp1qeibFRkZiWPHjqG8vNx22969e6FWq+u8dPL1aLXaGtcruGr69OnYtm0bFi1aBLPZjPHjx19zHz169ECnTp3w8ccf11lYrnXdiL1796Jfv36YOXMmevbsifbt29f57r5nz5545ZVXsG/fPnTp0gXLly+33RceHo45c+Zgy5YtGD9+fK25DkRyYBkgouvSaDQ4deoUTp48ec1LIjfUxIkTYTAYMHnyZJw4cQI7d+7E008/jcceewwtWrRo0L7CwsKwfft2ZGdno7Cw0HZ7ZGQk+vbti5deegkTJky47uWjVSoV4uLikJycjIEDB2LTpk24cOECEhMTMW/ePIwdO7bOx3Xo0AEJCQnYvHkzkpOT8frrr9smNQJASkoKXnnlFezfvx9paWnYsmULzp49i8jISFRWVmL27NnYtWsX0tLSsHfvXsTHxyMyMrJBr5+oMbAMENENeXl53dSVCq/Fzc0NmzdvRkFBAXr37o37778fw4cPv6nTOT/++GNs3boVISEhtU55nDZtGoxGY70Ob/Tp0wcJCQlo3749Hn/8cURGRmLMmDFISkq65oqHTzzxBMaPH4+HHnoIt99+O/Lz8zFz5swar/P06dO47777EB4ejhkzZmDWrFl44oknoNFokJ+fj0mTJiE8PBwPPvggRo4cWeNCWERy4bUJiMhhvfvuu1i1alWNqxoSUW0cGSAih1NWVoYTJ05g4cKFePrpp0XHIVI8lgEicjizZ89GVFQUhgwZ0qAzIIicFQ8TEBEROTmODBARETk5lgEiIiInxzJARETk5FgGiIiInBzLABERkZNjGSAiInJyLANEREROjmWAiIjIybmIDkBEt67abEFuSTVyS6uRV1qNkioTyqvNVz6Mlt////f/Gs0wmq2QJMAqSZAArNa+CajUVz40LoBGh2M+d+Gb0j5w1WrgqtPAXecCbzctfN118HXXwc9dD18P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ZPLkydLYsWOl3NxcSa/XS6mpqVJqaqpkMBikvLw8aezYsdLkyZOv+fi8vDwJgHT8+HHbbQCktWvXSpIkSUuWLJF8fHyksrIy2/0bN26U1Gq1lJ2dbcvQokULqbq6usa+Q0NDpU8++aTO/V61cuVKycfHR6qqqpIkSZIOHTokqVQqKSUlpc68K1eulABIhw8fvu7XJSUlRQIgHTly5JrbzJo1S7rvvvskSZKk/Px8CYC0a9euOrf19PSUli5det3nJCLnxpEBEi4gIAAxMTFYunQp4uLiEBMTA39//1rbnT17FhMmTEDbtm3h5eVlG76/ePFinfs9deoUunfvDnd3d9tt/fv3h9VqxZkzZ2y3de3aFTqdrsG5x40bB41Gg7Vr1wIAli5diqFDh9py/ZUkSQ1+jqs+//xzREVFISAgAB4eHliyZIntdfv6+iI2NhYjRozA6NGjsWDBAmRlZdke+/zzz2P69OmIjo7G+++/X+vQChERywApwtSpU7F06VIsW7YMU6dOrXOb0aNHo6CgAP/+979x4MABHDhwAMAfk/5u1p/LQkPodDpMmjQJcXFxMBqNWL58+TWzA0B4eDgA4PTp0w16nhUrVuCFF17AtGnTsGXLFhw9ehRTpkyp8brj4uKwf/9+9OvXDytXrkR4eDh+++03AMBbb72FpKQkxMTEYMeOHejUqZOtwBARASwDpBB33303jEYjTCYTRowYUev+/Px8nDlzBn//+98xfPhwREZGorCw8Lr7jIyMxLFjx1BeXm67be/evVCr1baJgvWl1WphsVhq3T59+nRs27YNixYtgtlsxvjx46+5jx49eqBTp074+OOP65znUFRUVOfj9u7di379+mHmzJno2bMn2rdvX+e7+549e+KVV17Bvn370KVLFyxfvtx2X3h4OObMmYMtW7Zg/PjxteY6EJFzYxkgRdBoNDh16hROnjwJjUZT634fHx/4+flhyZIlOHfuHHbs2IHnn3/+uvucOHEiDAYDJk+ejBMnTmDnzp14+umn8dhjj6FFixYNyhcWFobt27cjOzu7RgmJjIxE37598dJLL2HChAlwdXW95j5UKhXi4uKQnJyMgQMHYtOmTbhw4QISExMxb948jB07ts7HdejQAQkJCdi8eTOSk5Px+uuv2yY1AkBKSgpeeeUV7N+/H2lpadiyZQvOnj2LyMhIVFZWYvbs2di1axfS0tKwd+9exMfHIzIyskGvn4gcG8sAKYaXlxe8vLzqvE+tVmPFihU4dOgQunTpgjlz5uDDDz+87v7c3NywefNmFBQUoHfv3rj//vsxfPhwLFy4sMHZPv74Y2zduhUhISG1TnmcNm0ajEbjdQ8RXNWnTx8kJCSgffv2ePzxxxEZGYkxY8YgKSnpmisePvHEExg/fjweeugh3H777cjPz8fMmTNrvM7Tp0/jvvvuQ3h4OGbMmIFZs2bhiSeegEajQX5+PiZNmoTw8HA8+OCDGDlyJN5+++0Gfw2IyHGppFuZ1USkINXV1TAYDNi6dSuio6Nle953330Xq1atQmJiomzPSUTUmFxEByBqDCUlJVizZg3UajU6duwoy3OWlZUhNTUVCxcuxHvvvSfLcxIRNQUeJiCH8Oabb+Kll17CBx98gODgYFmec/bs2YiKisKQIUPqdYiAiEipeJiAiIjIyXFkgIiIyMmxDBARETk5lgEiIiInxzJARETk5FgGiIiInBzLABERkZNjGSAiInJyLANERERO7v8D/0b6WzR930QAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proportion of Minority Class: 0.52%\n"
     ]
    }
   ],
   "source": [
    "class_division_train = [np.sum(y_train == 0), np.sum(y_train == 1)]\n",
    "\n",
    "plt.pie(class_division_train, labels=my_labels, autopct='%1.1f%%', startangle=90)\n",
    "plt.title('Proportion of Classes')\n",
    "plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.\n",
    "plt.show()\n",
    "\n",
    "print(\"Proportion of Minority Class: \" + str(round(np.sum(y_train == 1) / len(y_train) * 100, 2)) + \"%\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "id": "uDFmXS5_CYiM"
   },
   "outputs": [],
   "source": [
    "adasyn = ADASYN(sampling_strategy='auto', random_state=42, n_neighbors=5)\n",
    "X_resampled, y_resampled = adasyn.fit_resample(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "3YvlyInlCYld",
    "outputId": "13dd897c-768e-46ea-8794-b32b07387c21"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proportion of Minority Class in train set after resampling: 50.05%\n"
     ]
    }
   ],
   "source": [
    "print(\"Proportion of Minority Class in train set after resampling: \" + str(round((len(y_resampled) - y_resampled.sum()) / len(y_resampled) * 100, 2)) + \"%\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 480
    },
    "id": "E6AHW4Z5CYo7",
    "outputId": "1b63eafe-5a8c-45e9-db9f-f0047136b304"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proportion of Minority Class: 50.05%\n",
      "Shape of Resampled X:  (100882, 10)\n",
      "Shape of Resampled y:  (100882,)\n"
     ]
    }
   ],
   "source": [
    "class_division_train_resampled = [np.sum(y_resampled == 1), np.sum(y_resampled == 0)]\n",
    "\n",
    "plt.pie(class_division_train_resampled, labels=my_labels, autopct='%1.1f%%', startangle=90)\n",
    "plt.title('Proportion of Classes')\n",
    "plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.\n",
    "plt.show()\n",
    "\n",
    "print(\"Proportion of Minority Class: \" + str(round(np.sum(y_resampled == 0) / len(y_resampled) * 100, 2)) + \"%\")\n",
    "print(\"Shape of Resampled X: \", X_resampled.shape)\n",
    "print(\"Shape of Resampled y: \", y_resampled.shape)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5m7Qhw-FcuGn"
   },
   "source": [
    "**BOOSTING METHOD**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "id": "m5WwC2FmCYzb"
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV\n",
    "from sklearn.ensemble import GradientBoostingClassifier\n",
    "import joblib\n",
    "from sklearn.metrics import classification_report, accuracy_score\n",
    "\n",
    "# Create a Gradient Boosting Classifier\n",
    "gbc = GradientBoostingClassifier()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "_hHbl0jmb9QH",
    "outputId": "b5ace6ef-2325-496b-9682-8df37593edc3"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Parameters for Gradient Boosting: {'learning_rate': 0.2, 'max_depth': 5, 'n_estimators': 150}\n"
     ]
    }
   ],
   "source": [
    "# Define the parameter grid for grid search\n",
    "param_grid_gbc = {\n",
    "    'n_estimators': [50, 100, 150],\n",
    "    'learning_rate': [0.01, 0.1, 0.2],\n",
    "    'max_depth': [3, 4, 5]\n",
    "}\n",
    "\n",
    "# Create the GridSearchCV object\n",
    "grid_search_gbc = GridSearchCV(estimator=gbc, param_grid=param_grid_gbc, scoring='accuracy', cv=3)\n",
    "\n",
    "# Perform grid search on the resampled training data\n",
    "grid_search_gbc.fit(X_resampled, y_resampled)\n",
    "\n",
    "# Print the best parameters found by grid search\n",
    "print(\"Best Parameters for Gradient Boosting:\", grid_search_gbc.best_params_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "kB_LoFfwCY2-",
    "outputId": "885f8fe3-eaa8-4105-9361-3d3c5cce7233"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Gradient Boosting): 90.73%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       1.00      0.91      0.95     16831\n",
      "        True       0.01      0.15      0.02        89\n",
      "\n",
      "    accuracy                           0.91     16920\n",
      "   macro avg       0.50      0.53      0.48     16920\n",
      "weighted avg       0.99      0.91      0.95     16920\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the best model from the grid search\n",
    "adasyn_gbc_model = grid_search_gbc.best_estimator_\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(adasyn_gbc_model, 'adasyn_gradient_boosting_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "adasyn_gbc_predictions = adasyn_gbc_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Gradient Boosting): {:.2f}%\".format(accuracy_score(y_val, adasyn_gbc_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, adasyn_gbc_predictions))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "fePBVGUdczKG"
   },
   "source": [
    "RANDOM FOREST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "id": "HNP4-T6rCY6w"
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "import joblib\n",
    "from sklearn.metrics import classification_report, accuracy_score\n",
    "\n",
    "# Define the Random Forest Classifier\n",
    "rfc = RandomForestClassifier()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "5hshDaqwdBA5",
    "outputId": "fd2b24ae-791c-4399-db90-59679b14f5d6"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Parameters for Random Forest: {'max_depth': None, 'min_samples_split': 5, 'n_estimators': 50}\n"
     ]
    }
   ],
   "source": [
    "# Define the parameter grid for grid search\n",
    "param_grid_rfc = {\n",
    "    'n_estimators': [50, 100, 150],\n",
    "    'max_depth': [None, 5, 10],\n",
    "    'min_samples_split': [2, 5, 10]\n",
    "}\n",
    "\n",
    "# Create the GridSearchCV object\n",
    "grid_search_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid_rfc, scoring='accuracy', cv=3)\n",
    "\n",
    "# Perform grid search on the resampled training data\n",
    "grid_search_rfc.fit(X_resampled, y_resampled)\n",
    "\n",
    "# Print the best parameters found by grid search\n",
    "print(\"Best Parameters for Random Forest:\", grid_search_rfc.best_params_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "C-dMJxURCY-I",
    "outputId": "c04c3eb7-4533-4c5e-80a7-1cb1c67235b8"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Random Forest): 99.26%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       0.99      1.00      1.00     16831\n",
      "        True       0.00      0.00      0.00        89\n",
      "\n",
      "    accuracy                           0.99     16920\n",
      "   macro avg       0.50      0.50      0.50     16920\n",
      "weighted avg       0.99      0.99      0.99     16920\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the best model from the grid search\n",
    "adasyn_rfc_model = grid_search_rfc.best_estimator_\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(adasyn_rfc_model, 'adasyn_random_forest_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "adasyn_rfc_predictions = adasyn_rfc_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Random Forest): {:.2f}%\".format(accuracy_score(y_val, adasyn_rfc_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, adasyn_rfc_predictions))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Mcl30QZtdfcR"
   },
   "source": [
    "**Stacking**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {
    "id": "7qeUtysldkEB"
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import GridSearchCV\n",
    "from sklearn.ensemble import StackingClassifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "import joblib\n",
    "from sklearn.metrics import classification_report, accuracy_score\n",
    "\n",
    "# Define base models\n",
    "base_models_stack = [('rfc', RandomForestClassifier()),\n",
    "                     ('gbc', GradientBoostingClassifier())]\n",
    "\n",
    "# Define the meta-classifier\n",
    "meta_model_stack = LogisticRegression()\n",
    "\n",
    "# Create the stacking classifier\n",
    "stack_model = StackingClassifier(estimators=base_models_stack, final_estimator=meta_model_stack)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ivqbfVtfdkmS",
    "outputId": "3237bee6-ab85-4b63-8f4e-1cfadde0a28a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Parameters for Stacking: {'final_estimator__C': 1, 'final_estimator__penalty': 'l2', 'final_estimator__solver': 'liblinear'}\n"
     ]
    }
   ],
   "source": [
    "# Define the parameter grid for grid search\n",
    "param_grid_stack = {\n",
    "    'final_estimator__C': [0.1, 1, 10],\n",
    "    'final_estimator__penalty': ['l1', 'l2'],\n",
    "    'final_estimator__solver': ['liblinear']\n",
    "}\n",
    "\n",
    "# Create the GridSearchCV object\n",
    "grid_search_stack = GridSearchCV(estimator=stack_model, param_grid=param_grid_stack, scoring='accuracy', cv=3)\n",
    "\n",
    "# Perform grid search on the resampled training data\n",
    "grid_search_stack.fit(X_resampled, y_resampled)\n",
    "\n",
    "# Print the best parameters found by grid search\n",
    "print(\"Best Parameters for Stacking:\", grid_search_stack.best_params_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "y6WlXi0adkp0",
    "outputId": "c231c2ee-a3f9-4673-d2c7-cd0bc75a2f0c"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Stacking): 95.33%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       0.99      0.96      0.98     16831\n",
      "        True       0.00      0.03      0.01        89\n",
      "\n",
      "    accuracy                           0.95     16920\n",
      "   macro avg       0.50      0.50      0.49     16920\n",
      "weighted avg       0.99      0.95      0.97     16920\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the best model from the grid search\n",
    "adasyn_stack_model = grid_search_stack.best_estimator_\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(adasyn_stack_model, 'adasyn_stacking_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "adasyn_stack_predictions = adasyn_stack_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Stacking): {:.2f}%\".format(accuracy_score(y_val, adasyn_stack_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, adasyn_stack_predictions))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {
    "id": "sK8zGHshdktS"
   },
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "from sklearn.metrics import classification_report, accuracy_score, confusion_matrix\n",
    "import joblib\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Evaluate the model performance on the validation set\n",
    "def evaluate_model(model, X_val, y_val, model_name):\n",
    "    predictions = model.predict(X_val)\n",
    "\n",
    "    # Accuracy\n",
    "    accuracy = accuracy_score(y_val, predictions)\n",
    "    print(f\"Accuracy on Validation Set ({model_name}): {accuracy:.2f}%\")\n",
    "\n",
    "    # Confusion Matrix\n",
    "    cm = confusion_matrix(y_val, predictions)\n",
    "    plt.figure(figsize=(6, 6))\n",
    "    sns.heatmap(cm, annot=True, fmt=\"d\", cmap=\"Blues\", cbar=False)\n",
    "    plt.title(f\"Confusion Matrix ({model_name})\")\n",
    "    plt.xlabel(\"Predicted\")\n",
    "    plt.ylabel(\"True\")\n",
    "    plt.show()\n",
    "\n",
    "    # Classification Report\n",
    "    print(f\"Classification Report ({model_name}):\\n{classification_report(y_val, predictions)}\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "ByyoReuUdkxD",
    "outputId": "49cff89e-51ab-48b4-c902-4316d6e3a46c"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Gradient Boosting): 0.91%\n"
     ]
    },
    {
     "data": {
      "image/png": "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fHxUvnx51/rrPeZDQ0Nd651Op9566y19/fXXKlasmCIiIvT222/r2LFjN3Usd9xxh1vMSen/L/jtt99UoUKFdOMy+x6Rrjzmrh2PnEFAwE1gYKBKliypbdu2Wd0uq9+wnp6eGS6/9geNzT6ufQ28n5+f1qxZo+XLl+vJJ5/UL7/8oscff1yNGjXK1tfL38yxpHE6nWrXrp1mzpyphQsXZnr2QbryvgEDBgxQRESEZs+erW+//VbLli3TnXfemeUzLZKsX7mwefNmnThxQpJcP6RupHDhwpLS/8AMDQ2VpHSPLy8vL9cPxrCwsCzPe//+/WrQoIFiY2M1evRoffnll1q2bJn69+8vSVb3S2bStjFy5EhX5Fz7ce0Zlex4bGRVgwYNJElr1qzJ9m2n6devn/bs2aPo6Gj5+vpq6NChqlq1qjZv3vynt5lT99GZM2dUpEiRm9oGsoaAQDotWrTQ/v37tX79+huODQkJUWpqquu3tDTHjx/X2bNnFRISkm3zKliwoNuFXWmuPcshXXnpWIMGDTR69Gjt2LFDb7zxhlauXKlVq1ZluO20ee7evTvdul27dqlIkSLy9/e/uQPIRKdOnbR582adP38+wwtP03z22WeqX7++PvjgA3Xo0EGNGzdWw4YN090n2fnbV3x8vLp27aqwsDA988wzevvtt/XTTz/d8HZlypSRn5+fDh486La8SpUqqlSpkhYtWpSlixdv5IsvvlBiYqIWL16snj176pFHHlHDhg3TxUba1/fax+nJkydveFagQoUKkq7EdVrkXPvh7e1tPffs+jpdvnxZ0v/O6mT2WE5KStLBgwdd66/3mN+9e3e6790KFSpo4MCBWrp0qbZt26akpCSNGjUq24/naiEhIdq/f3+6qNi3b1+G4y9fvqzff/9dVatWzfa5ID0CAun861//kr+/v7p3757hOwLu379f48aNk3TlFLykdK+UGD16tKQrz6dmlwoVKiguLk6//PKLa1lMTIwWLlzoNu706dPpbpt2xX5iYmKG2y5RooSqV6+umTNnuv1A3rZtm5YuXeo6zpxQv359vfbaa5o4caKKFy+e6ThPT890/5F++umnOnLkiNuytNDJKLZsDR48WIcPH9bMmTM1evRolS1bVpGRkZnej2m8vb1Vq1Ytbdy4Md264cOHKzY2Vj169HB7RUAam99A036Lvfo2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tsw4nU4zaNAgExkZaYoVK2YSExNd42fNmmWqVKliUlNTXcsSExONn5+f+fbbb40xxpQoUcK8/fbbrvXJycnmjjvucO3HGGPq1q1r+vbta4wxZvfu3UaSWbZsWYZzXLVqlZFkzpw541p26dIlky9fPvPDDz+4je3WrZvp2LGjMcaYIUOGmLCwMLf1gwcPTrctADeHayCA29SSJUuUP39+JScnKzU1VZ06ddLw4cPVu3dv3X333W7XPWzdulX79u1TQECA2zYuXbqk/fv3Ky4uTjExMQoPD3et8/LyUq1atdI9jZFmy5Yt8vT0VN26dbM853379ikhIUGNGjVyW56UlKR7771XkrRz5063eUjSAw88kOV9AMgaAgK4TdWvX19TpkyRj4+PSpYsKS+v//134O/v7zb2woULqlmzpubMmZNuO8HBwX9q/35+fta3uXDhgiTpyy+/VKlSpdzWOZ3OPzUPAH8OAQHcpvz9/VWxYsUsja1Ro4bmzZunokWLKjAwMMMxJUqU0H//+19FRERIki5fvqyff/5ZNWrUyHD83XffrdTUVH333Xdq2LBhuvVpZ0BSUlJcy8LCwuR0OnX48OFMz1xUrVpVixcvdlv2448/3vggAVjhIkoAN/TEE0+oSJEiat26tdauXauDBw9q9erV6tOnj/744w9JUt++ffXvf/9bixYt0q5du9SrV6/rvodD2bJlFRkZqaefflqLFi1ybfOTTz6RJIWEhMjhcGjJkiU6efKkLly4oICAAA0aNEj9+/fXzJkztX//fm3atEkTJkzQzJkzJUnPPvus9u7dqxdeeEG7d+/W3LlzNWPGjJy+i4DbDgEB4Iby5cunNWvWqEyZMmrXrp2qVq2qbt266dKlS64zEgMHDtSTTz6pyMhIPfDAAwoICFDbtm2vu90pU6boscceU69evRQaGqoePXooPj5eklSqVCmNGDFCL774oooVK6Z//vOfkqTXXntNQ4cOVXR0tKpWraqmTZvqyy+/VLly5SRJZcqU0fz587Vo0SJVq1ZNU6dO1ZtvvpmD9w5we3KYzK5wAgAAyARnIAAAgDUCAgAAWCMgAACANQICAABYIyAAAIA1AgIAAFgjIAAAgDUCAgAAWCMgAACANQICAABYIyAAAIC1/wcJLeImYFLmqAAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report (Gradient Boosting):\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "       False       1.00      0.91      0.95     16831\n",
      "        True       0.01      0.15      0.02        89\n",
      "\n",
      "    accuracy                           0.91     16920\n",
      "   macro avg       0.50      0.53      0.48     16920\n",
      "weighted avg       0.99      0.91      0.95     16920\n",
      "\n",
      "Accuracy on Validation Set (Random Forest): 0.99%\n"
     ]
    },
    {
     "data": {
      "image/png": "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q+qtt97KcJm0+Mmu19TZs2fTxRtyD45A4La1bt1a+/btU1xc3E3nDQkJkcPh0N69e12mHz9+XOfOnXNeUZEdChQokO7scin9O0FJ8vDwUJMmTfTWW29px44deuWVV7Ry5UrnIdnrpY1z9+7d6W7btWuXChcurHz58t3eDmTi8ccf1+bNm3XhwgV16dIl0/k+//xzNW7cWDNmzFCXLl3UrFkzRUREpLtPsvMdXmJionr06KGwsDD16dNH48eP14YNG266XKlSpeTr66sDBw5kaTvBwcEaMmSIvv76a/3888/O6Z9//rkiIyM1YcIEdezYUU2bNlX9+vUzfB5kRdrjfP3z9eTJk+liJyQkJNPnw7XrcpfMnrPJyck6cOBAlsZXtmxZnTlzRk2aNEl3pCMiIsLl6MbNXlM3e979/fffOnz4sPMIDnIfAgK37fnnn1e+fPnUu3dvHT9+PN3t+/bt06RJkyRdPQQvSW+//bbLPGnvaB555JFsG1fZsmWVkJCg3377zTnt6NGj6a70OHPmTLpl036xTWaXzwUHB6t69eqKjY11+eH0+++/a9myZc79vBMaN26ssWPH6p133lGxYsUync/T0zPdu9bPPvtMR44ccZmWFjq3+kP2Wi+88IL++OMPxcbG6q233lJoaKgiIyNvehmil5eXateurV9//TXL2xo4cKDy5s2r1157zTkto32eMmVKuqNOWRURESEvLy9NmTLFZb3XP3+lq8/t9evXu4R0YmKi3n//fYWGhiosLOyWxpBdIiIi5O3trcmTJ7vsy4wZM5SQkJCl117nzp115MgRffDBB+luu3z5svNju6y8pm72vNuxY4euXLmS5au7kPP4CAO3rWzZsvr000/12GOPqVKlSi6/ifKnn37SZ5995vybAdWqVVNkZKTef/99nTt3Tg0bNtT69esVGxurdu3aqXHjxtk2ri5duuiFF15Q+/bt9eyzz+rSpUuaNm2aypcv73JC3ZgxY/Tjjz/qkUceUUhIiE6cOKGpU6fqnnvucTkh7npvvPGGWrZsqbp166pXr17OyzgDAgJu+NHC7fLw8NC///3vm87XunVrjRkzRj169FC9evW0bds2zZkzR2XKlHGZr2zZsgoMDNT06dPl7++vfPnyqU6dOipdurTRuFauXKmpU6dq1KhRzstKZ86cqUaNGmnkyJEaP378DZdv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AACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACM2SzLstw9COBGkpKSFBMToxEjRshut7t7OACuwevz7kVAINc7f/68AgIClJCQoPz587t7OACuwevz7sVHGAAAwBgBAQAAjBEQAADAGAGBXM9ut2vUqFGcoAXkQrw+716cRAkAAIxxBAIAABgjIAAAgDECAgAAGCMgAACAMQICudq7776r0NBQ+fj4qE6dOlq/fr27hwRA0o8//qg2bdqoePHistlsWrhwobuHhBxGQCDXmjdvnoYOHapRo0Zp06ZNqlatmpo3b64TJ064e2jAXS8xMVHVqlXTu+++6+6hwE24jBO5Vp06dXT//ffrnXfekSQ5HA6VLFlSAwcO1PDhw908OgBpbDabvvzyS7Vr187dQ0EO4ggEcqXk5GRt3LhRERERzmkeHh6KiIhQXFycG0cGAJAICORSp06dUmpqqooWLeoyvWjRojp27JibRgUASENAAAAAYwQEcqXChQvL09NTx48fd5l+/PhxFStWzE2jAgCkISCQK3l7e6tWrVpasWKFc5rD4dCKFStUt25dN44MACBJedw9ACAzQ4cOVWRkpGrXrq0HHnhAb7/9thITE9WjRw93Dw246128eFHx8fHO7w8cOKAtW7aoYMGCKlWqlBtHhpzCZZzI1d555x298cYbOnbsmKpXr67JkyerTp067h4WcNdbvXq1GjdunG56ZGSkZs2alfMDQo4jIAAAgDHOgQAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAHDHdO/eXe3atXN+36hRIw0ePDjHx7F69WrZbDadO3cux7cN/FMREMBdqHv37rLZbLLZbPL29la5cuU0ZswY/f3333d0u1988YXGjh2bpXn5oQ/kbvwxLeAu1aJFC82cOVNJSUlaunSpBgwYIC8vL40YMcJlvuTkZHl7e2fLNgsWLJgt6wHgfhyBAO5SdrtdxYoVU0hIiPr166eIiAgtWrTI+bHDK6+8ouLFi6tChQqSpMOHD6tz584KDAxUwYIF1bZtWx08eNC5vtTUVA0dOlSBgYEqVKiQnn/+eV3/p3au/wgjKSlJL7zwgkqWLCm73a5y5cppxowZOnjwoPMPNRUoUEA2m03du3eXdPXPusfExKh06dLy9fVVtWrV9Pnnn7tsZ+nSpSpfvrx8fX3VuHFjl3ECyB4EBABJkq+vr5KTkyVJK1as0O7du7V8+XItXrxYKSkpat68ufz9/bVmzRqtW7dOfn5+atGihXOZCRMmaNasWfroo4+0du1anTlzRl9++eUNt/nkk09q7ty5mjx5snbu3Kn33ntPfn5+KlmypBYsWCBJ2r17t44ePapJkyZJkmJiYvTxxx9r+vTp2r59u4YMGaJu3brphx9+kHQ1dDp06KA2bdpoy5Yt6t27t4YPH36n7jbg7mUBuOtERkZabdu2tSzLshwOh7V8+XLLbrdbUVFRVmRkpFW0aFErKSnJOf/s2bOtChUqWA6HwzktKSnJ8vX1tb777jvLsiwrODjYGj9+vPP2lJQU65577nFux7Isq2HDhtagQYMsy7Ks3bt3W5Ks5cuXZzjGVatWWZKss2fPOqdduXLFyps3r/XTTz+5zNurVy+ra9eulmVZ1ogRI6ywsDCX21944YV06wJwezgHArhLLV68WH5+fkpJSZHD4dDjjz+u0aNHa8CAAapatarLeQ9bt25VfHy8/P39XdZx5coV7du3TwkJCTp69Kjq1KnjvC1PnjyqXbt2uo8x0mzZskWenp5q2LBhlsccHx+vS5cuqWnTpi7Tk5OTVaNGDUnSzp07XcYhSXXr1s3yNgBkDQEB3KUaN26sadOmydvbW8WLF1eePP/97yBfvnwu8168eFG1atXSnDlz0q0nKCjolrbv6+trvMzFixclSUuWLFGJEiVcbrPb7bc0DgC3hoAA7lL58uVTuXLlsjRvzZo1NW/ePBUpUkT58+fPcJ7g4GD98ssvatCggSTp77//1saNG1WzZs0M569ataocDod++OEHRUREpLs97QhIamqqc1pYWJjsdrv++OOPTI9cVKpUSYsWLXKZ9vPPP998JwEY4SRKADf1r3/9S4ULF1bbtm21Zs0aHThwQKtXr9azzz6rP//8U5I0aNAgvfbaa1q4cKF27dql/v373/B3OISGhioyMlI9e/bUwoULneucP3++JCkkJEQ2m02LFy/WyZMndfHiRfn7+ysqKkpDhgxRbGys9u3bp02bNmnKlCmKjY2VJPXt21d79+7Vc889p927d+vTTz/VrFmz7vRdBNx1CAgAN5U3b179+OOPKlWqlDp06KBKlSqpV69eunLlivOIxLBhw/TEE08oMjJSdevWlb+/v9q3b3/D9U6bNk0dO3ZU//79VbFiRT311FNKTEyUJJUoUULR0dEaPny4ihYtqmeeeUaSNHbsWI0cOVIxMTGqVKmSWrRooSVLlqh06dKSpFKlSmnBggVauHChqlWrpunTp+vVV1+9g/cOcHeyWZmd4QQAAJAJjkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAY/8PCDs27rBV5AcAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report (Random Forest):\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "       False       0.99      1.00      1.00     16831\n",
      "        True       0.00      0.00      0.00        89\n",
      "\n",
      "    accuracy                           0.99     16920\n",
      "   macro avg       0.50      0.50      0.50     16920\n",
      "weighted avg       0.99      0.99      0.99     16920\n",
      "\n",
      "Accuracy on Validation Set (Stacking): 0.95%\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 600x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report (Stacking):\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "       False       0.99      0.96      0.98     16831\n",
      "        True       0.00      0.03      0.01        89\n",
      "\n",
      "    accuracy                           0.95     16920\n",
      "   macro avg       0.50      0.50      0.49     16920\n",
      "weighted avg       0.99      0.95      0.97     16920\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Evaluate each model on the validation set\n",
    "evaluate_model(adasyn_gbc_model, X_val, y_val, \"Gradient Boosting\")\n",
    "evaluate_model(adasyn_rfc_model, X_val, y_val, \"Random Forest\")\n",
    "evaluate_model(adasyn_stack_model, X_val, y_val, \"Stacking\")"
   ]
  }
 ],
 "metadata": {
  "accelerator": "GPU",
  "colab": {
   "gpuType": "T4",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
