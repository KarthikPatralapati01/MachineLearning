{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 45,
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
   "execution_count": 44,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "sfntUICQ_bL3",
    "outputId": "c2210451-6436-4003-e957-7d0bc7ca6b98"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
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
   "execution_count": 46,
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
   "execution_count": 47,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 226
    },
    "id": "IFWDeTiJ6GHm",
    "outputId": "4cab06f0-5abe-4824-afea-c4c20f013ec3"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "  <div id=\"df-603c9b5b-a2c5-40a5-8636-587c7203422e\" class=\"colab-df-container\">\n",
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
       "      <td>0</td>\n",
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
       "      <td>0</td>\n",
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
       "      <td>0</td>\n",
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
       "      <td>0</td>\n",
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
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>\n",
       "    <div class=\"colab-df-buttons\">\n",
       "\n",
       "  <div class=\"colab-df-container\">\n",
       "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-603c9b5b-a2c5-40a5-8636-587c7203422e')\"\n",
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
       "        document.querySelector('#df-603c9b5b-a2c5-40a5-8636-587c7203422e button.colab-df-convert');\n",
       "      buttonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "\n",
       "      async function convertToInteractive(key) {\n",
       "        const element = document.querySelector('#df-603c9b5b-a2c5-40a5-8636-587c7203422e');\n",
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
       "<div id=\"df-c5153ec4-cb59-472c-b88f-e7e476c28857\">\n",
       "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-c5153ec4-cb59-472c-b88f-e7e476c28857')\"\n",
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
       "        document.querySelector('#df-c5153ec4-cb59-472c-b88f-e7e476c28857 button');\n",
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
       "0       1.579213     0.767435        -0.469474  0.542560          0  \n",
       "1      -1.012831     0.314247        -0.908024 -1.412304          0  \n",
       "2      -1.150994     0.375698        -0.600639 -0.291694          0  \n",
       "3       0.208864    -1.959670        -1.328186  0.196861          0  \n",
       "4      -0.460639     1.057122         0.343618 -1.763040          0  "
      ]
     },
     "execution_count": 47,
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
   "execution_count": 48,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "EhalPUEY6GK4",
    "outputId": "732c5fbf-1d17-4a3d-ec3c-65e93d7964a1"
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
     "execution_count": 48,
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
   "execution_count": 49,
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
   "execution_count": 50,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "lvZLXV6K6GOq",
    "outputId": "4bd653aa-ebd6-4148-ba18-63baf5b899cd"
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
       "IsAnomaly            int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 50,
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
   "execution_count": 51,
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
   "execution_count": 52,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "s8FDUyOq6GVs",
    "outputId": "c9d20629-6ce4-433c-efda-d4927c12e88c"
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
     "execution_count": 52,
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
   "execution_count": 53,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "qEuDQy4j6GZh",
    "outputId": "3e08a3c9-8e5e-4792-b680-de8ecbddf639"
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
     "execution_count": 53,
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
   "execution_count": 54,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 320
    },
    "id": "xIZyv0VS6Gdg",
    "outputId": "40d5cff6-7586-42e1-b97d-8b7071bfba1b"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "  <div id=\"df-b1357cd7-efa8-443f-91f5-78e1b64ca89d\" class=\"colab-df-container\">\n",
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
       "      <td>1000000.000000</td>\n",
       "      <td>1000000.000000</td>\n",
       "      <td>1000000.000000</td>\n",
       "      <td>1000000.000000</td>\n",
       "      <td>1000000.000000</td>\n",
       "      <td>1000000.000000</td>\n",
       "      <td>1000000.000000</td>\n",
       "      <td>1000000.000000</td>\n",
       "      <td>1000000.000000</td>\n",
       "      <td>1000000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>-0.000645</td>\n",
       "      <td>0.000899</td>\n",
       "      <td>-0.002857</td>\n",
       "      <td>0.001966</td>\n",
       "      <td>-0.000958</td>\n",
       "      <td>-0.001099</td>\n",
       "      <td>0.001715</td>\n",
       "      <td>0.000153</td>\n",
       "      <td>0.001019</td>\n",
       "      <td>-0.000832</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.000721</td>\n",
       "      <td>0.999597</td>\n",
       "      <td>1.000583</td>\n",
       "      <td>1.000004</td>\n",
       "      <td>0.999299</td>\n",
       "      <td>1.000560</td>\n",
       "      <td>1.000138</td>\n",
       "      <td>0.999976</td>\n",
       "      <td>0.999260</td>\n",
       "      <td>0.999992</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-4.980146</td>\n",
       "      <td>-4.841791</td>\n",
       "      <td>-4.829436</td>\n",
       "      <td>-4.644419</td>\n",
       "      <td>-4.950266</td>\n",
       "      <td>-4.630858</td>\n",
       "      <td>-4.462969</td>\n",
       "      <td>-4.564944</td>\n",
       "      <td>-5.195261</td>\n",
       "      <td>-4.625258</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>-0.675493</td>\n",
       "      <td>-0.672789</td>\n",
       "      <td>-0.679471</td>\n",
       "      <td>-0.672742</td>\n",
       "      <td>-0.675323</td>\n",
       "      <td>-0.676730</td>\n",
       "      <td>-0.671568</td>\n",
       "      <td>-0.674591</td>\n",
       "      <td>-0.673667</td>\n",
       "      <td>-0.676727</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>-0.000708</td>\n",
       "      <td>-0.000433</td>\n",
       "      <td>-0.003061</td>\n",
       "      <td>0.001888</td>\n",
       "      <td>-0.000974</td>\n",
       "      <td>-0.001224</td>\n",
       "      <td>0.002324</td>\n",
       "      <td>0.000994</td>\n",
       "      <td>0.001513</td>\n",
       "      <td>-0.000485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.672675</td>\n",
       "      <td>0.676014</td>\n",
       "      <td>0.670509</td>\n",
       "      <td>0.676370</td>\n",
       "      <td>0.671899</td>\n",
       "      <td>0.674718</td>\n",
       "      <td>0.677180</td>\n",
       "      <td>0.675133</td>\n",
       "      <td>0.675576</td>\n",
       "      <td>0.673657</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>5.032374</td>\n",
       "      <td>4.984215</td>\n",
       "      <td>4.565550</td>\n",
       "      <td>4.748345</td>\n",
       "      <td>4.920315</td>\n",
       "      <td>5.220045</td>\n",
       "      <td>5.033805</td>\n",
       "      <td>4.827623</td>\n",
       "      <td>4.795172</td>\n",
       "      <td>4.913122</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>\n",
       "    <div class=\"colab-df-buttons\">\n",
       "\n",
       "  <div class=\"colab-df-container\">\n",
       "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b1357cd7-efa8-443f-91f5-78e1b64ca89d')\"\n",
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
       "        document.querySelector('#df-b1357cd7-efa8-443f-91f5-78e1b64ca89d button.colab-df-convert');\n",
       "      buttonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "\n",
       "      async function convertToInteractive(key) {\n",
       "        const element = document.querySelector('#df-b1357cd7-efa8-443f-91f5-78e1b64ca89d');\n",
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
       "<div id=\"df-31985e5f-0eba-4cf7-a36c-66d9342b2851\">\n",
       "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-31985e5f-0eba-4cf7-a36c-66d9342b2851')\"\n",
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
       "        document.querySelector('#df-31985e5f-0eba-4cf7-a36c-66d9342b2851 button');\n",
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
       "             SourceIP   DestinationIP      SourcePort  DestinationPort  \\\n",
       "count  1000000.000000  1000000.000000  1000000.000000   1000000.000000   \n",
       "mean        -0.000645        0.000899       -0.002857         0.001966   \n",
       "std          1.000721        0.999597        1.000583         1.000004   \n",
       "min         -4.980146       -4.841791       -4.829436        -4.644419   \n",
       "25%         -0.675493       -0.672789       -0.679471        -0.672742   \n",
       "50%         -0.000708       -0.000433       -0.003061         0.001888   \n",
       "75%          0.672675        0.676014        0.670509         0.676370   \n",
       "max          5.032374        4.984215        4.565550         4.748345   \n",
       "\n",
       "             Protocol       BytesSent   BytesReceived     PacketsSent  \\\n",
       "count  1000000.000000  1000000.000000  1000000.000000  1000000.000000   \n",
       "mean        -0.000958       -0.001099        0.001715        0.000153   \n",
       "std          0.999299        1.000560        1.000138        0.999976   \n",
       "min         -4.950266       -4.630858       -4.462969       -4.564944   \n",
       "25%         -0.675323       -0.676730       -0.671568       -0.674591   \n",
       "50%         -0.000974       -0.001224        0.002324        0.000994   \n",
       "75%          0.671899        0.674718        0.677180        0.675133   \n",
       "max          4.920315        5.220045        5.033805        4.827623   \n",
       "\n",
       "       PacketsReceived        Duration  \n",
       "count   1000000.000000  1000000.000000  \n",
       "mean          0.001019       -0.000832  \n",
       "std           0.999260        0.999992  \n",
       "min          -5.195261       -4.625258  \n",
       "25%          -0.673667       -0.676727  \n",
       "50%           0.001513       -0.000485  \n",
       "75%           0.675576        0.673657  \n",
       "max           4.795172        4.913122  "
      ]
     },
     "execution_count": 54,
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
   "execution_count": 55,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 423
    },
    "id": "Ttlw76LD6Ghr",
    "outputId": "93bf8f58-26cc-4139-d7af-2010a21a5192"
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAhsAAAGFCAYAAABUozETAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA1oklEQVR4nO3dd3zV9eH98XPvTe7NnoQkJIGEEQh7OUBRVBQrooKKGxEVFdRarXX+HLVaW4toq/ZbtIKjCA6sdYEgTkAMG9mgEHZIyF43d/z+CAQwCWTdfG7yeT0fDx5m3XtPYsa57/WxeL1erwAAAHzEanQAAADQtlE2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACAT1E2AACATwUYHQCAsTwerw6VOpVTXKGcIqcOFpcrp6jq9VKnWx6vVx6v5PV65fYcfdlisSjQZlGgzSp7gLXqv4dfD7bb1D4iSImRQUqICFL7CIccATajP1UABqFsAG1YbnGFNu0v0v6C8qoyUVyhnOKqInGwqOrlvFKn3B6vz7PEhNoVf7iAxEdUlZCESEfVy5FBSowIVmRIoM9zAGh5Fq/X6/vfMgB8yuv1KutQqTbsLdT6vYXasK9Q6/cW6EBhhdHRGiQ40KYeieHqmxSpvslR6pcSqc7twmS1WoyOBqAJKBtAK1Pp9mjLgaKjxWJvoTbuK1RRhcvoaD4R5ghQrw4R6pcSpb7JkeqbFKWOsSFGxwLQAJQNwM8VlFXq2y0H9f3WHK3bU6Bt2cVyuj1GxzJUdEig+iRHqV9ypPokRap/SpTaRwQZHQtAHSgbgB/acqBIizZla9GmbK3cmSdXC6ypaO3S48N0Qc8End8zXn2TI2WxMPUC+AvKBuAHyivdWro9V4s2ZeurzdnanVdmdKRWLSEiSCN6ttf5PRM0tEusAm3s8geMRNkADLInv6yqXGzK1pLtOSqvNPfUiK+EOwJ0dvc4XdArQed0j1N4EDtegJZG2QBa0M8Hi/XByt1auCFbmw8UGR3HdOw2q07rHKMLesbr/J4JSohknQfQEigbgI+VOl36ZO0+vbd8lzJ35BkdB4dZLFLf5CiNG5ysS/snKczBsUOAr1A2AB9ZsfOQ3s3crU/X7VNxG92W2laE2m26pH8HXXtqJ/VJjjQ6DtDmUDaAZlTqdOmDlXv01tId2nKg2Og4aIQ+SZG69rSOuqRfB4Uy2gE0C8oG0Ax+PlisN5fu1Acrd6uonFGMtiA8KEBXn5KiG4emKjmaQ8SApqBsAI3k9Xq1aFO2Zi7Zoe+35YifpLbJZrVoZK943XxmmgZ1ijE6DtAqUTaARli44YCmLtiijfsKjY6CFtQvJUo3n5mmUX0SZeN6LUC9UTaABliyPUfPzd+sVVn5RkeBgbq2D9P9I7trZK8Eo6MArQJlA6iHVVl5+tsXm7V4W67RUeBHBneK1kMX9WB6BTgJygZwApv2F+pv87do4cYDRkeBHzu/Z7weuLCHurYPMzoK4JcoG0Atfskp0bQFW/TJ2r3iGmioD5vVonGDk3XPiHTFcwVa4DiUDeAYe/PL9Pcvt+r9Fbu50ioaJTjQpolnpur2s7twHRbgMMoGIKm4wqVpC7borR92yunigmhouphQu6ac01U3nN5J9gCuOgtzo2zA9L7anK1H5q7T3oJyo6OgDUqJCdb9I3vokn4djI4CGIayAdPKL3XqyY836MNVe4yOAhMYkdFez4zto/bhrOeA+VA2YEqfrdunxz5ar5ziCqOjwESiQgL15CW9dGn/JKOjAC2KsgFTyS4q12P/Xa956/cbHQUm9pveCfrTZb0VG+YwOgrQIigbMI33V+zWU59sUEFZpdFRAMWG2vX0mN66sHei0VEAn6NsoM3bk1+mh+eu0zdbDhodBajhkn4d9MdLeykqxG50FMBnKBtos7xer97+Yaf+Mm+ziiu47Dv8V/twh/48to/Oy4g3OgrgE5QNtEkHCst19zurtOyXQ0ZHAertikHJemx0T0VwGBjaGMoG2pwVOw/pjrdXKruInSZofRIjg/TXK/pqWLc4o6MAzYaygTblP8t26sn/bZDTzSmgaL2sFukPF/bQ7Wd3MToK0CwoG2gTnC6PHv/fer3zY5bRUYBmM3ZAkv58eR85AmxGRwGahLKBVi+7sFx3/GelVuzMMzoK0OwGdIzS9BsGKy6cMznQelE20KqtzMrTHW+v0IFC1meg7eoQGaTp4werd1Kk0VGARqFsoNWa/WOWHvtoPeszYArBgTZNHddPF/XhEDC0PpQNtDqVbo+e+N96/WcZ6zNgLhaL9Nvzuum353WTxWIxOg5Qb5QNtCoHiyo0+T8rlLmD9Rkwr1F9EzX1yn4KCmThKFoHygZajQ17CzVxZqb2F5YbHQUwXJ+kSL06frASIrlkPfwfZQOtwsqsPE14/UcVlnPsOHBE+3CHpo8frP4pUUZHAU6IsgG/t2Rbjm59c7lKnG6jowB+JyjQquk3DNZZ6Zw4Cv9F2YBfW7jhgCbPWimnix0nQF3sAVb93/UDdW4PLuQG/0TZgN/6aPUe3ffuGrk8fIsCJ2O3WfXStQN0Qa8Eo6MANVA24JfezdylB+euFT0DqL9Am0UvXj2Aszjgd6xGBwB+7d3lu/QARQNosEq3V3e9s0ofrd5jdBTgOJQN+JX3lu/Sgx+sFeNtQOO4PV79bs5q/W/NXqOjANUoG/AbH6zYrQc+YEQDaCqPV7p3zmrNX7/f6CiAJMoG/MSHq3br/vfXUDSAZuLyeHXXrFX6ZstBo6MAlA0Y7+M1e3XfuxQNoLk53R7d9tZyLd2ea3QUmBxlA4ZasfOQ7nuPogH4SnmlR7e8kakVO7meEIxD2YBhdueV6ra3VnBgF+BjJU63Jsz4UVsPFBkdBSZF2YAhiitcunnmcuUUO42OAphCUblLt765XAWllUZHgQlRNtDi3B6v7pq1Upt5lgW0qB25pbrznZVyM2+JFkbZQIt7+tON+mozK+QBI3y3NUd//myj0TFgMpQNtKhZy7L0+uJfjI4BmNpr3/+iD1bsNjoGTISygRazeFuOHvvoJ6NjAJD08IfrtHpXvtExYBKUDbSInw8Wa/J/VnIFV8BPVLiqzuDILiw3OgpMgLIBn8svdermN5aroIxV8IA/OVBYoUlvrVCFy210FLRxlA34VKXbo9vfXqFfckqMjgKgFqt35euRD5nehG9RNuBTj/9vvX74+ZDRMQCcwPsrduvf37NwG75D2YDPzF+/X7OWZRkdA0A9PPPZRn2/NcfoGGijKBvwiZziCj08d53RMQDUk9vj1ZRZK7Unv8zoKGiDKBvwiYfnrlNuCUeRA61JQVmlHvxgrdEx0AZRNtDs3l+xW19sOGB0DACN8N3WHL3zI9OfaF6UDTSrPfllevLj9UbHANAEz3y6UXuZTkEzomyg2Xi9Xt3/3hoVlbuMjgKgCYoqXHqQNVdoRpQNNJsZi3doyfZco2MAaAbfbjmoOZlMp6B5UDbQLLYfLNZf528yOgaAZvSnTzdqXwHTKWg6ygaazOX26N45q1Ve6TE6CoBmVFTu0kNMp6AZUDbQZC9/tV1rdhcYHQOAD3y9+aDeXb7L6Bho5SgbaJJ1uwv00ldbjY4BwIf+9MkG7S/g6rBoPMoGGs3l9ui+91ar0s1l44G2rLDcpYfmctgXGo+ygUab9WOWthwoNjoGgBbw1eaDen/FbqNjoJWibKBRisor9eJCpk8AM/njx+uVW1xhdAy0QpQNNMr/fbOda58AJlNY7tI/Fm0zOgZaIcoGGmxfQZn+/f0vRscAYIBZy7K0O6/U6BhoZSgbaLC/zd/CmRqASTndHj2/YIvRMdDKUDbQIBv2FurDVSwSA8zsv6v2aMuBIqNjoBWhbKBBnvlsozzsdAVMzeOV/jpvs9Ex0IpQNlBvX2/O1vfbcoyOAcAPLNx4QCt25hkdA60EZQP14vF49eznXGgNwFF/mcfvBNQPZQP18v6K3dq0nzlaAEf9+MshfbU52+gYaAUoGzipMqdbUxcwPwugpufmbZbXy0IunBhlAyf16nc/60AhpwYCqGnDvkL9b81eo2PAz1E2cEKF5ZV69dufjY4BwI89v2CLKt2cvYO6UTZwQrN/zFJRhcvoGAD82M7cUs3O3GV0DPgxygbq5HJ7NHPxDqNjAGgFXl60jdEN1ImygTp9um6f9haUGx0DQCuwv7Bcn63bZ3QM+CnKBur06nes1QBQfzOX7DA6AvwUZQO1WrI9Rz/tKTQ6BoBWZFVWvlbvyjc6BvwQZQO1+vd3XEIeQMPNXMzvDtRE2UANWbmlnAoIoFE+XbdP2YWs9cLxKBuo4T8/7uTKrgAapdLt1dvLsoyOAT9D2cBxKlxuvbd8t9ExALRis3/MkptnLDgGZQPH+WzdPh0qcRodA0Arll1UoUWbmIrFUZQNHOftHxj+BNB0s3/kdwmOomyg2oa9hVqxM8/oGADagK+3HNR+DgXEYZQNVJudyTMRAM3D7fHqveVcLwVVKBuQJHm9Xs37ab/RMQC0IXOW75LXy0JRUDZw2MqsPGUXVRgdA0AbsjuvTIu35RodA36AsgFJ0vz1B4yOAKANmr+eEVNQNnAYvxAA+MKXG3kiA8oGVLULZWduqdExALRBewvKtX5vgdExYDDKBhjVAOBTX27kgC+zo2yAsgHAp5hKAWXD5HbmlmjT/iKjYwBow9buKeBKsCZH2TA5ztYA4Gter/Ql10oxNcqGyc1jCgVAC2AqxdwoGyZ2oLBcq3flGx0DgAl8vy1H5ZVuo2PAIJQNE/ti/X5xkjCAllBe6dHibTlGx4BBKBsmxqmhAFrSQrbAmhZlw6TKK91a9gvXLADQchZtOsCF2UyKsmFSP+0pUKWbH3oALedAYYXW7eE0UTOibJgUC0MBGOHrzQeNjgADUDZMahVlA4AB1u7ONzoCDEDZMKnVWflGRwBgQkyjmBNlw4QOFlVoT36Z0TEAmNCBwgplF3F0udlQNkyI9RoAjLR+T6HREdDCKBsmtHpXntERAJgYUynmQ9kwIUY2ABiJsmE+lA2T8Xq9WruLH3QAxvmJsmE6lA2T2X6wWEUVLqNjADCxfQXlyi2uMDoGWhBlw2RWseUVgB9gKsVcKBsmw3oNAP6AqRRzoWyYDGUDgD/4ie2vpkLZMBG3x6vN+4uMjgEATKOYDGXDRA4Ulsvl4UqvAIy3J79MeSVOo2OghVA2TGRfAUeUA/AfG/YxlWIWlA0T2ZvP9QgA+A+u0WQelA0TYWQDgD85WMRZG2ZB2TARRjYA+JPsQn4nmQVlw0T2MmQJwI9kM7JhGpQNE9lXwLMIAP6DsmEelA0TYc0GAH+SXcQTILOgbJhEhcutXPa0A/Aj2YWMbJgFZcMk9heUy8t5XgD8SIXLo4KySqNjoAVQNkyCnSgA/NFBplJMgbJhEuxEAeCPmEoxB8qGSbA4FIA/YkeKOVA2TGI/h+cA8EPsSDEHw8uGxWLRf//73ybfT2pqql544YUm309j7NixQxaLRatXrzbk8eujpMJtdAQAqIFpFHNoUNmYMGGCLBaLbr/99hrvmzJliiwWiyZMmNCgAPv27dNvfvObBt2mNpmZmZo0aVL1681VYiRp27Ztuummm5ScnCyHw6G0tDRdc801Wr58ebPcf0sor6RsAPA/TKOYQ0BDb5CSkqLZs2dr2rRpCg4OliSVl5dr1qxZ6tixY4MDJCQkNPg2x3I6nbLb7YqLi2vS/dRl+fLlOu+889S7d2/961//Uo8ePVRUVKSPPvpI9913n7755hufPG5zq3B5jI5QzVNRqvzv3lbp1qXylBbI3r6zokdMkiMxXZLkLslT3tczVb5jlTzlJXKk9FLMiNsUGJNU530Wr1uo3M9eOP6NtkB1+v2H1a96vV4VfP8fFa+ZL09FiRxJGYq5YHL1/Xpdlcqd93eVbv1BttBoxVwwWcGp/atvX7DsA7kLDyrm/JplG0DjFJWz9dUMGjyNMnDgQKWkpGju3LnVb5s7d646duyoAQMGHPex8+bN05lnnqmoqCjFxsbq4osv1vbt24/7mF+PQKxbt07nnnuugoODFRsbq0mTJqm4uLj6/RMmTNBll12mp59+Wh06dFD37t0lHT+NkpqaKkkaM2aMLBaLUlNTtWPHDlmt1hqjES+88II6deokj6fmH2Ov16sJEyaoW7du+u677zRq1Ch16dJF/fv31+OPP66PPvqo1q+R2+3WzTffrLS0NAUHB6t79+568cUXj/uYr7/+WqeeeqpCQ0MVFRWlM844Qzt37pQkrVmzRuecc47Cw8MVERGhQYMGNXkUpcLlPyMbufP+ofIdq9Xu4vuUOPElBaUN0IHZj8pVlCOv16vsuX+SK3+/4sY+qsQJLyogor0OzHlUHueJ53Yt9hAlT3nr6L87Xj/u/YXLPlDhio8VM3KKEm6YKktgkLLffUxeV9VhZ0Vr5sm5f5sSrv+bwvpdqJyPn5P38OEklfn7VbxmvqLOGu+bLwpgUi4PBwCZQaPWbEycOFEzZsyofv3111/XTTfdVOPjSkpKdO+992r58uX68ssvZbVaNWbMmFr/sB/5+JEjRyo6OlqZmZl67733tHDhQt15553HfdyXX36pzZs3a8GCBfrkk09q3E9mZqYkacaMGdq3b58yMzOVmpqqESNGHJf7yMdMmDBBVmvNL8Xq1au1fv163XfffbW+PyoqqtbPw+PxKDk5We+99542bNigxx57TA8//LDeffddSZLL5dJll12ms88+W2vXrtXSpUs1adIkWSwWSdJ1112n5ORkZWZmasWKFXrwwQcVGBhY62PVV3mlf4xseCorVLp5saLOuUlBKb0VGN1BUWdep8DoRBWt+lyuvL1y7t2smAsmy5GYrsDYZMWMnCyvy6mSjScZRbJYZAuLPvovNLr6XV6vV0XLP1LkkKsU0u102dunqd3F98pVfEilW5ZKkipzdym462myx3VS+MBR8pQWyFNWKEk69MUrih4+QVZHiM++NoAZuSkbptDgaRRJuv766/XQQw9VPxNfvHixZs+era+//vq4j7v88suPe/31119XXFycNmzYoN69e9e431mzZqm8vFxvvvmmQkNDJUkvvfSSRo8erb/85S+Kj4+XJIWGhuq1116T3W6vNd+RKZWoqKjjpmluueUW3X777Xr++eflcDi0cuVKrVu3rs4Riq1bt0qSevTocbIvyXECAwP15JNPVr+elpampUuX6t1339W4ceNUWFiogoICXXzxxerSpYskKSMjo/rjs7KydP/991c/brdu3Rr0+LXxm5ENj1vyemSxHV+eLAEOVexer9CMYYdfP/r/1mKxymILVMXuDQrvN7LOu/Y6y7T7nzdJXq/s8V0UddZ42eM6SZJcBQfkLsk7blrE6giVo0N3VezdpNCeZ8vePk0lP30lT2WFyn9ZKVtYjKzBESpe/5UsAXaFpA9txi8E2qKilZ+oYNlcuUvyZG+fppgRt8nRoXutH8vUXxWXu+XLxvDhw9W/f/8W2VSQmpqqe+65R/fcc4/PH+vXduzYobS0NK1atUr9+/dv8cc/VqNGNuLi4jRq1CjNnDlTM2bM0KhRo9SuXbsaH7d161Zdc8016ty5syIiIqqnN7Kysmq9340bN6pfv37VRUOSzjjjDHk8Hm3evLn6bX369KmzaJzIZZddJpvNpg8/rPphnjlzps4555zqXL/mbcL53i+//LIGDRqkuLg4hYWFafr06dWfd0xMjCZMmKCRI0dq9OjRevHFF7Vv377q295777265ZZbNGLECD377LM1pp4aw+knazasjhA5OvRQwZLZchXlyutxq3j9V6rYu0nukjwFxiTLFhGn/G/ekLu8WF53pQp+eF/uohy5iw/Veb+BMUmKvei3aj/2/6ndxfdJXo/2v32/XIU5kiR3cV7V44dGHXc7W0iU3CX5kqSwPucrsH2a9v57sgqWvqt2lz4gT3mxCr7/j2JG3Ka8b9/Snn/dqgNz/p9cRTk++fqg9SrZ+K0OLXpNUWdco8QJL8rePk3Z7z5W/f1VG6b+JFcdI90N0dDNC3PnztVTTz3V5MetDzYvVGn01teJEydq5syZeuONNzRx4sRaP2b06NE6dOiQXn31VS1btkzLli2TVLWosymOLSMNYbfbNX78eM2YMUNOp1OzZs2qM7skpadXLVjctGlTgx5n9uzZ+v3vf6+bb75ZX3zxhVavXq2bbrrpuM97xowZWrp0qYYOHao5c+YoPT1dP/zwgyTpiSee0Pr16zVq1CgtWrRIPXv2rC5IjeVP86KxF98nSdrzyo3K+tsYFa34n0IzzpJkkcUWoLgxj6gyb492v3i1sqZervKstQrqPEiy1P3t6kjKUFjv82SP76ygjn0UN+YR2UIiVbz683rnstgCFHvBHUq+/d9KvHGagpJ7KW/RvxU+aLScB35W2dalSrzpH3J06KG8hdOb+mVAG1OY+V+F9xupsL7ny96uo2JGTpEl0KHidQvqvhFTf802jXJk80JZ2dEDDOvavBATE6Pw8PBmedy6HPl9HxcXp5CQ5v9/sHz5cg0aNEhbtmzRv/71L23YsEEffvihevToofvuu6/ZH6+pGl02LrzwQjmdTlVWVmrkyJpD27m5udq8ebMeffRRnXfeecrIyFBeXt4J7zMjI0Nr1qxRSUlJ9dsWL14sq9VavRC0vgIDA+V215w6uOWWW7Rw4UK98sorcrlcGjt2bJ330b9/f/Xs2VNTp06tdZ1Jfn5+rbdbvHixhg4dqsmTJ2vAgAHq2rVrraMTAwYM0EMPPaQlS5aod+/emjVrVvX70tPT9bvf/U5ffPGFxo4dW2OtSWsWGJ2ohGufVcrv3lfS5JlKHD9NXo9bgVFVU16OhK7qcNM/lHLPHCXf+Zbix/1RnrIiBUTVf+eSxRYge3xnVeZXjRjZwqp+iXt+9SzTXZov269GO44o37lWlbk7FT7wYpVnrVVw58Gy2oMU0uNMlWeta/gnjjbL666Uc/82BXXqX/02i8WqoNT+qthT95OVI1N/u1+ZoOwPnpLz4M7q951s6k+S7O3TVLF7Q6ue+muuJ0IN2bwwfPjw46Y1UlNT9cwzz2jixIkKDw9Xx44dNX368U8o2LzQtM0LjVqzIUk2m00bN26sfvnXoqOjFRsbq+nTpysxMVFZWVl68MEHT3if1113nR5//HHdeOONeuKJJ3Tw4EHddddduuGGG6rXa9RXamqqvvzyS51xxhlyOByKjq76Y5ORkaHTTz9dDzzwgCZOnFi9fbc2FotFM2bM0IgRIzRs2DA98sgj6tGjh4qLi/Xxxx/riy++qHXra7du3fTmm29q/vz5SktL01tvvaXMzEylpaVJkn755RdNnz5dl1xyiTp06KDNmzdr69atGj9+vMrKynT//ffriiuuUFpamnbv3q3MzMwa61/aAqs9SFZ7kNzlxSr7ZaWihx+/yNjqqBrBqjy0R8792xQ17Pp637fX45bz4E4Fdx4kSQqIjJctNFrlO1fLHt9ZUtUW3Iq9mxXev+Y5L16XU4cW/FPtRv9eFqtN8nrkPfIz73HL6/WPaSmj2K0eRQS4FW5zKSzArfAAt8JsLoXa3Aq1VirE5lKo1a1ga6WCLZUKtrgUZK1UkCoVZKmUQ5Wyq1IOOWX3OhUopwI9TgV4D//zOGX1OGVpJZcq3lvgVFevR++m/k+nJX1V/fZH4nfou22F+jbpmRq3WeYs0raYzurdIVSFZS69sGiLFs+6W9881F/J0Q79UFGocyV93+VNJUYenTa+PnafLJ59eispV5UJHt1fckjzZ16rlLAAvXNzmnpE/1HDlq7V0rt767XFt+v9lTnq3C5I/7y2i5KiHC3x5WgQV3QXScOa5b6ObF647rrrJB3dvPDr9YS1mTp1qp566ik9/PDDev/993XHHXfo7LPPVvfu3as3LwwZMkSZmZnKzs7WLbfcojvvvFMzZ86svo8vv/xSERERWrCg9tGszMxMtW/fXjNmzNCFF14om82muLi46s0LgwcPrv7Y+mxemDVrVqM3L8TGxmrJkiWaNGmSEhMTNW7cuOrNC7feeqveeecdOZ1O/fjjj8dtXhgwYID++c9/ymazafXq1fXevNDosiFJERERdb7ParVq9uzZuvvuu9W7d291795df//73zV8+PA6bxMSEqL58+frt7/9rU455RSFhITo8ssv1/PPP9/gbFOnTtW9996rV199VUlJSdqxY0f1+26++WYtWbLkhFMoR5x66qlavny5nn76ad16663KyclRYmKihg4dWufiottuu02rVq3SVVddJYvFomuuuUaTJ0/W559/Xv15btq0SW+88YZyc3OVmJioKVOm6LbbbpPL5VJubq7Gjx+vAwcOqF27dho7duxxC05bu7KfV0iSAmKS5Mrbp7yvX1dgTLLC+oyQJJVs+l62kAjZItqr8uAOHVo4XSHdTldw2sDq+8j5ZKps4bGKPnuCJCl/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\n",
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
      "Proportion of Minority Class: 0.5%\n"
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
   "execution_count": 56,
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
   "execution_count": 57,
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
   "execution_count": 58,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "A75jz_evCP6f",
    "outputId": "aaf72af5-1d2d-4af1-9e1e-ab71bddce442"
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
   "execution_count": 59,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "rlGisVHz6Gs8",
    "outputId": "b15909ba-b54c-4fc2-8f9f-f8e372b006a2"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proportion of Minority Class in train set: 0.5%\n",
      "Proportion of Minority Class in test set: 0.5%\n",
      "Proportion of Minority Class in validation set: 0.5%\n"
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
   "execution_count": 60,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ln5MnPns6Gw3",
    "outputId": "9b549ffc-c8c5-4722-948d-87df5bfa6f60"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The X_train shape:  (600000, 10)\n",
      "The X_test shape:  (200000, 10)\n",
      "The X_val shape:  (200000, 10)\n"
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
   "execution_count": 61,
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
   "execution_count": 62,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 452
    },
    "id": "yZqL94uSCYet",
    "outputId": "25713751-8cf7-4213-bdbc-d2a853f1e962"
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
      "Proportion of Minority Class: 0.5%\n"
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
   "execution_count": 63,
   "metadata": {
    "id": "uDFmXS5_CYiM"
   },
   "outputs": [],
   "source": [
    "from imblearn.over_sampling import RandomOverSampler\n",
    "ros = RandomOverSampler(sampling_strategy='auto', random_state=42)\n",
    "X_resampled, y_resampled = ros.fit_resample(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "3YvlyInlCYld",
    "outputId": "e1373e9e-4c46-469f-9fd6-b3f93880cb6c"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proportion of Minority Class in train set after resampling: 50.0%\n"
     ]
    }
   ],
   "source": [
    "print(\"Proportion of Minority Class in train set after resampling: \" + str(round((len(y_resampled) - y_resampled.sum()) / len(y_resampled) * 100, 2)) + \"%\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 480
    },
    "id": "E6AHW4Z5CYo7",
    "outputId": "bec3935a-3bde-4ea6-ef26-8e411e71a658"
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkgAAAGbCAYAAAA/XG+zAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABBZ0lEQVR4nO3dd3hUVeLG8Xdm0hshIdQAoYYuiCJSXBUWBEQRK6JSbcCylnXVdX92du2sa1txFV0VEUVlZVGKgiIggoD0GhJ6EhJIrzP390ckkgKkn5nM9/M882gmd+68E5LcN+ece8dmWZYlAAAAFLObDgAAAOBuKEgAAAClUJAAAABKoSABAACUQkECAAAohYIEAABQCgUJAACgFAoSAABAKRQkAACAUihIACokJiZG48ePNx3jrPbs2aMhQ4aoQYMGstls+uKLL2pkv+PHj1dMTEyN7AuAZ6AgAVXw7rvvymazFd8CAgLUsWNHTZs2TYmJiabjVdnq1av1+OOP6+TJk6ajVMm4ceO0ZcsWzZgxQ++//74uuOCCs26fnp6uJ554Quedd55CQkIUGBiobt266cEHH9SRI0fqKDUAd+RjOgDgyZ588km1adNGubm5+uGHH/TGG29o0aJF2rp1q4KCgkzHq7TVq1friSee0Pjx4xUeHl7ic7t27ZLd7r5/U+Xk5GjNmjV65JFHNG3atHNuHxcXp8GDB+vAgQO6/vrrdccdd8jPz0+bN2/W22+/rc8//1y7d++ug+QA3BEFCaiGYcOGFY9STJ48WZGRkXrppZe0YMECjRkzptzHZGVlKTg4uC5jnlNFMvn7+9dRmqpJTk6WpDLFrjyFhYUaPXq0EhMTtWLFCg0YMKDE52fMmKFnn322NmIC8BDu++cg4IEuv/xySdL+/fslFa1dCQkJ0b59+zR8+HCFhoZq7NixkopKyf3336+WLVvK399fsbGxeuGFF2RZVol92mw2TZs2TR9++KFiY2MVEBCg3r176/vvvy/z/Bs3btSwYcMUFhamkJAQDRo0SD/++GOJbU5ND3733XeaMmWKGjdurOjoaD3++ON64IEHJElt2rQpnj6Mj4+XVP4apLi4OF1//fWKiIhQUFCQ+vbtq//9738ltlmxYoVsNpvmzZunGTNmKDo6WgEBARo0aJD27t1boa/ruV7X448/rtatW0uSHnjgAdlstrOuGZo/f75++eUXPfLII2XKkSSFhYVpxowZZ830wgsvqF+/foqMjFRgYKB69+6tTz/9tMx2S5cu1YABAxQeHq6QkBDFxsbqL3/5S4ltXnnlFXXt2lVBQUFq2LChLrjgAs2ZM6fENocPH9bEiRPVpEkT+fv7q2vXrnrnnXfKPF9F9gXg3BhBAmrQvn37JEmRkZHF9xUWFmro0KEaMGCAXnjhBQUFBcmyLF111VVavny5Jk2apJ49e2rx4sV64IEHdPjwYc2cObPEfr/77jt9/PHHmj59uvz9/fX666/riiuu0E8//aRu3bpJkrZt26aBAwcqLCxMf/7zn+Xr66s333xTl156qb777jtddNFFJfY5ZcoURUVF6dFHH1VWVpaGDRum3bt366OPPtLMmTPVqFEjSVJUVFS5rzUxMVH9+vVTdna2pk+frsjISL333nu66qqr9Omnn+qaa64psf0zzzwju92uP/3pT0pLS9Nzzz2nsWPHau3atWf9mlbkdY0ePVrh4eG69957NWbMGA0fPlwhISFn3Od///tfSdKtt9561uc+m5dffllXXXWVxo4dq/z8fM2dO1fXX3+9Fi5cqBEjRhRnv/LKK9WjRw89+eST8vf31969e7Vq1ari/bz11luaPn26rrvuOv3xj39Ubm6uNm/erLVr1+rmm2+WVPS17tu3b3FZjoqK0ldffaVJkyYpPT1d99xzT4X3BaCCLACVNnv2bEuStWzZMis5Odk6ePCgNXfuXCsyMtIKDAy0Dh06ZFmWZY0bN86SZD300EMlHv/FF19Ykqynn366xP3XXXedZbPZrL179xbfJ8mSZK1fv774voSEBCsgIMC65ppriu8bNWqU5efnZ+3bt6/4viNHjlihoaHWJZdcUib7gAEDrMLCwhLP//zzz1uSrP3795d5za1bt7bGjRtX/PE999xjSbJWrlxZfF9GRobVpk0bKyYmxnI6nZZlWdby5cstSVbnzp2tvLy84m1ffvllS5K1ZcuWsl/g01T0de3fv9+SZD3//PNn3Z9lWVavXr2sBg0anHO7U8aNG2e1bt26xH3Z2dklPs7Pz7e6detmXX755cX3zZw505JkJScnn3HfV199tdW1a9ezPv+kSZOsZs2aWcePHy9x/0033WQ1aNCgOEtF9gWgYphiA6ph8ODBioqKUsuWLXXTTTcpJCREn3/+uVq0aFFiu7vvvrvEx4sWLZLD4dD06dNL3H///ffLsix99dVXJe6/+OKL1bt37+KPW7VqpauvvlqLFy+W0+mU0+nUkiVLNGrUKLVt27Z4u2bNmunmm2/WDz/8oPT09BL7vP322+VwOKr82hctWqQ+ffqUmKIKCQnRHXfcofj4eG3fvr3E9hMmTJCfn1/xxwMHDpRUNE13JlV5XRWRnp6u0NDQSj/udIGBgcX/f+LECaWlpWngwIHasGFD8f2n1kMtWLBALper3P2Eh4fr0KFDWrduXbmftyxL8+fP18iRI2VZlo4fP158Gzp0qNLS0oqf81z7AlBxFCSgGl577TUtXbpUy5cv1/bt2xUXF6ehQ4eW2MbHx0fR0dEl7ktISFDz5s3LHKQ7d+5c/PnTdejQocxzd+zYUdnZ2UpOTlZycrKys7MVGxtbZrvOnTvL5XLp4MGDJe5v06ZNxV9oORISEs74fKc+f7pWrVqV+Lhhw4aSisrFmVTldVVEWFiYMjIyKv240y1cuFB9+/ZVQECAIiIiFBUVpTfeeENpaWnF29x4443q37+/Jk+erCZNmuimm27SvHnzSpSlBx98UCEhIerTp486dOigqVOnlpiCS05O1smTJzVr1ixFRUWVuE2YMEGSlJSUVKF9Aag4ChJQDX369NHgwYN16aWXqnPnzuWeBu/v7++Wp8efPgJSF840WmWVWpReFzp16qS0tLQqlStJWrlypa666ioFBATo9ddf16JFi7R06VLdfPPNJV5PYGCgvv/+ey1btky33nqrNm/erBtvvFG///3v5XQ6JRUVvV27dmnu3LkaMGCA5s+frwEDBuixxx6TpOIydcstt2jp0qXl3vr371+hfQGoOPf7rQ14gdatW+vIkSNlRjF27txZ/PnT7dmzp8w+du/eraCgoOLRhKCgIO3atavMdjt37pTdblfLli3Pmctms1XqNZzp+U59vrpq6nWVNnLkSEnSBx98UKVc8+fPV0BAgBYvXqyJEydq2LBhGjx4cLnb2u12DRo0SC+99JK2b9+uGTNm6Ntvv9Xy5cuLtwkODtaNN96o2bNn68CBAxoxYoRmzJih3NxcRUVFKTQ0VE6nU4MHDy731rhx4wrtC0DFUZAAA4YPHy6n06lXX321xP0zZ86UzWbTsGHDSty/Zs2aEmtbDh48qAULFmjIkCFyOBxyOBwaMmSIFixYUHxavlR09tOcOXM0YMAAhYWFnTPXqWshVeRK2sOHD9dPP/2kNWvWFN+XlZWlWbNmKSYmRl26dDnnPs6lpl5Xadddd526d++uGTNmlMh/SkZGhh555JGz5rLZbMWjQJIUHx9f5q1NUlNTyzy2Z8+ekqS8vDxJUkpKSonP+/n5qUuXLrIsSwUFBXI4HLr22ms1f/58bd26tcz+Tl3/qSL7AlBxnOYPGDBy5EhddtlleuSRRxQfH6/zzjtPS5Ys0YIFC3TPPfeoXbt2Jbbv1q2bhg4dWuI0f0l64oknird5+umni6+5M2XKFPn4+OjNN99UXl6ennvuuQrlOrUQ/JFHHtFNN90kX19fjRw5styLSD700EP66KOPNGzYME2fPl0RERF67733tH//fs2fP7/GphVr4nWV5uvrq88++0yDBw/WJZdcohtuuEH9+/eXr6+vtm3bpjlz5qhhw4ZnvBbSiBEj9NJLL+mKK67QzTffrKSkJL322mtq3769Nm/eXLzdk08+qe+//14jRoxQ69atlZSUpNdff13R0dHFi9uHDBmipk2bqn///mrSpIl27NihV199VSNGjCheo/bMM89o+fLluuiii3T77berS5cuSk1N1YYNG7Rs2bLiIlaRfQGoIINn0AEe69Sp8uvWrTvrduPGjbOCg4PL/VxGRoZ17733Ws2bN7d8fX2tDh06WM8//7zlcrlKbCfJmjp1qvXBBx9YHTp0sPz9/a1evXpZy5cvL7PPDRs2WEOHDrVCQkKsoKAg67LLLrNWr15dqexPPfWU1aJFC8tut5c45b/0af6WZVn79u2zrrvuOis8PNwKCAiw+vTpYy1cuLDENqdO8//kk09K3H/qtPzZs2eXm6Oyr6syp/mfcuLECevRRx+1unfvbgUFBVkBAQFWt27drIcfftg6evRo8Xblneb/9ttvF/97dOrUyZo9e7b12GOPWaf/Wv3mm2+sq6++2mrevLnl5+dnNW/e3BozZoy1e/fu4m3efPNN65JLLrEiIyMtf39/q127dtYDDzxgpaWllXi+xMREa+rUqVbLli0tX19fq2nTptagQYOsWbNmVXpfAM7NZlkGVkgCqDCbzaapU6eWmY4DANQe1iABAACUQkECAAAohYIEAABQCmexAW6OZYIAUPcYQQIAACiFggQAAFAKBQkAAKAUChIAAEApFCQA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\n",
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
      "Proportion of Minority Class: 50.0%\n",
      "Shape of Resampled X:  (1194000, 10)\n",
      "Shape of Resampled y:  (1194000,)\n"
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
   "execution_count": 66,
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
   "execution_count": 67,
   "metadata": {
    "id": "RaBnqgT588lQ"
   },
   "outputs": [],
   "source": [
    "ideal_params = {\n",
    "    'n_estimators': 150,\n",
    "    'learning_rate': 0.2,\n",
    "    'max_depth': 5\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "kB_LoFfwCY2-",
    "outputId": "eb3537aa-49b2-4af8-e204-72feb90d47c9"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Gradient Boosting): 78.70%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       1.00      0.79      0.88    199000\n",
      "        True       0.01      0.22      0.01      1000\n",
      "\n",
      "    accuracy                           0.79    200000\n",
      "   macro avg       0.50      0.51      0.45    200000\n",
      "weighted avg       0.99      0.79      0.88    200000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Create a GradientBoostingClassifier with the ideal hyperparameters\n",
    "ros_gbc_model = GradientBoostingClassifier(**ideal_params)\n",
    "\n",
    "# Train the model on the resampled data\n",
    "ros_gbc_model.fit(X_resampled, y_resampled)\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(ros_gbc_model, 'ros_gradient_boosting_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "ros_gbc_predictions = ros_gbc_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Gradient Boosting): {:.2f}%\".format(accuracy_score(y_val, ros_gbc_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, ros_gbc_predictions))\n"
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
   "execution_count": 36,
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
   "execution_count": 37,
   "metadata": {
    "id": "5hshDaqwdBA5"
   },
   "outputs": [],
   "source": [
    "ideal_params_rfc = {\n",
    "    'n_estimators': 50,\n",
    "    'max_depth': None,\n",
    "    'min_samples_split': 5\n",
    "}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "C-dMJxURCY-I",
    "outputId": "cc164638-a91b-4a20-bee6-fc24704fc6af"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Random Forest): 99.50%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       0.99      1.00      1.00    199000\n",
      "        True       0.00      0.00      0.00      1000\n",
      "\n",
      "    accuracy                           0.99    200000\n",
      "   macro avg       0.50      0.50      0.50    200000\n",
      "weighted avg       0.99      0.99      0.99    200000\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/usr/local/lib/python3.10/dist-packages/sklearn/metrics/_classification.py:1344: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, msg_start, len(result))\n",
      "/usr/local/lib/python3.10/dist-packages/sklearn/metrics/_classification.py:1344: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, msg_start, len(result))\n",
      "/usr/local/lib/python3.10/dist-packages/sklearn/metrics/_classification.py:1344: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.\n",
      "  _warn_prf(average, modifier, msg_start, len(result))\n"
     ]
    }
   ],
   "source": [
    "# Create a RandomForestClassifier with the predefined hyperparameters\n",
    "ros_rfc_model = RandomForestClassifier(**ideal_params_rfc)\n",
    "\n",
    "# Train the model on the resampled data\n",
    "ros_rfc_model.fit(X_resampled, y_resampled)\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(ros_rfc_model, 'ros_random_forest_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "ros_rfc_predictions = ros_rfc_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Random Forest): {:.2f}%\".format(accuracy_score(y_val, ros_rfc_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, ros_rfc_predictions))\n"
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
   "execution_count": 39,
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
   "execution_count": null,
   "metadata": {
    "id": "y6WlXi0adkp0"
   },
   "outputs": [],
   "source": [
    "# Train the stacking model on the resampled data\n",
    "stack_model.fit(X_resampled, y_resampled)\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(stack_model, 'ros_stacking_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "stack_predictions = stack_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Stacking): {:.2f}%\".format(accuracy_score(y_val, stack_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, stack_predictions))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "execution_count": null,
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
    "evaluate_model(ros_gbc_model, X_val, y_val, \"Gradient Boosting\")\n",
    "evaluate_model(ros_rfc_model, X_val, y_val, \"Random Forest\")\n",
    "evaluate_model(ros_stack_model, X_val, y_val, \"Stacking\")"
   ]
  }
 ],
 "metadata": {
  "colab": {
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
