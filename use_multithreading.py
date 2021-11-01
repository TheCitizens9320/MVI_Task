from web3 import Web3
from interface import getInterface
from abiMVI import getMVIAbi
from sushiABI import getSushiABI
from UniswapPairAddress import getUniswapPair
from SushiPairAddress import getSushiswapPair
import threading
import time
time1 = time.time()
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545/"))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Lay du lieu cac pair tren uniswap
WETH_ENJ = w3.eth.contract(address="0xE56c60B5f9f7B5FC70DE0eb79c6EE7d00eFa2625", abi=getInterface())#WETH_ENJ
WETH_MANA = w3.eth.contract(address="0x11b1f53204d03E5529F09EB3091939e4Fd8c9CF3", abi=getInterface())#MANA_WETH
WETH_SAND = w3.eth.contract(address="0x3dd49f67E9d5Bc4C5E6634b3F70BfD9dc1b6BD74", abi=getInterface())#SAND_WETH
WETH_AUDIO = w3.eth.contract(address="0xC730EF0f4973DA9cC0aB8Ab291890D3e77f58F79", abi=getInterface())#AUDIO_WETH
WETH_WAX = w3.eth.contract(address="0x0ee0cb563A52Ae1170Ac34fBb94C50e89aDDE4bD", abi=getInterface())#WAX/WETH
WETH_ERN = w3.eth.contract(address="0x570fEbDf89C07f256C75686CaCa215289bB11CFc", abi=getInterface())#ERN_WETH
WETH_NFTX = w3.eth.contract(address="0x7B890092f81B337Ed68FBa266AfC7b4c3710A55b", abi=getInterface())#NFTX_WETH
WETH_AXS = w3.eth.contract(address="0xa040832b1e5026Da6DC843E6773a9e4d02Fff9b1", abi=getInterface())#AXS_WETH
WETH_DG = w3.eth.contract(address="0x44c21F5DCB285D92320AE345C92e8B6204Be8CdF", abi=getInterface())#WETH_DG
WETH_WHALE = w3.eth.contract(address="0x4fdA00D490C1c05Ff15d7313d1cebe9c711e434b", abi=getInterface())#WHALE_WETH
WETH_TVK = w3.eth.contract(address="0x0F5A2Eb364D8B722CbA4E1E30E2Cf57b6F515B2a", abi=getInterface())#WETH_TVK
WETH_ILV = w3.eth.contract(address="0x8Fb8BF2B444e37379e46de8BB77C551bd008f0aD", abi=getInterface())#ILV_WETH
WETH_REVV = w3.eth.contract(address="0x724d5c9c618A2152e99a45649a3B8cf198321f46", abi=getInterface())#REVV_WETH
WETH_RARI = w3.eth.contract(address="0x86fEf14C27C78dEAEb4349FD959CAA11fc5B5D75", abi=getInterface())#ETH_RARI
WETH_MVI = w3.eth.contract(address="0x4d3C5dB2C68f6859e0Cd05D080979f597DD64bff", abi=getInterface())#MVI_ETH

