from pylady import PyLady


eliska = PyLady("Eliška")

eliska.eat()
eliska.study(2)
eliska.eat()
eliska.meditate()
eliska.meditate()
eliska.eat()

eliska.coffee()
eliska.meditate()
eliska.study(1)
eliska.coffee()
eliska.meditate()
eliska.eat()
eliska.study(2)
eliska.coffee
eliska.take_advice()
eliska.meditate()
eliska.coffee()
eliska.meditate()
eliska.study(2)
eliska.sleep(8)


print(eliska)
print("knowledge", eliska.knowledge)
print("energie", eliska.energy)
print("focus", eliska.focus)
print("practice", eliska.practice)
print()
eliska.control()
