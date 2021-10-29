# Hijacker
A python tool to automatically scan for broken links on a webpage.
Sugesstions and issues are welcome because I know codes can never be perfect.

### Note: Please do not use this tool for blackhat hacking purposes. I am not resposible for any damage caused by this tool.


### How to install?
This command is for Debian/Linux Based Shells.
```bash
git clone https://github.com/HACKE-RC/hijacker
cd hijacker
chmod +x *
sudo setup.sh
```
For termux:
```bash
git clone https://github.com/HACKE-RC/hijacker
cd hijacker
chmod +x *
sudo termux-setup.sh
```

After running setup.sh you can simply type hijacker -h to see the help menu.

If you get any error while installing the tool you can create an issue or message me at twitter.com/coder_rc or If you are not able to run it after running the setup.sh you can simply run ```sudo setup.sh``` again to repair it.


### Requirements:
1. Python 3.x.x or greater.
2. sh based shell(Works fine in WSL, WSL2 and termux).

## How to use?
Just run the following command to see the help menu.
```bash
hijacker -h
```
Use this command to start scanning on the list of subdomains.
```bash
hijacker <website>
```
Enable verbose mode.
```bash
hijacker example.com -v
```

### Setup
[![asciicast](https://asciinema.org/a/BX9KgmIZ9cH93oa5D3e2rZ6fl.svg)](https://asciinema.org/a/BX9KgmIZ9cH93oa5D3e2rZ6fl)


#### Made with <3 by HACKE-RC commonly known as RC.
