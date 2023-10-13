import sys
import optparse
import hashlib

def hash(password):
  h = hashlib.sha512()
  h.update(password.encode())
  return h.hexdigest()

def main():
  usage = '%prog -h'
  parser = optparse.OptionParser(usage)
  parser.add_option('-p', '--password', dest='password', action='store', help='Hashed password to be cracked')
  parser.add_option('-w', '--wordlist', dest='wordlist', action='store', help='Path to a wordlist of passwords')

  (args, _) = parser.parse_args()
  wordlist_path = args.wordlist
  provided_password = args.password

  if not wordlist_path or not provided_password:
    parser.print_usage()
    sys.exit(1)

  with open(wordlist_path, 'r') as wordlist:
    passwords = wordlist.readlines()
    for password in passwords:
      p = password.strip('\n')
      print('[+] - Trying {0}'.format(p))
      wordlist_hash = hash(p)
      
      if wordlist_hash == provided_password:
        print('[+] - Password found: {0}'.format(p))
        sys.exit(0)

if __name__ == '__main__':
  main()