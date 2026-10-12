# Uknowder: Push Back on Patronizing Talk

[Overview](README.md) | [中文说明](README.zh-CN.md) | [English guide](README.en.md)

Respond to patronizing care, age-based dismissal, unsolicited life advice and controlling talk with rebellious, sarcastic or boundary-setting replies. Preserves the original humorous, stress-relieving persona. Python runs locally with keyword rules and templates: no API key, model download or network call.

## Install and use

Requires Python 3.9+. Install from this repository; a repository name does not imply a published PyPI package.

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

Example tone (random choices may differ):

> 为我好？先尊重我的选择，别替我决定。你知道个 der，别来教我做事。

## Modes and API

mode: rebellious / sarcastic / boundary; rage_level: 0–100. seed controls reproducible random selection. Invalid modes/strength raise ValueError; non-string inputs raise TypeError. Blank input falls back to general responses.

| Mode | Example tone (Chinese output) |
|---|---|
| rebellious | 别指指点点，别好为人师。 |
| sarcastic | 你说得都对，但我的人生没有远程控制接口。 |
| boundary | 我听到了你的观点，也请尊重我的边界。 |

The supported methods are say(text), batch(iterable) and explain(text). reply(text) aliases say(text), preserving both documented and existing callers. explain returns category, matched, mode, intensity and engine. batch returns a list of replies in input order.

## Scenario routing

Keywords are matched in the order below; the first matching category wins. Unmatched text uses general. English keywords are supported, while built-in output is Chinese.

| Category | Keywords |
|---|---|
| care | 为你好, 为你着想, for your own good |
| age | 年轻人, 浮躁, 不懂事, 等你到我年纪, young, age |
| experience | 过来人, 吃的盐, 走过的桥, experience |
| family | 结婚, 生孩子, 催婚, 催生, marriage |
| career | 稳定, 铁饭碗, 单位, 辞职, 裸辞, 创业, career, quit |
| comparison | 别人, 人家, 同龄, compare |
| control | 必须, 听我的, 照我说, 应该, obey |

## CLI and play

```sh
python -m uknowder "为你好" --seed 7
python -m uknowder "为你好" --seed 7 --json
```

Run --help for mode options. The installed command uknowder and python main.py use the same CLI.

Choose a scenario, compare modes, adjust strength where supported, then use a fixed seed to reproduce results. These are character lines, not factual assessments. At intensity 70 or above a mode-specific ending is appended; lower values use only the body. Intensity is a template setting, not a psychological score.

The three independent projects can form a comic exchange: diewei lectures, iknowder opts out, and uknowder pushes back or states a boundary. They do not call each other automatically.

## Agent skill

[SKILL.md](SKILL.md) defines persona, mode choice and contextual behavior. Put the folder containing SKILL.md and its guides in a skill directory supported by your client, or load it explicitly. Client-specific installation paths vary; this repository does not install itself into a personal assistant environment.

The Python implementation is a deterministic-seed template engine; an agent following SKILL.md can compose contextual wording. Neither includes a cloud-model integration.

## Development

```sh
python -m unittest -v test
python -m uknowder --help
```

Keywords/templates: uknowder/core.py. Engine: _engine.py. CLI: main.py. Add entries for every mode when adding categories, then update behavior tests. No third-party runtime dependencies; source builds use setuptools. The existing Uknowder API remains supported.

## License and intent

[MIT License](LICENSE). Intended for satire, roleplay and entertainment. Keep responses focused on statements/situations without invented private facts or threats. Leave the persona for serious requests and discuss facts and choices normally.
