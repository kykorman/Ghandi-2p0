import tweepy
import subprocess

scram_file = raw_input('Enter the file to use: ')

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def get_text():
    proc = subprocess.check_output(['./a.out', scram_file])
    return proc


def main():
    # Fill in the values noted in previous step here
    cfg = { 
        "consumer_key"        : "VALUE",
        "consumer_secret"     : "VALUE",
        "access_token"        : "VALUE",
        "access_token_secret" : "VALUE" 
    }

    #api = get_api(cfg)
    tweet = str(get_text())
    print tweet
    #status = api.update_status(status=tweet) 
    # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
    main()
    
