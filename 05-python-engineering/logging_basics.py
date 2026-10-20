"""Logging: use instead of print() for diagnostics.

Named logging_basics.py because a file called logging.py would shadow the
standard-library module.
"""

import logging

# Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL. Shows the set level and above.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(__name__)  # one logger per module

logger.debug("hidden: below INFO")
logger.info("starting training")
logger.warning("learning rate is high")

epoch, loss = 3, 0.4172
logger.info("epoch=%d loss=%.3f", epoch, loss)  # pass args, don't build the string

try:
    1 / 0
except ZeroDivisionError:
    logger.exception("calculation failed")  # logs the traceback too

# print() = output the user asked for; logging = diagnostics. Never log secrets.
