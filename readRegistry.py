#read evironment key-value from Windows registry  

from winreg import *

regpath = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE) #|HKEY_CURRRENT_USER
aKey = OpenKey(aReg, regpath, 0, KEY_ALL_ACCESS)

#iterate through subkeys and variables
try:
	print("Listing subkeys in %s" % regpath)
	i = 0
	while True:
		asubkey = EnumKey(aKey, i) #subkeys
		print(asubkey)
		i += 1
except WindowsError:
    pass

try:
	print("Listing variables in %s" % regpath)
	i = 0
	while True:
		asubName,asubValue,asubType = EnumValue(aKey, i)
		print("%s -> %s" % (asubName, asubValue))
		i += 1
except WindowsError:
    pass

#just one value
keyname = "Path" #key to read
key,ktype = QueryValueEx(aKey,keyname) #array 
#key = QueryValueEx(aKey,keyname)[0]
print(key)
