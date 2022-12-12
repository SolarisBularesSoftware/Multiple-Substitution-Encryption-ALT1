url = "https://github.com/flowlord/Multiple-Substitution-Encryption/blob/main/README.md"

version_actuelle = "001114588862 - 33221 - 1444593247B"

import urllib.request

try:
	data = urllib.request.urlopen(url)

	data = data.read().decode('utf-8')

	if version_actuelle not in data:
		print("\t** [ Version obsolète, mise à jour nécessaire. ] **")

except urllib.error.URLError:
	pass

