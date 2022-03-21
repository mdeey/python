
import re

phoneNumberRex = re.compile (r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

mo = phoneNumberRex.search('call me at 123-192-1291 or at 001-263-3746')

print(mo.group())
