import argparse
import sys
import random

header1 = '''
\033[95m
 .-') _    ('-. .-.   ('-.          (`\ .-') /`  ('-.         .-') _  _ .-') _   
(  OO) )  ( OO )  / _(  OO)          `.( OO ),' ( OO ).-.    ( OO ) )( (  OO) )  
/     '._ ,--. ,--.(,------.      ,--./  .--.   / . --. /,--./ ,--,'  \     .'_  
|'--...__)|  | |  | |  .---'      |      |  |   | \-.  \ |   \ |  |\  ,`'--..._) 
'--.  .--'|   .|  | |  |          |  |   |  |,.-'-'  |  ||    \|  | ) |  |  \  ' 
   |  |   |       |(|  '--.       |  |.'.|  |_)\| |_.'  ||  .     |/  |  |   ' | 
   |  |   |  .-.  | |  .--'       |         |   |  .-.  ||  |\    |   |  |   / : 
   |  |   |  | |  | |  `---.      |   ,'.   |   |  | |  ||  | \   |   |  '--'  / 
   `--'   `--' `--' `------'      '--'   '--'   `--' `--'`--'  `--'   `-------'  \033[0m'''

header2 = '''
\033[93m
                                                   
  *   )    )         (  (                    (     
` )  /( ( /(    (    )\))(   '    )          )\ )  
 ( )(_)))\())  ))\  ((_)()\ )  ( /(   (     (()/(  
(_(_())((_)\  /((_) _(())\_)() )(_))  )\ )   ((_)) 
|_   _|| |(_)(_))   \ \((_)/ /((_)_  _(_/(   _| |  
  | |  | ' \ / -_)   \ \/\/ / / _` || ' \))/ _` |  
  |_|  |_||_|\___|    \_/\_/  \__,_||_||_| \__,_|  
                                                 \033[0m'''

header3 = '''
\033[96m
   ▄▄▄▄▀ ▄  █ ▄███▄         ▄ ▄   ██      ▄   ██▄   
▀▀▀ █   █   █ █▀   ▀       █   █  █ █      █  █  █  
    █   ██▀▀█ ██▄▄        █ ▄   █ █▄▄█ ██   █ █   █ 
   █    █   █ █▄   ▄▀     █  █  █ █  █ █ █  █ █  █  
  ▀        █  ▀███▀        █ █ █     █ █  █ █ ███▀  
          ▀                 ▀ ▀     █  █   ██       
                                   ▀                \033[0m'''


headers = [header1,header2,header3]
print(headers[random.randint(0,2)])

parse = argparse.ArgumentParser()
parse.add_argument("-o","--output", help="To specify output file (only for repair)", required=False)
parse.add_argument("-i", "--input", help="To specify the input file", required=True)
parse.add_argument("-m", "--mode", help="Select mode : Repair or Analyse", required=True)
args = parse.parse_args()

global dico_signature
dico_signature = {'ffd8ffe0':"JPG","89504e470d0a1a0a":"PNG","255044462d":"PDF",'4d5a':"EXE","4d5a":"DLL","4d5a":"EXE","5a4d":"EXE","7f454c46":"ELF","524946":"WAV","1f8b":"GZ","504b0304":"ZIP",'7573746172':"TAR","424d":"BMP","47494638":"GIF","377abcaf271c":"7Z","0a0d0d0a":"PCAPNG","a1b2c3d4":"PCAP","526172211a07":"RAR"}

def identify(file):
    type = None
    print('\033[92m' +"[+] Starting Process"+'\033[0m')
    with open(file,"rb") as input_file:
        data = input_file.read().hex()
    liste_type = []
    for i in range(0,20):
        if data[0:i] in dico_signature:
            type = dico_signature[data[0:i]]
            liste_type.append(type)

    if type == None:
        print('\033[93m' + "[-] Cant identify header, may be broken"+'\033[0m')
    else:
        for type in liste_type:
            print('\033[92m' + f'[+] File Type : {type}'+'\033[0m')


def write_header(header,file):
    try:
        with open(file,"rb") as input_file:
            data = input_file.read().hex()
    except:
        print("\033[1;31;40m" + "[FATAL] File not Found"+'\033[0m')
        sys.exit()
    to_write = header + data[len(header):]
    with open(args.output,"wb") as output_file:
        output_file.write(bytes.fromhex(to_write))

def get_signature_from_ext():
    try:
        type = args.input.split(".")[1]
    except:
        print("\033[1;31;40m" + "[FATAL] Not good format"+'\033[0m')
        sys.exit()
    try:
        signature = list(dico_signature.keys())[list(dico_signature.values()).index(type.upper())]
    except:
        print("\033[1;31;40m" + "[FATAL] File not supported"+'\033[0m')
        sys.exit()
    return signature

if args.mode.upper() == "ANALYSE":
    try:
        identify(args.input)
    except:
        print("\033[1;31;40m" + "[FATAL] File not Found or other error"+'\033[0m')
elif args.mode.upper() == "REPAIR":
    if args.output != None:
        print('\033[92m' +"[+] Starting Repairing Process"+'\033[0m')
        write_header(get_signature_from_ext(),args.input)
        print('\033[92m' +"[+] Done !"+'\033[0m')
    else:
        print("\033[1;31;40m" + "[-] Select an output file"+'\033[0m')
else:
    print("\033[1;31;40m" + "[-] Invalid Mode"+'\033[0m')