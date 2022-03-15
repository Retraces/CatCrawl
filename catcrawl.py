from icrawler.builtin import GoogleImageCrawler, BingImageCrawler, BaiduImageCrawler
from colorama import Fore
import time

print(Fore.GREEN + r"""
   _____      _    _____                    _ 
  / ____|    | |  / ____|                  | |
 | |     __ _| |_| |     _ __ __ ___      _| |
 | |    / _` | __| |    | '__/ _` \ \ /\ / | |
 | |___| (_| | |_| |____| | | (_| |\ V  V /| |
  \_____\__,_|\__|\_____|_|  \__,_| \_/\_/ |_|

     """)

print(Fore.GREEN + r"""
 ((      /|_/|
  \\.._.'  , ,\   Mᴇᴏᴡ
  /\ | '.__ v /
 (_ .   /   "
  ) _)._  _ /
 '.\ \|( / ( 
   '' ''\\ \\
      """)
# User inputs
googleinput = input(Fore.MAGENTA + 'Would you like to crawl Google? (1/0): ')
baiduinput = input(Fore.BLUE + 'Would you like to crawl Baidu? (1/0): ')
binginput = input(Fore.CYAN + 'Would you like to crawl Bing? (1/0): ')
image_amount = int(input(Fore.GREEN + 'How many images in do you want to crawl per engine?: '))
image_keyword = input(Fore.GREEN + 'What keyword would you like to use?: ')
folder = input(Fore.RED + 'What do you want your folder name to be? (This will be in the same folder as your .py file): ')


if googleinput == "1":  # Google check
  crawler = GoogleImageCrawler(storage={'root_dir': folder})
  crawler.crawl(keyword=image_keyword, max_num=int(image_amount))
  
if baiduinput == "1":  # Baidu check
  crawler = BaiduImageCrawler(storage={'root_dir': folder})
  crawler.crawl(keyword=image_keyword, max_num=int(image_amount))
  
if binginput == "1":  # Bing check
    crawler = BingImageCrawler(storage={'root_dir': folder})
    crawler.crawl(keyword=image_keyword, max_num=int(image_amount))

time.sleep(1)  # iCrawler sometimes lags behind, resulting in a late log message which isn't cool
print(Fore.GREEN + r"""
      
           /\
       )  ( ')  Tʜᴀɴᴋs ꜰᴏʀ ᴜsɪɴɢ CᴀᴛCʀᴀᴡʟ, ɢᴏᴏᴅʙʏᴇ﹗
      (  /  )
       \(__)|
      
      """)
time.sleep(2)
