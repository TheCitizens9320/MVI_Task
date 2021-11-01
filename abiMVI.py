def getMVIAbi():
	return([{"inputs":[{"internalType":"contract IController","name":"_controller","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_setToken","type":"address"},{"indexed":True,"internalType":"address","name":"_issuer","type":"address"},{"indexed":True,"internalType":"address","name":"_to","type":"address"},{"indexed":False,"internalType":"address","name":"_hookContract","type":"address"},{"indexed":False,"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"SetTokenIssued","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"_setToken","type":"address"},{"indexed":True,"internalType":"address","name":"_redeemer","type":"address"},{"indexed":True,"internalType":"address","name":"_to","type":"address"},{"indexed":False,"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"SetTokenRedeemed","type":"event"},{"inputs":[],"name":"controller","outputs":[{"internalType":"contract IController","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ISetToken","name":"_setToken","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"getRequiredComponentUnitsForIssue","outputs":[{"internalType":"address[]","name":"","type":"address[]"},{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ISetToken","name":"_setToken","type":"address"},{"internalType":"contract IManagerIssuanceHook","name":"_preIssueHook","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract ISetToken","name":"_setToken","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"issue","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract ISetToken","name":"","type":"address"}],"name":"managerIssuanceHook","outputs":[{"internalType":"contract IManagerIssuanceHook","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"contract ISetToken","name":"_setToken","type":"address"},{"internalType":"uint256","name":"_quantity","type":"uint256"},{"internalType":"address","name":"_to","type":"address"}],"name":"redeem","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"removeModule","outputs":[],"stateMutability":"nonpayable","type":"function"}])