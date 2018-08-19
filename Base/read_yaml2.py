import yaml,os,sys
sys.path.append(os.getcwd())

def read_yml():
    with open("../Data/test_sms.yml","r",encoding="utf-8")as f:
        return yaml.load(f)

if __name__ == '__main__':
    print(read_yml())