#!/usr/bin/env python

import threading
import time

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
            state[(prog_id + 1) % 2]['q'].append(value)
            lock.release()
            sending_values += 1
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
            lock.acquire()
            if(len(state[prog_id]['q']) == 0):
                state[prog_id]['is_waiting'] = True
                lock.release()
                time.sleep(1)
                while(True):
                    lock.acquire()
                    if state[(prog_id + 1) % 2]['is_waiting']:
                        print ("DEADLOCK")
                        print ("PROGRAM %d SENT %d VALUES" % (prog_id, sending_values))
                        lock.release()
                        return
                    if len(state[prog_id]['q']) > 1:
                        registers[register] = state[prog_id]['q'][0]
                        state[prog_id]['q'] = state[prog_id]['q'][1:]
                        lock.release()
                        continue
                    lock.release()
                    time.sleep(1)
            registers[register] = state[prog_id]['q'][0]
            state[prog_id]['q'] = state[prog_id]['q'][1:]
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