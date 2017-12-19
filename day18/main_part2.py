#!/usr/bin/env python

import threading
import time

registers = {}
lock = threading.RLock()

state = {
    0: {
        'is_waiting': False,
        'q': []
    },
    1: {
        'is_waiting': False,
        'q': []
    }
}

def get_value(val):
    try:
        return int(val)
    except:
        return get_value(registers[val])

def play(instructions, prog_id):
    i = 0
    while i < len(instructions):
        instruction = instructions[i].strip()
        
        command = instruction[:3]
        register = instruction[4]
        value = instruction[6:]

        if not register in registers:
            registers[register] = 0

        if command == 'snd':
            if value == 'p':
                value = prog_id
            lock.acquire()
            state[(prog_id + 1) % 2]['q'].append(value)
            lock.release()
        elif command == 'set':
            registers[register] = value
        elif command == 'add':
            val = get_value(value)
            registers[register] = get_value(register) + val
        elif command == 'mul':
            val = get_value(value)
            registers[register] = get_value(register) * val
        elif command == 'mod':
            val = get_value(value)
            registers[register] = get_value(register) % val
        elif command == 'rcv':
            # Deadlock detection...
            lock.acquire()
            if(len(state[prog_id]['q']) == 0):
                state[prog_id]['is_waiting'] = True
                lock.release()
                while(True):
                    lock.acquire()
                    if state[(prog_id + 1) % 2]['is_waiting']:
                        print("DEADLOCK")
                        lock.release()
                        return
                    lock.release()
                    time.sleep(1)
            registers[register] = state[prog_id]['q'][0]
            state[prog_id]['q'] = state[prog_id]['q'][1:]
            lock.release()
        elif command == 'jgz':
            if get_value(register) > 0:
                i += get_value(value)
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