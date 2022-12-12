url = "https://github.com/SolarisBularesSoftware/Multiple-Substitution-Encryption-ALT1/blob/main/README.md"



version_actuelle = "002114588862 - 88221 - 1444593247X"

import urllib.request

try:
	data = urllib.request.urlopen(url)

	data = data.read().decode('utf-8')

	if version_actuelle not in data:
		print("\t** [ Version obsolète, mise à jour nécessaire. ] **")

except urllib.error.URLError:
	pass

