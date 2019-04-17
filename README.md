# Bitwarden decrypt CLI

> This is a port of the Bitwarden NodeJS CLI to Python focused on decryption of secrets

## How to install

### Pip
```
pip3 install bitwarden-simple-cli
```

## How to use ?

This tool do not replace the official NodeJs CLI of Bitwarden. It's a complementary tool to increase retrieval of numbers of secrets.

First, ensure that your bitwarden vault in unlocked and that your register the BW_SESSION in you environment.

### Get decrypted valued
```
bw-simple get UUID FIELD
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
time (for i in {1..20}; do IDS=('5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0' 'e050ece7-2361-4415-860b-aa2a00d9d2bd' '684119e7-3039-45f3-95e3-aa2a00db18f9') FIELDS=('password' 'username'); eval "time bw-simple get ${IDS[$((RANDOM % ${#IDS[@]}+1))]} ${FIELDS[$((RANDOM % ${#FIELDS[@]}+1))]} > /dev/null"; done)
bw-simple get 684119e7-3039-45f3-95e3-aa2a00db18f9 username > /dev/null  0,10s user 0,02s system 97% cpu 0,125 total
bw-simple get 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 username > /dev/null  0,11s user 0,02s system 97% cpu 0,142 total
bw-simple get 684119e7-3039-45f3-95e3-aa2a00db18f9 username > /dev/null  0,11s user 0,02s system 97% cpu 0,134 total
bw-simple get e050ece7-2361-4415-860b-aa2a00d9d2bd password > /dev/null  0,11s user 0,02s system 97% cpu 0,137 total
bw-simple get 684119e7-3039-45f3-95e3-aa2a00db18f9 password > /dev/null  0,11s user 0,02s system 97% cpu 0,131 total
bw-simple get 684119e7-3039-45f3-95e3-aa2a00db18f9 password > /dev/null  0,11s user 0,02s system 97% cpu 0,133 total
bw-simple get e050ece7-2361-4415-860b-aa2a00d9d2bd username > /dev/null  0,10s user 0,02s system 97% cpu 0,128 total
bw-simple get 684119e7-3039-45f3-95e3-aa2a00db18f9 password > /dev/null  0,11s user 0,02s system 97% cpu 0,135 total
bw-simple get e050ece7-2361-4415-860b-aa2a00d9d2bd password > /dev/null  0,11s user 0,02s system 97% cpu 0,141 total
bw-simple get 684119e7-3039-45f3-95e3-aa2a00db18f9 password > /dev/null  0,11s user 0,02s system 97% cpu 0,135 total
bw-simple get e050ece7-2361-4415-860b-aa2a00d9d2bd username > /dev/null  0,10s user 0,02s system 97% cpu 0,131 total
bw-simple get 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 username > /dev/null  0,12s user 0,03s system 97% cpu 0,151 total
bw-simple get 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 password > /dev/null  0,12s user 0,03s system 97% cpu 0,146 total
bw-simple get e050ece7-2361-4415-860b-aa2a00d9d2bd username > /dev/null  0,11s user 0,02s system 97% cpu 0,138 total
bw-simple get e050ece7-2361-4415-860b-aa2a00d9d2bd password > /dev/null  0,11s user 0,02s system 97% cpu 0,134 total
bw-simple get 684119e7-3039-45f3-95e3-aa2a00db18f9 password > /dev/null  0,11s user 0,02s system 97% cpu 0,139 total
bw-simple get 684119e7-3039-45f3-95e3-aa2a00db18f9 password > /dev/null  0,11s user 0,02s system 97% cpu 0,142 total
bw-simple get 684119e7-3039-45f3-95e3-aa2a00db18f9 password > /dev/null  0,11s user 0,02s system 97% cpu 0,131 total
bw-simple get e050ece7-2361-4415-860b-aa2a00d9d2bd username > /dev/null  0,11s user 0,02s system 97% cpu 0,138 total
bw-simple get 5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0 username > /dev/null  0,12s user 0,02s system 97% cpu 0,143 total
( for i in {1..20}; do; IDS=('5bfd3729-7074-46f8-bbe8-aa2a00d8c0f0'  ) FIELDS)  2,20s user 0,48s system 97% cpu 2,738 total

```

## License

GPLv3