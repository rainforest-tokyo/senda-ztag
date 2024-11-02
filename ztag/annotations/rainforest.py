import json

from bs4 import BeautifulSoup
from ztag.annotation import *

from colorama import Fore, Style
from art import text2art, tprint

class RainForest(Annotation):

    protocol = protocols.HTTP
    subprotocol = protocols.HTTP.GET
    port = None

    def process(self, obj, meta):
        #print(json.dumps(obj, indent=2))

        if "certificate" in obj :
            if "parsed" in obj["certificate"] :
                print(Fore.RED + text2art("SSL KEY", font='bulbhead') + Style.RESET_ALL)
                
                print(Fore.RED + text2art("issuer", font='smooth1') + Style.RESET_ALL)
                print(Fore.GREEN + obj["certificate"]["parsed"]["issuer_dn"] + Style.RESET_ALL)
                print(Fore.RED + text2art("subject", font='smooth1') + Style.RESET_ALL)
                print(Fore.GREEN + obj["certificate"]["parsed"]["subject_dn"] + Style.RESET_ALL)

                print(Fore.RED + text2art("validity", font='smooth1') + Style.RESET_ALL)
                for key in obj["certificate"]["parsed"]["validity"] :
                    v = obj["certificate"]["parsed"]["validity"][key]
                    print(Fore.GREEN + "%s : %s"%(key,v) + Style.RESET_ALL)
                print(Fore.RED + text2art("signature", font='smooth1') + Style.RESET_ALL)
                for key in obj["signature"] :
                    v = obj["signature"][key]
                    print(Fore.GREEN + "%s : %s"%(key,v) + Style.RESET_ALL)

        if "server_host_key" in obj :
            print(Fore.RED + text2art("SSH KEY", font='bulbhead') + Style.RESET_ALL)
            print(Fore.RED + text2art("server host key", font='smooth1') + Style.RESET_ALL)
            for key in obj["server_host_key"] :
                v = obj["server_host_key"][key]
                print(Fore.GREEN + "%s : %s"%(key,v) + Style.RESET_ALL)
        if "banner" in obj :
            print(Fore.RED + text2art("BANNER", font='bulbhead') + Style.RESET_ALL)
            try :
                for key in obj["banner"] :
                    v = obj["banner"][key]
                    print(Fore.GREEN + "%s : %s"%(key,v) + Style.RESET_ALL)
            except :
                print(Fore.GREEN + obj["banner"] + Style.RESET_ALL)
        if "headers" in obj :
            print(Fore.RED + text2art("HTTP HEADER", font='bulbhead') + Style.RESET_ALL)
            print(Fore.RED + text2art("headers", font='smooth1') + Style.RESET_ALL)
            for key in obj["headers"] :
                v = obj["headers"][key]
                print(Fore.GREEN + "%s : %s"%(key,v) + Style.RESET_ALL)

            if "server" in obj["headers"] :
                server = obj["headers"]["server"]
                print(Fore.RED + text2art("server", font='smooth1') + Style.RESET_ALL)
                print(Fore.GREEN + server + Style.RESET_ALL)
            if "authorization" in obj["headers"] :
                authorization = obj["headers"]["authorization"]
                print(Fore.RED + text2art("server", font='smooth1') + Style.RESET_ALL)
                print(Fore.GREEN + authorization + Style.RESET_ALL)
        if "body" in obj :
            print(Fore.RED + text2art("HTTP BODY", font='bulbhead') + Style.RESET_ALL)
            print(Fore.RED + text2art("body", font='smooth1') + Style.RESET_ALL)
            print(Fore.GREEN + obj["body"] + Style.RESET_ALL)

            soup = BeautifulSoup(obj["body"], 'html.parser')
            try :
                title = soup.title.string
            except :
                title = ""
            print(Fore.RED + text2art("TITLE", font='smooth1') + Style.RESET_ALL)
            print(Fore.GREEN + title + Style.RESET_ALL)

            copywrite_texts = soup.find_all(string=lambda text: text and ('©' in text.lower() or 'copyright' in text.lower() or 'all rights reserved' in text.lower()))
            text_list = [element.get_text() for element in copywrite_texts]
            copywrite_texts = ' '.join(text_list)
            print(Fore.RED + text2art("COPYRIGHT", font='smooth1') + Style.RESET_ALL)
            print(Fore.GREEN + copywrite_texts + Style.RESET_ALL)

            # scriptタグのsrc属性を持つものを抽出
            script_src_list = [script['src'] for script in soup.find_all('script') if script.has_attr('src')]
            print(Fore.RED + text2art("SCRIPT SCR", font='smooth1') + Style.RESET_ALL)
            for src in script_src_list:
                print(Fore.GREEN + src + Style.RESET_ALL)

        return meta

