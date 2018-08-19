import yaml
data= {
	"collection": {
	"version": "1.0",
	"href": " http://service-root/FactoryModelService/factories",
	"links": [],
	"items": [
				{
					"href": "/1001",
					"data":
						[
							{
								"name": "factoryId",
								"value": "1001"
							},
							{
								"name": "code",
								"value": " facNO1"
							},
							{
							"name": "name",
							"value": "茂名1号催化炼化厂"
							},
							{
								"name": "shortName",
								"value": "1号催化炼化厂"
							},
							{
								"name": "businessType",
								"value": "业务类型1"
							},
							{
								"name": "enabled",
								"value": "1"
							},
							{
								"name": "creator",
								"value": "admin"
							},
							{
								"name": "createTime",
								"value": "2016-12-06 13: 00: 00"
							},
							{
								"name": "editor",
								"value": "admin"
							},
							{
								"name": "maintainTime",
								"value": "2016-12-06 13: 00: 05"
							},
							{
								 "name": "des",
								 "value": "一号炼油厂说明"
							}
						]
				}
			]
			}
}
def write_yaml():
    with open("../Data/test_write_yaml.yml","w",encoding="utf-8") as f:
        yaml.dump(data,stream=f,encoding="utf-8",allow_unicode=True)
if __name__ == '__main__':
    write_yaml()