import anki.sched as oldSched


def _getCardReordered(self):
    "Return the next due card id, or None."
    # learning card due?
    c = self._getLrnCard()
    if c:
        return c
    # day learning card due?
    c = self._getLrnDayCard()
    if c:
        return c
    # new first, or time for one?
    if self._timeForNewCard():
        c = self._getNewCard()
        if c:
            return c
    # card due for review?
    c = self._getRevCard()
    if c:
        return c
    # new cards left?
    c = self._getNewCard()
    if c:
        return c
    # collapse or finish
    return self._getLrnCard(collapse=True)


oldSched.Scheduler._getCard = _getCardReordered