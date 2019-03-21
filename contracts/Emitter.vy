# Emitter.vy
import interface.IDumbContract as IDumbContract

owner: public(address)
counter: public(uint256)
dumb: IDumbContract


@public
def __init__(dumb_address: address):
    self.owner = msg.sender
    self.dumb = IDumbContract(dumb_address)


@public
def emit_owner():
    self.dumb.emitAddress(self.owner)
    self.counter += 1


@public
def emit_sender():
    self.dumb.emitAddress(msg.sender)
    self.counter += 1


@public
def emit_counter():
    self.dumb.emitUint256(self.counter)
