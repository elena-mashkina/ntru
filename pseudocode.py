import math

#global variables known to everyone
N = 0
p = 0
q = 0

#setup 1
def generate_params():
  #is q is considerably(?) larger than p?
  #check if gcd is 1 math.gcd(p,q)
  #if yes, return p, q
  return N, p, q

def generate_polynomial():
  return polynomial


#setup 2
def keypair_creation():
  generate_params()
  #generate 2 polynomials f and g
  # def generate_private_key() ==> generate polynomial f with inverses modulo q and modulo p,
  # def inverse_f() ==> calculate using modification of the Euclidean algorithm method
  # def compute public key ==> uses convolutional mulitplication
  return [pub_key, private_key, inv_f]


# encryption
def playtext_to_polynomial(message):
  #convert plaintext to polynomial somehow
  return m

def encrypt(message, pub_key):
  r = generate_polynomial()
  #computation according to the formula m_encrypted = p*(r~pub_key) + message
  return m_encrypted


def decrypt(message, private_key, inv_f):
  #a = private_key~message
  #change coefficients of a for the integers in interval [-q/2, +q/2]
  #m_decrypted = inv_f~a
  return m_decrypted

# setup
keys = keypair_creation()

# encryption
message = playtext_to_polynomial('input')
encrypted_message = encrypt(message, keys.pub_key)
decrypted_message = decrypt(m_encrypted, keys.private_key, inv_f)