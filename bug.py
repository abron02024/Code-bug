#love atena 
import os,random,sys,pyfiglet,time
r= "\033[31m"
g = "\033[32m"
y= "\033[36m"
u = "\033[35m"
i = "\033[93m"
o = "\033[34m"
lrd = '\033[01;32m'
cn = '\033[00;36m'
pe = '\033[01;35m'
b= "\033[94m"
w='\033[1;37m'
pk='\033[1;101m'

pl  = "\033[32m","\033[31m","\033[36m", "\033[35m", "\033[93m", "\033[34m"
pl1 = (random.choice(pl))
pl2 = (random.choice(pl))
pl3 = (random.choice(pl))
pl4 = (random.choice(pl))
pl5 = (random.choice(pl))
pl6 = (random.choice(pl))
#...
a=["""


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠴⠶⠒⠚⠋⠉⠉⠉⠉⠛⠒⠲⠶⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡤⠶⠶⠶⠶⠶⢶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⢉⠀⠀⠀⣀⣤⠶⡛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⣤⡀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⡀⠀⢀⣼⠟⠁⢻⣧⣄⣀⣀⠀⠀⠀⠀⠀⢀⢀⣀⣤⣄⣴⣦⠈⠙⣦⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⡇⠀⢸⠃⠀⠀⠘⠟⣿⣿⣿⢿⡟⠀⠀⠀⠸⠿⢿⣿⢟⡛⠛⠀⠀⠈⣧⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣧⠀⢸⡀⠀⠀⠀⠐⣿⣾⣿⠁⠀⠀⠀⠀⠀⠀⢿⣿⣾⡇⠀⠀⠀⠀⡿⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⣇⠈⢳⣄⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⣠⡾⠁⣰⠇⠀⠀⠀⠀⠀⢠⣴⢿⡝⠉⠻⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢦⡀⠙⠷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠶⠋⢀⡼⠋⠀⠀⠀⠀⣀⣾⠋⠻⣄⠹⣦⣴⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢤⣀⡉⠙⠲⠶⠦⠤⠤⠤⠤⠤⠴⠶⠖⠚⣉⣁⣤⠶⠋⠀⢰⣤⣤⣤⡾⠋⠙⣄⠀⢨⣷⠾⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠛⠒⠲⠤⠤⠤⠤⠤⠤⠤⠾⠒⠟⠻⣯⡀⠀⠀⠀⠘⣯⡝⢯⡛⠷⣤⣨⡷⠟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣄⣠⠞⠋⠻⣎⠳⣴⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⣄⢀⣴⠾⠷⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠙⢯⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣄⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠟⠀⠀⠀⠀⢀⣴⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣦⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠟⠀⠀⠀⠀⢀⡞⠁⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡈⢳⡀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⡏⠀⠀⠀⠀⢀⡞⠁⢸⠛⠒⠒⠲⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠒⠒⠚⣧⠀⢷⡄⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣼⠗⢦⣤⣀⢀⡼⠁⢀⡿⠒⠦⢤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣠⣤⣤⡤⠤⠖⢻⠀⠀⢷⡀⢀⣠⡴⠾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⠀⠀⠈⢹⣿⠴⢻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠈⡏⠉⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⢦⣀⣀⣠⡾⠁⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠹⣆⣀⣀⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣤⣶⣛⠉⠁⣀⣤⢾⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠛⠉⠁⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠻⡆⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⢧⣤⣄⣀⡀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⠀⠀⠀⣀⣀⣤⠴⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⠋⠀⠀⠀⠀⠈⠉⠉⠉⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠉⠉⠉⠁⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣆⣀⣀⣀⣀⣀⣀⣀⣀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""","""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⠿⠿⠿⠿⠿⠿⠿⠿⢷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⠀⣀⣠⣤⣶⣶⣶⣶⣶⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣏⠀⠀⣤⣴⣾⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠉⠛⠻⢿⣷⣶⣤⡄⠀⢸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣆⠀⠉⠉⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠈⠉⠁⢠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣼⣿⣧⡀⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⣰⣿⣿⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣾⠟⠛⠋⠉⠈⢻⣷⡄⠘⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠏⢀⣼⡿⠁⠉⠉⠛⠻⢿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⣀⣀⣀⣀⣀⣹⣿⣆⣈⣿⣷⣦⣄⣀⣀⣀⣀⣠⣤⣾⣿⣋⣠⣾⣟⣀⣀⣀⣀⣀⡀⠈⢿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠃⢰⣿⠟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡇⠈⢿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⠏⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠘⣿⣆⠀⠀⠀⠀
⠀⠀⠀⢠⣿⡟⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⠿⠿⣷⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠸⣿⣆⠀⠀⠀
⠀⠀⢀⣾⡟⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠉⠀⠀⠀⠀⠈⠻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠹⣿⡄⠀⠀
⠀⢀⣾⡟⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⣴⣄⠀⠀⣠⣤⡄⠸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠹⣿⡄⠀
⠀⣼⡟⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠈⠻⠇⠐⠿⠋⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠹⣷⡀
⢸⣿⠁⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣷⣦⡄⠀⠀⠀⣤⣶⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⣿⡧
⠈⠻⣷⣦⡀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣤⣤⣴⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢀⣠⣾⡿⠃
⠀⠀⠈⠙⢿⣷⣄⡀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣠⣴⡿⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠈⠻⢿⣾⣿⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⢀⣀⣀⣀⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀⠘⠛⠛⠛⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀
""","""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠶⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⠀⠸⠛⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⣿⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⣿⠀⢿⠀⣴⠟⠷⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⠀⠀⠀⢀⣤⡟⠀⢸⣿⠃⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⣸⡿⠿⠟⢿⡏⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣾⠟⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⣼⡇⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠛⡋⠉⣩⡇⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣰⠟⠋⠁⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⢠⡞⣱⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠟⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠃⢀⣿⢁⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⣠⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠁⠀⢸⣿⣿⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢀⣶⣾⡇⢸⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⢸⣿⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣏⣠⢰⢻⡟⢃⡿⡟⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠁⢿⠹⣿⣄⠀⠀⠀⢀⠀⠀⠀⠀⢺⠏⣿⣿⠼⠁⠈⠰⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡟⠃⠀⠈⢻⣷⣄⠈⠁⣿⣿⡇⠀⠀⠈⣧⠀⠀⠀⠘⣠⠟⠁⠀⠀⠀⠀⠀⢻⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠀⠀⣴⠀⠀⣿⡿⠀⠸⠋⢸⣿⣧⡐⣦⣸⡆⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡿⠃⠀⣀⣴⣿⡆⢀⣿⠃⠀⠀⠀⣸⠟⢹⣷⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣤⣾⡏⠛⠻⠿⣿⣿⣿⠁⣼⠇⠀⠀⠀⠀⠁⠀⢸⣿⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣇⠀⠀⠀⠀⠀
⠲⢾⣿⣿⣿⣿⣇⢀⣠⣴⣿⡿⢁⣼⣿⣀⠀⠀⠀⠀⠀⠀⠈⢿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀
⠀⠀⠉⠙⠛⠻⣿⣷⣶⣿⣷⠾⣿⣵⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⢤⡀⠀⠀⠀⠀⠀⠀⠀⡀⢿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⡟⣴⠀⠀⠉⠉⠁⢿⡇⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⣴⠀⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⢠⣿⠿⣿⣿⢠⠇⠀⠀⠀⢸⣿⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣀⠀⠀⢸⣿⡄⠀⠀⣼⣿⣇⢹⡟⢿⡇⠀⠀
⠀⠀⠀⠀⣿⠃⣠⣿⣿⣿⠀⠀⠀⠀⠀⢻⡈⢿⣆⠀⢳⡀⠀⢠⠀⠀⠀⠀⠀⢸⣿⣦⠀⣸⠿⣷⡀⠀⣿⣿⢿⣾⣿⠸⠇⠀⠀
⠀⠀⠀⠀⠋⣰⣿⣿⣿⣿⡀⢰⡀⠀⠀⠀⠀⠈⢻⣆⣼⣷⣄⠈⢷⡀⠀⠀⠀⢸⣿⢿⣶⠟⠀⠙⣷⣼⣿⣿⡄⠻⣿⣧⡀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣧⡿⠀⠀⠀⠀⠀⠀⠀⠙⢿⡄⠻⣷⣼⣿⣦⡀⠀⣼⠇⠸⠋⠀⠀⠀⠈⠻⣿⣿⣷⡀⠈⠻⣷⡀⠀
⠀⠀⠀⠀⠀⣿⣼⡿⢻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠈⠻⣷⡙⣿⣶⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⢠⣀⠘⣷⡀
⠀⠀⠀⠀⠀⠀⣿⠇⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⠛⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⢻⣷⣾⡇
⠀⠀⠀⠀⠀⠀⣿⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⢈⣿⡹⣷
⠀⠀⠀⠀⠀⠀⠈⠀⠻⠿⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⡇⠉

""","""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⣀⣴⡯⠖⣓⣶⣶⡶⠶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⢀⣴⣯⡾⣻⠽⡾⠽⠛⠚⠷⠯⠥⠤⠤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣢⣾⢿⣶⠿⣻⠿⠿⢋⣁⣠⠤⣶⢶⡆⠀⣀⣀⣀⣀⣀⣐⡻⢷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠟⠛⠉⠪⠟⣩⠖⠋⢀⡴⢚⣭⠾⠟⠋⡹⣾⠀⠀⢀⣠⠤⠤⠬⠉⠛⠿⣷⡽⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⣿⢝⣯⠆⣩⠖⢀⣤⢞⣁⣄⣴⣫⡴⠛⠁⠀⡀⣼⠀⣿⢠⡴⠚⠋⠉⠭⠿⣷⣦⡤⢬⣝⣲⣌⡙⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣷⣿⣿⣾⣿⣷⣿⣿⣿⣿⠋⠀⢀⢀⣶⣷⣿⠀⣿⠀⠀⠀⠀⠀⠀⠐⠚⠻⣿⣶⣮⣛⢯⡙⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣸⣿⠋⠀⡆⣾⣾⣿⣿⠿⢂⣿⣄⠀⠀⠀⠀⠀⠀⠐⠢⢤⣉⢳⣍⠲⣮⣳⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠿⣷⡀⢸⣿⣿⣿⠙⠏⠁⣸⣿⣿⣭⣉⡁⠀⠀⠀⠀⠀⠀⠘⣿⣿⡷⣌⣿⡟⢿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡿⡏⢡⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⣷⣼⣿⡟⠋⠀⠀⣴⣿⣿⣦⣍⣙⣓⡦⠄⠀⠈⠙⠲⢦⣻⣿⡅⠘⣾⣿⡄⠹⡳⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢹⠀⠀⠞⢭⣻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⠳⢼⣧⣄⣠⣾⣿⣿⣿⡻⢿⣭⡉⠁⠀⠀⠀⠀⠀⠀⠙⢿⢻⡄⠈⢻⣿⠀⠉⠹⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣻⡇⡆⠀⢀⣶⣾⣳⠏⠉⢹⡿⣿⣿⣟⡿⠿⢿⣿⣿⣿⣿⣧⠘⠒⠮⣿⣿⣿⣿⣿⣿⣿⣦⡬⠉⠀⠀⠀⢦⠀⠰⡀⠀⠈⠃⠓⠀⠈⣿⡀⠀⠀⢹⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣾⡧⣔⠾⡏⠙⠁⠀⣠⣿⢀⡎⠉⠈⠻⠭⠤⠤⣌⡻⣿⡿⡀⠈⠙⠻⠿⠿⣯⣅⠉⠉⣝⠛⢦⡘⣶⡀⠀⢣⠀⠙⢦⡀⠘⢇⣆⠀⣿⡇⠀⠀⠀⡇
⠀⠀⠀⠀⠀⣀⡠⠶⠿⠟⣃⣀⡀⠀⠀⠈⢓⣶⣾⣟⡡⠞⠀⠀⠀⠠⠴⠶⠿⠷⢿⡼⣿⣗⠀⠀⠀⠀⠀⠀⠈⠛⢆⠈⢧⡀⠁⠘⣿⡄⢢⠇⠀⠈⢧⠀⠸⣼⡄⣿⠇⠀⠀⢧⢸
⠀⣠⠴⠾⣿⡛⠛⠛⠁⠀⠀⠀⠙⠲⠈⠉⠀⠀⠀⠀⠤⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠷⣄⠘⣷⣄⡀⡄⠀⢀⡀⠀⢳⡄⠀⠀⠳⠀⡏⠀⠀⠸⡄⠀⢿⣧⣿⠀⠀⠀⡀⣼
⣾⣿⢶⣦⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣀⣤⣶⣶⣒⠢⢤⠀⠀⠈⠁⠉⠛⠿⣎⡛⢦⣀⠈⣿⣴⣾⣿⡞⡄⠀⠀⢹⡀⠀⠀⣿⠀⣾⣿⠇⠀⠀⠀⡇⢸
⠘⣿⣿⡾⡇⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡐⠲⢦⣦⢤⣤⣤⡶⠛⠉⠉⠀⠀⠀⠀⢀⣠⣤⣀⣤⠴⠂⠀⠀⠁⠀⢹⣧⣿⡿⢸⠇⢻⣿⣆⠀⠀⢷⣀⠀⣿⣷⠟⠉⠀⠀⠀⢸⡇⡄
⠀⠈⠳⢭⡗⠒⣛⣻⣽⠿⢿⣯⣷⣾⣿⣿⣿⣶⣬⡉⣉⠈⠑⠒⠉⠙⠻⠯⠉⣩⡟⢁⣾⠏⠀⣾⣷⣤⣄⣀⡀⢨⡿⣿⡇⣸⠀⠘⡿⢹⣆⠀⣸⣿⣷⡿⠁⠀⡀⠀⢸⡀⣾⣧⠀
⠀⠀⠀⠀⠈⠻⠿⣿⢿⡷⣌⣣⡉⠛⢿⣿⣿⣿⣿⣿⣧⡓⢄⠀⠀⠀⠀⠀⢰⡿⠷⣟⠿⠋⠀⢹⣿⡇⠀⠁⠙⣾⢧⠙⠙⠁⠀⠐⠁⠘⠹⣄⣿⠃⠹⣿⡀⠀⡇⠀⡿⣇⡿⢹⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠓⠻⠊⠙⠃⠀⠀⠹⣿⣿⡿⡏⠀⣿⣌⠳⡄⠀⢀⡴⠋⠈⠉⠉⡙⠲⣤⢸⡟⣿⠀⠀⠠⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠿⠃⠀⠀⠈⠃⣸⡇⣼⠇⣿⡇⢸⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⢳⣿⣿⣿⡆⢳⠀⡎⠀⠀⠀⠀⢀⣉⠳⣬⣿⠇⠃⠀⠀⢠⠆⢰⢊⡇⠀⠀⠀⠀⠀⠀⢲⠀⢰⡆⠀⠀⣽⣿⡟⠀⢸⡇⡞⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢸⡇⠈⣿⢟⣼⣇⡏⠀⠀⠔⣺⡭⠽⣿⡛⠛⠿⡏⠀⣆⠀⠀⣼⠀⣼⣼⣷⡆⠀⠀⣶⡆⢠⡿⣠⣿⡇⠀⢰⣿⠏⣴⢂⠋⡼⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⢻⢿⡁⣼⢣⣿⡿⠀⢀⢀⡴⠋⠀⠀⠀⠀⠙⣶⣦⡅⠀⣿⡄⢠⣿⣾⢿⠿⣿⡇⠀⠘⣾⣇⣼⣷⠟⡼⠀⣰⡿⠋⢠⠏⢦⣾⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡟⢾⢄⣹⣧⡿⡽⠁⠀⣿⠋⠀⠀⠀⠀⠀⠀⠀⠟⠉⣧⡾⡽⣠⣿⢛⠇⠏⠰⣻⠃⣼⣽⣿⡿⡿⠁⣴⣡⡾⠋⠀⢠⣞⣴⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣼⣿⣿⡟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠋⠰⠟⣻⣿⢋⠀⠀⣴⣷⣾⠟⡿⠋⠀⣥⠾⠛⡋⠀⠀⢠⣾⣿⠟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠽⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢁⡌⠀⢰⣿⠟⠁⠀⠀⠀⠀⡀⠀⣰⠃⠀⣴⡿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⢀⣴⠏⠀⠀⢸⡋⠀⡀⠀⣀⠖⠋⣠⣾⢃⣠⡾⠟⢡⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⣀⣴⡿⠃⠀⠀⠀⠀⢁⡾⠁⢈⣁⣴⣾⣿⣿⠟⠉⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣾⣿⡿⠁⠀⢀⣀⣤⣼⢟⣡⣶⠿⠟⠋⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣟⣿⣿⣃⣴⣶⣿⠿⣿⣿⡿⠋⠀⠀⠀⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣾⣿⣿⣿⠛⠉⠀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠟⠁⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""","""


⠀⠀⠀⠀⣠⣶⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣶⣄⠀⠀⠀⠀
⠀⠀⠀⢰⣿⠋⠀⠀⠉⢻⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠋⠀⠀⠉⣿⣆⣀⠀⠀
⢀⣶⣿⠿⠿⠀⠀⠀⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠛⠻⢿⣷⡄
⢸⣿⠁⠀⠀⠀⠀⠀⠀⢻⣿⣆⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣶⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠀⠀⠀⠀⠀⠀⠀⣿⣷
⠘⣿⣧⡀⠀⢀⣀⠀⠀⠀⠙⢿⣷⣄⠀⢀⣴⣾⣿⣿⠿⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠿⣿⣿⣷⣦⣀⠀⣰⣿⠟⠁⠀⠀⠀⣠⣀⠀⠀⣠⣿⠇
⠀⠈⠻⠿⠿⠿⢿⣷⣄⠀⠀⠀⠙⣿⣿⣿⡿⠟⠋⠀⠀⣀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣦⣤⣀⠀⠀⠉⠻⢿⣿⣿⣿⠋⠀⠀⠀⣠⣾⡿⠿⢿⣿⠿⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⣠⣾⣿⡿⠋⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠙⠿⣿⣷⣄⣠⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡿⠋⠀⢀⣴⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠿⣿⣿⣿⣿⣿⣦⡀⠀⠘⢿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠟⠀⠀⣴⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣦⡀⠀⠙⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠋⠀⢠⣾⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣄⠀⠘⢿⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣾⣿⣿⠃⠀⢠⣿⣿⣿⣿⣿⣁⣀⣀⣤⣤⣤⣤⣤⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⢶⣤⣤⣤⣤⣤⣌⣿⣿⣿⣿⣿⣆⠀⠈⢿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⠃⠀⢠⣿⣿⣿⣿⡿⠛⠉⠉⠉⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠉⠉⢻⣿⣿⣿⣿⣆⠀⠈⣿⣿⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⡏⠀⢠⣿⣿⣿⣿⡿⠷⠶⠞⠛⠛⠛⠋⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠙⠛⠛⠛⠺⠿⠿⣿⣿⣿⣆⡀⠘⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⡶⠾⠛⠋⠉⠁⠀⢀⣠⣤⣶⡶⠶⠾⠛⠛⠛⠛⠛⠋⠉⠉⠉⠉⠉⠉⠙⠛⠛⠛⠛⠛⠛⠻⠿⠷⠶⢶⣤⠀⠀⠀⠈⠉⠛⠻⠿⣿⣇⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣥⣤⣤⣀⣀⣀⣀⣰⣿⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣀⣤⣤⣤⡤⠴⢶⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⡄⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣷⠀⠀⣿⣿⣿⣿⣿⣿⣧⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣸⣿⣿⣿⣿⣿⣿⠇⠀⢸⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⠀⠀⢿⣿⣿⣿⣿⣿⣿⣇⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢠⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣿⣿⡇⠀⠘⣿⣿⣿⣿⣿⣿⣿⣦⠀⠙⢿⣿⣿⣿⣿⡿⠟⠁⠀⣀⣀⡀⠀⠙⠿⣿⣿⣿⣿⡿⠟⠁⣰⣿⣿⣿⣿⣿⣿⣿⡏⠀⢠⣿⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣿⣿⡀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠉⠉⠁⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠈⠉⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⣾⣿⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣷⡀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠈⠻⠿⠋⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⣼⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⡀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣄⣀⣀⣀⣀⣠⣤⣤⡶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⣼⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣄⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⣸⡏⠉⢹⡟⠛⢻⡋⠉⣿⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⢠⣾⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣷⣄⠀⠈⠻⢿⣿⣿⣿⣿⣿⡇⠈⣿⠛⠓⣿⠷⠶⢾⡗⠛⢻⡏⠀⣿⣿⣿⣿⣿⣿⠟⠉⠀⢀⣴⣿⣿⠿⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⣠⣶⣿⣿⣶⣶⣿⠟⠁⠈⠻⣿⣿⣷⣄⠀⠀⠙⠻⢿⣿⣿⡷⢴⣯⣀⣀⣿⠀⠀⢸⣇⣀⣠⣷⡶⣿⣿⣿⠟⠋⠁⠀⣠⣴⣿⣿⡟⠁⠀⠈⠻⣿⣶⡿⢿⣶⣄⠀
⢰⣿⠋⠁⠀⠈⠙⠁⠀⠀⢀⣴⣿⠟⢿⣿⣿⣶⣄⡀⠀⠈⠙⢿⡀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⢰⡟⠉⠀⠀⣠⣴⣾⣿⡿⠟⠻⣿⣦⡀⠀⠀⠈⠁⠀⠀⠙⣿⡆
⢸⣿⡀⠀⠀⠀⠀⠀⠀⢴⣿⠟⠁⠀⠀⠈⠛⢿⣿⣿⣷⣶⣤⣀⣻⣦⣄⡀⠀⠀⠀⠀⠀⢀⣠⣴⣏⣠⣴⣶⣿⣿⡿⠟⠉⠀⠀⠀⠈⣻⣿⠆⠀⠀⠀⠀⠀⠀⣿⡇
⠈⠿⣷⣦⣴⡆⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀⣶⣶⣾⠿⠁
⠀⠀⠀⠉⣿⣇⡀⠀⣀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣷⣄⠀⠀⣠⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠟⠋⠀⠀⠀⠀
""","""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⠶⠶⠶⠶⠶⠶⠶⢖⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠞⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠻⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠈⠹⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⢀⣤⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⣦⣀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⣠⡾⢁⣾⡿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠏⠋⠉⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣆⠹⣦⠀⠀⢻⣆⠀⠀⠀⠀
⠀⠀⢀⡾⠁⢀⢰⣿⠃⠾⢋⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡌⠻⠆⢿⣧⢀⠀⢻⣆⠀⠀⠀
⠀⠀⣾⠁⢠⡆⢸⡟⣠⣶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣷⣻⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣦⡸⣿⠀⣆⠀⢿⡄⠀⠀
⠀⢸⡇⠀⣽⡇⢸⣿⠟⢡⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠙⢿⣿⠀⣿⡀⠘⣿⠀⠀
⡀⣿⠁⠀⣿⡇⠘⣡⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣦⡙⠀⣿⡇⠀⢻⡇⠀
⢸⡟⠀⡄⢻⣧⣾⡿⢋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣴⣿⠉⡄⢸⣿⠀
⢾⡇⢰⣧⠸⣿⡏⢠⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠀⠓⢶⠶⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠙⣿⡟⢰⡧⠀⣿⠀
⣸⡇⠰⣿⡆⠹⣠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣿⡏⠀⠠⢺⠢⠀⠀⣿⣷⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣧⠸⠁⣾⡇⠀⣿⠀
⣿⡇⠀⢻⣷⠀⣿⡿⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡅⠀⠀⢸⡄⠀⠀⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡆⣰⣿⠁⠀⣿⠀
⢸⣧⠀⡈⢿⣷⣿⠃⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣇⠀⢀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⢿⣧⣿⠃⡀⢸⣿⠀
⠀⣿⡀⢷⣄⠹⣿⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿⡯⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢸⡟⢁⣴⠇⣼⡇⠀
⠀⢸⡇⠘⣿⣷⡈⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣿⣿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢰⣿⡧⠈⣴⣿⠏⢠⣿⠀⠀
⠀⠀⢿⡄⠘⢿⣿⣦⣿⣯⠘⣆⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⡎⢸⣿⣣⣾⡿⠏⠀⣾⠇⠀⠀
⠀⠀⠈⢷⡀⢦⣌⠛⠿⣿⡀⢿⣆⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢀⣿⡁⣼⡿⠟⣉⣴⠂⣼⠏⠀⠀⠀
⠀⠀⠀⠈⢷⡈⠻⣿⣶⣤⡁⠸⣿⣆⠡⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⣾⡟⠀⣡⣴⣾⡿⠁⣴⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣄⠈⢙⠿⢿⣷⣼⣿⣦⠹⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢡⣾⣿⣶⣿⠿⢛⠉⢀⣾⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣧⡀⠳⣦⣌⣉⣙⠛⠃⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠐⠛⠋⣉⣉⣤⡶⠁⣰⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⡀⠙⠛⠿⠿⠿⠿⠟⠛⠛⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠙⠟⠛⠿⠿⠿⠿⠟⠛⠁⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢶⣄⠙⠶⣦⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⡶⠖⣁⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣶⣄⡉⠉⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠉⠉⠉⠉⣡⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⢦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣠⣴⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""]

po =(f"FILTRING \n ABRON ")
user = (f"{po}")
fonts = ["slant", "3-d", "letters", "banner3-D"]
font = random.choice(fonts)
text = pyfiglet.figlet_format(f"{po}", font=font)


print(pl1+pl2+pl3+pl4+pl5+pl6)
time.sleep(0.0002)
def slow_print(Str):
    for char in Str:
        print(char, end='', flush=True)
        time.sleep(0.0002)
def clear():
    system('clear' if name == 'posix' else 'cls')
slow_print(text)
print(pl1+pl3+pl6+pl2+pl4+pl5)
banner = (random.choice(a))

#
#
for i in banner:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.007)
print ("""\033[31m
  ________________________________________________                
 |>>>-----------------------------------------<<<|
 |>>>--------\033[32mCREATOR MR ARYAN ABRON?\033[31m----------<<<|
 \033[36m|>>>—————————————————————————————————————————<<<|
 |>>>			    	              <<<|
 |>>>         \033[31m[\033[32mID TELEGRAM\033[31m] \033[33m@Lockear  \033[36m        <<<|
 |>>>     \033[31m[\033[32mCHANEL\033[31m] \033[33mt.me/Program_writing\033[36m       <<<|
 |>>>—————————————————————————————————————————<<<|
 |>>>                                         <<<|
 |>>>    \033[31m[\033[32m1\033[31m] \033[33m Rubika Account code\033[36m             <<<|
 |>>>    \033[31m[\033[32m2\033[31m] \033[33m Rubika Channel code\033[36m             <<<|
 |>>>    \033[31m[\033[32m3\033[31m] \033[33m Rubika Group code\033[36m               <<<|
 |>>>    \033[31m[\033[32m4\033[31m] \033[33m Shad Account code\033[36m               <<<|
 |>>>    \033[31m[\033[32m5\033[31m] \033[33m Shad Channel code\033[36m               <<<|
 |>>>    \033[31m[\033[32m6\033[31m] \033[33m Shad Group code\033[36m                 <<<|
 |>>>                                         <<<|
 |>>>—————————————————————————————————————————<<<|
\033[31m |>>>-----------------------------------------<<<|
 |>>>-----------------------------------------<<<|  
 —————————————————————————————————————————————————""")
mr_abron= input(f"   \033[35m[\033[32m<\033[31m$\033[32m>\033[35m]\033[33m-_-_-_-_-_\033[32m[\033[31mMR ABRON\033[32m]\033[33m-_-_-_-_\033[31m❯❯❯\033[32m❯❯❯{r}")

print ()
print ()
print (f"\033[33m")
print("\r[~] alert > 5s",end="",flush=False) 
time.sleep(1)
print("\r[~] alert >> 4s",end="",flush=False)
time.sleep(1) 
print("\r[~] alert >>> 3s",end="",flush=False) 
time.sleep(1)
print("\r[~] alert >>>> 2s",end="",flush=False) 
time.sleep(1)
print("\r[~] alert >>>>> 1s",end="",flush=False)
time.sleep(0.5)
print ()
print ()
os.system("clear")
time.sleep(1)
print ()

#
# moteghayers random code __
#
md = (random.randint(1, 9))
maryan = (random.randint(1, 9))
maryan1 = (random.randint(1, 9))
maryan3 = (random.randint(1, 9))
maryan4 = (random.randint(1, 9))
maryan5 = (random.randint(1, 9))
maryan6 = (random.randint(1, 9))
maryan7 = (random.randint(1, 9))
maryan8 = (random.randint(1, 9))
maryan9 = (random.randint(1, 9))
maryan9 = (random.randint(1, 9))
maryan10 = (random.randint(1, 9))
maryan11 = (random.randint(1, 9))
maryan12 = (random.randint(1, 9))
maryan13 = (random.randint(1, 9))
maryan14 = (random.randint(1, 9))
maryan15 = (random.randint(1, 9))
maryan16 = (random.randint(1, 9))
maryan17 = (random.randint(1, 9))
maryan18 = (random.randint(1, 9))
maryan19 = (random.randint(1, 9))
maryan20 = (random.randint(1, 9))
maryan21 = (random.randint(1, 9))
maryan22 = (random.randint(1, 9))
maryan23 = (random.randint(1, 9))
maryan24 = (random.randint(1, 9))

aryan1 = str(maryan)
aryan2 = str(md)
aryan3 = str(maryan3)
aryan4 = str(maryan4)
aryan5 = str(maryan5)
aryan6 = str(maryan6)
aryan7 = str(maryan7)
aryan8 = str(maryan8)
aryan9 = str(maryan9)
aryan10 = str(maryan10)
aryan11 = str(maryan11)
aryan12 = str(maryan12)
aryan13 = str(maryan13)
aryan14 = str(maryan14)
aryan15 = str(maryan15)
aryan16 = str(maryan16) 
aryan17 = str(maryan17)
aryan18 = str(maryan18)
aryan19 = str(maryan19)
aryan20 = str(maryan20)
aryan21 = str(maryan21)
aryan22 = str(maryan22)
aryan23 = str(maryan23)
aryan24 = str(maryan24)

h = ["/y//d/f/","/f//d/","/d//f/h/","/f//a/y/","/e////f.h/","/f/h.u//"]
h2 = ["/f//h//g.h/","/g//d/","/f/h.g//","/r//g/h"]
h3 = ("h")
hh = (random.choice(h))
hh2 = (random.choice(h2))
hh3 = (random.choice(h3))

shad = ["/FIL//T/G/","/FK//B/","/D//CH/V/","/F/I/L/SH/","/S//M//A.R.N/","/M/T.X//"]
shad2 = ["/C//S//S.X/","/GIF//SX/","/F/J.K//","/S//E/X"]
shad3 = ("HACK")

sha = (random.choice(shad))
sha2 = (random.choice(shad2))
sha3 = (random.choice(shad3))


sor = ["/FIL//T/G/","/SX//X/","/COS//W/V/","/F/I/L/SO/","/G//F//A.R.N/","/M/T.X//"]
sor1 = ["/C//O//D.X/","/GIF//SG/","/J/H.K//","/U//S/X","X/COD//ER/","yt/tr//k"]
sor2 = ("HACK","FILTRING","YTTRK","COD/SEX")

soro = (random.choice(sor))
soro1 = (random.choice(sor1))
soro2 = (random.choice(sor2))

fil = ["fl-shad","filtring(shad)"]
fil1 = (random.choice(fil))


pl = ["f","¥","€","$","£","¢","&"]
po = ["f","¥","€","$","£","¢","&"]
pi = ["f","¥","€","$","£","¢","&"]
pu = ["f","¥","€","$","£","¢","&","ß","ę","€","$","£","¢","&","₹","₱","†"]
pe = ["ß","ę","€","$","£","¢","&","₹","₱","†"]

pl1 = (random.choice(pl))
pl2 = (random.choice(pl))
pl3 = (random.choice(pl))
pl4 = (random.choice(pl))

pl5 = (random.choice(pi))
pl6 = (random.choice(po))
pl7 = (random.choice(pe))
pl8 = (random.choice(pu))

ary = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

aryn =['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

ate =["0","9","8","7","6","5","4","3","2","1"]

ary1 = (random.choice(ary))
ary2 = (random.choice(ary))
ary3 = (random.choice(ary))

ate1 = (random.choice(ate))
ate2 = (random.choice(ate))
ate3 = (random.choice(ate))

aryn1 = (random.choice(aryn))
aryn2 = (random.choice(aryn))
aryn3 = (random.choice(aryn))


arynm = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

aryan =['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

atena =["0","9","8","7","6","5","4","3","2","1"]

arn=["Gif_sex","gif-sxs-yttf8k","Gif_sex","yttf18k","sex-film","yttf","Filtring"]

LOVEatei=["/","!","*","#",":","+","-","=","$","×"]

LOVEatei1 = (random.choice(LOVEatei))
LOVEatei2 = (random.choice(LOVEatei))
LOVEatei3 = (random.choice(LOVEatei))

arn1 = (random.choice(arn))
arn2 = (random.choice(arn))
arn3 = (random.choice(arn))

aryan1 = (random.choice(aryan))
aryan2 = (random.choice(aryan))
aryan3 = (random.choice(aryan))

atena1 = (random.choice(atena))
atena2 = (random.choice(atena))
atena3 = (random.choice(atena))

arynm1 = (random.choice(arynm))
arynm2 = (random.choice(arynm))
arynm3 = (random.choice(arynm))

bug1 = (f"\033[36m({ary1}{LOVEatei2}{ate1}f{ary2}{ate2}{LOVEatei3}{ate3}{ary2}{aryn1}{LOVEatei2}{ary3}*)")
bug2 = (f"\033[31m({ary1}{LOVEatei3}{ate1}f{ary2}{ate2}{LOVEatei1}{ate3}{ary2}{aryn1}{LOVEatei2}{ary3}/)")
bug3 = (f"\033[32m({ary1}{LOVEatei1}{ate1}f{ary2}{ate2}{LOVEatei3}{ate3}{ary2}{aryn1}{LOVEatei3}{ary3}×)")


cod1=(f'\033[36mhttps://{arn1}{aryan1}/{atena1},{arynm1}{aryan1}')
cod2=(f'\033[31mhttps://{arn2}{aryan2}/{atena2},{arynm2}{aryan2}')
cod3=(f'\033[32mhttps://{arn3}{aryan3}/{atena3},{arynm3}{aryan3}')

xc =(f"\033[31m((/{aryan1}.{aryan2}.{aryan3}.{aryan4}{hh2}{aryan5}.{aryan6}.{aryan7}.{aryan8}.{aryan9}.{aryan10}.{aryan11}.{aryan12}.{aryan13}.{aryan14}.{aryan15}.{aryan16}.{aryan17}.{aryan18}.{aryan19}.{aryan20}.{aryan21}.{aryan22}.{aryan23}.{aryan24}/#))") 

xc1=(f"\033[32m((/{aryan1}.{aryan2}.{aryan3}.{aryan4}{hh}{aryan5}.{aryan6}.{aryan7}.{aryan8}.{aryan9}.{aryan10}.{aryan11}.{aryan12}.{aryan13}.{aryan14}.{aryan15}.{aryan16}.{aryan17}.{aryan18}.{aryan19}.{aryan20}/+))")

xc2=(f"\033[33m((/{aryan1}.{aryan2}.{aryan3}.{aryan4}{soro2}{aryan5}.{aryan6}.{aryan7}.{aryan8}.{aryan9}.{aryan10}.{aryan11}.{aryan12}.{aryan13}.{aryan14}.{aryan15}.{aryan16}.{aryan17}.{aryan18}.{aryan19}.{aryan20}.{aryan21}.{aryan22}.{aryan23}.{aryan24}/#))")

vir=(f"\033[31m(/https://bit.ly/{ary1}{ate1}f{ary2}{ate2}{ate3}{ary2}{aryn1}k{ary3}*)")

vir1=(f"\033[35m(/https://bit.ly/{ary1}{ate3}f{ary2}{ate1}{ate2}{ary3}{aryn1}k{ary2}*)")

vir2=(f"\033[33m(/https://bit.ly/{ary1}{ate1}f{ary3}{ate2}{ate3}{ary3}{aryn2}k{ary1}*)")


oh = (f"\033[34moh 'AHM' if your account is not spam and you to hit the code correctly, it will filter 65% !")

port = (f"{b}no report")

ping  = (f" '\033[31m(127.0.0.1:8080)'")

y = (f"{b}tap (1) order code")

z = (f"{b}tap (2) order")


#if s
#
if mr_abron == "1":
         slow_print(f"""{xc}\n \n{xc1}\n \n{xc2}\n \n{cod1}\n \n{cod2}\n \n{cod3}\n \n{vir}\n \n{vir1}\n \n{vir2}\n \n {bug1}\n \n{bug2}\n \n{bug3} \n \n""")
         print("https://t.me/Program_writing")
#
if mr_abron == "2":
         slow_print(f"""{xc}\n \n{xc1}\n \n{xc2}\n \n{cod1}\n \n{cod2}\n \n{cod3}\n \n{vir}\n \n{vir1}\n \n{vir2}\n \n {bug1}\n \n{bug2}\n \n{bug3} \n \n""")
         print("https://t.me/Program_writing")
#
if mr_abron == "3":
         slow_print(f"""{xc}\n \n{xc1}\n \n{xc2}\n \n{cod1}\n \n{cod2}\n \n{cod3}\n \n{vir}\n \n{vir1}\n \n{vir2}\n \n{bug1}\n \n{bug2}\n \n{bug3} \n  \n""")
         print("https://t.me/Program_writing")
#
if mr_abron == "4":
         slow_print(f"""{xc}\n \n{xc1}\n \n{xc2}\n \n{cod1}\n \n{cod2}\n \n{cod3}\n \n{vir}\n \n{vir1}\n \n{vir2}\n \n {bug1}\n \n{bug2}\n \n{bug3} \n \n""")
         print("https://t.me/Program_writing")
#
if mr_abron == "5":
         slow_print(f"""{xc}\n \n{xc1}\n \n{xc2}\n \n{cod1}\n \n{cod2}\n \n{cod3}\n \n{vir}\n \n{vir1}\n \n{vir2}\n \n {bug1}\n \n{bug2}\n \n{bug3} \n \n""")
         print("https://t.me/Program_writing")
#
if mr_abron == "6":
         slow_print(f"""{xc}\n \n{xc1}\n \n{xc2}\n \n{cod1}\n \n{cod2}\n \n{cod3}\n \n{vir}\n \n{vir1}\n \n{vir2}\n \n{bug1}\n \n{bug2}\n \n{bug3} \n  \n""")
         print("https://t.me/Program_writing")
#
#mi mr Abron 
#id @Lockear
