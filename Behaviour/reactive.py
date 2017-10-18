from rx import Observer, Observable


class MyObserver(Observer):
    def on_next(self, value):
        print("Got: %s" % value)

    def on_error(self, error):
        print("Got error: %s" % error)

    def on_completed(self):
        print("Sequence completed")


xs = Observable.from_iterable(range(10))
d = xs.subscribe(MyObserver())
print()

xf = Observable.from_(range(10))
f = xf.subscribe(print)
print()

g = xf.filter(lambda x: x % 2).subscribe(print)
print()

h = xf.map(lambda x: x * 2).subscribe(print)
print()

astream = Observable.range(1, 5)
bstream = Observable.from_('abcde')
cstream = astream.merge(bstream).subscribe(print)
