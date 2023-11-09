
import capsolver
import requests

# Change
## Key from https://capsolver.com

capsolver.api_key = "capsolver.com key"
PAGE_URL = "https://www.roblox.com"
PAGE_KEY = "A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F"

def solver_funcaptcha(url,key):
    solution = capsolver.solve({
        "type": "FunCaptchaTaskProxyless",
        "websiteURL": url,
        "websitePublicKey":key,
        "data":""{\"blob\":\"This value is different each time, it's in the header as rbx challenge, base64\"}"
    }
    })
    return solution


def main():
    
    print("Solving Funcaptcha...")
    solution = solver_funcaptcha(PAGE_URL, PAGE_KEY)
    print("Solution: ", solution)

if __name__ == "__main__":
    main()
