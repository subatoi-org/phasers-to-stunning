from phaser import Api
from timerit import Timerit
import simplejson as json

if __name__ == "__main__":
    phaser = Api()

    t1 = Timerit(num=1, verbose=2)

    for timer in t1:
        with timer:
            json_object = phaser.animal.get().json()
            json_formatted = json.dumps(json_object, indent=2)
            print(json_formatted)

    print('t1.total_time = %r' % (t1.total_time,))