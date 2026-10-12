import json
import subprocess
import sys
import unittest
from uknowder import Uknowder


class BehaviorTests(unittest.TestCase):
    def test_categories(self):
        bot = Uknowder()
        for category, keywords in bot.KEYWORDS:
            for keyword in keywords:
                self.assertEqual(bot.classify(keyword), category)
        self.assertEqual(bot.classify("完全未知话题 XYZ"), "general")

    def test_modes_and_seed(self):
        outputs = []
        for mode in ['rebellious', 'sarcastic', 'boundary']:
            kw = {"style": mode} if 'uknowder.skill' == "diewei.skill" else {"mode": mode}
            first, second = Uknowder(seed=7, **kw), Uknowder(seed=7, **kw)
            texts = ["为你好", "完全未知话题"] * 4
            self.assertEqual(first.batch(texts), second.batch(texts))
            outputs.append(Uknowder(seed=7, **kw).say("为你好"))
        self.assertEqual(len(set(outputs)), len(outputs))

    def test_input_and_configuration_errors(self):
        bot = Uknowder()
        for value in (None, 123, []):
            with self.assertRaises(TypeError):
                bot.say(value)
        self.assertTrue(bot.say("   "))
        with self.assertRaises(TypeError):
            bot.batch("not a list")
        kw = {"style": "unknown"} if 'uknowder.skill' == "diewei.skill" else {"mode": "unknown"}
        with self.assertRaises(ValueError):
            Uknowder(**kw)

    def test_cli_json(self):
        result = subprocess.run([sys.executable, "-m", "uknowder", "为你好", "--seed", "7", "--json"], capture_output=True, text=True, encoding="utf-8", check=True)
        data = json.loads(result.stdout)
        self.assertEqual(data["category"], 'care')
        self.assertTrue(data["reply"])
        self.assertEqual(data["engine"], "local-templates")

    def test_reply_alias_and_strength(self):
        self.assertEqual(Uknowder(seed=7).say("为你好"), Uknowder(seed=7).reply("为你好"))
        weak = Uknowder(rage_level=0, seed=7).reply("为你好")
        strong = Uknowder(rage_level=100, seed=7).reply("为你好")
        self.assertTrue(strong.startswith(weak))
        for value in (-1, 101, "100", True):
            with self.assertRaises(ValueError):
                Uknowder(rage_level=value)


if __name__ == "__main__":
    unittest.main()
