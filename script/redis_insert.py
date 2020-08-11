# This script generates fruit stock & prices,
# and randomly increments/decrements their numbers.

import time
import random
import redis

r = redis.Redis(host="localhost", port=6379, db=0)
fruits = ("apple", "banana", "cherry")


# Creates stock and price keys for every fruit in fruits.
# Initializes values to 50.
def create_keys():
    for fruit in fruits:
        r.execute_command('TS.CREATE stock:{0} LABELS label stock fruit {0}'.format(fruit))
        r.execute_command('TS.CREATE price:{0} LABELS label price fruit {0}'.format(fruit))

        r.execute_command('TS.ADD stock:{0} * 50'.format(fruit))
        r.execute_command('TS.ADD price:{0} * 50'.format(fruit))


# Randomly increments/decrements a random fruit for the given label by 1-5 units.
def update_random(label):
    fruit = fruits[random.randint(0, 2)]
    amount = random.randint(1, 5)
    command = "TS.INCRBY" if bool(random.getrandbits(1)) else "TS.DECRBY"

    r.execute_command("{0} {1}:{2} {3}".format(command, label, fruit, amount))


if __name__ == "__main__":
    create_keys()
    time.sleep(1)

    while True:
        update_random("stock")
        update_random("price")
        time.sleep(1)
