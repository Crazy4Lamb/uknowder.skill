# 你知道个der.skill

[首页](README.md) | [中文说明](README.zh-CN.md) | [English guide](README.en.md)

对“我都是为你好”、年龄压制、经验说教与强行安排生成反击；从叛逆吐槽到清晰边界表达。 保留原项目的整活、解压与反说教趣味。Python 使用本地规则，不需要 API Key、网络请求或模型下载。

## 快速开始

需要 Python 3.9+。从源码安装（仓库名不代表已发布到 PyPI）：

```sh
git clone https://github.com/Crazy4Lamb/uknowder.skill.git
cd uknowder.skill
python -m pip install .
```

```python
from uknowder import Uknowder

bot = Uknowder(mode='rebellious', seed=7, rage_level=100)
print(bot.reply("为你好"))
print(bot.explain("为你好"))
print(bot.batch(["为你好", "随便聊聊"]))
```

示例口吻（随机回复不保证逐字相同）：

> 为我好？先尊重我的选择，别替我决定。你知道个 der，别来教我做事。

## 模式与参数

mode: rebellious / sarcastic / boundary；rage_level: 0–100。seed 用于复现随机选择。未知模式或非法强度会抛出 ValueError，非字符串输入会抛出 TypeError，空字符串使用通用文案。

| 模式 | 通用口吻示例 |
|---|---|
| rebellious | 别指指点点，别好为人师。 |
| sarcastic | 你说得都对，但我的人生没有远程控制接口。 |
| boundary | 我听到了你的观点，也请尊重我的边界。 |

## 场景识别

输入先按下表顺序匹配关键词；多个场景命中时使用第一类，否则使用 general。中英文关键词都能触发，但内置回复默认中文。explain 返回 category、matched、mode、intensity、engine，便于调试。

| 分类 | 关键词 |
|---|---|
| care | 为你好, 为你着想, for your own good |
| age | 年轻人, 浮躁, 不懂事, 等你到我年纪, young, age |
| experience | 过来人, 吃的盐, 走过的桥, experience |
| family | 结婚, 生孩子, 催婚, 催生, marriage |
| career | 稳定, 铁饭碗, 单位, 辞职, 裸辞, 创业, career, quit |
| comparison | 别人, 人家, 同龄, compare |
| control | 必须, 听我的, 照我说, 应该, obey |

## 命令行与玩法

```sh
python -m uknowder "为你好" --seed 7
python -m uknowder "为你好" --seed 7 --json
```

用 --help 查看风格参数。也可用安装后的命令 uknowder，或 python main.py。

玩法：选择一个场景 → 切换模式 → 比较同一句话的不同口吻 → 调整强度（如支持）→ 固定 seed 复现输出。将输出当作角色文案或模拟练习，而非事实判断。

三个项目可组成一个娱乐对话：diewei 发出说教，iknowder 佛系退出，uknowder 表达反击或边界。各仓库独立安装，不会自动互相调用。

## 作为智能体 Skill

仓库根目录的 [SKILL.md](SKILL.md) 提供角色定位、模式选择和行为说明。将包含 SKILL.md 及说明文档的文件夹放入你的智能体支持的 skills 目录，或显式加载该文件。具体安装位置取决于客户端；这里不会自动安装到你的个人环境。

Python 是可复现的模板引擎；智能体则根据技能说明结合上下文生成文案。两者都不内置云端大模型调用。

## 开发与验证

```sh
python -m unittest -v test
python -m uknowder --help
```

模板、关键词在 uknowder/core.py；引擎在 _engine.py；命令行在 main.py。增加场景时同步补齐所有模式文案并更新测试。零运行时第三方依赖；源码安装需要 setuptools 构建工具。

保持原有 Uknowder 接口可用。Uknowder 同时支持 say 和 reply。强度 >=70 时增加模式结尾，低于该值仅输出主体，不声称进行心理学或语义模型评分。

## 许可与用途

[MIT License](LICENSE)。这是讽刺、角色扮演和娱乐文案项目。表达对象是话术与情境，不编造真实个人信息，不生成威胁。认真求助时请退出角色，正常讨论事实与选择。
