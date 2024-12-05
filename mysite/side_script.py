import sys
import pandas as pd
import time



def main(hhnbr, email):
    print(f"Processing HHNBR: {hhnbr}")
    print(f"Email: {email}")

    time.sleep(10)
    
    data = {
        "hhnbr": [hhnbr],
        "email": [email]
    }

    data = pd.DataFrame(data)
    data.to_csv("outputs/data.csv", index=False)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python side_script.py <hhnbr> <email>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])

    # get a random secret key
    # from django.core.management.utils import get_random_secret_key
    # print(get_random_secret_key())
