import os,time
print('\n\x1b[1;37m[•] Checking Update...');time.sleep(0.5)
os.system('git pull')
os.system('xdg-open https://www.facebook.com/groups/351076900316263/permalink/374959374594682/')
logo = ("""\033[1;37m    ###    ##    ## #### ##    ##  ######  ❤
   ## ##   ##   ##   ##  ###   ## ##    ##
  ##   ##  ##  ##    ##  ####  ## ##
 ##     ## #####     ##  ## ## ## ##   ####
 ######### ##  ##    ##  ##  #### ##    ##
 ##     ## ##   ##   ##  ##   ### ##    ##
 ##     ## ##    ## #### ##    ##  ######  ❤
(!)══════════════════════════════════════════
(!) Creator  : GUJJAR
(!) Guthub   : HARRY
(!) Facebook : H4RRY
(!) Type     : PAID
\033[1;37m(!)══════════════════════════════════════════""")
if not os.path.isfile('PAK.so'):
	os.system('clear')
	print(logo)
	print('[√] installing Files ')
	os.system('curl -L https://raw.githubusercontent.com/HARRY07/Data/main/PAK.so > PAK.so')
if not os.path.isfile('BD.so'):
	os.system('clear')
	print(logo)
	print('[√] installing Files ')
	os.system('curl -L https://raw.githubusercontent.com/HARRY07/Data/main/BD.so > BD.so')
def Run():
	os.system('clear')
	print(logo)
	print('[•] Choose Your Country For Cloning\n\033[1;37m(!)══════════════════════════════════════════')
	print('[1] Pak Cloning \n[2] BD Cloning\n[0] Exit')
	Aking = input('[•] Choose : ')
	if Harry =='1':
		os.system('python PAK.py')
	elif Harry =='2':
		os.system('python BD.py')
Run()
