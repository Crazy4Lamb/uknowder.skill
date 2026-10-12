"""Local, dependency-free template engine for satirical responses."""
import random
import re


class TemplateEngine:
    def _configure(self, mode, modes, intensity, seed):
        if mode not in modes:
            raise ValueError("mode must be one of: " + ", ".join(modes))
        if isinstance(intensity, bool) or not isinstance(intensity, int) or not 0 <= intensity <= 100:
            raise ValueError("intensity must be an integer between 0 and 100")
        self.mode = mode
        self.intensity = intensity
        self._rng = random.Random(seed)

    def classify(self, text):
        if not isinstance(text, str):
            raise TypeError("input must be a string")
        normalized = text.strip().lower()
        for category, keywords in self.KEYWORDS:
            if any((re.search(r"(?<![a-z0-9])" + re.escape(word) + r"(?![a-z0-9])", normalized) is not None) if word.isascii() else word in normalized for word in keywords):
                return category
        return "general"

    def explain(self, text):
        category = self.classify(text)
        return {"category": category, "matched": category != "general", "mode": self.mode,
                "intensity": self.intensity, "engine": "local-templates"}

    def _respond(self, text):
        category = self.classify(text)
        line = self._rng.choice(self.LINES[self.mode][category])
        if self.intensity >= 70:
            line += self.SUFFIX[self.mode]
        return line

    def batch(self, texts):
        if isinstance(texts, str):
            raise TypeError("batch expects an iterable of strings, not one string")
        return [self._respond(text) for text in texts]
