{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
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
   "execution_count": 1,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "8Qc4BxkW4xK3",
    "outputId": "2f0f05bc-ab4f-4649-d391-92c8d0948b11"
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
   "execution_count": 3,
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
   "execution_count": 4,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 206
    },
    "id": "IFWDeTiJ6GHm",
    "outputId": "e0cbbbe7-a2f2-4ad0-af5d-420fc25e8312"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "  <div id=\"df-76a73e81-70bd-41a1-bca4-e6ee58d44b0a\" class=\"colab-df-container\">\n",
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
       "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-76a73e81-70bd-41a1-bca4-e6ee58d44b0a')\"\n",
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
       "        document.querySelector('#df-76a73e81-70bd-41a1-bca4-e6ee58d44b0a button.colab-df-convert');\n",
       "      buttonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "\n",
       "      async function convertToInteractive(key) {\n",
       "        const element = document.querySelector('#df-76a73e81-70bd-41a1-bca4-e6ee58d44b0a');\n",
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
       "<div id=\"df-210db498-ba51-4152-bb1f-15bf22611127\">\n",
       "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-210db498-ba51-4152-bb1f-15bf22611127')\"\n",
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
       "        document.querySelector('#df-210db498-ba51-4152-bb1f-15bf22611127 button');\n",
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
     "execution_count": 4,
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
   "execution_count": 5,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "EhalPUEY6GK4",
    "outputId": "6e73fe63-9ef8-4720-abe7-90d875dae227"
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
     "execution_count": 5,
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
    "id": "xRflsCw191mb"
   },
   "source": [
    "**Changing the datatypes of a column from int to boolean**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "lvZLXV6K6GOq",
    "outputId": "3f4d76ac-c6a0-418d-abe1-29609187620b"
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
     "execution_count": 6,
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
   "execution_count": 7,
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
   "execution_count": 8,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "s8FDUyOq6GVs",
    "outputId": "9301d228-4262-4df8-f02f-d1839fec7e20"
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
     "execution_count": 8,
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
   "execution_count": 9,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "qEuDQy4j6GZh",
    "outputId": "8a4c8548-09c3-48dd-e512-dd1172c28368"
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
     "execution_count": 9,
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
   "execution_count": 10,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 300
    },
    "id": "xIZyv0VS6Gdg",
    "outputId": "d0d5f702-3377-4a40-bc3c-eb578fc4f451"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "  <div id=\"df-fa910141-b587-4ac1-a3ac-207b36b75e6b\" class=\"colab-df-container\">\n",
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
       "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-fa910141-b587-4ac1-a3ac-207b36b75e6b')\"\n",
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
       "        document.querySelector('#df-fa910141-b587-4ac1-a3ac-207b36b75e6b button.colab-df-convert');\n",
       "      buttonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "\n",
       "      async function convertToInteractive(key) {\n",
       "        const element = document.querySelector('#df-fa910141-b587-4ac1-a3ac-207b36b75e6b');\n",
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
       "<div id=\"df-036b0e6a-cbe3-4c76-a70d-b54115ad17d7\">\n",
       "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-036b0e6a-cbe3-4c76-a70d-b54115ad17d7')\"\n",
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
       "        document.querySelector('#df-036b0e6a-cbe3-4c76-a70d-b54115ad17d7 button');\n",
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
     "execution_count": 10,
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
   "execution_count": 11,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 423
    },
    "id": "Ttlw76LD6Ghr",
    "outputId": "7358e759-b63e-4d49-ee79-4f98c5ed9cde"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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nCyvy6mSjScZRbJYZAuLPvovNLr6XV6vV0XLP1LkkKsU0u102dunqd3F98pVfEilW5ZKkipzdym462myx3VS+MBR8pQWyFNWKEk69MUrih4+QVZHiM++NoAZuSkbptDgaRRJuv766/XQQw9VPxNfvHixZs+era+//vq4j7v88suPe/31119XXFycNmzYoN69e9e431mzZqm8vFxvvvmmQkNDJUkvvfSSRo8erb/85S+Kj4+XJIWGhuq1116T3W6vNd+RKZWoqKjjpmluueUW3X777Xr++eflcDi0cuVKrVu3rs4Riq1bt0qSevTocbIvyXECAwP15JNPVr+elpampUuX6t1339W4ceNUWFiogoICXXzxxerSpYskKSMjo/rjs7KydP/991c/brdu3Rr0+LXxm5ENj1vyemSxHV+eLAEOVexer9CMYYdfP/r/1mKxymILVMXuDQrvN7LOu/Y6y7T7nzdJXq/s8V0UddZ42eM6SZJcBQfkLsk7blrE6giVo0N3VezdpNCeZ8vePk0lP30lT2WFyn9ZKVtYjKzBESpe/5UsAXaFpA9txi8E2qKilZ+oYNlcuUvyZG+fppgRt8nRoXutH8vUXxWXu+XLxvDhw9W/f/8W2VSQmpqqe+65R/fcc4/PH+vXduzYobS0NK1atUr9+/dv8cc/VqNGNuLi4jRq1CjNnDlTM2bM0KhRo9SuXbsaH7d161Zdc8016ty5syIiIqqnN7Kysmq9340bN6pfv37VRUOSzjjjDHk8Hm3evLn6bX369KmzaJzIZZddJpvNpg8/rPphnjlzps4555zqXL/mbcL53i+//LIGDRqkuLg4hYWFafr06dWfd0xMjCZMmKCRI0dq9OjRevHFF7Vv377q295777265ZZbNGLECD377LM1pp4aw+knazasjhA5OvRQwZLZchXlyutxq3j9V6rYu0nukjwFxiTLFhGn/G/ekLu8WF53pQp+eF/uohy5iw/Veb+BMUmKvei3aj/2/6ndxfdJXo/2v32/XIU5kiR3cV7V44dGHXc7W0iU3CX5kqSwPucrsH2a9v57sgqWvqt2lz4gT3mxCr7/j2JG3Ka8b9/Snn/dqgNz/p9cRTk++fqg9SrZ+K0OLXpNUWdco8QJL8rePk3Z7z5W/f1VG6b+JFcdI90N0dDNC3PnztVTTz3V5MetDzYvVGn01teJEydq5syZeuONNzRx4sRaP2b06NE6dOiQXn31VS1btkzLli2TVLWosymOLSMNYbfbNX78eM2YMUNOp1OzZs2qM7skpadXLVjctGlTgx5n9uzZ+v3vf6+bb75ZX3zxhVavXq2bbrrpuM97xowZWrp0qYYOHao5c+YoPT1dP/zwgyTpiSee0Pr16zVq1CgtWrRIPXv2rC5IjeVP86KxF98nSdrzyo3K+tsYFa34n0IzzpJkkcUWoLgxj6gyb492v3i1sqZervKstQrqPEiy1P3t6kjKUFjv82SP76ygjn0UN+YR2UIiVbz683rnstgCFHvBHUq+/d9KvHGagpJ7KW/RvxU+aLScB35W2dalSrzpH3J06KG8hdOb+mVAG1OY+V+F9xupsL7ny96uo2JGTpEl0KHidQvqvhFTf802jXJk80JZ2dEDDOvavBATE6Pw8PBmedy6HPl9HxcXp5CQ5v9/sHz5cg0aNEhbtmzRv/71L23YsEEffvihevToofvuu6/ZH6+pGl02LrzwQjmdTlVWVmrkyJpD27m5udq8ebMeffRRnXfeecrIyFBeXt4J7zMjI0Nr1qxRSUlJ9dsWL14sq9VavRC0vgIDA+V215w6uOWWW7Rw4UK98sorcrlcGjt2bJ330b9/f/Xs2VNTp06tdZ1Jfn5+rbdbvHixhg4dqsmTJ2vAgAHq2rVrraMTAwYM0EMPPaQlS5aod+/emjVrVvX70tPT9bvf/U5ffPGFxo4dW2OtSWsWGJ2ohGufVcrv3lfS5JlKHD9NXo9bgVFVU16OhK7qcNM/lHLPHCXf+Zbix/1RnrIiBUTVf+eSxRYge3xnVeZXjRjZwqp+iXt+9SzTXZov269GO44o37lWlbk7FT7wYpVnrVVw58Gy2oMU0uNMlWeta/gnjjbL666Uc/82BXXqX/02i8WqoNT+qthT95OVI1N/u1+ZoOwPnpLz4M7q951s6k+S7O3TVLF7Q6ue+muuJ0IN2bwwfPjw46Y1UlNT9cwzz2jixIkKDw9Xx44dNX368U8o2LzQtM0LjVqzIUk2m00bN26sfvnXoqOjFRsbq+nTpysxMVFZWVl68MEHT3if1113nR5//HHdeOONeuKJJ3Tw4EHddddduuGGG6rXa9RXamqqvvzyS51xxhlyOByKjq76Y5ORkaHTTz9dDzzwgCZOnFi9fbc2FotFM2bM0IgRIzRs2DA98sgj6tGjh4qLi/Xxxx/riy++qHXra7du3fTmm29q/vz5SktL01tvvaXMzEylpaVJkn755RdNnz5dl1xyiTp06KDNmzdr69atGj9+vMrKynT//ffriiuuUFpamnbv3q3MzMwa61/aAqs9SFZ7kNzlxSr7ZaWihx+/yNjqqBrBqjy0R8792xQ17Pp637fX45bz4E4Fdx4kSQqIjJctNFrlO1fLHt9ZUtUW3Iq9mxXev+Y5L16XU4cW/FPtRv9eFqtN8nrkPfIz73HL6/WPaSmj2K0eRQS4FW5zKSzArfAAt8JsLoXa3Aq1VirE5lKo1a1ga6WCLZUKtrgUZK1UkCoVZKmUQ5Wyq1IOOWX3OhUopwI9TgV4D//zOGX1OGVpJZcq3lvgVFevR++m/k+nJX1V/fZH4nfou22F+jbpmRq3WeYs0raYzurdIVSFZS69sGiLFs+6W9881F/J0Q79UFGocyV93+VNJUYenTa+PnafLJ59eispV5UJHt1fckjzZ16rlLAAvXNzmnpE/1HDlq7V0rt767XFt+v9lTnq3C5I/7y2i5KiHC3x5WgQV3QXScOa5b6ObF647rrrJB3dvPDr9YS1mTp1qp566ik9/PDDev/993XHHXfo7LPPVvfu3as3LwwZMkSZmZnKzs7WLbfcojvvvFMzZ86svo8vv/xSERERWrCg9tGszMxMtW/fXjNmzNCFF14om82muLi46s0LgwcPrv7Y+mxemDVrVqM3L8TGxmrJkiWaNGmSEhMTNW7cuOrNC7feeqveeecdOZ1O/fjjj8dtXhgwYID++c9/ymazafXq1fXevNDosiFJERERdb7ParVq9uzZuvvuu9W7d291795df//73zV8+PA6bxMSEqL58+frt7/9rU455RSFhITo8ssv1/PPP9/gbFOnTtW9996rV199VUlJSdqxY0f1+26++WYtWbLkhFMoR5x66qlavny5nn76ad16663KyclRYmKihg4dWufiottuu02rVq3SVVddJYvFomuuuUaTJ0/W559/Xv15btq0SW+88YZyc3OVmJioKVOm6LbbbpPL5VJubq7Gjx+vAwcOqF27dho7duxxC05bu7KfV0iSAmKS5Mrbp7yvX1dgTLLC+oyQJJVs+l62kAjZItqr8uAOHVo4XSHdTldw2sDq+8j5ZKps4bGKPnuCJCl/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\n",
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
   "execution_count": 12,
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
   "execution_count": 13,
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
   "execution_count": 14,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "A75jz_evCP6f",
    "outputId": "03dd2043-f576-4f45-d370-aec4682dfe66"
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
   "execution_count": 15,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "rlGisVHz6Gs8",
    "outputId": "6c08db63-b7be-4644-cd88-15801996cee1"
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
   "execution_count": 16,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ln5MnPns6Gw3",
    "outputId": "497a5170-6885-4fb2-9b99-68020a95ac25"
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
   "execution_count": 18,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 452
    },
    "id": "yZqL94uSCYet",
    "outputId": "dab948f5-03f2-41b6-fa92-6d83780fa6f4"
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
   "execution_count": 19,
   "metadata": {
    "id": "9Dm2uftFNSht"
   },
   "outputs": [],
   "source": [
    "X_train = X_train.astype(float)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "id": "LqqToqUFTWjO"
   },
   "outputs": [],
   "source": [
    "from imblearn.under_sampling import NearMiss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "id": "fWpyXA6NNT0y"
   },
   "outputs": [],
   "source": [
    "nm = NearMiss(version=1, sampling_strategy='auto')\n",
    "X_resampled, y_resampled = nm.fit_resample(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 480
    },
    "id": "hWxs9M38IXjG",
    "outputId": "47ec63db-f7c1-4fd0-8af9-cfcfa2910725"
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
      "Shape of Resampled X:  (6000, 10)\n",
      "Shape of Resampled y:  (6000,)\n"
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
    "print(\"Proportion of Minority Class: \" + str(round(np.sum(y_resampled == 1) / len(y_resampled) * 100, 2)) + \"%\")\n",
    "print(\"Shape of Resampled X: \", X_resampled.shape)\n",
    "print(\"Shape of Resampled y: \", y_resampled.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "1meyk0nmIuhN",
    "outputId": "bf0add6a-e81f-4200-dd0e-78c951b9a214"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Minority:3000\n"
     ]
    }
   ],
   "source": [
    "print(f\"Minority:{np.sum(y_resampled == 1)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "VaETtkF3I3AM",
    "outputId": "61b1e7ae-9c22-460b-9b9c-fee06395da03"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Majority:3000\n"
     ]
    }
   ],
   "source": [
    "print(f\"Majority:{np.sum(y_resampled == 0)}\")"
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
   "execution_count": 25,
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
   "execution_count": 26,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "_hHbl0jmb9QH",
    "outputId": "1fb25b13-60d6-4e9b-aeaf-74644c83d179"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Parameters for Gradient Boosting: {'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 150}\n"
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
   "execution_count": 27,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "kB_LoFfwCY2-",
    "outputId": "851092c6-0679-406b-c281-2a46ade3ac18"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Gradient Boosting): 16.22%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       1.00      0.16      0.27    199000\n",
      "        True       0.01      0.84      0.01      1000\n",
      "\n",
      "    accuracy                           0.16    200000\n",
      "   macro avg       0.50      0.50      0.14    200000\n",
      "weighted avg       0.99      0.16      0.27    200000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the best model from the grid search\n",
    "nm_gbc_model = grid_search_gbc.best_estimator_\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(nm_gbc_model, 'nm_gradient_boosting_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "nm_gbc_predictions = nm_gbc_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Gradient Boosting): {:.2f}%\".format(accuracy_score(y_val, nm_gbc_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, nm_gbc_predictions))\n"
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
   "execution_count": 28,
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
   "execution_count": 29,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "5hshDaqwdBA5",
    "outputId": "ee879a6c-32f0-4696-80ab-195a4c46cbd7"
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
   "execution_count": 30,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "C-dMJxURCY-I",
    "outputId": "41360ecd-0d1b-4c4d-c15f-1be346ae9a82"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Random Forest): 10.51%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       1.00      0.10      0.18    199000\n",
      "        True       0.01      0.90      0.01      1000\n",
      "\n",
      "    accuracy                           0.11    200000\n",
      "   macro avg       0.50      0.50      0.10    200000\n",
      "weighted avg       0.99      0.11      0.18    200000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the best model from the grid search\n",
    "nm_rfc_model = grid_search_rfc.best_estimator_\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(nm_rfc_model, 'nm_random_forest_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "nm_rfc_predictions = nm_rfc_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Random Forest): {:.2f}%\".format(accuracy_score(y_val, nm_rfc_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, nm_rfc_predictions))\n"
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
   "execution_count": 31,
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
   "execution_count": 32,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ivqbfVtfdkmS",
    "outputId": "0542a045-9b74-4fc0-db44-95ed209d7dc8"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Parameters for Stacking: {'final_estimator__C': 10, 'final_estimator__penalty': 'l2', 'final_estimator__solver': 'liblinear'}\n"
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
   "execution_count": 33,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "y6WlXi0adkp0",
    "outputId": "c38bb09d-1569-4c03-fd36-331bf2ae14bb"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Stacking): 15.42%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       0.99      0.15      0.26    199000\n",
      "        True       0.00      0.85      0.01      1000\n",
      "\n",
      "    accuracy                           0.15    200000\n",
      "   macro avg       0.50      0.50      0.14    200000\n",
      "weighted avg       0.99      0.15      0.26    200000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the best model from the grid search\n",
    "nm_stack_model = grid_search_stack.best_estimator_\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(nm_stack_model, 'nm_stacking_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "nm_stack_predictions = nm_stack_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Stacking): {:.2f}%\".format(accuracy_score(y_val, nm_stack_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, nm_stack_predictions))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
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
   "execution_count": 35,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "ByyoReuUdkxD",
    "outputId": "ead8ed27-0993-4b06-9b45-8244b5b27f6e"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Gradient Boosting): 0.16%\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAhAAAAIjCAYAAABS7iKKAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA6KklEQVR4nO3deViU5eL/8c8gMCACbrimuC9kuZbHDTVx361jahaamqWZuXTMNpUsSnPfy0wz7ViZZlbmflyyzDU1cy+XFHfMBUS4f3/4Y76OA8pdIJTv13VxXc6z3s84wHueeWZwGGOMAAAALHhl9gAAAMDfDwEBAACsERAAAMAaAQEAAKwREAAAwBoBAQAArBEQAADAGgEBAACsERAAAMAaAYEsad++fWrUqJGCg4PlcDi0cOHCdN3+r7/+KofDoZkzZ6brdv/O6tWrp3r16qXrNo8cOSI/Pz+tX78+XbebnooVK6YuXbq4bq9evVoOh0OrV6/OtDH9k9yp+7NDhw5q3759hu4D7ggIpOrAgQPq2bOnSpQoIT8/PwUFBalWrVoaN26crly5kqH7joyM1I4dO/TGG29o9uzZqlatWobu707q0qWLHA6HgoKCUrwf9+3bJ4fDIYfDoXfeecd6+7///ruGDh2qbdu2pcNo/5qoqChVr15dtWrV8pi3du1atW/fXoULF5avr6+Cg4NVvXp1RUVFKSYmJhNGe2e9+eabaQ7j5OC98SsoKEiVKlXSxIkTlZiYmLGDTYPJkydnapAPGjRI8+fP1/bt2zNtDHcdA6Rg8eLFxt/f3+TMmdM899xz5t133zUTJ040HTp0MD4+PqZHjx4Ztu/Lly8bSebll1/OsH0kJSWZK1eumGvXrmXYPlITGRlpvL29TbZs2cy8efM85g8ZMsT4+fkZSWbkyJHW2//xxx+NJPPBBx9YrRcfH2/i4+Ot95eakydPGh8fHzN37lyPea+++qqRZEqUKGFeeuklM336dDNx4kTTtWtXExQUZEqUKJFu47id0NBQExkZ6bqdmJhorly5YhITEzN0vwEBAW77vZVDhw4ZSaZjx45m9uzZZvbs2WbixImmWbNmRpIZOHBgho41Le69915Tt25dj+l36v40xpgHH3zQPP744xm+H1znnZnxgqzp0KFD6tChg0JDQ7Vy5UoVLFjQNa93797av3+/vvrqqwzb/6lTpyRJOXPmzLB9OBwO+fn5Zdj2b8fpdKpWrVr6+OOPPU67zp07V82bN9f8+fPvyFguX76s7Nmzy9fXN123+9FHH8nb21stW7Z0mz5v3jy9/vrrat++vWbPnu2x3zFjxmjMmDG33LYxRnFxcfL390/XMUuSl5dXpj42bqVKlSrq3Lmz63avXr1UvXp1zZ07VyNHjszEkaXuTt6f7du315AhQzR58mTlyJHjjuzzrpbZBYOs5+mnnzaSzPr169O0fEJCgomKijIlSpQwvr6+JjQ01AwePNjExcW5LRcaGmqaN29u1q5dax544AHjdDpN8eLFzaxZs1zLDBkyxEhy+woNDTXGXH/mnvzvGyWvc6OlS5eaWrVqmeDgYBMQEGDKlCljBg8e7Jqf/Izu5mfpK1asMLVr1zbZs2c3wcHBplWrVubnn39OcX/79u0zkZGRJjg42AQFBZkuXbqYS5cu3fb+ioyMNAEBAWbmzJnG6XSac+fOueZt3LjRSDLz58/3OANx5swZM2DAAFOhQgUTEBBgAgMDTZMmTcy2bdtcy6xatcrj/rvxOOvWrWvuvfdes2nTJlOnTh3j7+9v+vbt65p34zPIJ554wjidTo/jb9SokcmZM6c5duzYLY8zPDzc1KtXz2N6mTJlTN68ec0ff/xx2/sqWfJjZ8mSJaZq1arG6XSaMWPGGGOMmTFjhqlfv74JCQkxvr6+pnz58mby5Mke20hKSjKvv/66KVy4sPH39zf16tUzO3fu9DgDkXwfrlq1ym3977//3jRu3NgEBQUZf39/Ex4ebtatW+e2TFofGyn9H93qbETy4zWlM1ItWrQwRYsW9Zg+adIkExYWZnx9fU3BggVNr1693B5ryT755BNTpUoV4+fnZ/LkyWMee+wxc/ToUbdljh8/brp06WIKFy5sfH19TYECBUyrVq3MoUOHjDHX/39uPp7kx1JK92fy43DXrl2mXr16xt/f3xQqVMi8/fbbHuP79ddfTcuWLU327NlNSEiIef75582SJUtS/D/avn27kWQ+//zzVO9LpB+ugYCHL7/8UiVKlFDNmjXTtHz37t312muvqUqVKhozZozq1q2r6OhodejQwWPZ/fv365FHHlHDhg01atQo5cqVS126dNGuXbskSe3atXM9++zYsaNmz56tsWPHWo1/165datGiheLj4xUVFaVRo0apVatWt72Qb/ny5WrcuLFOnjypoUOHqn///vruu+9Uq1Yt/frrrx7Lt2/fXn/88Yeio6PVvn17zZw5U8OGDUvzONu1ayeHw6HPP//cNW3u3LkqV66cqlSp4rH8wYMHtXDhQrVo0UKjR4/WCy+8oB07dqhu3br6/fffJUnly5dXVFSUJOmpp57S7NmzNXv2bIWHh7u2c+bMGTVt2lSVKlXS2LFjVb9+/RTHN27cOIWEhCgyMtL1Gvu0adO0dOlSTZgwQYUKFUr12BISEvTjjz96HMfevXu1d+9etWnTxvoZ4p49e9SxY0c1bNhQ48aNU6VKlSRJU6ZMUWhoqF566SWNGjVKRYoUUa9evTRp0iS39V977TW9+uqrqlixokaOHKkSJUqoUaNGunTp0m33vXLlSoWHh+vChQsaMmSI3nzzTZ0/f14PPfSQNm7c6LH87R4bs2fPltPpVJ06dVz/Rz179rztOC5fvqzTp0/r9OnTOnjwoCZNmqQlS5YoMjLSbbmhQ4eqd+/eKlSokEaNGqWHH35Y06ZNU6NGjZSQkOBabubMmWrfvr2yZcum6Oho9ejRQ59//rlq166t8+fPu5Z7+OGHtWDBAnXt2lWTJ0/Wc889pz/++EOHDx+WJI0dO1b33HOPypUr5zqel19++ZbHcu7cOTVp0kQVK1bUqFGjVK5cOQ0aNEjffPONa5lLly7poYce0vLly/Xcc8/p5Zdf1nfffadBgwaluM2wsDD5+/tn6Yt2/1Eyu2CQtcTGxhpJpnXr1mlaftu2bUaS6d69u9v0gQMHGklm5cqVrmnJz1LWrFnjmnby5EnjdDrNgAEDXNNSe7aV1jMQY8aMMZLMqVOnUh13SmcgKlWqZPLly2fOnDnjmrZ9+3bj5eVlnnjiCY/9Pfnkk27bbNu2rcmTJ0+q+7zxOAICAowxxjzyyCOmQYMGxpjrrxUXKFDADBs2LMX7IC4uzuN15EOHDhmn02mioqJc0251DUTdunWNJDN16tQU5938Gva3335rJJnhw4ebgwcPmhw5cpg2bdrc9hj3799vJJkJEya4Tf/iiy+MJDN27Fi36UlJSebUqVNuXwkJCa75yY+dJUuWeOzr8uXLHtMaN27sdh3FyZMnja+vr2nevLlJSkpyTX/ppZc8nv3f/Iw5KSnJlC5d2jRu3Nht3cuXL5vixYubhg0buqbZPDb+zDUQKX0988wzbuNKPtZGjRq5PV4mTpxoJJkZM2YYY4y5evWqyZcvn6lQoYK5cuWKa7nFixcbSea1114zxhhz7ty5NF2Pk9o1EKmdgZBkPvzwQ9e0+Ph4U6BAAfPwww+7po0aNcpIMgsXLnRNu3LliilXrlyKZyCMuX6Gq2nTprccK9IHZyDg5sKFC5KkwMDANC3/9ddfS5L69+/vNn3AgAGS5HGtRFhYmOrUqeO6HRISorJly+rgwYN/esw3S7524osvvlBSUlKa1jl+/Li2bdumLl26KHfu3K7p999/vxo2bOg6zhs9/fTTbrfr1KmjM2fOuO7DtOjUqZNWr16tEydOaOXKlTpx4oQ6deqU4rJOp1NeXte/ZRMTE3XmzBnlyJFDZcuW1ZYtW9K8T6fTqa5du6Zp2UaNGqlnz56KiopSu3bt5Ofnp2nTpt12vTNnzkiScuXK5TY9+b65+exDbGysQkJC3L5ufhdJ8eLF1bhxY4993XgdRGxsrE6fPq26devq4MGDio2NlXT97NLVq1fVp08fORwO1/LPP//8bY9l27Zt2rdvnzp16qQzZ864zgBcunRJDRo00Jo1azweZ+nx2EjJU089pWXLlmnZsmWaP3++evfurWnTprl9/yUf6/PPP+96vEhSjx49FBQU5Pqe3LRpk06ePKlevXq5XaPQvHlzlStXzrWcv7+/fH19tXr1ap07d+4vjf9GOXLkcLuew9fXVw8++KDbz4IlS5aocOHCatWqlWuan5+fevTokep2c+XKpdOnT6fbOJE6AgJugoKCJEl//PFHmpb/7bff5OXlpVKlSrlNL1CggHLmzKnffvvNbXrRokU9tpErV650/cH06KOPqlatWurevbvy58+vDh066JNPPrllTCSPs2zZsh7zypcv7/qFcaObjyX5l6XNsTRr1kyBgYGaN2+e5syZowceeMDjvkyWlJSkMWPGqHTp0nI6ncqbN69CQkL0008/uX5RpkXy2ybT6p133lHu3Lm1bds2jR8/Xvny5UvzusYYt9vJYXrx4kW36Tly5HD9YnzhhRdS3Fbx4sVTnL5+/XpFREQoICBAOXPmVEhIiF566SVJct0vyf+/pUuXdls3JCTEI3Jutm/fPknX31p8c+RMnz5d8fHxHvd/ejw2UlK6dGlFREQoIiJC7dq108SJE9WrVy+NHTtWO3bskJT6Y9nX11clSpRwzb/VY75cuXKu+U6nU2+//ba++eYb5c+fX+Hh4RoxYoROnDjxl47lnnvucYs5yfNnwW+//aaSJUt6LJfa94h0/TF38/LIGAQE3AQFBalQoULauXOn1Xpp/YbNli1bitNv/kVjs4+b3wPv7++vNWvWaPny5Xr88cf1008/6dFHH1XDhg3T9f3yf+VYkjmdTrVr106zZs3SggULUj37IF3/3ID+/fsrPDxcH330kb799lstW7ZM9957b5rPtEiyfufC1q1bdfLkSUly/ZK6nTx58kjy/IVZrlw5SfJ4fHl7e7t+MYaFhaV53AcOHFCDBg10+vRpjR49Wl999ZWWLVumfv36SZLV/ZKa5G2MHDnSFTk3f918RiU9Hhtp1aBBA0nSmjVr0n3byZ5//nnt3btX0dHR8vPz06uvvqry5ctr69atf3qbGXUfnTt3Tnnz5v1L20DaEBDw0KJFCx04cEAbNmy47bKhoaFKSkpyPUtLFhMTo/Pnzys0NDTdxpUrVy63C7uS3XyWQ7r+1rEGDRpo9OjR+vnnn/XGG29o5cqVWrVqVYrbTh7nnj17POb98ssvyps3rwICAv7aAaSiU6dO2rp1q/74448ULzxN9tlnn6l+/fp6//331aFDBzVq1EgREREe90l6Pvu6dOmSunbtqrCwMD311FMaMWKEfvzxx9uuV7RoUfn7++vQoUNu08uWLavSpUtr4cKFabp48Xa+/PJLxcfHa9GiRerZs6eaNWumiIgIj9hI/v+9+XF66tSp254VKFmypKTrcZ0cOTd/+fj4WI89vf6frl27Jun/zuqk9li+evWqDh065Jp/q8f8nj17PL53S5YsqQEDBmjp0qXauXOnrl69qlGjRqX78dwoNDRUBw4c8IiK/fv3p7j8tWvXdOTIEZUvXz7dxwJPBAQ8/Oc//1FAQIC6d++e4icCHjhwQOPGjZN0/RS8JI93SowePVrS9ddT00vJkiUVGxurn376yTXt+PHjWrBggdtyZ8+e9Vg3+Yr9+Pj4FLddsGBBVapUSbNmzXL7hbxz504tXbrUdZwZoX79+nr99dc1ceJEFShQINXlsmXL5vGD9NNPP9WxY8fcpiWHTkqxZWvQoEE6fPiwZs2apdGjR6tYsWKKjIxM9X5M5uPjo2rVqmnTpk0e84YOHarTp0+rR48ebu8ISGbzDDT5WeyN68TGxuqDDz5wWy75l/yECRPclk3LO3yqVq2qkiVL6p133vF46UX6v88tsRUQEJAu/0dffvmlJKlixYqSrh+rr6+vxo8f73as77//vmJjY13fk9WqVVO+fPk0depUt//Pb775Rrt373Ytd/nyZcXFxbnts2TJkgoMDHRbL72O50aNGzfWsWPHtGjRIte0uLg4vffeeyku//PPPysuLi7N7yDDX8MHScFDyZIlNXfuXD366KMqX768nnjiCVWoUEFXr17Vd999p08//dT1twMqVqyoyMhIvfvuuzp//rzq1q2rjRs3atasWWrTpk2qbxH8Mzp06KBBgwapbdu2eu6553T58mVNmTJFZcqUcbuIMCoqSmvWrFHz5s0VGhqqkydPavLkybrnnntUu3btVLc/cuRINW3aVDVq1FC3bt105coVTZgwQcHBwRo6dGi6HcfNvLy89Morr9x2uRYtWigqKkpdu3ZVzZo1tWPHDs2ZM0clSpRwW65kyZLKmTOnpk6dqsDAQAUEBKh69eqpXkOQmpUrV2ry5MkaMmSI6+2YH3zwgerVq6dXX31VI0aMuOX6rVu31ssvv6wLFy64rq2Rrp9x2blzp6Kjo7Vx40Z16NBBxYsX16VLl7Rz5059/PHHCgwMvO21CdL1izx9fX3VsmVL9ezZUxcvXtR7772nfPny6fjx467lQkJCNHDgQEVHR6tFixZq1qyZtm7dqm+++ea2p7u9vLw0ffp0NW3aVPfee6+6du2qwoUL69ixY1q1apWCgoJcv8RtVK1aVcuXL9fo0aNVqFAhFS9eXNWrV7/lOlu2bNFHH30k6fp1SitWrND8+fNVs2ZNNWrUyHWsgwcP1rBhw9SkSRO1atVKe/bs0eTJk/XAAw+4Llz08fHR22+/ra5du6pu3brq2LGjYmJiNG7cOBUrVsz1MtDevXvVoEEDtW/fXmFhYfL29taCBQsUExPjdsasatWqmjJlioYPH65SpUopX758euihh6zvlxv17NlTEydOVMeOHdW3b18VLFhQc+bMcV30efNZj2XLlil79uxq2LDhX9ov0ihz3vyBv4O9e/eaHj16mGLFihlfX18TGBhoatWqZSZMmOD2IVEJCQlm2LBhpnjx4sbHx8cUKVLklh8kdbOb3z54qw/NWbp0qalQoYLx9fU1ZcuWNR999JHH2zhXrFhhWrdubQoV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+fJlNWzY0G361atXVblyZUnS7t273cYhSTVq1EjzPgCkDQEB3KXq16+vKVOmyNfXV4UKFZK39//9OAgICHBb9uLFi6patarmzJnjsZ2QkJA/tX9/f3/rdS5evChJ+uqrr1S4cGG3eU6n80+NA8CfQ0AAd6mAgACVKlUqTctWqVJF8+bNU758+RQUFJTiMgULFtQPP/yg8PBwSdK1a9e0efNmValSJcXl77vvPiUlJel///ufIiIiPOYnnwFJTEx0TQsLC5PT6dThw4dTPXNRvnx5LVq0yG3a999/f/uDBGCFiygB3NZjjz2mvHnzqnXr1lq7dq0OHTqk1atX67nnntPRo0clSX379tVbb72lhQsX6pdfflGvXr1u+RkOxYoVU2RkpJ588kktXLjQtc1PPvlEkhQaGiqHw6HFixfr1KlTunjxogIDAzVw4ED169dPs2bN0oEDB7RlyxZNmDBBs2bNkiQ9/fTT2rdvn1544QXt2bNHc+fO1cyZMzP6LgLuOgQEgNvKnj271qxZo6JFi6pdu3YqX768unXrpri4ONcZiQEDBujxxx9XZGSkatSoocDAQLVt2/aW250yZYoeeeQR9erVS+XKlVOPHj106dIlSVLhwoU1bNgwvfjii8qfP7+effZZSdLrr7+uV199VdHR0SpfvryaNGmir776SsWLF5ckFS1aVPPnz9fChQtVsWJFTZ06VW+++WYG3jvA3clhUrvCCQAAIBWcgQAAANYICAAAYI2AAAAA1ggIAABgjYAAAADWCAgAAGCNgAAAANYICAAAYI2AAAAA1ggIAABgjYAAAADW/h+nWakzVv2sywAAAABJRU5ErkJggg==\n",
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
      "       False       1.00      0.16      0.27    199000\n",
      "        True       0.01      0.84      0.01      1000\n",
      "\n",
      "    accuracy                           0.16    200000\n",
      "   macro avg       0.50      0.50      0.14    200000\n",
      "weighted avg       0.99      0.16      0.27    200000\n",
      "\n",
      "Accuracy on Validation Set (Random Forest): 0.11%\n"
     ]
    },
    {
     "data": {
      "image/png": "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s7xORvzk1nPq9OnTmeINBQd7IHDD2rRpo71792rt2rXXnNff31/p6enas2eP0/TY2FidOXPGcUZFbihatGimo8ulzO8EJcnFxUVNmjTR5MmTtX37dr3yyitavny5Y5fslTLGuWvXrkyX7dy5UyVKlJCPj8+NbUA2unXrpk2bNun8+fPq2rVrtvN9+umnaty4sd5//3117dpVzZo1U3h4eKbbJDff4SUkJKhnz54KDg5Wv379NGHCBK1fv/6a16tUqZK8vLy0f//+HK2nbNmyGjJkiL7++mv99ttvjumffvqpIiIiNGnSJHXq1ElNmzbV/fffn+XjICcy7ucrH68nTpzIFDv+/v7ZPh4uX1Z+ye4xm5KSov379+dofFWqVNGpU6fUpEmTTHs6wsPDnfZuXOs5da3H3cWLF3X48GHHHhwUPAQEbthzzz0nHx8f9enTR7GxsZku37t3r6ZOnSrp0i54SXrzzTed5sl4R9O6detcG1eVKlV09uxZbd261THt6NGjmc70OHXqVKbrZnyxTXanz5UtW1Z33323oqOjnV6c/vzzTy1ZssSxnXmhcePGGjdunGbMmKEyZcpkO5+rq2umd62LFi3S33//7TQtI3Su90X2cs8//7wOHTqk6OhoTZ48WQEBAYqIiLjmaYju7u6qW7eu/vjjjxyva9CgQfL29tZrr73mmJbVNk+fPj3TXqecCg8Pl7u7u6ZPn+603Csfv9Klx/a6deucQjohIUHvvPOOAgICFBwcfF1jyC3h4eHy8PDQtGnTnLbl/fff19mzZ3P03OvSpYv+/vtvvfvuu5kuu3DhguNju5w8p671uNu+fbuSkpJyfHYXbj4+wsANq1Klij7++GM9/PDDCgoKcvomyl9//VWLFi1y/M2A2rVrKyIiQu+8847OnDmjhg0bat26dYqOjlb79u3VuHHjXBtX165d9fzzz6tDhw56+umnlZiYqFmzZqlatWpOB9SNHTtWv/zyi1q3bi1/f38dP35cM2fOVIUKFZwOiLvSG2+8oZYtW6p+/frq3bu34zTOwoULX/WjhRvl4uKil1566ZrztWnTRmPHjlXPnj113333adu2bZo/f74qV67sNF+VKlVUpEgRzZ49W35+fvLx8VFoaKgCAwONxrV8+XLNnDlTo0ePdpxWOmfOHDVq1Egvv/yyJkyYcNXrt2vXTi+++KLOnTvnOLbmaooXL66ePXtq5syZ2rFjh4KCgtSmTRvNmzdPhQsXVnBwsNauXauffvrJ8RGJqZIlS2r48OGKiopSmzZt1KpVK23atEnff/+9SpQo4TTviBEj9Mknn6hly5Z6+umnVaxYMUVHR2v//v367LPPnA5czA8lS5bUyJEjFRkZqRYtWuihhx7Srl27NHPmTN177705+gKqxx57TAsXLlT//v21YsUKhYWFKS0tTTt37tTChQv1448/qm7dujl6Tl3rcbd06VJ5e3uradOmeXq74Abk09kfuAXt3r3b6tu3rxUQEGB5eHhYfn5+VlhYmDV9+nQrKSnJMV9qaqoVGRlpBQYGWu7u7lbFihWtkSNHOs1jWZdO42zdunWm9Vx5+mB2p3FalmUtWbLEqlmzpuXh4WFVr17d+uijjzKdxrls2TKrXbt2Vrly5SwPDw+rXLly1iOPPGLt3r070zquPOXsp59+ssLCwiwvLy+rUKFCVtu2ba3t27c7zZOxvitPacs4lXD//v3Z3qaW5XwaZ3ayO41z2LBhVtmyZS0vLy8rLCzMWrt2bZanX3755ZdWcHCw5ebm5rSdDRs2tO68884s13n5cs6dO2f5+/tbderUsVJTU53mGzJkiOXi4mKtXbv2qtsQGxtrubm5WfPmzcvx9u/du9dydXV1nE55+vRpq2fPnlaJEiUsX19fq3nz5tbOnTstf39/p1MuM2779evXOy0v4xTLFStWOKalpaVZkZGRjtuxUaNG1p9//plpmRnj6dSpk1WkSBHL09PTqlevnvXNN99kuY5FixY5Tc9uTNk9fq6Uk8eJZV06bbNGjRqWu7u7Vbp0aWvAgAHW6dOnnea52v2ekpJivf7669add95p2e12q2jRolZISIgVGRlpnT171rKsnD2nLCv7x51lWVZoaKjVvXv3a24P8o/Nsm7ykTkAkI3evXtr9+7dWrVqVX4PBflo8+bNqlOnjjZu3Gj091lwcxEQAAqMQ4cOqVq1alq2bJnTX+TE7SXjrJmFCxfm91BwFQQEAAAwxlkYAADAGAEBAACMERAAAMAYAQEAAIwREAAAwNgt+U2Uh05d/WtzAeSv6k2G5fcQAGTjwqYZOZqPPRAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMCYW34PALeeT6Lf0+qfl+nwwf2y2+0KrnW3+jw5WBX9Ax3zpCQna/a0iVr50w9KTU1R3dD79PSzL6loseKOed6a/Jr+2rpJB/bFqGJAZb394SKn9aQkJ+vNCeO0Z+d2HTq4X/8Ka6DI16c6zfPnlo169603dfjgfiUnJal0mbJq3b6z/v3IY3l7IwAFRFidKhryeLjqBFdS2ZKF1WXIO/p65VbH5Rc2zcjyei9M+UJTPlwmSapaqZReHdJe9WtXloe7q/7cc0SRM7/RL3/sccwfElxJ455up3uCK8qypD/+PKgXpy7Wtt1/O+YJrx+kl/u3UlCVskpKSdWajXv1/KTPdejoKUnSO5Hd9dhD/8o0lu17jyqk0yu5cnsg97AHArlu66Y/9NC/u2raux/ptanv6OLFixoxuL8uXEh0zDNr6gT9tuZnvfzKRE2aOUdxJ09ozIghmZbVvE0HNWzSPMv1pKWnyW63q0OXbqpTNzTLeTw9vdSuU1dNnjVH7//fYnXr2U9z35mubxd/mjsbCxRwPl52bdv9twZHLcjy8oDwkU4//UZ/pPT0dH2xbLNjns+n9Zebq4taPjFN9z06QVt3/63Pp/VX6eJ+/12Hh758a6AOHzutBo9NVJOekxWfmKSv3hooN7dLLzP+5Ypr0ZR+Wrl+t0K7vqaHnnxLxYv46P8m9XWsZ/gbnzqNpWrzlxR3JkGfL92UdzcQrht7IJDrot6c7fT7sy+NU+dWjbRn53bddU9dJcSf1w9ff6GRka/pnv++8A9/cZx6P9JO2//couCatSVJA4eOkCSdPXNK+/bu0ZW8vLz1zHMvS5L+3LpZCfHnM81TtXqQqlYPcvxepmx5rV65TNu2bFTr9p1yZ4OBAmzJmu1asmZ7tpfHxjk/b9o2qqWf1+/Rgb/jJEnFi/joDv9SGhA5X3/uOSJJennal+r/cAMFVy2n2Lhdqh5YRsWL+GjcrG/0n9gzkqRX3v5efyx6QZXKFtO+wydVJ7iiXF1cNOatb2RZliTpzQ+XadGUfnJzc9HFi+k6F5+kc/FJl43lLhUt5KV5X63NzZsEuSRf90CcPHlSEyZMUIcOHVS/fn3Vr19fHTp00BtvvKETJ07k59CQixLi4yVJfoUKS5J279yuixcvqs69/9tVWSkgUKXKlNWObVuzXEZuidm1Q9u3bdZd94Tk6XqAf6JSxfzU4v6ail78vxfsuDMJ2rX/mLq1qSdvTw+5urqoz7/vV2zcOW3afkiStPtArE6ejldE+/vk7uYqT7u7erSvrx37jurgkUsfT2zcfljpVroeb/cvubjYVMjXU91a19Py33fp4sX0LMcT0b6+lv++S4eOns77jYexfNsDsX79ejVv3lze3t4KDw9XtWrVJEmxsbGaNm2aXnvtNf3444+qW7fuVZeTnJys5OTkK6ZJdrs9z8aOnEtPT9esNyfozrvuUWCVOyRJp+NOyt3dXb5+hZzmLVq0uE6dOpkn43jkoXCdPXNaaWlpeqz3ALV66N95sh7gn6x721CdT0zS4uWbnaa37j9DC6b004k1E5WebunE6Xi1GzhTZ85fkCTFJyared+pWji5n0b2bSFJijl0XA8NfEtpaZfi4OCROLV58i199HovzXixq9zcXPXbln1q/9SsLMdStmRhNQ8LVo8X5ubZ9uLG5FtADBo0SJ07d9bs2bNls9mcLrMsS/3799egQYO0du3Vd11FRUUpMjLSadrg517UkOdfzvUxw9z0ia/owL4YTXl7br6OY/LsuUpKTNSOv7bqvZlTVa5CRT3YrFW+jgkoaB5v9y8t+P4PJadcdJo+ZWQXnTh1XuG93tSF5BT16HCfPpv6hO7v/oaOnTwnT7u7Zo9+VGu37FPEyDlydXXR4Meb6PNpA3R/9zeUlJyq0sX9NPPlbpr/9e9a+MMG+frYNWpAG308sbda9898IOejbUN15vwFfbUib/dK4vrlW0Bs2bJFc+fOzRQPkmSz2TRkyBDdc88911zOyJEjNXToUKdpsQm5NkzcgOkTX9Xva37RpFlzVLJUGcf0osVLKDU1VfHnzznthTh9Ok7FipXIk7GULVdBkhRYtZpOnzqlee/PIiCAy4TdU0XVA8vosRFznKY3qldNrR6oqbINn9P5hEvHJwyOWqgm/6qh7m1DNXHOUj3csq4qlSumhhGTHMc3RIycq6O/TFDbRndp0Y8b9MTDDXQu/oJenPqlY9m9XoxWzI/jVa9WgNZtO+C03oh2/9In365T6sW0vN1wXLd8OwaiTJkyWrduXbaXr1u3TqVLl77mcux2uwoVKuT0w8cX+cuyLE2f+KrW/LxcE2a853jxzlCtRrDc3Ny06Y/fHdMOH9yv48eOKqjWXXk+vvT0dKWmpOb5eoB/koj29bVh+yGn0y4lydvTQ9Kl583l0tMtxxtAb08PpadbjniQpHTLkmVJLlfMc7m0/y7TxcX5jeQDIXeoaqVSmruYgycLsnzbAzF8+HD169dPGzZsUJMmTRyxEBsbq2XLlundd9/VxIkT82t4uAHTJ76i5Uu+V+TrU+Xt7aNTcZeOa/Dx8ZXd01M+vn5q0baDZk+bKL9CheXt46u3JkUpuGZtxxkYkvT34UO6cCFRp+LilJKcpJjdOyVJ/oFV5O7uLkk6uH+vUlNTdf7cWV1ITHTMU7VaDUnSl5/+n0qVLqOKAZe+g2Lbpg369ONote/S7abdHkB+8vHyUJWKJR2/B5Qvrruqldfpc4k6fOzSwYl+Pp7q2PQejZj8Rabr/751v06fS9R74x7Xq+98rwtJqerV8T4FlC+uH1b/JUla9ttOvTq4vd4c2UWz/u9nudhsGt6zmS6mpennP3ZLkr5f9ZcGPdpYI/u10MIfNsjP267Ipx7SwSNx2rzzP07r7NG+vtZt3a/te4/m1c2CXGCzLk/Gm2zBggWaMmWKNmzYoLS0S7upXF1dFRISoqFDh6pLly7XtdxDp5KvPRPyTNP6We9FGP7SODVv3U7SZV8ktfR7paamKCQ0TE8/+6KKFf/fRxjDnuylrZv+yLSceZ9/rzJly0uSundoodhjRzLNs3Ttpc9NFy/6WN8uXqRjR/6Wi6ubypWvoFbt/q3W7TvLxYWvQckv1ZsMy+8h3DYeCLlDS957JtP0eV/9pn6jP5Ik9eoYpjeG/1uBzV5wOo0yQ53gShozsK3qBFeSu5uLduw7plff+d7p9NAHQ2voxSdaKrhqWaWnW9qy8z8a89bXTh9NdG4eoiER4brDv5QSk1L0+9b9emnql9p9INYxTyFfT+1f8qqGv/Gp5nzxay7eEsip7L5c7Er5GhAZUlNTdfLkpXepJUqUcLy7vF4EBFCwERBAwZXTgCgQXyTl7u6usmXL5vcwAABADrEPFwAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgLHrCohVq1ape/fuql+/vv7++29J0rx587R69epcHRwAACiYjAPis88+U/PmzeXl5aVNmzYpOTlZknT27Fm9+uqruT5AAABQ8BgHxPjx4zV79my9++67cnd3d0wPCwvTxo0bc3VwAACgYDIOiF27dqlBgwaZphcuXFhnzpzJjTEBAIACzjggypQpo5iYmEzTV69ercqVK+fKoAAAQMFmHBB9+/bVM888o99//102m01HjhzR/PnzNXz4cA0YMCAvxggAAAoYN9MrjBgxQunp6WrSpIkSExPVoEED2e12DR8+XIMGDcqLMQIAgALGZlmWdT1XTElJUUxMjOLj4xUcHCxfX9/cHtt1O3QqOb+HAOAqqjcZlt9DAJCNC5tm5Gg+4z0QGTw8PBQcHHy9VwcAAP9gxgHRuHFj2Wy2bC9fvnz5DQ0IAAAUfMYBcffddzv9npqaqs2bN+vPP/9UREREbo0LAAAUYMYBMWXKlCynjxkzRvHx8Tc8IAAAUPDl2h/T6t69uz744IPcWhwAACjArvsgyiutXbtWnp6eubW4G1KqkD2/hwDgKk6ty9lR3gAKLuOA6Nixo9PvlmXp6NGj+uOPP/Tyyy/n2sAAAEDBZRwQhQsXdvrdxcVF1atX19ixY9WsWbNcGxgAACi4jL5IKi0tTWvWrFGtWrVUtGjRvBzXDUm6mN8jAHA11/f1dQBuBi/3a88jGR5E6erqqmbNmvFXNwEAuM0Zn4VRs2ZN7du3Ly/GAgAA/iGMA2L8+PEaPny4vvnmGx09elTnzp1z+gEAALe+HB8DMXbsWA0bNkx+fn7/u/JlX2ltWZZsNpvS0tJyf5SGOAYCKNg4BgIouHJ6DESOA8LV1VVHjx7Vjh07rjpfw4YNc7bmPERAAAUbAQEUXLkeEC4uLjp27JhKlSp1I+O6KQgIoGAjIICCK0/OwrjaX+EEAAC3D6M9EIULF75mRJw6dSpXBnYj2AMBFGzsgQAKrpzugTD6JsrIyMhM30QJAABuPxwDAeCmYw8EUHDl+jEQHP8AAAAy5DggDP5kBgAAuMXl+BiI9PT0vBwHAAD4BzH+KmsAAAACAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICBUZCQrwmRL2iFuGNVa/OXXr80a76c9tWp3n27d2rpwf2V1hoiELr3q1uXf6to0eO5NOIgVtXQkK8Jrz2ilo2bazQkMzPR8uyNHPGVIU3ul+hIXfpiT49dPDggSyXlZKSoi7/bqe7a1bXzp07btIWIK8RECgwxox6SWvX/qpXXpugT7/4WvXvC9MTfXoqNjZWknT40CH1eKybAgMr67258/Tp51+pX/8n5WG35/PIgVtP5KiX9NvaXzU+aoIW/ff52L/v/56Pcz94Vx/Pn6cXR43RvI8XysvLS08+0VvJycmZljVl0gSVLFXqZm8C8hgBgQIhKSlJy5Yu0ZBhzyqk7r2q5O+vAQMHqWIlfy36v48lSdOnTdH9DRpoyPDnFBQUrIqVKqnRg01UvHjxfB49cGtJSkrSsp+WaPDQ/z4fK132fFzwsSzL0vx5H6pvvwFq/GC4qlWvoXGvTtCJ48e1YtlPTstavepn/fbrGg0d/nw+bQ3yCgGBAiEt7aLS0tJkv2Jvgt1u16ZNG5Wenq5VP6+Uv3+A+vftrUYP1NejXTtr+RX/WQG4cVd9Pm7cqL//8x+dPHlCofXvc1zm5+enWnfV1pYtmxzT4k6e1NgxL2t81AR5enretPHj5ijQAXH48GH16tXrqvMkJyfr3LlzTj9Z7UJDwebj46vad9+jd2bP1PHjsUpLS9M3X3+prVs268SJ4zoVF6fExER98P67Crv/Ac1+5wM92KSphj7zlP5Yvy6/hw/cUnx8fHVXbefn47f/fT6ePHlcJ0+ekKRMe/+KFS+uuJMnJV06RmLUSyPUuUtX3Vmz1k3fBuS9Ah0Qp06dUnR09FXniYqKUuHChZ1+3ng96iaNELnplagJsixLTRs30L331NLHH81Ti1at5eLionQrXZLUuHETPRbRQzWCgtS7bz81aNhIixb8Xz6PHLj1vBI1QZKlZg82UL06tfTx/Hlq0bK1XGw5e9n4ZP48JSQkqFefJ/J2oMg3bvm58q+++uqql+/bt++ayxg5cqSGDh3qNM1y5aC6f6KKlSrpg+iPlJiYqISEeJUsWUrPDhusChUqqmiRonJzc1PlKlWcrhNYuYo2b9yQTyMGbl0VK1XS+3M/0oXERMX/9/n43LDBKl+hokqUKClJiouLU8mS/zs48lRcnKpVryFJWrfuN23dsln16jjvfXj04X+rZeu2Gv/q6zdvY5An8jUg2rdvL5vNJsuysp3HZrNddRl2uz3T53RJF3NleMgn3t7e8vb21rmzZ7V2zWoNHvqs3D08dGfNWjpwYL/TvAcPHlDZcuXzaaTArc/L21te/30+/vrrpedj+QoVVKJESa37ba1q1AiSJMXHx2vb1i3q3OURSdLzI1/SU4MGO5Zz/PhxPflEb70+cYpq1aqdH5uCXJavAVG2bFnNnDlT7dq1y/LyzZs3KyQk5CaPCvllzepVkmXJPzBQhw8d0pSJExQQWFntOnSUJEX07K3nhg1RSMi9urdeqNasXqVfVq7Qe3M+zOeRA7eeX9eskmVZCggI1KFDhzRl0gQFBlZWu/YdZbPZ9Ohjj+vdd2apkr+/ypevoLdmTFXJUqXUuEm4JKls2XJOy/Py9pYkVahYSaXLlLnp24Pcl68BERISog0bNmQbENfaO4FbS3z8eU17c7Jijx1T4cJF1KRpMw16Zojc3d0lSU3Cm+ql0WP0wbvv6PWo8QoICNSkN6epTkjdfB45cOs5f/68pr85WbGx/3s+PvX0/56PPXr11YULFzRuzCidP39O99QJ0czZ72XaI4xbl83Kx1foVatWKSEhQS1atMjy8oSEBP3xxx9q2LCh0XL5CAMo2HhfABRcXu45my9fAyKvEBBAwXbr/a8D3DpyGhAF+jROAABQMBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjNksy7LyexDA1SQnJysqKkojR46U3W7P7+EAuAzPz9sXAYEC79y5cypcuLDOnj2rQoUK5fdwAFyG5+fti48wAACAMQICAAAYIyAAAIAxAgIFnt1u1+jRozlACyiAeH7evjiIEgAAGGMPBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQKtLfeeksBAQHy9PRUaGio1q1bl99DAiDpl19+Udu2bVWuXDnZbDYtXrw4v4eEm4yAQIG1YMECDR06VKNHj9bGjRtVu3ZtNW/eXMePH8/voQG3vYSEBNWuXVtvvfVWfg8F+YTTOFFghYaG6t5779WMGTMkSenp6apYsaIGDRqkESNG5PPoAGSw2Wz64osv1L59+/weCm4i9kCgQEpJSdGGDRsUHh7umObi4qLw8HCtXbs2H0cGAJAICBRQJ0+eVFpamkqXLu00vXTp0jp27Fg+jQoAkIGAAAAAxggIFEglSpSQq6urYmNjnabHxsaqTJky+TQqAEAGAgIFkoeHh0JCQrRs2TLHtPT0dC1btkz169fPx5EBACTJLb8HAGRn6NChioiIUN26dVWvXj29+eabSkhIUM+ePfN7aMBtLz4+XjExMY7f9+/fr82bN6tYsWKqVKlSPo4MNwuncaJAmzFjht544w0dO3ZMd999t6ZNm6bQ0ND8HhZw21u5cqUaN26caXpERITmzp178weEm46AAAAAxjgGAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICQJ7p0aOH2rdv7/i9UaNGGjx48E0fx8qVK2Wz2XTmzJmbvm7gVkVAALehHj16yGazyWazycPDQ1WrVtXYsWN18eLFPF3v559/rnHjxuVoXl70gYKNP6YF3KZatGihOXPmKDk5Wd99950GDhwod3d3jRw50mm+lJQUeXh45Mo6ixUrlivLAZD/2AMB3KbsdrvKlCkjf39/DRgwQOHh4frqq68cHzu88sorKleunKpXry5JOnz4sLp06aIiRYqoWLFiateunQ4cOOBYXlpamoYOHaoiRYqoePHieu6553Tln9q58iOM5ORkPf/886pYsaLsdruqVq2q999/XwcOHHD8oaaiRYvKZrOpR48eki79WfeoqCgFBgbKy8tLtWvX1qeffuq0nu+++07VqlWTl5eXGjdu7DROALmDgAAgSfLy8lJKSookadmyZdq1a5eWLl2qb775RqmpqWrevLn8/Py0atUqrVmzRr6+vmrRooXjOpMmTdLcuXP1wQcfaPXq1Tp16pS++OKLq67z8ccf1yeffKJp06Zpx44devvtt+Xr66uKFSvqs88+kyTt2rVLR48e1dSpUyVJUVFR+vDDDzV79mz99ddfGjJkiLp3766ff/5Z0qXQ6dixo9q2bavNmzerT58+GjFiRF7dbMDtywJw24mIiLDatWtnWZZlpaenW0uXLrXsdrs1fPhwKyIiwipdurSVnJzsmH/evHlW9erVrfT0dMe05ORky8vLy/rxxx8ty7KssmXLWhMmTHBcnpqaalWoUMGxHsuyrIYNG1rPPPOMZVmWtWvXLkuStXTp0izHuGLFCkuSdfr0ace0pKQky9vb2/r111+d5u3du7f1yCOPWJZlWSNHjrSCg4OdLn/++eczLQvAjeEYCOA29c0338jX11epqalKT09Xt27dNGbMGA0cOFC1atVyOu5hy5YtiomJkZ+fn9MykpKStHfvXp09e1ZHjx5VaGio4zI3NzfVrVs308cYGTZv3ixXV1c1bNgwx2OOiYlRYmKimjZt6jQ9JSVF99xzjyRpx44dTuOQpPr16+d4HQByhoAAblONGzfWrFmz5OHhoXLlysnN7X//Hfj4+DjNGx8fr5CQEM2fPz/TckqWLHld6/fy8jK+Tnx8vCTp22+/Vfny5Z0us9vt1zUOANeHgABuUz4+PqpatWqO5q1Tp44WLFigUqVKqVChQlnOU7ZsWf3+++9q0KCBJOnixYvasGGD6tSpk+X8tWrVUnp6un7++WeFh4dnujxjD0haWppjWnBwsOx2uw4dOpTtnougoCB99dVXTtN+++23a28kACMcRAngmh599FGVKFFC7dq106pVq7R//36tXLlSTz/9tP7zn/9Ikp555hm99tprWrx4sXbu3Kknn3zyqt/hEBAQoIiICPXq1UuLFy92LHPhwoWSJH9/f9lsNn3zzTc6ceKE4uPj5efnp+HDh2vIkCGKjo7W3r17tXHjRk2fPl3R0dGSpP79+2vPnj169tlntWvXLn388ceaO3duXt9EwG2HgABwTd7e3vrll19UqVIldezYUUFBQerdu7eSkpIceySGDRumxx57TBEREapfv778/PzUoUOHqy531qxZ6tSpk5588knVqFFDffv2VUJCgiSpfPnyioyM1IgRI1S6dGk99dRTkqRx48bp5ZdfVlRUlIKCgtSiRQt9++23CgwMlCRVqlRJn332mRYvXqzatWtr9uzZevXVV/Pw1gFuTzYruyOcAAAAssEeCAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGDs/wGX9AD+uzXkIgAAAABJRU5ErkJggg==\n",
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
      "       False       1.00      0.10      0.18    199000\n",
      "        True       0.01      0.90      0.01      1000\n",
      "\n",
      "    accuracy                           0.11    200000\n",
      "   macro avg       0.50      0.50      0.10    200000\n",
      "weighted avg       0.99      0.11      0.18    200000\n",
      "\n",
      "Accuracy on Validation Set (Stacking): 0.15%\n"
     ]
    },
    {
     "data": {
      "image/png": "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BsrN7f+/HXh7ezuNvXLliipVqqTZs2cn2U7u3Lnvaf+enp7Gj7ly5YokaeHChSpQoIDTOrvdfk/zAHBvCAjgAeXt7a3ixYunamzFihX11VdfKU+ePPLz80t2TP78+fXHH38oLCxMknTz5k1FR0erYsWKyY4vW7asEhIS9Msvv6hu3bpJ1ieeAYmPj3csK126tOx2u44cOZLimYtSpUpp/vz5Tst+//33ux8kACNcRAngrp5//nnlypVLERERWr16tQ4ePKiVK1fqrbfe0n//+19JUufOnfXBBx9o3rx52rVrl1577bU7vodD4cKFFRkZqZdeeknz5s1zbPPrr7+WJAUFBclms+nHH3/U6dOndeXKFfn6+qp79+7q0qWLpk+frv3792vDhg0aN26cpk+fLkl65ZVXtHfvXvXo0UO7d+/WnDlzNG3atPR+ioAHDgEB4K68vLy0atUqFSpUSM2bN1epUqXUvn17Xb9+3XFGolu3bnrxxRcVGRmpatWqydfXV82aNbvjdj/55BO1aNFCr732mkqWLKmOHTvq6tWrkqQCBQpowIAB6tWrl/Lmzas33nhDkjRo0CD17dtXUVFRKlWqlBo0aKCFCxeqSJEikqRChQrpu+++07x581SuXDlNnDhRQ4cOTcdnB3gw2ayUrnACAABIAWcgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgLH/A58nqsCiduBOAAAAAElFTkSuQmCC\n",
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
      "       False       0.99      0.15      0.26    199000\n",
      "        True       0.00      0.85      0.01      1000\n",
      "\n",
      "    accuracy                           0.15    200000\n",
      "   macro avg       0.50      0.50      0.14    200000\n",
      "weighted avg       0.99      0.15      0.26    200000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Evaluate each model on the validation set\n",
    "evaluate_model(nm_gbc_model, X_val, y_val, \"Gradient Boosting\")\n",
    "evaluate_model(nm_rfc_model, X_val, y_val, \"Random Forest\")\n",
    "evaluate_model(nm_stack_model, X_val, y_val, \"Stacking\")"
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
