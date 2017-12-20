#!/usr/bin/env python

import threading
import time
from queue import Queue

lock = threading.Lock()

state = {
    0: {
        'is_waiting': False,
        'q': Queue()
    },
    1: {
        'is_waiting': False,
        'q': Queue()
    }
}

def get_value(val, registers):
    try:
        return int(val)
    except:
        try:
            return get_value(registers[val], registers)
        except:
            print(registers)

def play(instructions, prog_id):
    i = 0
    registers = {'p': prog_id}
    sending_values = 0
    other_prog_id = (prog_id + 1) % 2

    while i < len(instructions):
        instruction = instructions[i].strip()
        
        command = instruction[:3]
        register = instruction[4]
        value = instruction[6:]

        if not register in registers:
            registers[register] = 0

        if command == 'snd':
            lock.acquire()
            value = get_value(register, registers)
            state[other_prog_id]['q'].put(value)
            state[other_prog_id]['is_waiting'] = False
            sending_values += 1
            lock.release()
        elif command == 'set':
            registers[register] = value
        elif command == 'add':
            val = get_value(value, registers)
            registers[register] = get_value(register, registers) + val
        elif command == 'mul':
            val = get_value(value, registers)
            registers[register] = get_value(register, registers) * val
        elif command == 'mod':
            val = get_value(value, registers)
            registers[register] = get_value(register, registers) % val
        elif command == 'rcv':
            # Deadlock detection...
            if(state[prog_id]['q'].qsize() == 0):
                lock.acquire()
                state[prog_id]['is_waiting'] = True
                lock.release()
                while(True):
                    lock.acquire()
                    if not state[prog_id]['is_waiting']:
                        print ("NOT WAITING ANYMORE \n %s" % state)
                        lock.release()
                        break
                    if state[other_prog_id]['is_waiting']:
                        print ("DEADLOCK STATE \n %s" % str(state))
                        print ("PROGRAM %d SENT %d VALUES" % (prog_id, sending_values))
                        lock.release()
                        return
                    lock.release()
            lock.acquire()
            registers[register] = state[prog_id]['q'].get()
            lock.release()
        elif command == 'jgz':
            if get_value(register, registers) > 0:
                i += get_value(value, registers)
                continue
        i+=1

if __name__ == '__main__':
    f = open('/Users/kosta/dev/advent-of-code-17/day18/input.txt', 'r')
    instructions = f.readlines()
    f.close()
    t1 = threading.Thread(target=play, args=(instructions,0))
    t1.start()
    t2 = threading.Thread(target=play, args=(instructions,1))
    t2.start()

    t1.join()
    t2.join()