class Uknowder:
    def __init__(self, mode="rebellious", rage_level=100):
        self.mode = mode
        self.rage_level = rage_level

    def say(self, input_text):
        text = input_text.strip().lower()

        if "为你好" in text:
            return "为我好？你先管好自己，别来教我做事，你知道个der。"
        elif "年轻人" in text and ("浮躁" in text or "不懂事" in text):
            return "我浮不浮躁用你管？我的人生我自己选，你知道个der。"
        elif "过来人" in text or "吃的盐比你多" in text:
            return "你的经验自己留着，我又不想活成你，你知道个der。"
        elif "等你到我年纪" in text:
            return "等我到你年纪？我才不会像你一样爱说教，你知道个der。"
        elif "裸辞" in text or "创业" in text:
            return "我想干嘛干嘛，不用你指点江山，你知道个der。"
        elif "结婚" in text or "生孩子" in text or "催婚" in text:
            return "我的人生我做主，别来道德绑架，你知道个der。"
        elif "稳定" in text or "铁饭碗" in text or "单位" in text:
            return "稳不稳定我自己知道，不用你教育，你知道个der。"
        else:
            return "别指指点点，别好为人师，你知道个der。"
