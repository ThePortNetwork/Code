#Gets User Name
def run():
 with open('username.txt', 'r') as f:
  for word in f:
   username = bytearray.fromhex(word).decode()
   return username
