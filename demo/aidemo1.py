# generate a powerball number pickup 7 numbers from 1 to 35 and one number from 1 to 20

import random
print(random.sample(range(1, 36), 7) + random.sample(range(1, 21), 1))
