{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "HDjgAX1Z6F_0",
    "outputId": "946016d1-4212-4248-ce9b-8153a4b3e9e8"
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
    "drive.mount('/content/drive')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 206
    },
    "id": "IFWDeTiJ6GHm",
    "outputId": "cca59dd7-fd36-4739-9e24-3d5b68fc5d60"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "  <div id=\"df-0e1dd54a-ed84-4f72-9e62-2996da92b8c2\" class=\"colab-df-container\">\n",
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
       "      <td>0.0</td>\n",
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
       "      <td>0.0</td>\n",
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
       "      <td>0.0</td>\n",
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
       "      <td>0.0</td>\n",
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
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>\n",
       "    <div class=\"colab-df-buttons\">\n",
       "\n",
       "  <div class=\"colab-df-container\">\n",
       "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-0e1dd54a-ed84-4f72-9e62-2996da92b8c2')\"\n",
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
       "        document.querySelector('#df-0e1dd54a-ed84-4f72-9e62-2996da92b8c2 button.colab-df-convert');\n",
       "      buttonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "\n",
       "      async function convertToInteractive(key) {\n",
       "        const element = document.querySelector('#df-0e1dd54a-ed84-4f72-9e62-2996da92b8c2');\n",
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
       "<div id=\"df-59f3009b-bea4-4645-b1bf-49c1d126dc29\">\n",
       "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-59f3009b-bea4-4645-b1bf-49c1d126dc29')\"\n",
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
       "        document.querySelector('#df-59f3009b-bea4-4645-b1bf-49c1d126dc29 button');\n",
       "      quickchartButtonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "    })();\n",
       "  </script>\n",
       "</div>\n",
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
       "0       1.579213     0.767435        -0.469474  0.542560        0.0  \n",
       "1      -1.012831     0.314247        -0.908024 -1.412304        0.0  \n",
       "2      -1.150994     0.375698        -0.600639 -0.291694        0.0  \n",
       "3       0.208864    -1.959670        -1.328186  0.196861        0.0  \n",
       "4      -0.460639     1.057122         0.343618 -1.763040        0.0  "
      ]
     },
     "execution_count": 6,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "EhalPUEY6GK4",
    "outputId": "3377dd89-eaa6-433b-dd8d-2e3acce8a45d"
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
       "IsAnomaly          1\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "lvZLXV6K6GOq",
    "outputId": "478dc9a3-516e-47a7-a290-b97a286a675a"
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
       "IsAnomaly          float64\n",
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
   "execution_count": null,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "s8FDUyOq6GVs",
    "outputId": "16576f7d-5fec-4bbc-cbd1-3536faf52810"
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
     "execution_count": 10,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "qEuDQy4j6GZh",
    "outputId": "1f20139a-8df6-46f1-9d93-c90652d66c31"
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
     "execution_count": 11,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 300
    },
    "id": "xIZyv0VS6Gdg",
    "outputId": "30510dc5-0c7b-43af-e05e-bbae914a36a8"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "  <div id=\"df-f4565801-802c-46fb-9dd3-8dfef5d749c2\" class=\"colab-df-container\">\n",
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
       "      <td>111038.000000</td>\n",
       "      <td>111038.000000</td>\n",
       "      <td>111038.000000</td>\n",
       "      <td>111038.000000</td>\n",
       "      <td>111038.000000</td>\n",
       "      <td>111038.000000</td>\n",
       "      <td>111038.000000</td>\n",
       "      <td>111038.000000</td>\n",
       "      <td>111038.000000</td>\n",
       "      <td>111038.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>-0.000455</td>\n",
       "      <td>0.003397</td>\n",
       "      <td>-0.005465</td>\n",
       "      <td>-0.008094</td>\n",
       "      <td>0.000039</td>\n",
       "      <td>-0.003078</td>\n",
       "      <td>-0.001207</td>\n",
       "      <td>-0.000021</td>\n",
       "      <td>0.000528</td>\n",
       "      <td>0.000829</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.001749</td>\n",
       "      <td>1.003108</td>\n",
       "      <td>1.002134</td>\n",
       "      <td>1.003180</td>\n",
       "      <td>0.998689</td>\n",
       "      <td>0.998923</td>\n",
       "      <td>0.999691</td>\n",
       "      <td>0.999059</td>\n",
       "      <td>1.001935</td>\n",
       "      <td>0.999018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-4.295391</td>\n",
       "      <td>-4.465604</td>\n",
       "      <td>-4.829436</td>\n",
       "      <td>-4.644419</td>\n",
       "      <td>-4.596948</td>\n",
       "      <td>-4.179930</td>\n",
       "      <td>-4.462969</td>\n",
       "      <td>-4.319465</td>\n",
       "      <td>-3.984321</td>\n",
       "      <td>-4.157734</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>-0.675814</td>\n",
       "      <td>-0.673774</td>\n",
       "      <td>-0.683850</td>\n",
       "      <td>-0.684779</td>\n",
       "      <td>-0.669928</td>\n",
       "      <td>-0.677556</td>\n",
       "      <td>-0.675978</td>\n",
       "      <td>-0.676394</td>\n",
       "      <td>-0.676643</td>\n",
       "      <td>-0.676809</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>-0.000289</td>\n",
       "      <td>0.002028</td>\n",
       "      <td>-0.006162</td>\n",
       "      <td>-0.003362</td>\n",
       "      <td>0.000406</td>\n",
       "      <td>-0.006628</td>\n",
       "      <td>0.002949</td>\n",
       "      <td>0.003124</td>\n",
       "      <td>0.001301</td>\n",
       "      <td>0.000027</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>0.671398</td>\n",
       "      <td>0.678626</td>\n",
       "      <td>0.669560</td>\n",
       "      <td>0.665431</td>\n",
       "      <td>0.674971</td>\n",
       "      <td>0.671888</td>\n",
       "      <td>0.678327</td>\n",
       "      <td>0.676078</td>\n",
       "      <td>0.678087</td>\n",
       "      <td>0.673134</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>4.143895</td>\n",
       "      <td>4.616384</td>\n",
       "      <td>4.004674</td>\n",
       "      <td>4.479084</td>\n",
       "      <td>4.526784</td>\n",
       "      <td>4.065773</td>\n",
       "      <td>4.153257</td>\n",
       "      <td>4.678949</td>\n",
       "      <td>3.989945</td>\n",
       "      <td>4.595828</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>\n",
       "    <div class=\"colab-df-buttons\">\n",
       "\n",
       "  <div class=\"colab-df-container\">\n",
       "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-f4565801-802c-46fb-9dd3-8dfef5d749c2')\"\n",
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
       "        document.querySelector('#df-f4565801-802c-46fb-9dd3-8dfef5d749c2 button.colab-df-convert');\n",
       "      buttonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "\n",
       "      async function convertToInteractive(key) {\n",
       "        const element = document.querySelector('#df-f4565801-802c-46fb-9dd3-8dfef5d749c2');\n",
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
       "<div id=\"df-58494657-7eb6-4fb7-92a3-35b19db622d9\">\n",
       "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-58494657-7eb6-4fb7-92a3-35b19db622d9')\"\n",
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
       "        document.querySelector('#df-58494657-7eb6-4fb7-92a3-35b19db622d9 button');\n",
       "      quickchartButtonEl.style.display =\n",
       "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
       "    })();\n",
       "  </script>\n",
       "</div>\n",
       "    </div>\n",
       "  </div>\n"
      ],
      "text/plain": [
       "            SourceIP  DestinationIP     SourcePort  DestinationPort  \\\n",
       "count  111038.000000  111038.000000  111038.000000    111038.000000   \n",
       "mean       -0.000455       0.003397      -0.005465        -0.008094   \n",
       "std         1.001749       1.003108       1.002134         1.003180   \n",
       "min        -4.295391      -4.465604      -4.829436        -4.644419   \n",
       "25%        -0.675814      -0.673774      -0.683850        -0.684779   \n",
       "50%        -0.000289       0.002028      -0.006162        -0.003362   \n",
       "75%         0.671398       0.678626       0.669560         0.665431   \n",
       "max         4.143895       4.616384       4.004674         4.479084   \n",
       "\n",
       "            Protocol      BytesSent  BytesReceived    PacketsSent  \\\n",
       "count  111038.000000  111038.000000  111038.000000  111038.000000   \n",
       "mean        0.000039      -0.003078      -0.001207      -0.000021   \n",
       "std         0.998689       0.998923       0.999691       0.999059   \n",
       "min        -4.596948      -4.179930      -4.462969      -4.319465   \n",
       "25%        -0.669928      -0.677556      -0.675978      -0.676394   \n",
       "50%         0.000406      -0.006628       0.002949       0.003124   \n",
       "75%         0.674971       0.671888       0.678327       0.676078   \n",
       "max         4.526784       4.065773       4.153257       4.678949   \n",
       "\n",
       "       PacketsReceived       Duration  \n",
       "count    111038.000000  111038.000000  \n",
       "mean          0.000528       0.000829  \n",
       "std           1.001935       0.999018  \n",
       "min          -3.984321      -4.157734  \n",
       "25%          -0.676643      -0.676809  \n",
       "50%           0.001301       0.000027  \n",
       "75%           0.678087       0.673134  \n",
       "max           3.989945       4.595828  "
      ]
     },
     "execution_count": 12,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 423
    },
    "id": "Ttlw76LD6Ghr",
    "outputId": "6140792b-11f0-40e2-ce6d-84332bac92fb"
   },
   "outputs": [
    {
     "data": {
      "image/png": "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EXp6Yn8N6RxjdBTAUJQN4Civ16sP1x3QMwu36kB+mdFxEMCcQVbdc14PTTu7q+w2trMClA3gF8oq3fr3tz/pn1/t4twcaBSHzaqrhiXrznO6swAUOAFlA6hHVmGZnl+0XfNW7ZWH7xKcBCUDODnKBnAKWzIL9NQnW/Tdzmyjo8DPOGxWXXm0ZHCacaB+lA2ggZZuzdILi7eziBSUDKCRKBtAI63YlaOZ3+zSV9sPi+8ec7HbLLpyaCfddS4lA2gMygbQRNsOFupf3+zSf9cf4PTnbdyxknHnOd2UHBNqdBwg4FA2gGbKzC/V7GW79c6qvcorqTQ6DlpQhDNIE4ck6dazu1IygGagbAAtpKzSrQ/X7dcbK/Zo04ECo+OgGQYmR+m6Mzrr0oFJCnHYjI4DBDzKBuADq/cc0evL9+izHzOZYgkQYQ6bLhucpOtO76y0JC75DrQkygbgQ1mFZfpg7X59uvGg1u/LY0Gpn7FYpNNTYnXFkGT9akCiwp1BRkcC2iTKBtBKDuSV6rMfD2rhj5lavSeXE4UZqGtcmCYOTtKEwUmsxQBaAWUDMEBWQZkWbjqoTzdmKn13rtw0D59Lig7R2D4ddPmQZA3qFG10HMBUKBuAwbKLyvX5poP6bONBff9TjlwUjxYR6rDpjNRYnd0zTqN6xKl7h3CjIwGmRdkA/EhucYUWbT6oz348qB9+PqISLgTXYBaL1CchUqN6ttfoHnEalhIrRxBXXAX8AWUD8FNuj1dbMgu0NiNXazLytCYjV3tySoyO5Vfahzs1qkd7nd2zvc7qHqe4CKfRkQDUgbIBBJDsonKtPVo81uzJ1YZ9+SqtNMfoR5DVotT2YeqZEKH+SVEa1aO9+iZGymKxGB0NwClQNoAA5nJ7tPVgYXX5WJORp725JQG9xdZiqVrM2Ss+Qj0TItQ7IUI94yPULS6caREgQFE2gDamrNKtA3ml2p9Xqn25pdqfe+zvJdqfW6pDheV+s/ulfbhDPeOrykTvhKpy0TM+gvNdAG0MZQMwGZfbo8z8sqoickIJySosV2mFW6WVR98qjv9Z5nKfdLTEZrUoOsSu6FC7YkIdig51KCbUrpgwR/VtMaF2RYU4FBN27D52OYM4FThgBpQNAA3i9Xrl9Uoer1eeo396vZJXXoXYbaydAFAvygYAAPApVlsBAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACfomwAAACf+v/KzPSmXKpqgwAAAABJRU5ErkJggg==\n",
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
      "Proportion of Minority Class: 0.51%\n"
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
   "execution_count": null,
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
   "execution_count": null,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "A75jz_evCP6f",
    "outputId": "9dec58c5-0103-4318-a7ff-e07ac05025c1"
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "rlGisVHz6Gs8",
    "outputId": "7c219805-e320-4202-8a49-cce3a603b83a"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proportion of Minority Class in train set: 0.51%\n",
      "Proportion of Minority Class in test set: 0.51%\n",
      "Proportion of Minority Class in validation set: 0.51%\n"
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ln5MnPns6Gw3",
    "outputId": "ac0033e0-2a36-43a8-f062-21437392b21d"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The X_train shape:  (66622, 10)\n",
      "The X_test shape:  (22208, 10)\n",
      "The X_val shape:  (22208, 10)\n"
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
   "execution_count": null,
   "metadata": {
    "id": "U9IbgXsT1QWG"
   },
   "outputs": [],
   "source": [
    "from imblearn.over_sampling import SMOTE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 452
    },
    "id": "yZqL94uSCYet",
    "outputId": "adf90ebd-0c1a-48a6-abd8-22ac894c59f9"
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
      "Proportion of Minority Class: 0.51%\n"
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
   "execution_count": null,
   "metadata": {
    "id": "uDFmXS5_CYiM"
   },
   "outputs": [],
   "source": [
    "smote = SMOTE(sampling_strategy='auto', random_state=42)\n",
    "X_resampled, y_resampled = smote.fit_resample(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "3YvlyInlCYld",
    "outputId": "1533d992-77c1-4077-e289-a4a846e8f23b"
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 480
    },
    "id": "E6AHW4Z5CYo7",
    "outputId": "8467f69c-715c-4510-8f3b-119151bd1d09"
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
      "Shape of Resampled X:  (132568, 10)\n",
      "Shape of Resampled y:  (132568,)\n"
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
   "execution_count": null,
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
   "execution_count": null,
   "metadata": {
    "colab": {
     "background_save": true
    },
    "id": "_hHbl0jmb9QH",
    "outputId": "035a3a64-b6c1-4725-e134-2bab569ef66f"
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
   "execution_count": 26,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "kB_LoFfwCY2-",
    "outputId": "23d82bbb-993f-42b5-9ad0-f07bedca6ab0"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Gradient Boosting): 89.40%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       1.00      0.90      0.94     22095\n",
      "        True       0.01      0.15      0.01       113\n",
      "\n",
      "    accuracy                           0.89     22208\n",
      "   macro avg       0.50      0.52      0.48     22208\n",
      "weighted avg       0.99      0.89      0.94     22208\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the best model from the grid search\n",
    "smote_gbc_model = grid_search_gbc.best_estimator_\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(smote_gbc_model, 'smote_gradient_boosting_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "smote_gbc_predictions = smote_gbc_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Gradient Boosting): {:.2f}%\".format(accuracy_score(y_val, smote_gbc_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, smote_gbc_predictions))\n"
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
   "execution_count": 30,
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
   "execution_count": 31,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "5hshDaqwdBA5",
    "outputId": "79b2411b-b06c-47c6-898d-55661d4abdd5"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Parameters for Random Forest: {'max_depth': None, 'min_samples_split': 2, 'n_estimators': 150}\n"
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
   "execution_count": 32,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "C-dMJxURCY-I",
    "outputId": "cc0a4451-c2e8-44ea-b8fc-272ac529d8ce"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Random Forest): 99.41%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       0.99      1.00      1.00     22095\n",
      "        True       0.00      0.00      0.00       113\n",
      "\n",
      "    accuracy                           0.99     22208\n",
      "   macro avg       0.50      0.50      0.50     22208\n",
      "weighted avg       0.99      0.99      0.99     22208\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the best model from the grid search\n",
    "smote_rfc_model = grid_search_rfc.best_estimator_\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(smote_rfc_model, 'smote_random_forest_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "smote_rfc_predictions = smote_rfc_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Random Forest): {:.2f}%\".format(accuracy_score(y_val, smote_rfc_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, smote_rfc_predictions))\n"
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
   "execution_count": 33,
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
   "execution_count": 34,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ivqbfVtfdkmS",
    "outputId": "097c8342-af66-4687-e4c8-cddf6be5302d"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Parameters for Stacking: {'final_estimator__C': 1, 'final_estimator__penalty': 'l1', 'final_estimator__solver': 'liblinear'}\n"
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
   "execution_count": 41,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "y6WlXi0adkp0",
    "outputId": "4a1459e8-d6c8-4037-f2ff-24a32478667e"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Stacking): 99.42%\n",
      "\n",
      "Classification Report:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "       False       0.99      1.00      1.00     22095\n",
      "        True       0.00      0.00      0.00       113\n",
      "\n",
      "    accuracy                           0.99     22208\n",
      "   macro avg       0.50      0.50      0.50     22208\n",
      "weighted avg       0.99      0.99      0.99     22208\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Get the best model from the grid search\n",
    "smote_stack_model = grid_search_stack.best_estimator_\n",
    "\n",
    "# Save the best model\n",
    "joblib.dump(smote_stack_model, 'smote_stacking_model.pkl')\n",
    "\n",
    "# Make predictions on the validation set using the best model\n",
    "smote_stack_predictions = smote_stack_model.predict(X_val)\n",
    "\n",
    "# Evaluate the model performance\n",
    "print(\"Accuracy on Validation Set (Stacking): {:.2f}%\".format(accuracy_score(y_val, smote_stack_predictions) * 100))\n",
    "print(\"\\nClassification Report:\\n\", classification_report(y_val, smote_stack_predictions))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
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
   "execution_count": 40,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 1000
    },
    "id": "ByyoReuUdkxD",
    "outputId": "6ec0670e-098e-4258-845c-41ef2d5438d3"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy on Validation Set (Gradient Boosting): 0.89%\n"
     ]
    },
    {
     "data": {
      "image/png": "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v3IORFpfzz//vNu4Uva1UaNGbs+XKVOmGElm1qxZxhhjEhISTKFChcydd95pLl++7FpuxYoVRpJ54403jDHGnD9/PkPn46R3DkR6RyAkmQ8++MA1LT4+3hQpUsQ8/PDDrmljx441ksyyZctc0y5fvmwqVKiQ5hEIY64e4WratOkNx4rMwREIuLl48aIkyd/fP0PLf/7555KkPn36uE3v27evJKU6VyIsLEwPPPCA63ZQUJDKly+vw4cP/+UxXy/l3IlPPvlEycnJGbrPiRMntGvXLnXq1En58+d3Tb/77rvVsGFD135e67nnnnO7/cADD+js2bOuxzAjHn/8ca1fv14nT57UunXrdPLkST3++ONpLut0OuXhcfVHNikpSWfPnlWePHlUvnx57dixI8PbdDqd6ty5c4aWbdSokbp166Zhw4apbdu28vHx0YwZM256v7Nnz0qS8uXL5zY95bG5/uhDdHS0goKC3L6u/xRJaGioGjdunGpb154HER0draioKIWHh+vw4cOKjo6WdPXoUkJCgl588UU5HA7X8r169brpvuzatUsHDhzQ448/rrNnz7qOAMTExKh+/frasGFDqudZZjw30vLss89q9erVWr16tZYsWaIePXpoxowZbj9/Kfvaq1cv1/NFkrp27aqAgADXz+S2bdt0+vRpde/e3e0chWbNmqlChQqu5Xx9feXt7a3169fr/Pnzf2v818qTJ4/b+Rze3t6699573f4vWLlypYoVK6aWLVu6pvn4+Khr167prjdfvnyKiorKtHEifQQE3AQEBEiS/vzzzwwt/+uvv8rDw0N33HGH2/QiRYoob968+vXXX92mlyxZMtU68uXLl6n/MT322GOqXbu2unTposKFC6t9+/ZavHjxDWMiZZzly5dPNa9ixYquXxjXun5fUn5Z2uzLQw89JH9/fy1atEgLFizQPffck+qxTJGcnKzx48erbNmycjqdKliwoIKCgvTjjz+6flFmRMrHJjNqzJgxyp8/v3bt2qVJkyapUKFCGb6vMcbtdkqYXrp0yW16njx5XL8YX3755TTXFRoamub0zZs3q0GDBvLz81PevHkVFBSkV199VZJcj0vK97ds2bJu9w0KCkoVOdc7cOCApKsfLb4+cmbOnKn4+PhUj39mPDfSUrZsWTVo0EANGjRQ27ZtNWXKFHXv3l0TJkzQTz/9JCn957K3t7dKly7tmn+j53yFChVc851Op95++2198cUXKly4sOrUqaNRo0bp5MmTf2tfihcv7hZzUur/C3799VeVKVMm1XLp/YxIV59z1y+PrEFAwE1AQICKFi2q3bt3W90voz+wuXLlSnP69b9obLZx/WfgfX19tWHDBq1Zs0ZPPvmkfvzxRz322GNq2LBhpn5e/u/sSwqn06m2bdtq7ty5Wrp0abpHH6Sr1w3o06eP6tSpo/nz5+vLL7/U6tWrValSpQwfaZFk/cmFnTt36vTp05Lk+iV1MwUKFJCU+hdmhQoVJCnV88vT09P1izEsLCzD4z506JDq16+vqKgojRs3Tp999plWr16t3r17S5LV45KelHWMHj3aFTnXf11/RCUznhsZVb9+fUnShg0bMn3dKXr16qX9+/crMjJSPj4+GjRokCpWrKidO3f+5XVm1WN0/vx5FSxY8G+tAxlDQCCV5s2b69ChQ9qyZctNlw0JCVFycrLrVVqKU6dO6cKFCwoJCcm0ceXLl8/txK4U1x/lkK5+dKx+/foaN26cfv75Z7355ptat26dvvrqqzTXnTLOffv2pZr3yy+/qGDBgvLz8/t7O5COxx9/XDt37tSff/6Z5omnKT766CPVq1dP77//vtq3b69GjRqpQYMGqR6TzHz1FRMTo86dOyssLEzPPvusRo0ape+///6m9ytZsqR8fX115MgRt+nly5dX2bJltWzZsgydvHgzn376qeLj47V8+XJ169ZNDz30kBo0aJAqNlK+v9c/T8+cOXPTowJlypSRdDWuUyLn+i8vLy/rsWfW9+nKlSuS/ndUJ73nckJCgo4cOeKaf6Pn/L59+1L97JYpU0Z9+/bVqlWrtHv3biUkJGjs2LGZvj/XCgkJ0aFDh1JFxcGDB9Nc/sqVK/rtt99UsWLFTB8LUiMgkMorr7wiPz8/denSJc0rAh46dEgTJ06UdPUQvKRUn5QYN26cpKvvp2aWMmXKKDo6Wj/++KNr2okTJ7R06VK35c6dO5fqviln7MfHx6e57uDgYFWpUkVz5851+4W8e/durVq1yrWfWaFevXoaPny4pkyZoiJFiqS7XK5cuVL9R/rf//5Xx48fd5uWEjppxZat/v3769ixY5o7d67GjRunUqVKKSIiIt3HMYWXl5dq1Kihbdu2pZo3ZMgQRUVFqWvXrm6fCEhh8wo05VXstfeJjo7W7Nmz3ZZL+SU/efJkt2Uz8gmf6tWrq0yZMhozZkyqt16k/123xJafn1+mfI8+/fRTSVLlypUlXd1Xb29vTZo0yW1f33//fUVHR7t+JmvUqKFChQpp+vTpbt/PL774Qnv37nUtFxsbq7i4OLdtlilTRv7+/m73y6z9uVbjxo11/PhxLV++3DUtLi5O7733XprL//zzz4qLi8vwJ8jw93AhKaRSpkwZLVy4UI899pgqVqyop556SnfeeacSEhL0zTff6L///a/rbwdUrlxZERERevfdd3XhwgWFh4dr69atmjt3rlq3bp3uRwT/ivbt26t///5q06aNevbsqdjYWE2bNk3lypVzO4lw2LBh2rBhg5o1a6aQkBCdPn1aU6dOVfHixXX//fenu/7Ro0eradOmqlWrlp555hldvnxZkydPVmBgoIYMGZJp+3E9Dw8Pvf766zddrnnz5ho2bJg6d+6s++67Tz/99JMWLFig0qVLuy1XpkwZ5c2bV9OnT5e/v7/8/PxUs2bNdM8hSM+6des0depUDR482PVxzNmzZ6tu3boaNGiQRo0adcP7t2rVSq+99pouXrzoOrdGunrEZffu3YqMjNTWrVvVvn17hYaGKiYmRrt379aHH34of3//m56bIF09ydPb21stWrRQt27ddOnSJb333nsqVKiQTpw44VouKChI/fr1U2RkpJo3b66HHnpIO3fu1BdffHHTw90eHh6aOXOmmjZtqkqVKqlz584qVqyYjh8/rq+++koBAQGuX+I2qlevrjVr1mjcuHEqWrSoQkNDVbNmzRveZ8eOHZo/f76kq+cprV27VkuWLNF9992nRo0aufZ14MCBGjp0qJo0aaKWLVtq3759mjp1qu655x7XiYteXl56++231blzZ4WHh6tDhw46deqUJk6cqFKlSrneBtq/f7/q16+vdu3aKSwsTJ6enlq6dKlOnTrldsSsevXqmjZtmkaMGKE77rhDhQoV0oMPPmj9uFyrW7dumjJlijp06KCXXnpJwcHBWrBggeukz+uPeqxevVq5c+dWw4YN/9Z2kUHZ8+EP/BPs37/fdO3a1ZQqVcp4e3sbf39/U7t2bTN58mS3i0QlJiaaoUOHmtDQUOPl5WVKlChxwwtJXe/6jw/e6KI5q1atMnfeeafx9vY25cuXN/Pnz0/1Mc61a9ea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NQICAABYIyAAAIA1AgIAAFgjIAAAgDUCAgAAWCMgAACANQICAABYIyAAAIA1AgIAAFgjIAAAgDUCAgAAWCMgAACANQICAABYIyAAAIA1AgIAAFhzGGNMdg8CuJH4+HhFRkZq4MCBcjqd2T0cANfg5/P2RUAgx7t48aICAwMVHR2tgICA7B4OgGvw83n74i0MAABgjYAAAADWCAgAAGCNgECO53Q6NXjwYE7QAnIgfj5vX5xECQAArHEEAgAAWCMgAACANQICAABYIyAAAIA1AgI52jvvvKNSpUrJx8dHNWvW1NatW7N7SAAkbdiwQS1atFDRokXlcDi0bNmy7B4SbjECAjnWokWL1KdPHw0ePFg7duxQ5cqV1bhxY50+fTq7hwbc9mJiYlS5cmW988472T0UZBM+xokcq2bNmrrnnns0ZcoUSVJycrJKlCihF198UQMGDMjm0QFI4XA4tHTpUrVu3Tq7h4JbiCMQyJESEhK0fft2NWjQwDXNw8NDDRo00JYtW7JxZAAAiYBADhUVFaWkpCQVLlzYbXrhwoV18uTJbBoVACAFAQEAAKwREMiRChYsqFy5cunUqVNu00+dOqUiRYpk06gAACkICORI3t7eql69utauXeualpycrLVr16pWrVrZODIAgCR5ZvcAgPT06dNHERERqlGjhu69915NmDBBMTEx6ty5c3YPDbjtXbp0SQcPHnTdPnLkiHbt2qX8+fOrZMmS2Tgy3Cp8jBM52pQpUzR69GidPHlSVapU0aRJk1SzZs3sHhZw21u/fr3q1auXanpERITmzJlz6weEW46AAAAA1jgHAgAAWCMgAACANQICAABYIyAAAIA1AgIAAFgjIAAAgDUCAgAAWCMgAACANQICQJbp1KmTWrdu7bpdt25d9erV65aPY/369XI4HLpw4cIt3zbwb0VAALehTp06yeFwyOFwyNvbW3fccYeGDRumK1euZOl2P/74Yw0fPjxDy/JLH8jZ+GNawG2qSZMmmj17tuLj4/X555+rR48e8vLy0sCBA92WS0hIkLe3d6ZsM3/+/JmyHgDZjyMQwG3K6XSqSJEiCgkJ0fPPP68GDRpo+fLlrrcd3nzzTRUtWlTly5eXJP32229q166d8ubNq/z586tVq1Y6evSoa31JSUnq06eP8ubNqwIFCuiVV17R9X9q5/q3MOLj49W/f3+VKFFCTqdTd9xxh95//30dPXrU9Yea8uXLJ4fDoU6dOkm6+mfdIyMjFRoaKl9fX1WuXFkfffSR23Y+//xzlStXTr6+vqpXr57bOAFkDgICgCTJ19dXCQkJkqS1a9dq3759Wr16tVasWKHExEQ1btxY/v7+2rhxozZv3qw8efKoSZMmrvuMHTtWc+bM0axZs7Rp0yadO3dOS5cuveE2n3rqKX344YeaNGmS9u7dqxkzZihPnjwqUaKElixZIknat2+fTpw4oYkTJ0qSIiMj9cEHH2j69Onas2ePevfurY4dO+rrr7+WdDV02rZtqxYtWmjXrl3q0qWLBgwYkFUPG3D7MgBuOxEREaZVq1bGGGOSk5PN6tWrjdPpNP369TMRERGmcOHCJj4+3rX8vHnzTPny5U1ycrJrWnx8vPH19TVffvmlMcaY4OBgM2rUKNf8xMREU7x4cdd2jDEmPDzcvPTSS8YYY/bt22ckmdWrV6c5xq+++spIMufPn3dNi4uLM7lz5zbffPON27LPPPOM6dChgzHGmIEDB5qwsDC3+f3790+1LgB/D+dAALepFStWKE+ePEpMTFRycrIef/xxDRkyRD169NBdd93ldt7DDz/8oIMHD8rf399tHXFxcTp06JCio6N14sQJ1axZ0zXP09NTNWrUSPU2Ropdu3YpV65cCg8Pz/CYDx48qNjYWDVs2NBtekJCgqpWrSpJ2rt3r9s4JKlWrVoZ3gaAjCEggNtUvXr1NG3aNHl7e6to0aLy9Pzffwd+fn5uy166dEnVq1fXggULUq0nKCjoL23f19fX+j6XLl2SJH322WcqVqyY2zyn0/mXxgHgryEggNuUn5+f7rjjjgwtW61aNS1atEiFChVSQEBAmssEBwfru+++U506dSRJV65c0fbt21WtWrU0l7/rrruUnJysr7/+Wg0aNEg1P+UISFJSkmtaWFiYnE6njh07lu6Ri4oVK2r58uVu07799tub7yQAK5xECeCmnnjiCRUsWFCtWrXSxo0bdeTIEa1fv149e/bU77//Lkl66aWX9NZbb2nZsmX65Zdf1L179xtew6FUqVKKiIjQ008/rWXLlrnWuXjxYklSSEiIHA6HVqxYoTNnzujSpUvy9/dXv3791Lt3b82dO1eHDh3Sjh07NHnyZM2dO1eS9Nxzz+nAgQN6+eWXtW/fPi1cuFBz5szJ6ocIuO0QEABuKnfu3NqwYYNKliyptm3bqmLFinrmmWcUFxfnOiLRt29fPfnkk4qIiFCtWrXk7++vNm3a3HC906ZN0yOPPKLu3burQoUK6tq1q2JiYiRJxYoV09ChQzVgwAAVLlxYL7zwgiRp+PDhGjRokCIjI1WxYkU1adJEn332mUJDQyVJJUuW1JIlS7Rs2TJVrlxZ06dP18iRI7Pw0QFuTw6T3hlOAAAA6eAIBAAAsEZAAAAAawQEAACwRkAAAABrBAQAALBGQAAAAGsEBAAAsEZAAAAAawQEAACwRkAAAABrBAQAALD2/wCiN0ZQU+aTDQAAAABJRU5ErkJggg==\n",
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
      "       False       1.00      0.90      0.94     22095\n",
      "        True       0.01      0.15      0.01       113\n",
      "\n",
      "    accuracy                           0.89     22208\n",
      "   macro avg       0.50      0.52      0.48     22208\n",
      "weighted avg       0.99      0.89      0.94     22208\n",
      "\n",
      "Accuracy on Validation Set (Random Forest): 0.99%\n"
     ]
    },
    {
     "data": {
      "image/png": "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Q6+//nqOt8mOn/x6Tp08edIl3lB4cAQC161NmzbatWuXkpKSrrpsWFiYsrKytHPnTqfphw8f1qlTpxxXVOSH4OBgl7PLJddXgpLk4eGhpk2b6vXXX9fWrVv14osvavny5Y5DspfLHueOHTtc5m3fvl0lS5ZUsWLFrm8HcvHYY4/phx9+0J9//qkuXbrkutynn36qJk2aaMaMGerSpYuaNWummJgYl/skP1/hpaamqnv37oqMjFSfPn00YcIEbdiw4aq3K1++vHx9fbVnz548bSc0NFSDBw/Wl19+qe+++84x/dNPP1VsbKxee+01dezYUQ8++KDuv//+HB8HeZH9c7788Xr06FGX2AkLC8v18XDputwlt8dsenq69uzZk6fx3XHHHTpx4oSaNm3qcqQjJibG6ejG1Z5TV3vcXbhwQQcOHHAcwUHhQ0Dguj333HMqVqyYevXqpcOHD7vM37VrlyZNmiTp4iF4SXrjjTeclsl+RdO6det8G9cdd9yhlJQU/fTTT45pBw8edLnS48SJEy63zf5gm9wunwsNDVWtWrWUmJjo9Mvpl19+0ZIlSxz7WRCaNGmicePG6c0331SZMmVyXc7T09PlVesnn3yi33//3Wladuhc6y/ZSw0bNkz79+9XYmKiXn/9dYWHhys2NvaqlyF6eXmpbt26+v777/O8rYEDB6po0aJ6+eWXHdNy2ucpU6a4HHXKq5iYGHl5eWnKlClO67388StdfGyvX7/eKaRTU1P1zjvvKDw8XJGRkdc0hvwSExMjb29vTZ482WlfZsyYoZSUlDw99zp37qzff/9d7777rsu8c+fOOd62y8tz6mqPu61bt+r8+fN5vroLNx5vYeC63XHHHfroo4/0yCOPqGrVqk6fRPntt9/qk08+cfzNgJo1ayo2NlbvvPOOTp06pUaNGmn9+vVKTExUu3bt1KRJk3wbV5cuXTRs2DC1b99eTz/9tM6ePatp06apcuXKTifUjR07VqtWrVLr1q0VFhamI0eOaOrUqbr99tudToi73CuvvKKWLVsqKipKPXv2dFzGGRgYeMW3Fq6Xh4eH/v73v191uTZt2mjs2LHq3r276tevr59//llz5sxRxYoVnZa74447FBQUpOnTp8vf31/FihVTvXr1VKFCBaNxLV++XFOnTtXo0aMdl5XOnDlTjRs31siRIzVhwoQr3r5t27Z64YUXdPr0ace5NVdSokQJde/eXVOnTtW2bdtUtWpVtWnTRrNnz1ZgYKAiIyOVlJSkb775xvEWiamQkBDFxcUpISFBbdq0UatWrfTDDz/oX//6l0qWLOm07PDhw/Xxxx+rZcuWevrpp1W8eHElJiZqz549mj9/vtOJi+4QEhKiESNGKD4+Xi1atNDDDz+sHTt2aOrUqbrnnnvy9AFUjz/+uObNm6e+fftqxYoVio6OVmZmprZv36558+bp66+/Vt26dfP0nLra427p0qUqWrSoHnzwwQK9X3Ad3HT1B25Cv/76q9W7d28rPDzc8vb2tvz9/a3o6GhrypQp1vnz5x3LZWRkWPHx8VaFChUsLy8vq1y5ctaIESOclrGsi5dxtm7d2mU7l18+mNtlnJZlWUuWLLGqV69ueXt7WxEREdaHH37ochnnsmXLrLZt21ply5a1vL29rbJly1qPPvqo9euvv7ps4/JLzr755hsrOjra8vX1tQICAqyHHnrI2rp1q9My2du7/JK27EsJ9+zZk+t9alnOl3HmJrfLOIcOHWqFhoZavr6+VnR0tJWUlJTj5ZcLFy60IiMjrSJFijjtZ6NGjaxq1arluM1L13P69GkrLCzMql27tpWRkeG03ODBgy0PDw8rKSnpivtw+PBhq0iRItbs2bPzvP+7du2yPD09HZdTnjx50urevbtVsmRJy8/Pz2revLm1fft2KywszOmSy+z7fsOGDU7ry77EcsWKFY5pmZmZVnx8vON+bNy4sfXLL7+4rDN7PB07drSCgoIsHx8f695777UWLVqU4zY++eQTp+m5jSm3x8/l8vI4sayLl21WqVLF8vLyskqXLm3169fPOnnypNMyV/q5p6enW//4xz+satWqWXa73QoODrbq1KljxcfHWykpKZZl5e05ZVm5P+4sy7Lq1atnde3a9ar7A/exWdYNPjMHAHLRs2dP/frrr1q9erW7hwI32rx5s2rXrq1NmzYZ/X0W3FgEBIBCY//+/apcubKWLVvm9Bc5cWvJvmpm3rx57h4KroCAAAAAxrgKAwAAGCMgAACAMQICAAAYIyAAAIAxAgIAABi7KT+J0vfuAe4eAoArOLnhTXcPAUAufPJYBhyBAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxoq4ewC4+cT1aKZ2D9RU5fDSOpeWoXU/7tYLkxZq574jkqTggKIa2a+1mt5XReXKBOvYyTP6cuVPip+6SKfPnHesp1yZYE16/hE1qltZZ86lac6X6zRyyhfKzMySJL0T31WPP3yfy/a37jqoOh1fdHxfNiRQ459pq2bR1VTUx0u7DhzTk2M+1Kat+wv4ngBuHhu/36BZ78/Qtq2/6OjRo5o4+S090DTGMf/4sWN64/VXlfTtGv3555+qXaeuhr8wUmFh4e4bNAoUAYF816B2JU2fu0obt+xTkSKeih/wkBZNG6C7O4zX2fPpCg0JVGhIoEZM/Fzbdh9S+dDimvJCF4WGBOqxZ2dIkjw8bPpscj8dPn5aTbq9pjIhgXpv3OPKuJCp0W9+KUmKe+VTjZy80LHdIp6eWjd3hD5b+oNjWpC/r5bPGqL/bNipdgOm6ujJM6pUPkQnT5+9sXcK8Bd37txZRUREqF2H/9OQZwY4zbMsS4Oe7q8iRYrojSlT5efnpw8SZ+nJnt312ReLVbRoUTeNGgXJZlmW5e5B5DffuwdcfSHcMCWD/XRg+cuK6TlRazftynGZDjF36/0Xn1CJ+kOVmZmlZtGR+mxSX1Vs9oKOnPhTktSr4/0a/3RblXtguDIuZLqs46HGd+mfr/VS1Tajtf/gSUnSuKcfVlTNiorp+UaB7R/MndzwpruHgOtQs1qE0xGIvXv3qG3rFpq/cJEqVbpTkpSVlaUHGkXr6WeGqEPHTu4cLgz55PHQglvPgTh27JgmTJig9u3bKyoqSlFRUWrfvr1eeeUVHT161J1DQz4K8PORJJ1Myf1Vf4C/j06nnne8PVHvrgr6JfkPRzxI0tJvtynQ31eRd4TmuI7YdlFavm6HIx4kqXWjGtq0db/mTOihfcsSlPTxMHVvXz8/dgvAf2Wkp0uS7N52xzQPDw95e3vrh00b3TUsFDC3BcSGDRtUuXJlTZ48WYGBgWrYsKEaNmyowMBATZ48WVWqVNH3339/1fWkpaXp9OnTTl9WluurU7iHzWbTK3Ed9e0Pu7R118EclykRVEwjerfU+/O/dUwrXSJAR47/6bTckROnL84rGeCyjtCQQDWPjtSsz791ml7htpLq3amBkvcf1cNPvaV3P1mj157rqL89VO96dw3Af4VXqKjQ0LKa/MZrOp2Sooz0dL3/3js6fOgQLwZvYm47B2LgwIHq1KmTpk+fLpvN5jTPsiz17dtXAwcOVFJS0hXXk5CQoPj4eKdpnqXvkVfovfk+Zph7Y0RnVasUqqbdJ+Y437+Yjz6f3E/bdh/U+LcXX/N2/vZQPZ3685y+WPGT03QPD5s2bd3vOG/ixx2/qVqlUPXueL/mfLnumrcH4H+8vLz0+qQpGjPyBTWof688PT1V774o3d+goW7Cd8nxX247AvHjjz9q8ODBLvEgXXzVOnjwYG3evPmq6xkxYoRSUlKcvoqUrlMAI4apicM6qVWD6mree7J+P3LKZb5fUbu+eOsp/Xn2vB4Z8q4uXMhyzDt8/LRKlfB3Wr5U8YtHHg4fO+2yrti29+njxetdzo04dOy0tu0+5DRt+55DKlcm+Fp3C0AOIqtV17zPFmrNd9/rm5VrNO2dGTp16pRuv72cu4eGAuK2gChTpozWr1+f6/z169erdOnSV12P3W5XQECA05fNwzM/h4prMHFYJz38QE21eHKy9v1x3GW+fzEfLZo2QOkZmeo46G2lpV9wmr/upz2qXqmsQoL9HNOa3ldFKX+ecwmCBnXuVKXypTRrgevRqqTNu1U5rJTTtDvLl9L+gyeuZ/cA5MLf31/FixfXvn17tXXLL2r8QFN3DwkFxG1vYcTFxalPnz7auHGjmjZt6oiFw4cPa9myZXr33Xf16quvumt4uA5vjOisR1rWVafB7+hM6nmV/u+RhJQz53U+LeNiPEztL18fb3V/IVEBxXwUUOziiZZHT55RVpalb5K2advuQ5oxPlYvTFqg0iUCNLp/G709b5XSM5xjo1u7KK3/aU+O51hM+XC5Vswaqmd7NNP8pZt0T7Vw9fi/aA0Y93HB3xHATeRsaqr27//fZ6f8/ttv2r5tmwIDAxVatqyWfP0vBQcXV2hoWe3cuUMTEl5SkwdiVD/6fjeOGgXJrZdxzp07VxMnTtTGjRuVmXnx0LOnp6fq1KmjIUOGqHPnzte0Xi7jdK9zP+R8iV7vUbP14Zfr1KDOnVry3jM5LhPRapTj6ED50GBNer6LGta5U6nn0zTny/X6++SFjis1pItXeOxZ8pLiXvlUMy87gTJbywbVNXbgw6pUPkR7fz+uyR8uz3VZ3BhcxvnXs2H9OvXq/oTL9Ifbtte4l17WnA8/UOLMGTp+7LhCQkLU5uG2erLvU/Ly9nbDaHE98noZZ6H4HIiMjAwdO3ZMklSyZEl5eXld1/oICKBwIyCAwiuvAVEoPonSy8tLoaE5X9sPAAAKH/6YFgAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBAQAADBGQAAAAGPXFBCrV69W165dFRUVpd9//12SNHv2bK1ZsyZfBwcAAAon44CYP3++mjdvLl9fX/3www9KS0uTJKWkpOill17K9wECAIDCxzggxo8fr+nTp+vdd9+Vl5eXY3p0dLQ2bdqUr4MDAACFk3FA7NixQw0bNnSZHhgYqFOnTuXHmAAAQCFnHBBlypRRcnKyy/Q1a9aoYsWK+TIoAABQuBkHRO/evfXMM89o3bp1stls+uOPPzRnzhzFxcWpX79+BTFGAABQyBQxvcHw4cOVlZWlpk2b6uzZs2rYsKHsdrvi4uI0cODAghgjAAAoZGyWZVnXcsP09HQlJyfrzJkzioyMlJ+fX36P7Zr53j3A3UMAcAUnN7zp7iEAyIVPHg8tGB+ByObt7a3IyMhrvTkAAPgLMw6IJk2ayGaz5Tp/+fLl1zUgAABQ+BkHRK1atZy+z8jI0ObNm/XLL78oNjY2v8YFAAAKMeOAmDhxYo7Tx4wZozNnzlz3gAAAQOGXb39Mq2vXrnr//ffza3UAAKAQu+aTKC+XlJQkHx+f/FrddTmxnjO8AQAoSMYB0aFDB6fvLcvSwYMH9f3332vkyJH5NjAAAFB4GQdEYGCg0/ceHh6KiIjQ2LFj1axZs3wbGAAAKLyMPkgqMzNTa9euVY0aNRQcHFyQ47ou5zLcPQIAV3KFK8EBuFleP0jK6CRKT09PNWvWjL+6CQDALc74Kozq1atr9+7dBTEWAADwF2EcEOPHj1dcXJwWLVqkgwcP6vTp005fAADg5pfncyDGjh2roUOHyt/f/383vuSNTMuyZLPZlJmZmf+jNMQ5EEDhxjkQQOGV13Mg8hwQnp6eOnjwoLZt23bF5Ro1apS3LRcgAgIo3AgIoPDK94Dw8PDQoUOHVKpUqesZ1w1BQACFGwEBFF4FchXGlf4KJwAAuHUYHYEIDAy8akScOHEiXwZ2PTgCARRuvBYBCq+8HoEw+iTK+Ph4l0+iBAAAtx7OgQBww3EEAii88v0cCM5/AAAA2fIcEAZ/MgMAANzk8nwORFZWVkGOAwAA/IUYf5Q1AAAAAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAbfY+P0GPd2/rx5scr9qVY/Q8mXfOM1ftnSJ+vbuoUbR9VSreoS2b9/mso5x8aPUpkWM6tW5S00a3KdBA/tpz+5dN2oXAEj650dz1PLBB3TP3TX0ty6d9PNPP7l7SLhBCAi4xblzZ1U5IkIjXhid6/y7a9fWM4Pjcl1H1chqih+foM+++EpT354hy7LUr09PZWZmFtSwAVzi3//6Sq9OSNCTT/XXPz/5XBERVdTvyZ46fvy4u4eGG8BmWZbl7kHkt3MZ7h4BTNSqHqHXJ72lB5rGuMz7/fff1Lp5U/3z0wWqUqXqFdfz647t6vx/bfXlV0tVrnz5ghou8oHN5u4RID/8rUsnVateQ8//fZQkKSsrS82aNtKjjz2unr37uHl0uFY+RfK2HEcgcFM4d/asFi74TLfdfrvKhJZx93CAm15Gerq2bd2i+6LqO6Z5eHjovvvq66cff3DjyHCjFOqAOHDggHr06HHFZdLS0nT69Gmnr7S0tBs0Qrjb3H/OUdQ9dyvq3ru1ds0qTX9npry8vN09LOCmd/LUSWVmZqpEiRJO00uUKKFjx465aVS4kQp1QJw4cUKJiYlXXCYhIUGBgYFOX6/8I+EGjRDu1qr1w/rnp59rxqwPFRYWrufiBhGQAHAD5PGdjoLxxRdfXHH+7t27r7qOESNGaMiQIU7Tsjzs1zUu/HX4+/vL399fYWHhuqtmTTWof6+WL1uqlq3auHtowE0tOChYnp6eLidMHj9+XCVLlnTTqHAjuTUg2rVrJ5vNpiudx2m7ytlWdrtddrtzMHAS5a3Jsi7+Jz093d1DAW56Xt7eqhpZTeu+S3KcAJ2VlaV165LU5dGubh4dbgS3BkRoaKimTp2qtm3b5jh/8+bNqlOnzg0eFW6Es2dTtX//fsf3v//+m7Zv36bAwECFhpZVSsopHTx4UEePHJEk7duzR5JUsmRJlSwZot8OHNDX//5KUfWjFVy8uA4fOqSZM96R3e6jBg0auWWfgFvN47HdNfL5YapWrbqq17hLH85O1Llz59SufQd3Dw03gFsDok6dOtq4cWOuAXG1oxP469ryyy/q3eMJx/evTbh43spDbdtr3Isva+WK5Rr99xGO+cOeHSxJerLfAPXrP1Dedm9t2vS95sxO1OnTp1WiRAnVrltXiR9+rOKXndQFoGC0aNlKJ0+c0NQ3J+vYsaOKqFJVU99+TyV4C+OW4NbPgVi9erVSU1PVokWLHOenpqbq+++/V6NGZq8oeQsDKNz4HAig8Mrr50DwQVIAbjgCAii8+CApAABQYAgIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxmyWZVnuHgRwJWlpaUpISNCIESNkt9vdPRwAl+D5eesiIFDonT59WoGBgUpJSVFAQIC7hwPgEjw/b128hQEAAIwREAAAwBgBAQAAjBEQKPTsdrtGjx7NCVpAIcTz89bFSZQAAMAYRyAAAIAxAgIAABgjIAAAgDECAgAAGCMgUKi99dZbCg8Pl4+Pj+rVq6f169e7e0gAJK1atUoPPfSQypYtK5vNpgULFrh7SLjBCAgUWnPnztWQIUM0evRobdq0STVr1lTz5s115MgRdw8NuOWlpqaqZs2aeuutt9w9FLgJl3Gi0KpXr57uuecevfnmm5KkrKwslStXTgMHDtTw4cPdPDoA2Ww2mz7//HO1a9fO3UPBDcQRCBRK6enp2rhxo2JiYhzTPDw8FBMTo6SkJDeODAAgERAopI4dO6bMzEyVLl3aaXrp0qV16NAhN40KAJCNgAAAAMYICBRKJUuWlKenpw4fPuw0/fDhwypTpoybRgUAyEZAoFDy9vZWnTp1tGzZMse0rKwsLVu2TFFRUW4cGQBAkoq4ewBAboYMGaLY2FjVrVtX9957r9544w2lpqaqe/fu7h4acMs7c+aMkpOTHd/v2bNHmzdvVvHixVW+fHk3jgw3CpdxolB788039corr+jQoUOqVauWJk+erHr16rl7WMAtb+XKlWrSpInL9NjYWM2aNevGDwg3HAEBAACMcQ4EAAAwRkAAAABjBAQAADBGQAAAAGMEBAAAMEZAAAAAYwQEAAAwRkAAAABjBASAAtOtWze1a9fO8X3jxo01aNCgGz6OlStXymaz6dSpUzd828DNioAAbkHdunWTzWaTzWaTt7e3KlWqpLFjx+rChQsFut3PPvtM48aNy9Oy/NIHCjf+mBZwi2rRooVmzpyptLQ0ffXVV+rfv7+8vLw0YsQIp+XS09Pl7e2dL9ssXrx4vqwHgPtxBAK4RdntdpUpU0ZhYWHq16+fYmJi9MUXXzjednjxxRdVtmxZRURESJIOHDigzp07KygoSMWLF1fbtm21d+9ex/oyMzM1ZMgQBQUFqUSJEnruued0+Z/aufwtjLS0NA0bNkzlypWT3W5XpUqVNGPGDO3du9fxh5qCg4Nls9nUrVs3SRf/rHtCQoIqVKggX19f1axZU59++qnTdr766itVrlxZvr6+atKkidM4AeQPAgKAJMnX11fp6emSpGXLlmnHjh1aunSpFi1apIyMDDVv3lz+/v5avXq11q5dKz8/P7Vo0cJxm9dee02zZs3S+++/rzVr1ujEiRP6/PPPr7jNJ554Qh9//LEmT56sbdu26e2335afn5/KlSun+fPnS5J27NihgwcPatKkSZKkhIQEffDBB5o+fbq2bNmiwYMHq2vXrvrPf/4j6WLodOjQQQ899JA2b96sXr16afjw4QV1twG3LgvALSc2NtZq27atZVmWlZWVZS1dutSy2+1WXFycFRsba5UuXdpKS0tzLD979mwrIiLCysrKckxLS0uzfH19ra+//tqyLMsKDQ21JkyY4JifkZFh3X777Y7tWJZlNWrUyHrmmWcsy7KsHTt2WJKspUuX5jjGFStWWJKskydPOqadP3/eKlq0qPXtt986LduzZ0/r0UcftSzLskaMGGFFRkY6zR82bJjLugBcH86BAG5RixYtkp+fnzIyMpSVlaXHHntMY8aMUf/+/VWjRg2n8x5+/PFHJScny9/f32kd58+f165du5SSkqKDBw+qXr16jnlFihRR3bp1Xd7GyLZ582Z5enqqUaNGeR5zcnKyzp49qwcffNBpenp6uu6++25J0rZt25zGIUlRUVF53gaAvCEggFtUkyZNNG3aNHl7e6ts2bIqUuR//xwUK1bMadkzZ86oTp06mjNnjst6QkJCrmn7vr6+xrc5c+aMJGnx4sW67bbbnObZ7fZrGgeAa0NAALeoYsWKqVKlSnlatnbt2po7d65KlSqlgICAHJcJDQ3VunXr1LBhQ0nShQsXtHHjRtWuXTvH5WvUqKGsrCz95z//UUxMjMv87CMgmZmZjmmRkZGy2+3av39/rkcuqlatqi+++MJp2nfffXf1nQRghJMoAVzV3/72N5UsWVJt27bV6tWrtWfPHq1cuVJPP/20fvvtN0nSM888o5dfflkLFizQ9u3b9dRTT13xMxzCw8MVGxurHj16aMGCBY51zps3T5IUFhYmm82mRYsW6ejRozpz5oz8/f0VFxenwYMHKzExUbt27dKmTZs0ZcoUJSYmSpL69u2rnTt36tlnn9WOHTv00UcfadasWQV9FwG3HAICwFUVLVpUq1atUvny5dWhQwdVrVpVPXv21Pnz5x1HJIYOHarHH39csbGxioqKkr+/v9q3b3/F9U6bNk0dO3bUU089pSpVqqh3795KTU2VJN12222Kj4/X8OHDVbp0aQ0YMECSNG7cOI0cOVIJCQmqWrWqWrRoocWLF6tChQqSpPLly2v+/PlasGCBatasqenTp+ull14qwHsHuDXZrNzOcAIAAMgFRyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAMQICAAAYIyAAAIAxAgIAABgjIAAAgDECAgAAGCMgAACAsf8HtmwjOe2+7TMAAAAASUVORK5CYII=\n",
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
      "       False       0.99      1.00      1.00     22095\n",
      "        True       0.00      0.00      0.00       113\n",
      "\n",
      "    accuracy                           0.99     22208\n",
      "   macro avg       0.50      0.50      0.50     22208\n",
      "weighted avg       0.99      0.99      0.99     22208\n",
      "\n",
      "Accuracy on Validation Set (Stacking): 0.99%\n"
     ]
    },
    {
     "data": {
      "image/png": "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xIkT9fjjj2v8+PHat2+funbtqszMTMc6S5cuVffu3VWyZEnFx8era9eu6tevnxITE/PcZoMGDXTy5EnHnwvcwizgJnHq1ClLkhUTE1Og9ZOSkixJVv/+/Z3G4+LiLElWQkKCYywkJMSSZK1evdoxduTIEctut1tDhw51jO3du9eSZE2cONFpm7GxsVZISEiuOYwePdr68x+zyZMnW5Kso0eP5jvvnH189NFHjrG6deta5cuXt1JTUx1jmzdvttzc3KxevXrl2l/fvn2dttmlSxerbNmy+e7zz8fh7e1tWZZlPfjgg1bLli0ty7KsrKwsq2LFitbYsWPzfA7Onz9vZWVl5ToOu91ujRs3zjG2cePGXMeWIzo62pJkzZgxI89l0dHRTmPffPONJckaP368tWfPHsvHx8fq3LnzVY8xOTnZkmRNmzYt17KXXnrJkmR5e3tb7du3t1555RUrMTEx13pXOo709PRcY/Hx8ZbNZrP279/vGIuKirJ8fX2dxizLsrKzsx3/n/P7efToUWv79u1WcHCw1ahRI+v48eNOj7n89Zfze1S2bFmndb/66itLkrV48WLHWO3ata3bb7/dOn36tGNs1apVlqQ8X9M//PCDJcmaP39+rmW4tXAGAjeNtLQ0SZKvr2+B1s+53WzIkCFO40OHDpWkXNdK1KxZU82aNXN8HRgYqLCwMO3Zs+ea53y5nGsnvvrqqwJf9JaSkqKkpCT17t1bZcqUcYzfeeedat26dZ631T3xxBNOXzdr1kypqamO57AgevbsqVWrVunQoUNKSEjQoUOH8nz7Qrp03YSb26W/TrKyspSamup4e+bHH38s8D7tdrv69OlToHXbtGmjxx9/XOPGjVPXrl3l6empd99996qPS01NlSQFBATkWjZ27FjNmzdP9erV0zfffKORI0eqQYMGql+/fq63S/Lj5eXl+P+zZ8/q2LFjatq0qSzL0k8//STp0rU0q1evVt++fVW5cmWnx1/+lpckbdu2TdHR0QoNDdWKFSvynHteunfv7rRuzus75zV98OBBbd26Vb169XJ6Oyc6Olq1a9fOc5s527varaX46yMgcNPw8/OTJJ0+fbpA6+/fv19ubm6qXr2603jFihVVunRp7d+/32n88r/IpUt/WZ44ceIaZ5xb9+7dFRkZqf79+6tChQrq0aOH/vWvf10xJnLmGRYWlmtZeHi4jh07prNnzzqNX34sOX/pmxzLfffdJ19fX82fP19z585Vo0aNcj2XObKzszV58mT97W9/k91uV7ly5RQYGKgtW7bo1KlTBd7nbbfdZnTB5KRJk1SmTBklJSVp6tSpjusUCsLK5z38hx9+WGvWrNGJEye0bNky9ezZUz/99JM6depUoLtPDhw44Ig9Hx8fBQYGKjo6WpIcz0XOP+AREREFmmunTp3k6+urb775xvHnoCCu9jrIeW3l9fua3+91zvOWV+jg1kJA4Kbh5+en4OBgbdu2zehxBf2LrkSJEnmO5/cPTUH2kfP+fA4vLy+tXr1aK1as0KOPPqotW7aoe/fuat26da51r8f1HEsOu92url27avbs2VqwYEG+Zx8k6dVXX9WQIUMUFRWlTz75RN98842WL1+uWrVqGd1e+Ofv3gvip59+ctwdsXXr1gI9pmzZspKuHlN+fn5q3bq15s6dq9jYWO3evVvr16+/4mOysrLUunVrLV26VMOHD9fChQu1fPlyxwWW13qr5QMPPKDdu3dr7ty5Ro8rjNfB5XKet3Llyl3zNvDXQEDgptKxY0ft3r1b69atu+q6ISEhys7O1q5du5zGDx8+rJMnTzruqCgMAQEBTncs5Lj8LIckubm5qWXLlnrjjTf0yy+/6JVXXlFCQoK+/fbbPLedM8+dO3fmWrZjxw6VK1dO3t7e13cA+cj57vv06dN5Xnia4/PPP1eLFi30wQcfqEePHmrTpo1atWqV6zkpzO9az549qz59+qhmzZp67LHHNGHChDzvMLhc5cqV5eXlpb179xZ4XzkfFpaSkiIp/+PYunWrfv31V73++usaPny4YmJi1KpVq1wXdVatWlWSChzDEydOVL9+/fTkk09q3rx5BZ731eS8tpKTk3Mty2tMkuN5Cw8PL7R54OZEQOCm8vzzz8vb21v9+/d33ML2Z7t379aUKVMkXToFLynXnRJvvPGGJKlDhw6FNq9q1arp1KlT2rJli2MsJSVFCxYscFovr6v7cz6I6PJbS3MEBQWpbt26mj17ttM/yNu2bdOyZcscx1kUWrRooZdfflnTp09XxYoV812vRIkSub6r/eyzz/THH384jeWETl6xZWr48OE6cOCAZs+erTfeeEOhoaGKjY3N93nMUbJkSTVs2FCbNm1yGk9PT883TP/9739L+t/bSPkdR853/H9+LizLcrwmcwQGBioqKkoffvihDhw44LQsr7MDNptNM2fO1IMPPqjY2FgtWrToisdYUMHBwYqIiNDHH3+sM2fOOMa/++67fM/oJCYmyt/fX7Vq1SqUOeDmxQdJ4aZSrVo1zZs3T927d1d4eLjTJ1H+8MMP+uyzz9S7d29JUp06dRQbG6uZM2fq5MmTio6O1oYNGzR79mx17tw531sEr0WPHj00fPhwdenSRc8884zS09P1zjvv6I477nC6iHDcuHFavXq1OnTooJCQEB05ckRvv/22br/9dt1zzz35bn/ixIlq3769mjRpon79+uncuXOaNm2a/P39NWbMmEI7jsu5ubnpH//4x1XX69ixo8aNG6c+ffqoadOm2rp1q+bOnev4TjtHtWrVVLp0ac2YMUO+vr7y9vZW48aNVaVKFaN5JSQk6O2339bo0aMdt2N+9NFHat68uUaNGqUJEyZc8fExMTEaOXKk0tLSHNcUpKenq2nTprr77rvVrl07VapUSSdPntTChQu1Zs0ade7cWfXq1bvicdSoUUPVqlVTXFyc/vjjD/n5+emLL77I8+2SqVOn6p577lH9+vX12GOPqUqVKtq3b5+WLl2a50dku7m56ZNPPlHnzp3VrVs3ff3114XyYU6vvvqqYmJiFBkZqT59+ujEiROaPn26IiIinKIix/Lly9WpUyeugQC3ceLm9Ouvv1oDBgywQkNDLQ8PD8vX19eKjIy0pk2bZp0/f96xXmZmpjV27FirSpUqVsmSJa1KlSpZI0aMcFrHsi7dxtmhQ4dc+7n89sH8buO0LMtatmyZFRERYXl4eFhhYWHWJ598kus2zpUrV1oxMTFWcHCw5eHhYQUHB1sPP/yw9euvv+bax+W3CK5YscKKjIy0vLy8LD8/P6tTp07WL7/84rTOn2/7+7OPPvrIkmTt3bs33+fUspxv48xPfrdxDh061AoKCrK8vLysyMhIa926dXnefvnVV19ZNWvWtNzd3Z2OMzo62qpVq1ae+/zzdtLS0qyQkBCrfv36VmZmptN6gwcPttzc3Kx169Zd8RgOHz5subu7W3PmzHGMZWZmWu+9957VuXNnKyQkxLLb7VapUqWsevXqWRMnTrQyMjIKdBy//PKL1apVK8vHx8cqV66cNWDAAGvz5s15/p5u27bN6tKli1W6dGnL09PTCgsLs0aNGuVYntfvZ3p6uhUdHW35+PhY//3vfy3Lyv82zrxep5Ks0aNHO419+umnVo0aNSy73W5FRERYixYtsh544AGrRo0aTutt377dkmStWLHiis8vbg02y+LjxADcevr166dff/1Va9ascfVUiqW6desqMDBQy5cvd4w999xzWr16tRITEzkDAa6BAHBrGj16tDZu3Fisf5z3jZCZmamLFy86ja1atUqbN292+vjw1NRUvf/++xo/fjzxAEkSZyAA4Ba2b98+tWrVSo888oiCg4O1Y8cOzZgxQ/7+/tq2bZvjtlfgclxECQC3sICAADVo0EDvv/++jh49Km9vb3Xo0EGvvfYa8YAr4gwEAAAwxjUQAADAGAEBAACMERAAAMDYX/IiSq96T7t6CgCu4MTG6a6eAoB8eBawDDgDAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwREAAAwBgBAQAAjBEQAADAGAEBAACMERAAAMAYAQEAAIwR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//yzBg8erEceeUTfffedpEuh07VrV3Xq1ElJSUnq37+/XnjhhaJ62oBblwXglhMbG2vFxMRYlmVZ2dnZ1vLlyy273W7FxcVZsbGxVoUKFayMjAzH+nPmzLHCwsKs7Oxsx1hGRobl5eVlffPNN5ZlWVZQUJA1YcIEx/LMzEzr9ttvd+zHsiwrOjraevbZZy3LsqydO3dakqzly5fnOcdvv/3WkmSdOHHCMXb+/HmrVKlS1g8//OC0br9+/ayHH37YsizLGjFihFWzZk2n5cOHD8+1LQDXh2sggFvUkiVL5OPjo8zMTGVnZ6tnz54aM2aMnnrqKdWuXdvpuofNmzcrOTlZvr6+Tts4f/68du/erVOnTiklJUWNGzd2LHN3d1fDhg1zvY2RIykpSSVKlFB0dHSB55ycnKz09HS1bt3aafzChQuqV6+eJGn79u1O85CkJk2aFHgfAAqGgABuUS1atNA777wjDw8PBQcHy939f38deHt7O6175swZNWjQQHPnzs21ncDAwGvav5eXl/Fjzpw5I0launSpbrvtNqdldrv9muYB4NoQEMAtytvbW9WrVy/QuvXr19f8+fNVvnx5+fn55blOUFCQ1q9fr6ioKEnSxYsXlZiYqPr16+e5fu3atZWdna3vvvtOrVq1yrU85wxIVlaWY6xmzZqy2+06cOBAvmcuwsPDtWjRIqex//73v1c/SABGuIgSwFX9/e9/V7ly5RQTE6M1a9Zo7969WrVqlZ555hn9/vvvkqRnn31Wr732mhYuXKgdO3boySefvOJnOISGhio2NlZ9+/bVwoULHdv817/+JUkKCQmRzWbTkiVLdPToUZ05c0a+vr6Ki4vT4MGDNXv2bO3evVs//vijpk2bptmzZ0uSnnjiCe3atUvDhg3Tzp07NW/ePM2aNauonyLglkNAALiqUqVKafXq1apcubK6du2q8PBw9evXT+fPn3eckRg6dKgeffRRxcbGqkmTJvL19VWXLl2uuN133nlHDz74oJ588knVqFFDAwYM0NmzZyVJt912m8aOHasXXnhBFSpU0NNPPy1JevnllzVq1CjFx8crPDxc7dq109KlS1WlShVJUuXKlfXFF19o4cKFqlOnjmbMmKFXX321CJ8d4NZks/K7wgkAACAfnIEAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxggIAABgjIAAAADGCAgAAGCMgAAAAMYICAAAYIyAAAAAxv4PST2qrAk/frsAAAAASUVORK5CYII=\n",
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
      "       False       0.99      1.00      1.00     22095\n",
      "        True       0.00      0.00      0.00       113\n",
      "\n",
      "    accuracy                           0.99     22208\n",
      "   macro avg       0.50      0.50      0.50     22208\n",
      "weighted avg       0.99      0.99      0.99     22208\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Evaluate each model on the validation set\n",
    "evaluate_model(smote_gbc_model, X_val, y_val, \"Gradient Boosting\")\n",
    "evaluate_model(smote_rfc_model, X_val, y_val, \"Random Forest\")\n",
    "evaluate_model(smote_stack_model, X_val, y_val, \"Stacking\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "gtwLcD61SiHO"
   },
   "outputs": [],
   "source": []
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
