import yaml,os,sys
class ReadYaml():
    def __init__(self,filename):
        self.filename=os.getcwd()+os.sep+"Data"+os.sep+filename
    def read_yml(self):
        with open(self.filename,"r",encoding="utf-8")as f:
            return yaml.load(f)