#Lay du lieu cac pair tren sushiswap
WETH_ENJ_SU = w3.eth.contract(address="0x6D7c40746Accd8e028Da5848E38093e5BaFE8a18", abi=getInterface())#WETH_ENJ
WETH_MANA_SU = w3.eth.contract(address="0x1bEC4db6c3Bc499F3DbF289F5499C30d541FEc97", abi=getInterface())#MANA_WETH
WETH_SAND_SU=0
WETH_AUDIO_SU = w3.eth.contract(address="0x4F871F310AD0E8a170db0021c0ce066859d37469", abi=getInterface())#AUDIO_WETH
WETH_WAX_SU = 0
WETH_ERN_SU = 0
WETH_NFTX_SU = w3.eth.contract(address="0x31d64f9403E82243e71C2af9D8F56C7DBe10C178", abi=getSushiABI())#NFTX_WETH
WETH_AXS_SU = w3.eth.contract(address="0x0C365789DbBb94A29F8720dc465554c587e897dB", abi=getSushiABI())#AXS_WETH
WETH_DG_SU = w3.eth.contract(address="0xd3dA6236aEcb6b55F571249c011B8EEC340a418E", abi=getSushiABI())#WETH_DG
WETH_WHALE_SU = 0
WETH_TVK_SU = 0
WETH_ILV_SU = w3.eth.contract(address="0x6a091a3406E0073C3CD6340122143009aDac0EDa", abi=getSushiABI())#ILV_WETH
WETH_REVV_SU = w3.eth.contract(address="0xc926990039045611eb1DE520C1E249Fd0d20a8eA", abi=getSushiABI())#REVV_WETH
WETH_RARI_SU = w3.eth.contract(address="0x53aaBCcAE8C1713a6a150D9981D2ee867D0720e8", abi=getInterface())#ETH_RARI
WETH_MVI_SU = w3.eth.contract(address="0x7468171C8904F813302719e190292F61f3698C63", abi=getInterface())#MVI_ETH

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
dataPairsUNI = [WETH_ENJ, WETH_MANA, WETH_SAND,WETH_AUDIO,WETH_WAX,WETH_ERN,WETH_NFTX,WETH_AXS,WETH_DG,WETH_WHALE,WETH_TVK,WETH_ILV,WETH_REVV,WETH_RARI,WETH_MVI]
dataPairSUSHI = [WETH_ENJ_SU, WETH_MANA_SU, WETH_SAND_SU,WETH_AUDIO_SU,WETH_WAX_SU,WETH_ERN_SU,WETH_NFTX_SU,WETH_AXS_SU,WETH_DG_SU,WETH_WHALE_SU,WETH_TVK_SU,WETH_ILV_SU,WETH_REVV_SU,WETH_RARI_SU,WETH_MVI_SU]
mintData = []
def getChildTokenData():
	childToken = w3.eth.contract(address="0xd8EF3cACe8b4907117a45B0b125c68560532F94D", abi=getMVIAbi())
	data = childToken.functions.getRequiredComponentUnitsForIssue(Web3.toChecksumAddress('0x72e364f2abdc788b7e918bc238b21f109cd634d7'), 1000000000000000000).call()
	count_=0
	for i in data[1]:
		if count_ == 4:
			mintData.append(i/100000000)
		elif count_ == 9:
			mintData.append(i/10000)
		else: 
			mintData.append(i/1000000000000000000)
		count_ +=1
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
reserversUNI = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
reserversSUSHI = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
check = []
def getPairData(count, pair, type):
	if type == 1:
		if count in [0,8,10,13]:
			reserversUNI[2*count] = pair.functions.getReserves().call()[0]/1000000000000000000
			reserversUNI[2*count+1] = pair.functions.getReserves().call()[1]/1000000000000000000
		elif count == 4:
			reserversUNI[2*count] = pair.functions.getReserves().call()[1]/1000000000000000000
			reserversUNI[2*count+1] = pair.functions.getReserves().call()[0]/100000000
		elif count == 9:
			reserversUNI[2*count] = pair.functions.getReserves().call()[1]/1000000000000000000
			reserversUNI[2*count+1] = pair.functions.getReserves().call()[0]/10000
		else:
			reserversUNI[2*count] = pair.functions.getReserves().call()[1]/1000000000000000000
			reserversUNI[2*count+1] = pair.functions.getReserves().call()[0]/1000000000000000000
	else:
		if pair == 0:
			reserversSUSHI[2*count] = 0
			reserversSUSHI[2*count+1] = 0
		elif count in [0,8,10,13]:
			reserversSUSHI[2*count] = pair.functions.getReserves().call()[0]/1000000000000000000
			reserversSUSHI[2*count+1] = pair.functions.getReserves().call()[1]/1000000000000000000
		elif count == 4:
			reserversSUSHI[2*count] = pair.functions.getReserves().call()[1]/1000000000000000000
			reserversSUSHI[2*count+1] = pair.functions.getReserves().call()[0]/100000000
		elif count == 9:
			reserversSUSHI[2*count] = pair.functions.getReserves().call()[1]/1000000000000000000
			reserversSUSHI[2*count+1] = pair.functions.getReserves().call()[0]/10000
		else:
			reserversSUSHI[2*count] = pair.functions.getReserves().call()[1]/1000000000000000000
			reserversSUSHI[2*count+1] = pair.functions.getReserves().call()[0]/1000000000000000000
	check.append(1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# reserversUNI = []
def getInfoUniPair():
	count_1 = 0
	for i in dataPairsUNI:
		t = threading.Thread(target=getPairData, args=(count_1, i, 1))
		t.start()
		count_1 +=1
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# reserversSUSHI = []
def getInfoSushiPair():
	count_2 = 0
	for i in dataPairSUSHI:
		t = threading.Thread(target=getPairData, args=(count_2, i, 2))
		t.start()
		count_2 +=1
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
getInfoUniPair()
getInfoSushiPair()
t = threading.Thread(target=getChildTokenData, args=())
t.start()
while len(mintData)<14 or len(check)<30:
	continue
def whichBeUsedToSwap(x, index):
	temp = reserversUNI[2*index]*reserversSUSHI[2*index+1] - reserversUNI[2*index+1]*reserversSUSHI[2*index] + 0.997*x*(reserversUNI[2*index] - reserversSUSHI[2*index])
	x = x*mintData[index]
	if index in [2, 4, 5, 9, 10]:
		return 1
	elif temp > 0:
		return 1
	else:
		return 2
def calculateBenefit(y):
	benefit = -(reserversUNI[28]*y*1000)/(997*reserversUNI[29] - 997*y)
	for i in range(14):
		if whichBeUsedToSwap(y, i)==2:
			benefit = benefit + (997*mintData[i]*reserversSUSHI[2*i]*y)/(1000*reserversSUSHI[2*i+1]+997*mintData[i]*y)
		else:
			benefit = benefit + (997*mintData[i]*reserversUNI[2*i]*y)/(1000*reserversUNI[2*i+1]+997*mintData[i]*y)
	return benefit
right = reserversUNI[29]-0.000000000000001
def calculateMaximumBenefit(left, right):
	while right-left > 0.00000001:
		x1 = left + (right-left)/3.0
		x2 = right - (right-left)/3.0
		if calculateBenefit(x1) > calculateBenefit(x2):
			right=x2
		else: 
			left=x1
	return right
right = calculateMaximumBenefit(0, right)
x = 283.44115599631499264
print("their:")
print(calculateBenefit(283.44115599631499264))
print("my:")
print(calculateBenefit(right))
# print(right)
result = 1000*reserversUNI[28]*right/(997*(reserversUNI[29]+right))
print("WETH: ")
print(result)
print("Time")
print(time.time()-time1)



