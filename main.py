from is_telegram_bot import BotChecker

with open('telegram_data.csv', 'r', encoding='utf-8') as out:
    train_data = [[int(i) for i in item.split(',')] for item in out.read().split('\n')[1:]]

detector = BotChecker.detect(
    [item[:5] for item in train_data],
    [[item[5:][0] for item in train_data]]
)

detector.save_weights('test')

print(detector.is_bot([0,0,1,1,1]))