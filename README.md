# ni-config

把json文件当作配置文件使用时，为了方便对配置文件进行操作而创建的配置文件类库

配置文件的内容为json格式。

规范化json内容的实现层面上，主要通过 [JSON Schema](https://json-schema.org/) 对配置文件的json结构进行定义并进行校验实现的。

## 安装

> pip install ni-config
> 
> pip install --upgrade ni-config

## 构建实例

```python
from ni.config import Config

c = Config(desc)
```

| desc | 说明 |
| --- | --- |
| str | 不含扩展名的文件名，一般为当前目录下、以”desc“为后缀的文件名，如：server.desc |
| dict | 包含“name”、“default”、“schema”定义的词典 |

## 关于默认值

可以通过*set_default*方法来初始化配置实例的默认值

```python
Config("server").set_default()
```

如若想检查目前的设定是否是默认值，可以使用*is_default*方法

```python
c = Config("server")

c.set_default()

c.is_default()

c.is_default('ip')
```

如果仅希望检查某个配置是否为默认值，把该配置项作为参数传递给*is_default*方法，默认不传递参数的情况下，将会对所有配置项进行检查。

若配置项下有多个*key*，可以通过传递一个*list*对象来校验具体配置是否为默认值。

```python
{
   'server': {
       'db': {
           'port': 6666
       }
   },
   'ip': '127.0.0.1'
}

c.is_default(['server', 'db', 'port'])
```

## validate

校验配置文件的内容是否与定义的一致。

```python
Config("server").validate()
```

## load_config

加载配置文件内容，并对内容进行校验，如果校验失败，则回退到原来的配置内容。

```python
Config("server").load_config("slaver.cfg")
```

## dump

把配置内容输出到指定文件

```python
Config("server").dump()

Config("server").dump("master.cfg")
```

## Get + Set

对Config对象中的配置进行修订、设置，或者获取相关配置项的信息；进行修改/设置时，会对变更后的配置内容进行有效性校验，如果校验失败，则回退到原来的配置内容。

```python
c = Config("server")

c["ip"] = "192.168.1.101"

print(c["ip"])

"192.168.1.101"
```

## 加密型Config：EncryptionConfig

为了更好的保护Config，不那么容易被篡改，在*Config*的基础上，构建*EncryptionConfig*。

为了创建一个*EncryptionConfig*对象，必须为其提供一个*Codec*；为此，你必须根据自己实际的需要，设计一个*Codec*的子类。

为了更好的展示其使用方式，我建立了一个*EasyCodec*，可以通过测试用例中参考其应用方式。

## 参数校验器：ParameterValidator

为了方便对参数进行校验处理，通过对封装，以便于日常代码中的参数校验使用。

```python
from ni.config import ParameterValidator

validator = ParameterValidator({'x': {"type": ["number", "string"]}})

validator.validates({'b': '231'})

validator.validates({'x': '231'})

validator.validate('x', 231)
```

> 版本v0.0.13开始，*ParameterValidator.validates*支持**strict**参数，当其为*True*时，被校验参数必须包含必须的默认参数，否则当作校验失败处理。为兼容之前版本，**strict**参数的默认值为*False*。