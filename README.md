# Bitwarden decrypt CLI

> This is a port of the Bitwarden NodeJS CLI to Python focused on decryption of secrets

## How to install

### Pip
```
pip3 install bitwarden-simple-cli
```

## How to use ?

This tool do not replace the official NodeJs CLI of Bitwarden. You still need it to perform auth, unlock and sync operations.

First, ensure that your bitwarden vault in unlocked and that you register the BW_SESSION in your environment.

### Get decrypted valued
```
bw-simple get [FIELD=password] UUID
```
### List items
```
bw-simple list
```

## Currently supported fields

The script currently handles the decryption of the following entities and fields:

- login
    - [ custom field name ]
    - name
    - notes
    - password
    - uri: retrieve first uri without new line
    - uris: retrieve all uris, one per line
    - username
- note
    - [ custom field name ]
    - name
    - notes
    
It supports decryption of personal and organization ciphers.

## Why this project ?

We use Ansible to manage infrastructures and use a lookup plugin to grab hundred of secrets. Each secret is retrieven 
with the native NodeJS CLI in about 0.85s on my computer. When you have hundreds of secrets, that makes long minutes to wait.

According to https://github.com/bitwarden/cli/issues/67, node looks like to suffer from slow bootstrap.

This port to Python is aimed to increase secrets lookup performance. First benchmarks spotted that secrets could be 
retrieven in around 0.15s with this port.

### Benchmark

#### Original bw cli: 20 requests - 17,21s
```
time (for i in {1..20}; do IDS=('5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0' 'e050ece7-2361-4415-860b-aa2a00d9d2bd' '684119e7-3039-45f3-95e3-aa2a00db18f9') FIELDS=('password' 'username'); eval "time bw get ${FIELDS[$((RANDOM % ${#FIELDS[@]}+1))]} ${IDS[$((RANDOM % ${#IDS[@]}+1))]} > /dev/null"; done)
bw get password 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,83s user 0,10s system 118% cpu 0,786 total
bw get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,83s user 0,10s system 118% cpu 0,786 total
bw get password 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,86s user 0,11s system 117% cpu 0,817 total
bw get username e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,87s user 0,11s system 117% cpu 0,832 total
bw get username 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,86s user 0,11s system 119% cpu 0,809 total
bw get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,84s user 0,10s system 119% cpu 0,787 total
bw get username e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,84s user 0,10s system 119% cpu 0,790 total
bw get password 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,85s user 0,10s system 118% cpu 0,807 total
bw get username 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,85s user 0,10s system 117% cpu 0,806 total
bw get username e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,84s user 0,10s system 117% cpu 0,794 total
bw get username 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,84s user 0,10s system 118% cpu 0,796 total
bw get username e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,85s user 0,10s system 118% cpu 0,800 total
bw get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,85s user 0,10s system 118% cpu 0,797 total
bw get password 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,85s user 0,10s system 117% cpu 0,804 total
bw get password 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,86s user 0,10s system 118% cpu 0,810 total
bw get password 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,86s user 0,10s system 118% cpu 0,816 total
bw get password e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,87s user 0,11s system 118% cpu 0,821 total
bw get password 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,85s user 0,10s system 118% cpu 0,806 total
bw get password e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,93s user 0,12s system 117% cpu 0,888 total
bw get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  1,00s user 0,13s system 116% cpu 0,970 total
( for i in {1..20}; do; IDS=('5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0'  ) FIELDS)  17,21s user 2,11s system 118% cpu 16,327 total
```


#### bw-simple: 20 requests - 2,2s

```
time (for i in {1..20}; do IDS=('5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0' 'e050ece7-2361-4415-860b-aa2a00d9d2bd' '684119e7-3039-45f3-95e3-aa2a00db18f9') FIELDS=('password' 'username'); eval "time bw-simple get ${FIELDS[$((RANDOM % ${#FIELDS[@]}+1))]} ${IDS[$((RANDOM % ${#IDS[@]}+1))]} > /dev/null"; done)
bw-simple get username e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,08s user 0,03s system 84% cpu 0,134 total
bw-simple get password 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,08s user 0,02s system 96% cpu 0,110 total
bw-simple get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,08s user 0,02s system 96% cpu 0,113 total
bw-simple get password e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,09s user 0,03s system 96% cpu 0,116 total
bw-simple get password e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,08s user 0,03s system 95% cpu 0,108 total
bw-simple get password e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,08s user 0,02s system 96% cpu 0,107 total
bw-simple get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,09s user 0,03s system 97% cpu 0,116 total
bw-simple get password 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,09s user 0,03s system 96% cpu 0,122 total
bw-simple get password 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,09s user 0,03s system 95% cpu 0,115 total
bw-simple get username e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,09s user 0,03s system 97% cpu 0,115 total
bw-simple get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,08s user 0,03s system 96% cpu 0,113 total
bw-simple get username e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,09s user 0,03s system 96% cpu 0,118 total
bw-simple get password e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,08s user 0,03s system 95% cpu 0,109 total
bw-simple get password 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,08s user 0,02s system 96% cpu 0,102 total
bw-simple get password e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,08s user 0,02s system 96% cpu 0,102 total
bw-simple get username e050ece7-2361-4415-860b-aa2a00d9d2bd > /dev/null  0,08s user 0,02s system 96% cpu 0,106 total
bw-simple get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,08s user 0,02s system 97% cpu 0,106 total
bw-simple get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,08s user 0,02s system 96% cpu 0,110 total
bw-simple get password 684119e7-3039-45f3-95e3-aa2a00db18f9 > /dev/null  0,09s user 0,03s system 96% cpu 0,115 total
bw-simple get username 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 > /dev/null  0,08s user 0,02s system 96% cpu 0,107 total
( for i in {1..20}; do; IDS=('5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0'  ) FIELDS)  1,64s user 0,52s system 95% cpu 2,250 total
```

## Development

Development requirements are listed in requirements/dev.txt

```
mkvirtualenv3 bitwarden-simple-cli
workon bitwarden-simple-cli
pip3 install -r requirements/dev.txt
```

Testing is done through `pytest`. A sample database unlocked with `BW_SESSION` are provided.

## License

GPLv3
