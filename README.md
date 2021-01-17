# The Wand


![](wand.png)


## Presentation

The wand is a file recognizer and header repairer.

## Usage

### Linux :

#### Install
```sh
Set execution perms : chmod +x install.sh
Run install .sh : sudo bash install.sh
```
or
```sh
python3 EasySetup.py
```
#### Uninstall
```sh
Set execution perms : chmod +x uninstall.sh
Run install .sh : sudo bash uninstall.sh
```
or
```sh
python3 EasySetup.py
```

### Windows :
```sh
run shuriken from terminal or wsl
```

## Examples

### Repair the header of a file : 
```sh
wand -i file.jpg -o file_repaired.jpg -m repair
```
### Identify e file : 
```sh
wand -i file -m analyse
```

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
