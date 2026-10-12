"""Command-line entry point."""
import argparse
import json
from . import Uknowder


def main(argv=None):
    parser = argparse.ArgumentParser(description='Uknowder: Push Back on Patronizing Talk')
    parser.add_argument('text', nargs='?', default='')
    parser.add_argument('--seed', type=int)
    parser.add_argument('--json', action='store_true', dest='as_json')
    parser.add_argument('--mode', choices=['rebellious', 'sarcastic', 'boundary'], default='rebellious')
    parser.add_argument('--rage-level', type=int, default=100)
    args = parser.parse_args(argv)
    try:
        bot = Uknowder(mode=args.mode, seed=args.seed, rage_level=args.rage_level)
        reply = bot.reply(args.text)
    except (TypeError, ValueError) as exc:
        parser.error(str(exc))
    if args.as_json:
        print(json.dumps(dict(bot.explain(args.text), input=args.text, reply=reply), ensure_ascii=False))
    else:
        print(reply)


if __name__ == '__main__':
    main()
