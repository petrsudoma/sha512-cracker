# SHA-512 Hash cracker

Python script to crack SHA-512 hash using password wordlist.

You can use common.txt wordlist in the repository which is _100k-most-used-passwords-NCSC.txt from [SecLists](https://github.com/danielmiessler/SecLists)_

## Usage

**Get help**

```
python3 cracker.py -h
```

**Crack hashed password**

```
python3 cracker.py -p 6d9434097fa042666664e1d8a0f3dfd72f22e00d664f2e58e283e8b7f47909b77fac7fbbf28ab4e719c3fd593111431965227722cf714b25c0020773219f07af -w ./common.txt
```

### Author: Petr Šudoma
