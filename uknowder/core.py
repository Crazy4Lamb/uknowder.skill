"""Satirical local response templates; no model or network calls."""
from ._engine import TemplateEngine


class Uknowder(TemplateEngine):
    KEYWORDS = [('care', ['为你好', '为你着想', 'for your own good']),
     ('age', ['年轻人', '浮躁', '不懂事', '等你到我年纪', 'young', 'age']),
     ('experience', ['过来人', '吃的盐', '走过的桥', 'experience']),
     ('family', ['结婚', '生孩子', '催婚', '催生', 'marriage']),
     ('career', ['稳定', '铁饭碗', '单位', '辞职', '裸辞', '创业', 'career', 'quit']),
     ('comparison', ['别人', '人家', '同龄', 'compare']),
     ('control', ['必须', '听我的', '照我说', '应该', 'obey'])]

    LINES = {'rebellious': {'care': ['为我好？先尊重我的选择，别替我决定。'],
                    'age': ['年纪大不代表永远正确，我的人生我自己选。'],
                    'experience': ['你的经验可以分享，不能拿来接管我的人生。'],
                    'family': ['结不结婚、生不生孩子，是我的决定。'],
                    'career': ['稳不稳定我自己评估，不用你替我安排。'],
                    'comparison': ['别人怎么活是别人的事，我不参加这场比较。'],
                    'control': ['建议我可以听，命令我不接受。'],
                    'general': ['别指指点点，别好为人师。']},
     'sarcastic': {'care': ['为我好这三个字，是不是自带免征求同意功能？'],
                   'age': ['原来年龄还能自动兑换正确答案？'],
                   'experience': ['经验分享欢迎，人生代驾就免了。'],
                   'family': ['谢谢关心，我的人生进度条暂不接受催更。'],
                   'career': ['你这么会规划，先把自己的路线跑明白。'],
                   'comparison': ['人生不是排行榜，别拿别人的账号给我打分。'],
                   'control': ['这份人生操作手册，我没有订阅。'],
                   'general': ['你说得都对，但我的人生没有远程控制接口。']},
     'boundary': {'care': ['我理解你想帮忙，但请先问我是否需要建议。'],
                  'age': ['我们可以讨论具体问题，请不要用年龄否定我的判断。'],
                  'experience': ['谢谢分享经验，最后的选择和责任由我承担。'],
                  'family': ['这是我的私人安排，我不继续讨论这个话题。'],
                  'career': ['我会评估风险，请尊重我对工作的决定。'],
                  'comparison': ['请不要把我和别人比较，我们可以谈具体事情。'],
                  'control': ['我愿意听建议，但不会接受替我做决定。'],
                  'general': ['我听到了你的观点，也请尊重我的边界。']}}

    SUFFIX = {'rebellious': '你知道个 der，别来教我做事。', 'sarcastic': '你知道个 der，指导到这里就够了。', 'boundary': '这个边界我会坚持。'}

    def __init__(self, mode="rebellious", rage_level=100, seed=None):
        self._configure(mode, ("rebellious", "sarcastic", "boundary"), rage_level, seed)
        self.rage_level = rage_level

    def say(self, input_text):
        return self._respond(input_text)

    def reply(self, input_text):
        return self.say(input_text)
