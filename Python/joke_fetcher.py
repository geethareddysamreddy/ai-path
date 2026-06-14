import requests
def get_joke():
    url="https://official-joke-api.appspot.com/random_joke"
    try:
        response=requests.get(url,timeout=5)
        response.raise_for_status()
        data=response.json()
        print("Setup:",data["setup"])
        print("Punchline:",data["punchline"])
    except requests.exceptions.ConnectionError:
        print("No Internet Connection")
    except requests.exceptions.Timeout:
        print("Request Time Out")
    except requests.exceptions.HTTPError as e:
        print(f"HTTPError:{e}")
def main():
    print("Random Joke Generator\n")
    while True:
        get_joke()
        again = input("\nAnother joke? (y/n): ").strip().lower()
        if again!="y":
            print("BYE!")
            break
main()



